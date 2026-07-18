# New Structured Clients Needed — Wave 3 (tier-c)

Eight wave-3 tier-c candidates, across three source files
(`docs/source-expansion/regions-wave3/more-legislation-apis.md`,
`docs/source-expansion/regions-wave3/carbon-ets.md`, and
`docs/source-expansion/regions-wave3/permitting-eia.md`) — each needs a NEW
`source_type` client under `src/sources/` (registered in
`src/sources/__init__.py`) because none fit the shape of the 9 existing
clients (`riksdagen`, `uk_bills`, `legisinfo`, `folketing`, `eurlex_nim`,
`legiscan`, `govinfo`, `regulations_gov`, `dip`), the 16 wave-1 tier-c clients
(`draft/new-clients.md`), or the 17 wave-2 tier-c clients
(`draft/new-clients-wave2.md`). No client code is included here — this is a
spec for a future engineer, per the brief. Dedup confirmed against all three
lists plus every existing `api_sources.yaml` entry — no `source_type` or
`base_url` overlaps.

Each spec below: proposed `source_type` id, base URL, auth, response format,
endpoint(s), CrawlResult field mapping, pagination/rate-limit notes. The draft
`api_sources.yaml` entries (all `enabled: false`) follow in one fenced block
at the end of this file.

---

## 1. `federal_register_api` — US Federal Register API

- **Region**: United States (national) — **highest-value find of wave 3's
  more-legislation-apis pass**
- **API base**: `https://www.federalregister.gov`
- **Auth**: none — fully keyless, no signup, no headers
- **Format**: JSON
- **Endpoints to call**: `GET /api/v1/documents.json?conditions[term]=<keyword>`
  (full-text search across all Federal Register documents — proposed rules,
  final rules, notices, presidential documents — with agency/date/type
  filters, paginated via `next_page_url`); `GET /api/v1/documents/{number}.json`
  for detail; `GET /api/v1/agencies` for the agency list.
- **CrawlResult mapping**: `url` = response's `html_url` field; `title` =
  document `title` field; `content` = document `abstract` field (full text
  requires a follow-up fetch of `pdf_url`/`body_html_url`); `lifecycle_stage`
  = `type` field (`RULE`, `PRORULE`, `NOTICE`, `PRESDOCU`).
- **Pagination/rate limits**: no documented rate limit observed; response
  includes `count`, `next_page_url` for straightforward pagination.
- **Why it matters**: distinct from Regulations.gov (the docket/public-
  comment layer, already an existing client) — this is the *official
  publication of record* for every US federal rule/notice. Verified live,
  end-to-end, on-topic this session:
  `curl "https://www.federalregister.gov/api/v1/documents.json?per_page=1&conditions%5Bterm%5D=data+center+waste+heat"`
  returned `{"count":2651,...}` with a real first result — a DOE "Request
  for Information on Artificial Intelligence Infrastructure on DOE Lands"
  notice (document `2025-05936`, published 2025-04-07) discussing AI/data-
  center infrastructure siting on federal land.

---

## 2. `congress_gov_api` — Congress.gov API (US federal bill lifecycle)

- **Region**: United States (national)
- **API base**: `https://api.congress.gov`
- **Auth**: **api_key** — free registration at `https://api.congress.gov/sign-up/`
  (confirmed live, HTTP 200 signup page). Env var: `CONGRESS_GOV_API_KEY`.
  Pass as `?api_key=` query param or `X-Api-Key` header.
- **Format**: JSON
- **Endpoints to call**: `GET /v3/bill` (bill list/search); `GET /v3/bill/{congress}/{type}/{number}`
  (detail, incl. text versions, actions, cosponsors, committees); `GET /v3/law`;
  `GET /v3/summaries` (CRS-authored bill summaries — useful for keyword-
  matching without pulling full text).
