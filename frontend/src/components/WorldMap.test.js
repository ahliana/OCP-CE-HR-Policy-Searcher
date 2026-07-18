import React from 'react';
import { act, fireEvent, render, screen, waitFor, within } from '@testing-library/react';
import WorldMap from './WorldMap';

const BASE_COVERAGE = {
  countries: [
    {
      name: 'United States', iso_numeric: '840', sources: 162, policies: 23,
      top_policy_names: ['Heat Reuse Act', 'Thermal Energy Network Pilot Program'],
    },
    {
      name: 'Sweden', iso_numeric: '752', sources: 8, policies: 0, top_policy_names: [],
    },
    {
      // Absent from the 110m atlas entirely - no <path> can ever exist for
      // it. Must still reach the map (as a micro dot) and the browse list.
      name: 'Singapore', iso_numeric: '702', sources: 2, policies: 0, top_policy_names: [],
    },
  ],
  supranational: [
    {
      name: 'European Union', slug: 'eu', sources: 0, policies: 7,
      top_policy_names: ['EU Energy Efficiency Directive'],
    },
  ],
  totals: { sources: 372, policies: 118 },
};

function mockFetch(coverage = BASE_COVERAGE) {
  return jest.fn(async (url) => {
    if (String(url).includes('/api/coverage')) {
      return { ok: true, json: async () => coverage };
    }
    return { ok: false, text: async () => 'not found' };
  });
}

afterEach(() => {
  jest.restoreAllMocks();
});

describe('WorldMap', () => {
  it('shows totals from the live coverage endpoint', async () => {
    global.fetch = mockFetch();
    render(<WorldMap onSelectPlace={jest.fn()} />);

    await waitFor(() => {
      expect(screen.getByText('372')).toBeInTheDocument();
    });
    expect(screen.getByText('118')).toBeInTheDocument();
    // 3 countries (incl. Singapore, off-atlas) + 1 supranational entry
    expect(screen.getByText('4')).toBeInTheDocument();
  });

  it('never drops a tracked country with no atlas polygon: it reaches the map and the list', async () => {
    const onSelectPlace = jest.fn();
    global.fetch = mockFetch();
    render(<WorldMap onSelectPlace={onSelectPlace} />);

    // Renders as a <circle> micro marker, not a <path> - there is no
    // Singapore polygon in the 110m atlas at all.
    const dot = await screen.findByRole('button', { name: /Singapore: tracked/ });
    expect(dot.tagName.toLowerCase()).toBe('circle');

    expect(await screen.findByText('Browse all tracked places as a list (4)')).toBeInTheDocument();

    fireEvent.click(dot);
    expect(await screen.findByRole('heading', { name: 'Singapore' })).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: 'Search Singapore' }));
    expect(onSelectPlace).toHaveBeenCalledWith('Singapore');
  });

  it('reaches an off-atlas country through the quick-filter box too', async () => {
    global.fetch = mockFetch();
    render(<WorldMap onSelectPlace={jest.fn()} />);

    await screen.findByRole('button', { name: /United States of America/ });
    fireEvent.change(screen.getByLabelText('Find a tracked place on the map'), {
      target: { value: 'Singapor' },
    });
    fireEvent.keyDown(screen.getByLabelText('Find a tracked place on the map'), { key: 'Enter' });

    expect(await screen.findByRole('heading', { name: 'Singapore' })).toBeInTheDocument();
  });

  it('clicking a tracked country opens the panel with its policies and a working search CTA', async () => {
    const onSelectPlace = jest.fn();
    global.fetch = mockFetch();
    render(<WorldMap onSelectPlace={onSelectPlace} />);

    const path = await screen.findByRole('button', { name: /United States of America/ });
    fireEvent.click(path);

    expect(await screen.findByRole('heading', { name: 'United States' })).toBeInTheDocument();
    expect(screen.getByText(/162 tracked sources/)).toBeInTheDocument();
    expect(screen.getByText('Heat Reuse Act')).toBeInTheDocument();

    fireEvent.click(screen.getByRole('button', { name: 'Search United States' }));
    expect(onSelectPlace).toHaveBeenCalledWith('United States');
  });

  it('an untracked country still opens the panel, offering "search anyway"', async () => {
    global.fetch = mockFetch();
    render(<WorldMap onSelectPlace={jest.fn()} />);

    const path = await screen.findByLabelText(/Germany: not yet tracked/);
    fireEvent.click(path);

    expect(await screen.findByRole('heading', { name: 'Germany' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Search Germany anyway' })).toBeInTheDocument();
  });

  it('never drops an off-map jurisdiction: the EU renders as a clickable chip', async () => {
    const onSelectPlace = jest.fn();
    global.fetch = mockFetch();
    render(<WorldMap onSelectPlace={onSelectPlace} />);

    const tray = await screen.findByLabelText('Coverage without a map shape');
    const chip = within(tray).getByRole('button', { name: /European Union/ });
    fireEvent.click(chip);

    expect(await screen.findByRole('heading', { name: 'European Union' })).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: 'Search European Union' }));
    expect(onSelectPlace).toHaveBeenCalledWith('European Union');
  });

  it('legend click filters: dims every bin except the one selected', async () => {
    global.fetch = mockFetch();
    render(<WorldMap onSelectPlace={jest.fn()} />);

    await screen.findByRole('button', { name: /United States of America/ });
    const highTierButton = screen.getByRole('button', { name: '16+ policies' });
    fireEvent.click(highTierButton);

    expect(highTierButton).toHaveAttribute('aria-pressed', 'true');
    const sweden = screen.getByLabelText(/Sweden: 8 sources/);
    expect(sweden).toHaveClass('wm-dim');
    const usa = screen.getByRole('button', { name: /United States of America/ });
    expect(usa).not.toHaveClass('wm-dim');
  });

  it('refetches and redraws when the app dispatches policy-data-changed', async () => {
    const fetchMock = mockFetch();
    global.fetch = fetchMock;
    render(<WorldMap onSelectPlace={jest.fn()} />);

    await waitFor(() => expect(screen.getByText('118')).toBeInTheDocument());

    fetchMock.mockImplementation(async (url) => {
      if (String(url).includes('/api/coverage')) {
        return { ok: true, json: async () => ({ ...BASE_COVERAGE, totals: { sources: 372, policies: 119 } }) };
      }
      return { ok: false, text: async () => 'not found' };
    });

    await act(async () => {
      window.dispatchEvent(new Event('policy-data-changed'));
    });

    await waitFor(() => expect(screen.getByText('119')).toBeInTheDocument());
  });
});
