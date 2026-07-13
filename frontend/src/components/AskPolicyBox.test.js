import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import AskPolicyBox, { linkifyAnswer } from './AskPolicyBox';

describe('linkifyAnswer', () => {
  it('turns bare URLs into anchor descriptors', () => {
    const parts = linkifyAnswer('See https://ec.europa.eu/law for details.');
    expect(parts).toEqual([
      { type: 'text', value: 'See ' },
      { type: 'link', value: 'https://ec.europa.eu/law' },
      { type: 'text', value: ' for details.' },
    ]);
  });

  it('returns plain text untouched', () => {
    expect(linkifyAnswer('No policies found.')).toEqual([
      { type: 'text', value: 'No policies found.' },
    ]);
  });
});

describe('AskPolicyBox', () => {
  beforeEach(() => {
    global.fetch = jest.fn();
  });

  afterEach(() => {
    jest.restoreAllMocks();
  });

  it('submits a question and shows the answer', async () => {
    global.fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ answer: 'Germany requires heat reuse plans.', remaining_today: 10 }),
    });

    render(<AskPolicyBox />);
    fireEvent.change(screen.getByPlaceholderText(/ask about discovered policies/i), {
      target: { value: 'What does Germany require?' },
    });
    fireEvent.click(screen.getByRole('button', { name: /ask/i }));

    await waitFor(() => {
      expect(screen.getByText(/Germany requires heat reuse plans\./)).toBeInTheDocument();
    });
    expect(global.fetch).toHaveBeenCalledWith(
      expect.stringContaining('/api/ask'),
      expect.objectContaining({ method: 'POST' })
    );
  });

  it('shows the server detail message on 429', async () => {
    global.fetch.mockResolvedValueOnce({
      ok: false,
      status: 429,
      json: async () => ({ detail: 'The daily question limit has been reached.' }),
    });

    render(<AskPolicyBox />);
    fireEvent.change(screen.getByPlaceholderText(/ask about discovered policies/i), {
      target: { value: 'Anything in France?' },
    });
    fireEvent.click(screen.getByRole('button', { name: /ask/i }));

    await waitFor(() => {
      expect(screen.getByText(/daily question limit/i)).toBeInTheDocument();
    });
  });

  it('disables the button while empty', () => {
    render(<AskPolicyBox />);
    expect(screen.getByRole('button', { name: /ask/i })).toBeDisabled();
  });
});