- **CrawlResult mapping**: `url` = constructed congress.gov bill page from
  `congress`/`type`/`number`; `title` = bill `title` field; `content` =
  CRS summary text from `/v3/summaries`; `lifecycle_stage` = latest `action`
  entry's `text`/`type`.
- **Pagination/rate limits**: rate limit not published in the error
  response; standard REST, no documented pagination-cap issues. Official
  successor to the deprecated ProPublica Congress API.
- **Why it matters**: only structured source of the actual bill-introduction-
  to-law pipeline for US federal legislation with full-text search on bill
  summaries — GovInfo (existing client) serves finished document
  collections, not a queryable bill-lifecycle API. Verified: `curl
  "https://api.congress.gov/v3/bill?limit=1"` (no key) returned a real,
  well-formed JSON auth-gate error naming the exact signup URL, confirming
  the service and auth mechanism are live, not hallucinated.

---

## 3. `openstates_api` — Open States API v3 (all 50 US states + DC + PR)

- **Region**: United States (subnational — one integration covers all 50
  states at once)
- **API base**: `https://v3.openstates.org`
- **Auth**: **api_key** — free registration at
  `https://openstates.org/account/profile/`. Env var: `OPENSTATES_API_KEY`.
  Pass via `X-API-KEY` header or `?apikey=` query param.
- **Format**: JSON
- **Endpoints to call**: `GET /jurisdictions`; `GET /people` (legislators,
  incl. geolocation lookup); `GET /bills?jurisdiction=<state>&q=<keyword>`
  (search by jurisdiction/session/query, returns bill actions, sponsors,
  linked full-text/version documents); `GET /committees`; `GET /events`.
  Interactive docs at `v3.openstates.org/docs/`.
- **CrawlResult mapping**: `url` = `openstates_url` field on the bill
  object; `title` = bill `title` field; `content` = latest `action`
  description + linked version document text; `lifecycle_stage` = bill
  `latest_action` field.
- **Pagination/rate limits**: no rate-limit figure surfaced in the error
  response or docs page this pass — confirm exact limits at key-
  registration time.
- **Why it matters**: complementary to the existing `legiscan` client, not a
  duplicate — LegiScan's free tier is query-limited and full bill text/bulk
  access sits behind a paid tier; Open States (nonprofit Plural Policy/Open
  States Foundation) covers the same 50-state bill corpus plus committees/
  events/geolocation-based legislator lookup with a free key. Single best
  "one integration = a whole jurisdiction" multiplier for US subnational
  coverage. Verified: `curl "https://v3.openstates.org/bills?jurisdiction=Texas&q=energy"`
  (no key) returned the real, documented auth-gate JSON naming the exact
  signup URL.

---

## 4. `kenya_law_api` — Kenya Law / National Council for Law Reporting search API

- **Region**: Kenya (national)
- **API base**: `https://new.kenyalaw.org`
- **Auth**: none — keyless, no signup
- **Format**: JSON (documents modeled in Akoma Ntoso / FRBR URIs — the same
  open-legal-data standard used by AfricanLII / Laws.Africa across
  multiple African jurisdictions)
- **Endpoints to call**: `GET /search/api/documents/?search=<term>` (full-text
  search across all document types); add `&doc_type=legislation` to
  restrict to Acts/statutes (vs. `judgment` for case law).
- **CrawlResult mapping**: `url` = constructed from the returned FRBR
  work/expression URI; `title` = `title` field; `content` = `citation` +
  `date` + any excerpt fields present; `lifecycle_stage` = not directly
  applicable (enacted-law repository, not a bill tracker).
- **Pagination/rate limits**: no documented rate limit found this pass;
  clean REST, no pagination issues observed at `count`-level.
- **Why it matters**: only verified national gazette/legislation API found
  in sub-Saharan Africa this pass — a live keyword + doc_type filter
  returned a direct hit on Kenya's Energy Act. The same AfricanLII/
  Laws.Africa AKN pattern likely recurs across other African LII sites -
  worth a follow-up pass if African coverage becomes a priority. Verified:
  `curl "https://new.kenyalaw.org/search/api/documents/?search=energy&doc_type=legislation"`
  returned real JSON: `{"count": 492, "results": [{"doc_type":
  "legislation", "title": "Energy Act", "date": "2022-12-31", "citation":
  "Cap. 314", ...}]}`.

