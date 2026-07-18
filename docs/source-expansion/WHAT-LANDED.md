# What Landed - Source Expansion Status

Living status of the source-expansion research. Updated each research wave.
Branch: `feature/source-expansion-research` (local commits, not pushed).
Nothing here is enabled in a live scan - every draft crawl entry is `enabled: false`
and no client code is written. This is a review queue.

Last updated: 2026-07-18.

---

## Rebase + jurisdiction-registry compliance (2026-07-18)

This branch was rebased onto the latest `main`, which now includes the merged
**canonical jurisdiction registry** (`config/jurisdictions.yaml` +
`src/core/jurisdictions.py`). Region validation changed: a source's `region:`
value is now resolved against that registry (`jurisdictions.get()`), not the old
`VALID_REGIONS` dict. Re-validated all 371 draft entries against it:

- **67 of 70 distinct region values already resolve** - including everything the
  earlier waves flagged as "not in VALID_REGIONS" (central_asia, caucasus, the
  city/province slugs, china, malaysia, ...). The registry is far richer + has
  alias/substring resolution.
- **3 values still miss**, in 5 of 371 entries: `supranational` (4), `global` (3),
  `manitoba` (1). Warnings only, never errors, and the drafts are `enabled: false`,
  so nothing is broken.
- Fix is proposed in **[jurisdiction-additions.yaml](jurisdiction-additions.yaml)**:
  two rows to merge into the registry (a `manitoba` subnational row like
  ontario/quebec; a `global` group row like europe/apac, aliasing `supranational`).
  My earlier "add to VALID_REGIONS" note is obsolete - the registry's own rule is
  "add a source's new region = add one row in jurisdictions.yaml."

### Coordination with the map interface + wave1 build track

Per the multi-track plan (`C:\Files\Code\OCP\20260718_0200_PolicyPulse_Track_Coordination.md`):

- **The jurisdiction registry is the shared contract.** Map track reads it
  (`/api/coverage` iterates it; new countries "simply light up", no map code change).
  Source track owns `src/sources/`, `config/domains/`, `docs/source-expansion/*` and
  **appends rows to `config/jurisdictions.yaml`** (append-only, conflict-safe).
