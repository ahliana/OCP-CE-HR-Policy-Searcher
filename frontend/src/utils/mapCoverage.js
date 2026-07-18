// Pure helpers for the world map: binning, the atlas/coverage join, and the
// small set of tracked places too small to click reliably on a 110m polygon.
// Kept dependency-free so they're trivial to unit test without rendering.

export const BIN_KEYS = ['untracked', 't0', 'b1', 'b2', 'b3'];

export const BIN_LABELS = {
  untracked: 'Not yet tracked',
  t0: 'Tracked, nothing found yet',
  b1: '1–5 policies',
  b2: '6–15 policies',
  b3: '16+ policies',
};

// Two grays, deliberately: "untracked" (no coverage record at all - we have
// not looked) must never be visually or semantically confused with "t0"
// (a coverage record exists, sources are watched, nothing has surfaced yet).
export function binForCoverage(entry) {
  if (!entry) return 'untracked';
  if (entry.policies === 0) return 't0';
  if (entry.policies <= 5) return 'b1';
  if (entry.policies <= 15) return 'b2';
  return 'b3';
}

// Countries whose 110m polygon exists but is too small to hover/click
// reliably, plus countries absent from the 110m atlas entirely. Both get a
// dot marker layered on top so precision never gates access to a tracked
// place. Singapore's coordinates are pinned to this map's own projection
// (Equal Earth, viewBox 0 0 960 421.5) - not a general-purpose lookup.
export const MICRO_AREA_THRESHOLD = 30;
export const OFF_ATLAS_MICROSTATES = {
  702: { name: 'Singapore', cx: 762.1, cy: 231.0 },
};

// Joins the static world-atlas geometry to a live /api/coverage response,
// keyed by iso_numeric (the pinned join key). Every atlas country appears
// exactly once, tagged with its bin; countries with no coverage record are
// 'untracked' rather than dropped, so the map still draws their outline.
//
// Three de-facto territories (Kosovo, N. Cyprus, Somaliland) are drawn in
// the 110m atlas with an empty id - world-atlas carries no numeric code for
// them. Per the pinned design decision, contested territories with no
// iso_numeric render list-only in the off-map tray, never as a border fill
// ("loses no data, takes no cartographic stance"). The registry backs this:
// a resolved country with a falsy iso_numeric always routes to `supranational`,
// never `countries`, so these ids could never join to a coverage record
// anyway - excluding them here also sidesteps a React key collision, since
// all three would otherwise share the key "".
export function joinCountries(worldCountries, coverageCountries) {
  const byIso = new Map();
  for (const c of coverageCountries || []) {
    byIso.set(String(c.iso_numeric), c);
  }

  return worldCountries
    .filter((geo) => geo.id)
    .map((geo) => {
      const cov = byIso.get(geo.id) || null;
      return { geo, cov, bin: binForCoverage(cov) };
    });
}

// Dot markers for tracked places a click can't reliably land on: on-atlas
// polygons under the area threshold, plus places absent from the atlas
// entirely (Singapore). Untracked microstates get no marker - there's no
// coverage record to show, and the polygon (however tiny) already renders.
export function computeMicroMarkers(worldCountries, coverageCountries) {
  const byId = new Map(worldCountries.map((c) => [c.id, c]));
  const byIso = new Map((coverageCountries || []).map((c) => [String(c.iso_numeric), c]));
  const markers = [];

  for (const cov of coverageCountries || []) {
    const id = String(cov.iso_numeric);
    const geo = byId.get(id);
    if (geo && geo.area >= MICRO_AREA_THRESHOLD) continue;
    const coords = geo || OFF_ATLAS_MICROSTATES[id];
    if (!coords) continue;
    markers.push({
      id,
      name: cov.name,
      cx: coords.cx,
      cy: coords.cy,
      bin: binForCoverage(byIso.get(id)),
    });
  }

  return markers;
}

export function pluralize(count, singular, plural = `${singular}s`) {
  return count === 1 ? singular : plural;
}