---

## 5. `oparl` — oParl standard (German municipal council information systems)

- **Region**: Germany — **municipal/local only, NOT state-level** (see scope
  correction below)
- **API base**: per-body, no single root; verified example: Cologne,
  `https://ratsinformation.stadt-koeln.de/oparl/system`
- **Auth**: none — keyless, standardized JSON-LD schema (`schema.oparl.org`)
- **Format**: JSON (JSON-LD)
- **Endpoints to call**: every implementing body exposes the same shape
  starting from a `System` object: `GET /oparl/system` → links to `body` →
  `organization`, `meeting`, `paper` (agenda items/motions/resolutions —
  where waste-heat/district-heating council motions would live), `person`.
- **CrawlResult mapping**: `url` = `paper`'s own web URL field (`web`);
  `title` = `paper.name`; `content` = `paper.mainFile` text or linked
  document; `lifecycle_stage` = not directly present in the schema —
  would need deriving from `consultation` sub-objects.
- **Pagination/rate limits**: no rate limit documented; each municipality's
  instance is independently hosted/maintained (uptime varies — a Bonn
  instance tried this pass returned HTTP 500).
- **Scope correction — include only as municipal, not Landtag**: oParl is
  implemented by city/county council information systems
  (Ratsinformationssysteme), NOT by Landtage (German state parliaments). No
  Landtag running an oParl endpoint was found or is known to exist; Landtage
  run bespoke parliamentary-documentation systems (already covered via
  direct Landesrecht/ministry crawl domains in dach.yaml instead). Per the
  brief's "oParl is municipal-only — include only if a concrete on-topic
  endpoint was verified" instruction: **a concrete endpoint WAS verified**
  (Cologne, below), so this is included, but flagged as lower-priority than
  originally hoped since it does not reach the Landtag level.