- **CI guardrail**: `test_every_domain_slug_resolves` globs `config/domains/**`. My
  drafts live in `docs/`, so they don't trip it yet; the registry rows get added **in
  the same PR that promotes a source into `config/domains/`** (the plan's rule, line 29).
  So [jurisdiction-additions.yaml](jurisdiction-additions.yaml) (manitoba + global)
  is correctly timed - merge those rows when promoting the sources they serve. For any
  new *country* not yet in the registry, fill `iso3` + `iso_numeric` (the map's join key).
- This branch stays docs-only for now, so it cannot conflict with the map or registry
  work. Map is FINALIZED and ready to build (Phase 1 = `GET /api/coverage`).
- **RESOLVED with the map track (2026-07-18):** non-country jurisdictions render via a
  **supranational tray** - `/api/coverage` returns a `supranational` array, shown as
  off-map clickable chips. So the staged `global` IGO bucket lands cleanly (tray chip),
  and `manitoba` fills + rolls up to Canada via `country_of`. Nothing from the corpus
  drops off the map. Promotion instruction from the map track: **for any new COUNTRY
  not yet in the registry, fill `iso3` + `iso_numeric`** (the map's world-atlas join
  key), not just the slug. Subnational/group rows don't need iso_numeric.
- **Shared-working-tree rule (coordination doc):** both sessions use one physical
  checkout; a `git checkout`/`switch` to another branch here rewrites files for the
  other session mid-edit. The **research track owns the primary checkout** - stay on
  `feature/source-expansion-research`, never switch branches in it; other tracks use a
  `git worktree`. (Rebasing in place is fine; it stays on this branch.)

### ALREADY BUILT on `feature/source-expansion-wave1` - do NOT rebuild

7 of my tier-c API proposals are already implemented on that branch (23 clients total).
Cross off before building any client from my inventory:

| My proposal | Built client id |
|---|---|
| Oireachtas (Ireland) | `oireachtas` |
| Norway Storting | `stortinget` |
| Japan e-Gov Law | `egov_japan` |
| NZ Legislation (PCO) | `nz_pco` |
| Poland Sejm | `sejm` |
| Netherlands Tweede Kamer | `tweede_kamer` |
| Brazil Camara | `camara` |

Also built there (not all in my formal tier-c list): `diavgeia` (Greece), `kokkai`
(Japan Diet), `riigikogu` (Estonia), `pmg` (South Africa PMG), `eu_have_your_say`,
`govuk`. So the genuinely net-new tier-c set to build shrinks from 41 to ~34 - the
strongest remaining keyless ones: US Federal Register, EPA GHGRP, EU Parliament,
Scottish Parliament, Finland Eduskunta, LeyChile, Kenya Law, Open States.

---

## Totals so far

| Wave | Verified sources | Crawl domains (tier-b) | New-client APIs (tier-c) | Unverified (needs human check) |
|---|---|---|---|---|
| Wave 1 | 154 | 138 | 16 | 45 |
| Wave 2 | 158 | 141 | 17 | ~71 |
| Wave 3 | 100 | 92 | 8 | ~34 |
| **Combined (1+2+3)** | **412** | **371** | **41** | **~150** |

Deduped against 390 existing sources in `config/domains/**` (33 country files +
50-state `us/` subdir + 9 structured API clients), plus cross-wave dedup (wave 2
merged 3 Swiss-canton duplicates against wave 1).

**Wave 2 added** (angles wave 1 under-mined): 7 keyless legislation APIs (Poland Sejm,
NL Tweede Kamer, Brazil Camara, AU Federal Register of Legislation, Spain Congreso,
CH Curia Vista, FR Assemblee Nationale), 18 grid operators/TSOs (ENTSO-E + 12 EU TSOs
+ 4 US ISOs + AEMO), 15 standards bodies (China SAMR free PUE-limit text), 39 sources
across 30 uncovered countries, 50 deep-subnational, 11 US county/municipal, 8
multilateral bodies + 10 open-data portal APIs.

**Wave 3 added** (thematic angles): 22 carbon/ETS/GHG bodies (EPA Envirofacts GHGRP
API - keyless facility emissions), 21 municipal heat-zoning (Helsinki Helen Oy live
heat-recovery program), 19 DC tax-incentive programs (Singapore DC-CFA2: incentive
requires PUE <=1.25), 13 environmental permitting/EIA (Ireland EPA DC emissions
licences), 9 water/cooling (Virginia DEQ HB589 water disclosure), 9 digital-infra
strategies (Ireland DETE 80%-renewables rule), 6 more legislation APIs (US Federal
Register - keyless, 2,651 DC hits; Open States - all 50 states; Congress.gov).

---

## Where the files are

- **[INVENTORY.md](INVENTORY.md)** - ranked master table of every verified candidate,
  tier-c API index, and the unverified appendix (with the reason each failed).
- **[draft/crawl/*.yaml](draft/crawl/)** - the tier-b crawl domains, in real config
  schema, `enabled: false`. One file per region.
- **[draft/new-clients.md](draft/new-clients.md)** - the tier-c API-client specs +
  draft `api_sources.yaml` blocks.
- **[regions/*.md](regions/)** - wave-1 raw per-region findings.
- **regions-wave2/*.md** - wave-2 raw findings (this wave).

---

## Highest-value finds (queryable APIs, mostly no login)

| Source | What it gives | Access | Wave |
|---|---|---|---|
| European Parliament Open Data API v2 | pan-EU legislative process | none | 1 |
| api.oireachtas.ie | every Irish bill/debate | none | 1 |
| Japan e-Gov Law API v2 | Japanese statute text | none | 1 |
| Korea Open Assembly / Open Law APIs | Korean legislation | key | 1 |
| LeyChile / BCN XML | full consolidated Chilean law | none | 1 |
| Scottish Parliament / Storting (NO) / Eduskunta (FI) / NZ Legislation APIs | national legislation | none | 1 |
| data.europa.eu Search + OECD SDMX | multi-country policy datasets | none | 1 |

Standout policy finds: Tokyo Mar-2026 DC waste-heat guideline; Geneva law naming
server heat for mandatory recovery; Virginia SCC data-center rate class; IEA 4E EDNA
data-centre efficiency workstream.

---

## What YOU need to decide (before anything is enabled)

1. **`gov.ie` overlap** - one Ireland draft (`ie_dcee_district_heating`) shares a
   base_url with the existing `gov_ie_dc` entry. Keep separate or merge start_paths.
   Flagged inline in `draft/crawl/uk-ireland.yaml`.
2. **4 national-portal duplicate pairs** (wave 2 validation) - two draft entries each
   share one unified portal (`argentina.gob.ar`, `gob.pe`, `gub.uy`, `aragon.es`).
   Keep as separate department entries or merge each pair's start_paths.
3. **Jurisdiction-registry additions** - merge the 2 proposed rows in
   [jurisdiction-additions.yaml](jurisdiction-additions.yaml) (`manitoba`, and a
   `global` bucket for IGO sources). Needs the registry/map owner; includes one map
   rendering decision (how to show a members-less "Global" bucket). Supersedes the
   old "add to VALID_REGIONS" note.
4. **US data.gov now needs an api_key** (was keyless) - noted for the portal-API client.

None of these block review; they are the open human decisions so far.

---

## Suggested next steps (my recommendation, your call)

- Convert the ~8 no-auth legislative APIs (Oireachtas, Scottish Parliament, Storting,
  Eduskunta, e-Gov Law, LeyChile, NZ Legislation, EU Parliament) into real
  `src/sources/` clients on a follow-up branch - highest coverage per unit of work.
- Batch-enable the strongest crawl domains after a human skim of the INVENTORY table.
