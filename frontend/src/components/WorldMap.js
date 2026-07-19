import React, { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import worldAtlas from '../assets/worldAtlas110m.json';
import useCoverage from '../hooks/useCoverage';
import usePanZoom from '../hooks/usePanZoom';
import { binForCoverage, computeMicroMarkers, joinCountries } from '../utils/mapCoverage';
import CoverageStatStrip from './CoverageStatStrip';
import MapLegend from './MapLegend';
import MapTooltip from './MapTooltip';
import OffMapTray from './OffMapTray';
import BrowseList from './BrowseList';
import CountryPanel from './CountryPanel';
import WorldMapSvg from './WorldMapSvg';
import './WorldMap.css';

const MIN_QUERY_LENGTH = 2;

function normalize(value) {
  return value.trim().toLowerCase();
}

// PolicyPulse's front door: shows where coverage exists before anyone types
// a word, and every entry point here - map click, quick-filter, legend,
// off-map chip, browse list - ends at the same place, the "Search {place}"
// action that feeds the app's existing place-first search box below.
function WorldMap({ onSelectPlace }) {
  const { coverage, error } = useCoverage();
  const holderRef = useRef(null);
  const svgRef = useRef(null);
  const panZoom = usePanZoom(svgRef);

  const [hover, setHover] = useState(null);
  const [activeBin, setActiveBin] = useState(null);
  const [query, setQuery] = useState('');
  const [selectedId, setSelectedId] = useState(null);

  const joined = useMemo(
    () => joinCountries(worldAtlas.countries, coverage.countries),
    [coverage.countries],
  );
  const microMarkers = useMemo(
    () => computeMicroMarkers(worldAtlas.countries, coverage.countries),
    [coverage.countries],
  );
  const worldById = useMemo(
    () => new Map(worldAtlas.countries.map((c) => [c.id, c])),
    [],
  );
  const covByIso = useMemo(
    () => new Map(coverage.countries.map((c) => [String(c.iso_numeric), c])),
    [coverage.countries],
  );
  const supByslug = useMemo(
    () => new Map(coverage.supranational.map((s) => [s.slug, s])),
    [coverage.supranational],
  );

  const nameOfCountry = useCallback(
    (id) => covByIso.get(id)?.name || worldById.get(id)?.name || '',
    [covByIso, worldById],
  );

  const trimmedQuery = normalize(query);
  const hitIds = useMemo(() => {
    if (trimmedQuery.length < MIN_QUERY_LENGTH) return new Set();
    const hits = new Set();
    for (const { geo } of joined) {
      if (nameOfCountry(geo.id).toLowerCase().includes(trimmedQuery)) hits.add(geo.id);
    }
    for (const marker of microMarkers) {
      if (marker.name.toLowerCase().includes(trimmedQuery)) hits.add(marker.id);
    }
    return hits;
  }, [trimmedQuery, joined, microMarkers, nameOfCountry]);

  const supHitSlugs = useMemo(() => {
    if (trimmedQuery.length < MIN_QUERY_LENGTH) return new Set();
    const hits = new Set();
    for (const entry of coverage.supranational) {
      if (entry.name.toLowerCase().includes(trimmedQuery)) hits.add(entry.slug);
    }
    return hits;
  }, [trimmedQuery, coverage.supranational]);

  const browseRows = useMemo(() => {
    // Built from coverage.countries directly, not the atlas join: a tracked
    // country with no 110m polygon (Singapore) still gets a map dot via
    // computeMicroMarkers, but joinCountries has nothing to key it to, so
    // deriving rows from the join would silently drop it here too.
    const countryRows = coverage.countries.map((c) => ({
      id: String(c.iso_numeric),
      name: c.name,
      policies: c.policies,
      bin: binForCoverage(c),
    }));
    const supRows = coverage.supranational.map((entry) => ({
      id: `sup:${entry.slug}`,
      name: entry.name,
      policies: entry.policies,
      bin: binForCoverage(entry),
    }));
    return [...countryRows, ...supRows].sort(
      (a, b) => b.policies - a.policies || a.name.localeCompare(b.name),
    );
  }, [coverage.countries, coverage.supranational]);

  const handleHover = useCallback((id, event) => {
    const holderRect = holderRef.current?.getBoundingClientRect();
    if (!holderRect) return;
    let x = event.clientX - holderRect.left + 14;
    let y = event.clientY - holderRect.top + 14;
    if (x > holderRect.width - 220) x = event.clientX - holderRect.left - 220;
    if (y > holderRect.height - 90) y = event.clientY - holderRect.top - 90;
    setHover({
      id,
      x,
      y,
      name: nameOfCountry(id),
      cov: covByIso.get(id) || null,
    });
  }, [nameOfCountry, covByIso]);

  const handleHoverEnd = useCallback(() => setHover(null), []);

  const handleToggleBin = useCallback((bin) => {
    setActiveBin((prev) => (prev === bin ? null : bin));
  }, []);

  const handleSelectId = useCallback((id) => setSelectedId(id), []);
  const handleSelectSupranational = useCallback(
    (entry) => setSelectedId(`sup:${entry.slug}`),
    [],
  );
  const handleClosePanel = useCallback(() => setSelectedId(null), []);

  useEffect(() => {
    if (!selectedId) return undefined;
    const onKeyDown = (event) => {
      if (event.key === 'Escape') setSelectedId(null);
    };
    window.addEventListener('keydown', onKeyDown);
    return () => window.removeEventListener('keydown', onKeyDown);
  }, [selectedId]);

  const handleSearchPlace = useCallback((name) => {
    onSelectPlace(name);
    setSelectedId(null);
    document.querySelector('.search-panel')
      ?.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }, [onSelectPlace]);

  const handleQueryKeyDown = useCallback((event) => {
    if (event.key !== 'Enter') return;
    if (trimmedQuery.length < MIN_QUERY_LENGTH) return;

    // Tracked countries first (this also covers ones with no atlas polygon,
    // like Singapore, that "joined" can't key to), then the full atlas list
    // so an untracked place can still open the "search anyway" panel.
    const trackedMatch = coverage.countries.find(
      (c) => c.name.toLowerCase().startsWith(trimmedQuery),
    ) || coverage.countries.find((c) => c.name.toLowerCase().includes(trimmedQuery));
    if (trackedMatch) {
      setSelectedId(String(trackedMatch.iso_numeric));
      return;
    }
    const atlasMatch = joined.find((item) => nameOfCountry(item.geo.id)
      .toLowerCase().startsWith(trimmedQuery))
      || joined.find((item) => nameOfCountry(item.geo.id)
        .toLowerCase().includes(trimmedQuery));
    if (atlasMatch) {
      setSelectedId(atlasMatch.geo.id);
      return;
    }
    const supMatch = coverage.supranational.find(
      (entry) => entry.name.toLowerCase().startsWith(trimmedQuery),
    ) || coverage.supranational.find(
      (entry) => entry.name.toLowerCase().includes(trimmedQuery),
    );
    if (supMatch) setSelectedId(`sup:${supMatch.slug}`);
  }, [trimmedQuery, coverage.countries, joined, nameOfCountry, coverage.supranational]);

  const selection = useMemo(() => {
    if (!selectedId) return null;
    if (selectedId.startsWith('sup:')) {
      const entry = supByslug.get(selectedId.slice(4));
      if (!entry) return null;
      return {
        id: selectedId,
        name: entry.name,
        sources: entry.sources,
        policies: entry.policies,
        topPolicyNames: entry.top_policy_names || [],
      };
    }
    const cov = covByIso.get(selectedId);
    return {
      id: selectedId,
      name: cov?.name || worldById.get(selectedId)?.name || selectedId,
      sources: cov?.sources || 0,
      policies: cov?.policies || 0,
      topPolicyNames: cov?.top_policy_names || [],
    };
  }, [selectedId, supByslug, covByIso, worldById]);

  const trackedPlaceCount = coverage.countries.length
    + coverage.supranational.filter((s) => s.sources > 0 || s.policies > 0).length;

  return (
    <div className="world-map">
      {error && (
        <p className="wm-error" role="alert">
          Coverage data could not be loaded. The map below may be out of date.
        </p>
      )}
      <CoverageStatStrip totals={coverage.totals} placeCount={trackedPlaceCount} />
      <p className="wm-note">
        Green countries have policy findings. Pale green means we watch their sources but
        nothing has surfaced yet. Gray means not tracked yet.
      </p>

      <div className="wm-searchrow">
        <input
          type="text"
          className="wm-quickfilter"
          placeholder='Find on the map - try "Sweden" or "Japan"'
          aria-label="Find a tracked place on the map"
          autoComplete="off"
          value={query}
          onChange={(event) => setQuery(event.target.value)}
          onKeyDown={handleQueryKeyDown}
        />
        <span className="wm-searchrow-hint">
          Map, legend, and this box all drive the same selection.
        </span>
      </div>

      <div className="wm-stage" ref={holderRef}>
        <WorldMapSvg
          svgRef={svgRef}
          joined={joined}
          microMarkers={microMarkers}
          activeBin={activeBin}
          hitIds={hitIds}
          viewBox={panZoom.viewBox}
          panZoomHandlers={panZoom.handlers}
          onHover={handleHover}
          onHoverEnd={handleHoverEnd}
          onSelect={handleSelectId}
        />
        <div className="wm-controls" role="group" aria-label="Map zoom controls">
          <button
            type="button"
            className="wm-control-btn"
            aria-label="Zoom in"
            onClick={panZoom.zoomIn}
            disabled={!panZoom.canZoomIn}
          >
            +
          </button>
          <button
            type="button"
            className="wm-control-btn"
            aria-label="Zoom out"
            onClick={panZoom.zoomOut}
            disabled={!panZoom.canZoomOut}
          >
            &minus;
          </button>
          <button
            type="button"
            className="wm-control-btn wm-control-reset"
            aria-label="Reset map view"
            onClick={panZoom.reset}
            disabled={!panZoom.canZoomOut}
          >
            Reset
          </button>
        </div>
        <MapTooltip hover={hover} />
        <CountryPanel
          selection={selection}
          onClose={handleClosePanel}
          onSearchPlace={handleSearchPlace}
        />
      </div>

      <MapLegend activeBin={activeBin} onToggleBin={handleToggleBin} />
      <OffMapTray
        entries={coverage.supranational}
        activeBin={activeBin}
        activeId={selectedId}
        hitSlugs={supHitSlugs}
        onSelect={handleSelectSupranational}
      />
      <BrowseList rows={browseRows} onSelect={handleSelectId} />
    </div>
  );
}

export default WorldMap;
