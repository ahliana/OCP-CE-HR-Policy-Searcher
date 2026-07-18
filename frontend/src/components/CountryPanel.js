import React from 'react';
import { pluralize } from '../utils/mapCoverage';

// Click commits: a side panel, never a modal, so the map stays explorable
// while a result is open. The "Search {place}" action is the one path from
// the map into the app's real place-first search - same resolve_place flow
// typing the name would use.
function CountryPanel({ selection, onClose, onSearchPlace }) {
  const isOpen = Boolean(selection);
  const tracked = selection && (selection.sources > 0 || selection.policies > 0);

  return (
    <aside
      className={`wm-panel${isOpen ? ' wm-panel-open' : ''}`}
      aria-label="Place details"
      aria-hidden={!isOpen}
    >
      <button type="button" className="wm-panel-close" aria-label="Close panel" onClick={onClose}>
        &times;
      </button>
      {selection && (
        <div className="wm-panel-body">
          <h3>{selection.name}</h3>
          {tracked ? (
            <>
              <div className="wm-panel-stats">
                {selection.sources} tracked {pluralize(selection.sources, 'source')}
                {' · '}
                {selection.policies} {pluralize(selection.policies, 'policy', 'policies')} found
              </div>
              {selection.topPolicyNames.length > 0 ? (
                <>
                  {selection.topPolicyNames.map((name) => (
                    <div className="wm-panel-policy" key={name}>{name}</div>
                  ))}
                  {selection.policies > selection.topPolicyNames.length && (
                    <p className="wm-panel-note">
                      + {selection.policies - selection.topPolicyNames.length} more in the
                      results list below.
                    </p>
                  )}
                </>
              ) : (
                <p className="wm-panel-empty">
                  Sources are watched here, but no qualifying policy has surfaced yet.
                  A fresh scan may change that.
                </p>
              )}
              <button
                type="button"
                className="wm-panel-cta"
                onClick={() => onSearchPlace(selection.name)}
              >
                Search {selection.name}
              </button>
            </>
          ) : (
            <>
              <p className="wm-panel-empty">
                No tracked sources yet. Searching still works - finding sources here
                is how coverage grows.
              </p>
              <button
                type="button"
                className="wm-panel-cta"
                onClick={() => onSearchPlace(selection.name)}
              >
                Search {selection.name} anyway
              </button>
            </>
          )}
        </div>
      )}
    </aside>
  );
}

export default CountryPanel;
