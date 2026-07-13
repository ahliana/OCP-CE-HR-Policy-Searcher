import { DEFAULT_CHANNELS, buildChannels } from './scanTargets';

describe('DEFAULT_CHANNELS', () => {
  it('defaults to crawl, law_apis, and transposition', () => {
    expect(DEFAULT_CHANNELS).toEqual(['crawl', 'law_apis', 'transposition']);
  });
});

describe('buildChannels', () => {
  it('returns the selected channels when provided', () => {
    expect(buildChannels(['crawl', 'news'])).toEqual(['crawl', 'news']);
  });

  it('falls back to crawl-only when no channels are selected', () => {
    expect(buildChannels([])).toEqual(['crawl']);
  });

  it('falls back to crawl-only when channels is undefined', () => {
    expect(buildChannels(undefined)).toEqual(['crawl']);
  });
});
