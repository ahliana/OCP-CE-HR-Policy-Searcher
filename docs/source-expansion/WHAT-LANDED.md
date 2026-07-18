# What Landed - Source Expansion Status

Living status of the source-expansion research. Updated each research wave.
Branch: `feature/source-expansion-research` (local commits, not pushed).
Nothing here is enabled in a live scan - every draft crawl entry is `enabled: false`
and no client code is written. This is a review queue.

Last updated: 2026-07-18.

---

## Totals so far

| Wave | Verified sources | Crawl domains (tier-b) | New-client APIs (tier-c) | Unverified (needs human check) |
|---|---|---|---|---|
| Wave 1 | 154 | 138 | 16 | 45 |
| Wave 2 | 158 | 141 | 17 | ~71 |
| Wave 3 | *in progress* | - | - | - |
| **Combined (1+2)** | **312** | **279** | **33** | **~116** |

Deduped against 390 existing sources in `config/domains/**` (33 country files +
50-state `us/` subdir + 9 structured API clients), plus cross-wave dedup (wave 2
merged 3 Swiss-canton duplicates against wave 1).

**Wave 2 added** (angles wave 1 under-mined): 7 keyless legislation APIs (Poland Sejm,
NL Tweede Kamer, Brazil Camara, AU Federal Register of Legislation, Spain Congreso,
CH Curia Vista, FR Assemblee Nationale), 18 grid operators/TSOs (ENTSO-E + 12 EU TSOs
+ 4 US ISOs + AEMO), 15 standards bodies (China SAMR free PUE-limit text), 39 sources
across 30 uncovered countries, 50 deep-subnational, 11 US county/municipal, 8
multilateral bodies + 10 open-data portal APIs.

**Wave 3 in progress** (thematic angles): DC water/cooling regulation, carbon/ETS,
DC tax incentives, environmental permitting/EIA, Open States + Congress.gov + Federal
Register + more legislature APIs, digital-infra ministries & national DC strategies,
municipal heat-network zoning.

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
3. **Enum additions** - 3 region values (`manitoba`, `supranational`, `global`) sit
   outside `VALID_REGIONS` in `src/core/config.py` (loader only warns). One small edit
   adds them; I can do it on your go, or map them to existing buckets instead.
4. **US data.gov now needs an api_key** (was keyless) - noted for the portal-API client.

None of these block review; they are the open human decisions so far.

---

## Suggested next steps (my recommendation, your call)

- Convert the ~8 no-auth legislative APIs (Oireachtas, Scottish Parliament, Storting,
  Eduskunta, e-Gov Law, LeyChile, NZ Legislation, EU Parliament) into real
  `src/sources/` clients on a follow-up branch - highest coverage per unit of work.
- Batch-enable the strongest crawl domains after a human skim of the INVENTORY table.
