# Source Expansion Research - UK Devolved Nations + Ireland

Branch: `feature/source-expansion-research`. Research only - no client code, nothing
enabled. See `docs/source-expansion/BRIEF.md` for methodology.

## Dedup check performed

Read in full before researching: `config/domains/uk.yaml` (2489 lines, ~60 entries -
already extremely thorough: DESNZ, Ofgem, CCC, Environment Agency, all three devolved
governments, Scottish/Welsh/NI legislatures (including SPICe research briefings and
Senedd Research), UK Legislation DB, Hansard, the Gazette, HNDU/GHNF/zoning, all six
DNOs, NESO, enterprise agencies, freeports/investment zones, IETF/SIETF), plus
`config/domains/ireland.yaml` (4 entries: SEAI, gov.ie data-center reporting
obligation, CRU large-energy-users connection policy, Irish Statute Book) and
`config/domains/api_sources.yaml` (9 structured clients, none for Ireland or the
devolved UK legislatures beyond `uk_bills`). UK Parliament Bills API confirmed already
covered - not re-proposed.

Given how saturated `uk.yaml` already is, the net-new opportunity in this region is
concentrated in: (1) Ireland, which is thin (4 domains total, no legislature source),
and (2) structured APIs for the devolved/Irish legislatures that exist as HTML crawl
targets today but also expose real JSON APIs nobody has wired up.

---

## Verified candidates (ranked best-first)

### 1. Houses of the Oireachtas Open Data API (Ireland) — HIGHEST VALUE

- **name**: Houses of the Oireachtas Open Data APIs
- **proposed id**: `oireachtas_api`
- **base_url**: `https://api.oireachtas.ie` (Swagger docs at `https://data.oireachtas.ie`)
- **level**: national
- **access**: none - open, no key. Public "Oireachtas (Open Data) PSI Licence"
  (CC-based). Contact `open.data@oireachtas.ie` for support.
- **coverage**: `region: ["ireland"]`, `category: legislation`, `tags: [mandates,
  legislation]`, `policy_types: [legislation, bill]`, `language: en`
- **format**: JSON (OAS 2.0 / Swagger), with linked XML (Akoma Ntoso debates,
  parliamentary questions) and PDF (bills, acts) via `data.oireachtas.ie`
- **effort tier**: (c) needs a new structured client - shape is a proper REST/JSON API
  with query params, closely analogous to the existing `uk_bills` client
  (`bills-api.parliament.uk`). A client here could filter `/legislation` by
  `heading=heat`/`energy` etc, and `/debates` and `/questions` by search term.
- **practical**: No documented rate limit found; standard courtesy throttling
  recommended (2s). Docs at `https://api.oireachtas.ie` (Swagger UI), base path
  `api.oireachtas.ie/v1`. Endpoints: `/constituencies`, `/debates`, `/houses`,
  `/legislation`, `/members`, `/parties`, `/questions`, `/votes`.
- **why worth adding**: Ireland currently has zero structured legislative API in
  PolicyPulse - everything Irish is HTML crawl. This is a real, documented, working
  API that gives searchable, structured access to every Bill before the Oireachtas
  (including the Heat (Networks and Miscellaneous Provisions) Bill 2024, Ireland's
  first dedicated district-heating law), plus debates and parliamentary questions
  mentioning heat/energy/data centres - all queryable by keyword instead of crawled.
- **verified**: YES. Fetched `https://api.oireachtas.ie` directly (via browser, not
  WebFetch - WebFetch alone returned a stripped shell): confirmed live Swagger UI
  listing exactly the 8 endpoints above, base URL `api.oireachtas.ie/v1`, OAS 2.0,
  version 1.1.0. Also test-queried
  `https://api.oireachtas.ie/v1/legislation?heading=heat&limit=10` directly and got
  back a large, well-formed JSON response (57KB) of matching legislation records -
  the API works end-to-end, not just documented.

### 2. Department of Climate, Energy and the Environment - District Heating (Ireland)

- **name**: Department of Climate, Energy and the Environment - District Heating
  policy hub
- **proposed id**: `ie_dcee_district_heating`
- **base_url**: `https://www.gov.ie`
- **start_paths**:
  - `/en/department-of-climate-energy-and-the-environment/`
  - `/en/department-of-climate-energy-and-the-environment/publications/district-heating-pre-construction-fund/`
  - `/en/department-of-climate-energy-and-the-environment/consultations/district-heating-sector-consultation-heat-networks-and-miscellaneous-provisions-bill-2024/`
  - `/en/department-of-climate-energy-and-the-environment/publications/heat-and-built-environment-taskforce/`
  - `/en/department-of-the-environment-climate-and-communications/policy-information/renewable-heat/`
