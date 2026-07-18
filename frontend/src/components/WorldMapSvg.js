import React from 'react';

function countryLabel(geo, cov) {
  if (!cov) return `${geo.name}: not yet tracked`;
  return `${geo.name}: ${cov.sources} sources, ${cov.policies} policies`;
}

function CountryPath({ item, isHit, isDimmed, onHover, onHoverEnd, onSelect }) {
  const { geo, cov, bin } = item;
  const tracked = bin !== 'untracked';
  const classes = ['wm-country', `wm-bin-${bin}`];
  if (isHit) classes.push('wm-hit');
  if (isDimmed) classes.push('wm-dim');

  return (
    <path
      d={geo.d}
      className={classes.join(' ')}
      data-bin={bin}
      aria-label={countryLabel(geo, cov)}
      tabIndex={tracked ? 0 : undefined}
      role={tracked ? 'button' : undefined}
      onPointerMove={(event) => onHover(geo.id, event)}
      onPointerLeave={onHoverEnd}
      onClick={() => onSelect(geo.id)}
      onKeyDown={tracked ? (event) => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          onSelect(geo.id);
        }
      } : undefined}
    />
  );
}

function MicroMarker({ marker, isHit, isDimmed, onHover, onHoverEnd, onSelect }) {
  const classes = ['wm-micro', `wm-bin-${marker.bin}`];
  if (isHit) classes.push('wm-hit');
  if (isDimmed) classes.push('wm-dim');

  return (
    <circle
      cx={marker.cx}
      cy={marker.cy}
      r={4.2}
      className={classes.join(' ')}
      data-bin={marker.bin}
      aria-label={`${marker.name}: tracked, too small to show on the map outline`}
      tabIndex={0}
      role="button"
      onPointerMove={(event) => onHover(marker.id, event)}
      onPointerLeave={onHoverEnd}
      onClick={() => onSelect(marker.id)}
      onKeyDown={(event) => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          onSelect(marker.id);
        }
      }}
    />
  );
}

// Inline SVG choropleth: precomputed Equal Earth paths (world-atlas 110m),
// styled entirely by CSS class so bins/hover/dim/hit states are one class
// list each, no per-element style computation.
function WorldMapSvg({ joined, microMarkers, activeBin, hitIds, onHover, onHoverEnd, onSelect }) {
  return (
    <svg
      className="wm-svg"
      viewBox="0 0 960 421.5"
      role="group"
      aria-label="World map of PolicyPulse coverage"
    >
      {joined.map((item) => (
        <CountryPath
          key={item.geo.id}
          item={item}
          isHit={hitIds.has(item.geo.id)}
          isDimmed={activeBin !== null && item.bin !== activeBin}
          onHover={onHover}
          onHoverEnd={onHoverEnd}
          onSelect={onSelect}
        />
      ))}
      {microMarkers.map((marker) => (
        <MicroMarker
          key={marker.id}
          marker={marker}
          isHit={hitIds.has(marker.id)}
          isDimmed={activeBin !== null && marker.bin !== activeBin}
          onHover={onHover}
          onHoverEnd={onHoverEnd}
          onSelect={onSelect}
        />
      ))}
    </svg>
  );
}

export default WorldMapSvg;
