# Source Expansion - How to Proceed

Handoff for whoever picks this up next (a future session or a human). Written
2026-07-18 at the end of 4 research waves. Read [WHAT-LANDED.md](WHAT-LANDED.md)
first for the live status; this doc is the "what to do next and how."

---

## 1. Current state (TL;DR)

- Branch: **`feature/source-expansion-research`**, cut from main, rebased onto main
  (has the merged jurisdiction registry). 9 commits, **docs-only, NOT pushed.**
- **~501 verified candidate sources** across 4 waves: 452 crawl domains + 49 tier-c
  APIs. Everything is `enabled: false` draft config + research notes. **No client code
  written, nothing enabled in a live scan.** This is a review queue, not shipped work.
- Deduped against the ~390 existing sources and across waves.
- Wave 4 also staged **63 jurisdiction-registry rows** (new countries + subnational)
  for the map track.

Nothing here has shipped. The next move is a human choosing what to promote/build.

---

## 2. Where everything is

| File | What it is |
|---|---|
| [INVENTORY.md](INVENTORY.md) | Ranked master table of every candidate, all 4 waves, tier-c API index, unverified appendix. **Start here to pick sources.** |
| [WHAT-LANDED.md](WHAT-LANDED.md) | Living status: totals, coordination state, open decisions. |
| `draft/crawl/*.yaml` (wave 1) + `draft/crawl/wave2,wave3,wave4/*.yaml` | The crawl-domain drafts, real `_template` schema, `enabled: false`. Ready to move into `config/domains/`. |
| `draft/new-clients.md`, `new-clients-wave2.md`, `-wave3.md`, `-wave4.md` | Tier-c API-client specs (endpoint, auth, format, CrawlResult mapping) + draft `api_sources.yaml` blocks. |
| `jurisdiction-additions.yaml` + `jurisdiction-additions-wave4.yaml` | Registry rows to merge into `config/jurisdictions.yaml` when the sources they serve promote. |
| `regions/`, `regions-wave2/`, `-wave3/`, `-wave4/` | Raw per-topic research findings (the evidence behind each entry). |
| `BRIEF.md` | The shared spec every research agent followed (schema, fields, verification rule). Reuse it for future waves. |

---

## 3. Open decisions for a human (nothing else blocks)

| # | Decision | Recommendation |
|---|---|---|
| 1 | **Push destination.** `origin` dual-pushes to your mirror AND the public OCP org. Branch is unpushed. | Mirror-only until the source branches consolidate, or leave parked. |
| 2 | **Kosovo** jurisdiction - no ISO 3166-1 code (contested). | Map track recommends `XK` + list-only/off-map (same class as N. Cyprus, Somaliland). Record on the `kosovo` row when decided. |
| 3 | **Belgium** regions - `belgium` registry row's aliases (wallonia/flanders/brussels) must be trimmed when their own subnational rows merge. | No map impact (coverage rolls up via `country_of`). Research track owns this modify; do it in the promotion PR. |
| 4 | **`gov.ie` overlap** + 4 national-portal dup pairs (argentina.gob.ar, gob.pe, gub.uy, aragon.es). | Keep as separate department entries or merge start_paths. Flagged inline. |
| 5 | **API keys** (free signup) for keyed clients. | Get keys before building: data.gov, Congress.gov, Open States, Korea Open Assembly, India OGD. |

---

## 4. Path A - Promote crawl sources into `config/domains/`

The straightforward win. Per source (or batch):

1. Pick entries from [INVENTORY.md](INVENTORY.md) (strongest first, or by region).
2. Move each entry from `draft/crawl/**` into the matching `config/domains/<region>.yaml`
   (the top comment in each draft file says which file). Set `enabled: true` when ready.
3. **In the SAME PR**, add any new region slug's row to `config/jurisdictions.yaml`
   (copy from `jurisdiction-additions*.yaml`). For a new COUNTRY fill `iso3` +
   `iso_numeric`. This is enforced: `tests/unit/test_jurisdictions.py::test_every_domain_slug_resolves`
   fails CI if a slug is missing.