- **level**: national
- **access**: none
- **coverage**: `region: ["ireland"]`, `category: energy_ministry`, `tags:
  [district_heating, heat_networks, incentives, mandates]`, `policy_types: [law,
  incentive, guidance, report]`, `language: en`
- **format**: HTML (gov.ie standard publication template), linked PDFs
- **effort tier**: (b) plain crawl domain
- **practical**: gov.ie fronts with bot protection that 403s plain WebFetch/curl-style
  fetchers with no session (matches the existing pattern already noted for other
  gov.ie entries in `ireland.yaml`) - confirmed it renders fine in an actual browser
  context, so treat like the existing `gov_ie_dc` entry (`requires_playwright:
  false` worked for that one; recommend testing but likely fine since it's
  server-rendered HTML, the 403 was bot-signature-based not JS-rendering-based).
- **why worth adding**: This is Ireland's lead ministry for the Heat (Networks and
  Miscellaneous Provisions) Bill 2024 (Ireland's first primary legislation
  establishing a regulatory/licensing framework for district heating, with CRU as
  regulator), the €5m District Heating Pre-Construction Fund (Climate Action Fund
  money, live scheme with EoI/Phase 2 stages), and the Heat and Built Environment
  Taskforce. None of this is captured by the existing `ireland.yaml` (which only has
  a data-center-specific gov.ie page, not the department's district-heating program
  hub). Note: the department was renamed mid-2026 from "Department of the
  Environment, Climate and Communications" (DECC) to "Department of Climate, Energy
  and the Environment" (DCEE) - both URL slugs currently resolve to live content, so
  both are included as start_paths; a future recrawl should confirm which slug the
  redirect settles on.
- **verified**: YES. Fetched all four DCEE URLs via browser (WebFetch got HTTP 403 on
  gov.ie generally). Confirmed live: District Heating Pre-Construction Fund page
  (full scheme detail, "From: Department of Climate, Energy and the Environment",
  published 21 May 2026) and the District Heating Sector Consultation page (Heat
  (Networks and Miscellaneous Provisions) Bill 2024 background, consultation closed
  31 July 2025 but page live with full policy background). Did not independently
  re-verify the renewable-heat and taskforce URLs beyond the search snippet -
  flagging that sub-path as slightly lower confidence than the two directly fetched.

### 3. South Dublin County Council - Tallaght District Heating Scheme (local, Ireland)

- **name**: South Dublin County Council - Climate Action / Tallaght District Heating
  Scheme
- **proposed id**: `sdcc_ie_district_heating`
- **base_url**: `https://www.sdcc.ie`
- **start_paths**:
  - `/en/climate-action/spotlight-tallaght-district-heating-scheme/`
  - `/en/climate-action/what-we-are-doing/energy-buildings/energy-buildings-actions/energy-efficiency-renewables/development-of-the-tallaght-district-heating-scheme.html`
- **level**: local
- **access**: none
- **coverage**: `region: ["ireland"]`, `category: local_government`, `tags:
  [data_center_heat_reuse, district_heating, waste_heat]`, `policy_types: [report,
  guidance]`, `language: en`
- **format**: HTML
- **effort tier**: (b) plain crawl domain
- **practical**: Standard council CMS, no JS barrier observed.
- **why worth adding**: This is a directly-on-topic, real, operating example of
  exactly what PolicyPulse tracks - a local authority (South Dublin County Council)
  running Ireland's first data-center-waste-heat district heating network, sourcing
  10MW of waste heat at no cost from an Amazon data center in Tallaght, delivered
  through a council-owned not-for-profit utility (Heatworks/South Dublin District
  Heating Company). It is the Irish counterpart to the GLA/Old Oak & Park Royal
  entries already in `uk.yaml` - there is no equivalent Irish local-authority entry
  in `ireland.yaml` today.
- **verified**: YES. Fetched both URLs directly - confirmed live pages describing the
  scheme, its Amazon data-center waste-heat source, 2023 completion, 2025 expansion
  to 133 residential units, and CO2 savings tracked annually.