- **Why it matters**: real, live, standardized, keyless municipal
  legislative-motion API, best used opportunistically for specific high-
  value cities (e.g. a city known to be piloting DC district heating) once a
  registry of live endpoints is compiled — no central directory of live
  endpoints was found this pass (the `oparl.org/koerperschaften/` listing
  page redirected but its content wasn't independently enumerated), so a
  client would need a small hardcoded list of known-good municipal
  endpoints. Verified: `curl "https://ratsinformation.stadt-koeln.de/oparl/system"`
  returned a real JSON-LD `System` object for "Stadt Koeln - OParl 1.1"
  with a working `body` link.

---

## 6. `epa_ghgrp_envirofacts_api` — EPA Envirofacts Greenhouse Gas RESTful Data Service

- **Region**: United States (national)
- **API base**: `https://data.epa.gov` (documented at
  `https://www.epa.gov/enviro/greenhouse-gas-restful-data-service`)
- **Auth**: none — fully keyless, no signup, no headers required
- **Format**: JSON (also XML, CSV, HTML, JSONP, Parquet, PDF via URL suffix)
- **Endpoints to call**: a generic Oracle-table-passthrough shape — one URL
  segment per table name, e.g. `GET /efservice/PUB_DIM_FACILITY/JSON/rows/0:10`
  (facility name/address/lat-long/NAICS code/year for every reporting
  facility); other `/efservice/<TABLE>/<FORMAT>` tables (not individually
  tested this session) cover reported emissions by subpart/gas.
- **CrawlResult mapping**: `url` = constructed EPA GHGRP facility page from
  `FACILITY_ID`; `title` = `FACILITY_NAME`; `content` = address/NAICS/
  program fields concatenated; `lifecycle_stage` = not applicable (a
  reporting dataset, not a bill/regulation tracker).
- **Pagination/rate limits**: no documented hard rate limit found this
  session; the `/JSON/` suffix in the URL path did not change the actual
  response format in this session's test (came back as XML regardless) — a
  human/engineer should confirm the correct format-selector syntax before
  building a client (the docs page has the full syntax reference).
- **Why it matters**: the only true open-data API found in this entire
  carbon/ETS pass — live, keyless, facility-level US GHG emissions data
  updated annually, pairing with the `us_epa_ghgrp` crawl-domain entry
  (wave-3 carbon-ets.yaml) that covers the reporting-requirement guidance
  pages. A generic table-passthrough rather than a purpose-built search API,
  so response parsing will be table-schema-specific. Verified: `curl
  "https://data.epa.gov/efservice/PUB_DIM_FACILITY/JSON/rows/0:2"` returned
  HTTP 200 with real facility records (e.g. FACILITY_ID 1000001, "PSE
  Ferndale Generating Station," Ferndale WA, NAICS 221112, YEAR 2010) with
  full address/lat-long/NAICS/program fields.

---

## 7. `ga_epd_permit_search` — Georgia EPD Air Permit Search Engine

- **Region**: Georgia, US (subnational)
- **API base**: `https://permitsearch.gaepd.org`
- **Auth**: none required to search; unclear if bulk/API access exists —
  flag for a human to check with GA EPD directly
- **Format**: HTML search UI (form-driven); PDF permit documents (e.g. Title V
  permits naming DC operators with 50+ diesel emergency generators)
- **source_type feasibility**: searchable web form (AIRS Number, Facility
  Name, Permit Number/SIC Code) backed by a database; NO documented public
  REST API was found — this needs a client that drives the search form (or
  scrapes result pages), not a documented-API-shaped client. Distinct base_url
  from the existing static crawl domain `ga_epd` (`epd.georgia.gov`, which
  only crawls `/air-protection` and `/water-protection` pages) — this would
  be a facility-level searchable permit database supplement, not a
  replacement.
- **CrawlResult mapping**: `url` = permit-detail page URL from the search
  result; `title` = facility name + permit number; `content` = permit PDF
  text (once fetched); `lifecycle_stage` = permit status field on the
  results page (issued/pending/expired).
- **Pagination/rate limits**: no published rate limit or ToS review done
  this pass — recommend a manual ToS check before scripted querying.
- **Why it matters**: Georgia is a fast-growing DC market; this facility-
  level searchable permit database would let a future client pull specific
  DC air-permit records (e.g. the confirmed 50+-generator synthetic-minor
  Title V permit) rather than relying on generic page crawling. Verified:
  fetched, confirmed a live search form with the three fields listed and a
  "Search Permits" button; could not confirm from static content whether
  the backend is actually responsive to a live query (not tested, per
  read-only research scope).

---

## 8. `eea_industrial_emissions_portal` — European Industrial Emissions Portal (EEA)

- **Region**: EU/EEA (supranational)
- **API base**: `https://industry.eea.europa.eu`
- **Auth**: none — open download, no key found required for the dataset
  pages
- **Format**: HTML portal + CSV/XML bulk download + geospatial catalogue
  record (INSPIRE/ISO19139)
- **source_type feasibility**: dataset download (CSV/XML) of facility-level
  IED installations, E-PRTR releases, and Large Combustion Plant (LCP) data
  across the EU/EEA, per the "Industrial Reporting under IED 2010/75/EU and
  E-PRTR Regulation (EC) 166/2006" catalogue record; a GeoNetwork/CSW-style
  metadata API backs the spatial catalogue. NO existing client handles
  OGC/GeoNetwork-shaped or bulk-CSV EU environmental data — needs a NEW
  client. Download-only, not a live query API in the REST sense.
- **CrawlResult mapping**: `url` = dataset landing page or CSV/XML download
  link; `title` = installation/facility name from the CSV row; `content` =
  concatenated pollutant/threshold/permit fields; `lifecycle_stage` = not
  applicable (a reporting dataset).
- **Pagination/rate limits**: dataset covers E-PRTR facility releases
  2007-2024, IED installations 2017-2024, LCPs 2016-2024; no rate limit
  found on the static pages.
- **Why it matters**: the closest thing to an EU-wide, cross-country
  permitted-installation register that exists, entirely absent from
  `eu.yaml` today (EUR-Lex/JRC/RVO/Commission guidance only, no
  installation-level permit data). IMPORTANT CAVEAT: most standalone data-
  centre backup-generator setups sit below the IED Annex I / Large
  Combustion Plant thermal-input thresholds (the individual national
  permitting bodies in wave-3 permitting-eia.yaml — e.g. Hesse's RP
  Darmstadt or Ireland's EPA — are triggered at lower or facility-aggregate
  thresholds), so this portal will likely only surface a minority of
  DC-relevant installations — highest-value use is as a cross-check/
  discovery layer for which DCs *do* cross IED/LCP thresholds, not primary
  coverage. Verified: fetched `/industrial-emissions/about` (HTTP 200), and
  confirmed via search that `/industrial-emissions/dataset` and `/download`
  pages exist and describe the CSV/XML/API-style download offering.

---

## Deferred (not specced as a client): oParl at the Landtag level

Per the brief's oParl instruction, the Landtag-level ask that motivated this
research target was NOT found — see the scope-correction note under #5
above. No Landtag (German state parliament) runs an oParl endpoint; the
municipal-level example (#5, Cologne) is the only concrete on-topic endpoint
verified this pass. Deferred for a future wave: a compiled registry of
additional high-value municipal oParl endpoints (e.g. cities with confirmed
DC-district-heating deals), rather than a blanket "German subnational"
client.

---

## Draft `api_sources.yaml` entries (all `enabled: false`)

```yaml
domains:
  - name: "US Federal Register API"
    id: "federal_register_api"
    enabled: false
    source_type: "federal_register_api"
    base_url: "https://www.federalregister.gov"
    region:
      - "us"
    category: "regulatory"
    tags:
      - "mandates"
      - "reporting"
    policy_types:
      - "regulation"
      - "report"
    notes: |
      Wave 3 tier-c candidate from more-legislation-apis.md #2 (highest-
      value find of the pass). Keyless. Distinct from the existing
      regulations_gov client (docket/public-comment layer) - this is the
      official publication of record. Verified end-to-end with an
      on-topic "data center waste heat" query (2,651 results incl. a DOE
      AI-infrastructure RFI).

  - name: "Congress.gov API (US federal bill lifecycle)"
    id: "congress_gov_api"
    enabled: false
    source_type: "congress_gov_api"
    base_url: "https://api.congress.gov"
    region:
      - "us"
    category: "legislative"
    tags:
      - "mandates"
    policy_types:
      - "law"
      - "legislation"
    notes: |
      Wave 3 tier-c candidate from more-legislation-apis.md #1. Requires
      CONGRESS_GOV_API_KEY (free signup at api.congress.gov/sign-up/);
      self-disables until set, same pattern as legiscan/govinfo/
      regulations_gov. Distinct from GovInfo (finished document
      collections) - this is the queryable bill-lifecycle layer.

  - name: "Open States API v3 (all 50 US states)"
    id: "openstates_api"
    enabled: false
    source_type: "openstates_api"
    base_url: "https://v3.openstates.org"
    region:
      - "us"
      - "us_states"
    category: "legislative"
    tags:
      - "mandates"
    policy_types:
      - "law"
      - "legislation"
    notes: |
      Wave 3 tier-c candidate from more-legislation-apis.md #3. Requires
      OPENSTATES_API_KEY (free signup at openstates.org/account/profile/);
      self-disables until set. Complementary to the existing legiscan
      client (free tier, not a strict duplicate) - covers all 50 states in
      one integration plus committees/events/geolocation lookup.

  - name: "Kenya Law / National Council for Law Reporting search API"
    id: "kenya_law_api"
    enabled: false
    source_type: "kenya_law_api"
    base_url: "https://new.kenyalaw.org"
    region:
      - "africa"
    category: "legislation"
    tags:
      - "mandates"
    policy_types:
      - "law"
      - "legislation"
    notes: |
      Wave 3 tier-c candidate from more-legislation-apis.md #4. Keyless.
      Region note: "kenya" not in VALID_REGIONS; mapped to "africa". Only
      verified national gazette/legislation API found in sub-Saharan
      Africa this pass; direct keyword hit on Kenya's Energy Act
      confirmed.

  - name: "oParl standard (German municipal council information systems)"
    id: "oparl_koeln"
    enabled: false
    source_type: "oparl"
    base_url: "https://ratsinformation.stadt-koeln.de"
    region:
      - "germany"
      - "eu"
    category: "legislative"
    tags:
      - "mandates"
    policy_types:
      - "legislation"
    notes: |
      Wave 3 tier-c candidate from more-legislation-apis.md #5.
      MUNICIPAL ONLY, not Landtag-level - see the deferred note in
      new-clients-wave3.md. Keyless, JSON-LD, verified live for Cologne
      only; a generic oparl client would need a small hardcoded registry
      of additional known-good municipal endpoints to be worth more than
      this single city. id uses a per-city suffix since oParl has no
      single root base_url (per-implementing-body).

  - name: "EPA Envirofacts Greenhouse Gas RESTful Data Service"
    id: "epa_ghgrp_envirofacts_api"
    enabled: false
    source_type: "epa_ghgrp_envirofacts_api"
    base_url: "https://data.epa.gov"
    region:
      - "us"
    category: "environmental_agency"
    tags:
      - "reporting"
      - "carbon"
    policy_types:
      - "report"
    notes: |
      Wave 3 tier-c candidate from carbon-ets.md #21. Keyless, fully open.
      Pairs with the us_epa_ghgrp crawl-domain entry (wave-3
      carbon-ets.yaml). Generic Oracle-table-passthrough API
      (/efservice/<TABLE>/<FORMAT>) - not a purpose-built search API, so
      response parsing will be table-schema-specific. Verified live with a
      real facility record from PUB_DIM_FACILITY.

  - name: "Georgia EPD Air Permit Search Engine"
    id: "ga_epd_permit_search"
    enabled: false
    source_type: "ga_epd_permit_search"
    base_url: "https://permitsearch.gaepd.org"
    region:
      - "us"
      - "us_states"
      - "georgia"
    category: "regulatory"
    tags:
      - "mandates"
      - "reporting"
    policy_types:
      - "regulation"
    notes: |
      Wave 3 tier-c candidate from permitting-eia.md #12. No documented
      public REST API - needs a client that drives the search form (AIRS
      Number, Facility Name, Permit Number/SIC Code) or scrapes result
      pages. Distinct base_url from the existing static ga_epd crawl
      domain (epd.georgia.gov) - supplements it with facility-level
      searchable permit records, does not replace it.

  - name: "European Industrial Emissions Portal (EEA)"
    id: "eea_industrial_emissions_portal"
    enabled: false
    source_type: "eea_industrial_emissions_portal"
    base_url: "https://industry.eea.europa.eu"
    region:
      - "eu"
    category: "regulatory"
    tags:
      - "reporting"
      - "carbon"
      - "mandates"
    policy_types:
      - "report"
      - "regulation"
    notes: |
      Wave 3 tier-c candidate from permitting-eia.md #13. Keyless bulk
      CSV/XML download + GeoNetwork/CSW-style metadata catalogue - needs a
      new client (no existing client handles OGC/GeoNetwork-shaped or bulk
      EU environmental data). CAVEAT: most standalone DC backup-generator
      setups sit below IED/LCP thresholds, so this will surface only a
      minority of DC-relevant installations - best used as a cross-check/
      discovery layer, not primary coverage.
```