4. Run `pytest` and `ruff check src/ tests/` (both must pass - see repo CLAUDE.md).
5. Rebase on main, open PR, merge when green. The map picks up new jurisdictions
   automatically via `/api/coverage`, no map code change.

Follow the **source-build doctrine** in the project memory / OCP docs: live re-probe
the day you enable, and never trust HTTP 200 (assert content-type, nonsense-query = 0,
etc.). Many of the "unverified" appendix items are WAF-blocked, not dead - re-check
from a normal network.

---

## 5. Path B - Build the tier-c API clients

Highest coverage per unit of work. Specs are in the `new-clients*.md` files.

**Do NOT rebuild these - already built on `feature/source-expansion-wave1`:**
`oireachtas`, `stortinget`, `egov_japan`, `nz_pco`, `sejm`, `tweede_kamer`, `camara`
(plus `diavgeia`, `kokkai`, `riigikogu`, `pmg`, `eu_have_your_say`, `govuk`).

**Strongest net-new KEYLESS clients to build first** (no signup, verified live):
US Federal Register (2,651 DC hits on a test query), EPA Envirofacts GHGRP, EU
Parliament Open Data, Scottish Parliament, Finland Eduskunta, LeyChile, Kenya Law,
Italy Senato SPARQL, plus the generic CKAN client (covers Argentina + others).

Pattern: subclass `PolicySource` in `src/sources/<id>.py`, register it, add the
`api_sources.yaml` entry (from the spec's fenced block), add a source test, live
smoke-test end to end before committing. See an existing client (e.g.
`src/sources/riksdagen.py`) for the shape.

---

## 6. Path C - Run another research wave

The harness is reusable. Pattern that worked (4 waves):

1. Pick net-new angles (geography, government tier, or policy theme) not yet mined -
   see the wave-4 angles for the latest frontier. Diminishing returns are setting in;
   bias toward angles that add new jurisdictions or unbuilt APIs.
2. Spawn one sonnet agent per angle (parallel), each told to: read `BRIEF.md`, dedup
   against `config/domains/**` + `docs/source-expansion/draft/crawl/**` + the built
   wave1 clients, verify every URL, write to `regions-waveN/<angle>.md`.
3. Spawn one sonnet assembler: dedup across waves, write `draft/crawl/waveN/*.yaml`
   (+ `new-clients-waveN.md`, + jurisdiction rows with ISO codes), append a Wave N
   section to INVENTORY.md.
4. Validate (parse, `enabled: false`, 0 id collisions, every region slug resolves via
   `jurisdictions.get()`), commit, update WHAT-LANDED + the coordination board, and
   send the map session the jurisdiction delta.

Use the top model to plan/validate, sonnet agents for the research and assembly.

---

## 7. Coordination rules (READ before touching git or shared config)

Full detail: `C:\Files\Code\OCP\20260718_0200_PolicyPulse_Track_Coordination.md`.

- **Shared working tree.** Multiple sessions run in this one checkout. **Never
  `git checkout`/`switch` to another branch here** - it rewrites files under another
  session mid-edit. The research track owns the primary checkout; other tracks use
  `git worktree`. (Rebasing in place is fine - it stays on this branch.)
- **File ownership.** Source track owns `src/sources/`, `config/domains/`,
  `docs/source-expansion/*`, and append-only rows to `config/jurisdictions.yaml`. The
  map track owns `src/api/routes/coverage.py` + `frontend/.../WorldMap*` and only reads
  the registry. Don't cross these.
- **The registry is the shared contract.** New source region -> one registry row.
  New country -> fill `iso3` + `iso_numeric` (the map's world-atlas join key).
- **Keep the map session in the loop** on material changes (new jurisdictions, new
  built APIs) via the coordination-doc status board + a direct message. Session:
  "PolicyPulse map interface design".

---

## 8. Recommended next action

Promote a small first batch (Path A) - the ~10 strongest, clearly-verified crawl
sources (e.g. the ones flagged "highest-value" per region in INVENTORY) plus their
registry rows - as one clean PR. That proves the promotion workflow end to end and
lights up the map, before committing to the larger build (Path B) or more research.