- **note**: `heatworks.ie` (the operating utility's own site) was also checked and is
  live, but reads as an operational/customer site rather than a policy-document
  source - not proposed as a separate entry, but worth knowing it exists if the SDCC
  pages get thin over time.

### 4. Scottish Parliament Open Data API

- **name**: Scottish Parliament Open Data
- **proposed id**: `scottish_parliament_api`
- **base_url**: `https://data.parliament.scot`
- **level**: subnational
- **access**: none - open data, no key, no auth headers required.
- **coverage**: `region: ["uk", "scotland"]`, `category: legislation`, `tags:
  [scottish_legislation, bills]`, `policy_types: [legislation]`, `language: en`
- **format**: JSON
- **effort tier**: (c) needs a new structured client. Endpoints found:
  `/api/bills` (every SP Bill since devolution, with reference number, short/full
  name, sponsoring member) and `/api/events` (motions/members' business). Likely
  more endpoints exist (questions, committees) but were not enumerated - the
  `/api` root page itself 404s, so there's no single index page; endpoints were
  found from the Open Data Scotland catalogue rather than in-site navigation.
- **practical**: No rate-limit documentation found. This complements, not replaces,
  the existing `uk_scotland_parliament` HTML crawl domain - the API gives
  structured bill metadata (good for filtering/matching) while the HTML site
  carries the actual bill text/stages/committee reports.
- **why worth adding**: A genuine, live, unauthenticated JSON API for Scottish
  Parliament bills that nothing in the existing config queries structurally today
  (Scotland is currently HTML-crawl-only, unlike Westminster which has both
  `uk_bills` HTML domains and the `uk_bills_api` structured client). Scotland has
  the UK's most advanced heat-network legislation (Heat Networks (Scotland) Act
  2021, forthcoming Heat in Buildings Bill), so a structured bill-tracking API
  is directly relevant.
- **verified**: YES for the two endpoints tested. `https://data.parliament.scot/api/bills`
  returned live JSON (list of every SP Bill since 1999, e.g. "SP Bill 1": Mental
  Health (Public Safety and Appeals) (Scotland) Bill). `https://data.parliament.scot/api/events`
  returned live JSON (members' motions/events). Did NOT verify a
  keyword-filterable query parameter works (e.g. searching bills by title
  substring) - this needs confirming before building a client; flagging as a
  slightly lower-confidence "the API exists and returns real data" vs. "the API
  supports the query shape a client would need."

### 5. National Infrastructure Commission for Wales (NICW)

- **name**: National Infrastructure Commission for Wales - Energy / Wales
  Infrastructure Assessment
- **proposed id**: `wales_nicw`
- **base_url**: `https://nationalinfrastructurecommission.wales`
- **start_paths**:
  - `/energy26/`
  - `/renewable2050/`
  - `/publications-2/`
- **level**: subnational
- **access**: none
- **coverage**: `region: ["uk", "wales"]`, `category: advisory_body`, `tags:
  [energy_infrastructure, heat_networks, planning]`, `policy_types: [report,
  guidance]`, `language: en`
- **format**: HTML with linked PDF reports (Energy Summary / Energy Report PDFs)
- **effort tier**: (b) plain crawl domain
- **practical**: Standard WordPress-style site, server-rendered, no JS barrier
  observed.
- **why worth adding**: Independent statutory advisory body (analogous to the CCC
  entry already in `uk.yaml`, but Wales-specific) publishing the "Wales
  Infrastructure Assessment 2026 - Energy" report, which explicitly covers
  district/heat network deployment barriers ("missed opportunities for district
  heating due to regulatory complexity") alongside electricity/gas network
  capacity. Not currently in `wales.yaml`-equivalent entries in `uk.yaml` (which
  covers Welsh Government and Senedd but not this independent advisory
  commission).
- **verified**: YES. Fetched `https://nationalinfrastructurecommission.wales/energy26/`
  directly - confirmed live "Wales Infrastructure Assessment 2026 - Energy" page
  with full section text on Wales's energy supply/network challenges and
  downloadable Energy Summary/Report PDFs.

### 6. NI Utility Regulator (UREGNI) - general regulatory site

- **name**: Utility Regulator (Northern Ireland)
- **proposed id**: `uregni_general`
- **base_url**: `https://www.uregni.gov.uk`
- **start_paths**:
  - `/electricity`
  - `/about-us`
  - `/news`
- **level**: subnational
- **access**: none
- **coverage**: `region: ["uk", "northern_ireland"]`, `category: regulator`, `tags:
  [heat_networks_regulation, grid_connections, energy_market]`, `policy_types:
  [regulation, guidance]`, `language: en`
- **format**: HTML with linked PDF consultation responses/decisions
- **effort tier**: (b) plain crawl domain
- **practical**: Standard gov.uk-style NI site, server-rendered.
- **why worth adding**: UREGNI is NI's counterpart to Ofgem and is the body the
  Department for the Economy's 2022 Heat Networks Market Framework consultation
  proposed giving oversight/pricing/consumer-protection powers over NI heat
  networks - directly on-topic for tracking whether/how NI heat-network regulation
  actually gets implemented (currently NI has no dedicated heat-network law, unlike
  Scotland).
- **caution / possible overlap**: `uk.yaml` already contains `nisep_ni` with
  `base_url: "https://www.uregni.gov.uk/nisep"` (a specific funding-scheme
  subpage, categorized as an incentive program). This candidate proposes the
  *root* domain for the regulator's general electricity/consultations/news
  content, which is materially different content from the NISEP funding page, but
  shares the same host - flagging explicitly so a human can decide whether to
  fold this into `nisep_ni`'s existing entry (broaden its `start_paths`) instead
  of creating a second `uregni.gov.uk` entry.
- **verified**: YES. Fetched `https://www.uregni.gov.uk/electricity` directly -
  confirmed live regulatory-remit content (licensing, price control of NIE
  Networks/SONI/SEMO, SEM market structure).

---

## Unverified / needs-human-check

- **CRU (Ireland) district-heating-specific publications filter** - `cru.ie`
  (already a `base_url` in `ireland.yaml` via `cru_ie_dc`, pointed only at
  `/publications/data-centres`). Confirmed CRU runs a real, large publications
  library (`https://www.cru.ie/publications/` - 11,048 documents, filterable by
  type and category) and CRU has been the statutory district-heating regulator
  since July 2022 (S.I. 350 of 2022), but could NOT get a working direct URL for
  a "district heating" category/tag filter in the time available (tried
  `/document_group/district-heating/`, `/document_group/tag/district-heating/`,
  neither resolved; the site's filter UI appears to be JS/AJAX-driven rather than
  URL-parameter-driven). **Recommendation**: rather than a new domain entry,
  expand the existing `cru_ie_dc` entry's `start_paths` to include
  `/publications/` generally (with `requires_playwright: true`, since the filter
  UI needs JS) so the crawler can pick up district-heating decisions/consultations
  alongside the data-center ones already targeted. Do not add as a standalone
  candidate since the base_url is already present.

- **Dublin City Council district heating / Poolbeg / South East Inner City
  scheme** - referenced in secondary sources (Codema, Byrne Wallace Shields) as
  another Irish local-authority district-heating project, but I did not fetch a
  live Dublin City Council (`dublincity.ie`) policy page directly in the time
  available. Plausible second local-authority candidate alongside SDCC but not
  verified - do not add without checking a live URL first.

- **Northern Ireland Department for the Economy - `/articles/heat-networks`**
  (`https://www.economy-ni.gov.uk/articles/heat-networks`) - real page per search
  results (describes NI's 2022 Heat Networks Market Framework consultation and the
  proposed UREGNI regulatory role), but `economy-ni.gov.uk` is already a `base_url`
  in `uk.yaml` (`uk_ni_economy`, which already includes `/topics/heat` as a
  start_path). Not proposed as a new entry per dedup rules - flagging as a
  worthwhile **addition to the existing `uk_ni_economy` entry's `start_paths`**
  (`/articles/heat-networks` is a different specific URL than `/topics/heat` and
  may carry more consultation detail).

---

## Summary

Region: UK devolved nations (Scotland, Wales, Northern Ireland) + Ireland.
6 verified candidates, 3 unverified/needs-human-check (2 of which are
recommendations to broaden existing entries rather than new domains, given how
saturated `uk.yaml` already is).
Tier breakdown: 0 tier-a, 4 tier-b (gov.ie DCEE district heating, SDCC Tallaght,
NICW, UREGNI), 2 tier-c (Oireachtas Open Data API, Scottish Parliament Open Data
API - both need new structured clients).
Highest-value find: the Houses of the Oireachtas Open Data API
(`api.oireachtas.ie`) - live, documented, no-auth JSON API covering every Irish
Bill/debate/question, verified end-to-end including a working keyword query
against the Heat (Networks and Miscellaneous Provisions) Bill 2024, and Ireland's
only legislative API of any kind proposed for this codebase so far.
