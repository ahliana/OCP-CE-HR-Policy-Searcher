# Wave 3 — Additional Legislature/Gazette Structured APIs

Scope: net-new structured API sources not covered in waves 1-2. Dedup checked against
the 9 existing clients (riksdagen, uk_bills, legisinfo, folketing, eurlex_nim, legiscan,
govinfo, regulations_gov, dip), the wave-1 tier-c list (`draft/new-clients.md`), and the
wave-2 list (`regions-wave2/legislation-apis.md`). Every candidate below was fetched live
this session (`curl`/WebFetch), not taken from docs alone.

---

## Verified candidates (ranked best-first)

### 1. `congress_gov_api` — Congress.gov API (US federal)
- **base_url**: `https://api.congress.gov`
- **level**: national
- **access**: **api_key** — free registration at `https://api.congress.gov/sign-up/`
  (confirmed live, HTTP 200). Env var: `CONGRESS_GOV_API_KEY`. Pass as `?api_key=` query
  param or `X-Api-Key` header.
- **format**: JSON
- **endpoints**: `/v3/bill` (bill list/search), `/v3/bill/{congress}/{type}/{number}`
  (detail, incl. text versions, actions, cosponsors, committees), `/v3/law`,
  `/v3/summaries` (CRS-authored bill summaries — useful for keyword-matching without
  pulling full text).
- **coverage**: full US federal bill lifecycle (introduced through enacted), distinct
  from GovInfo (bulk document collections) and Regulations.gov (agency rulemaking
  dockets/comments) — this is the bill-tracking/legislative-history layer. `region: usa`,
  `category: legislative`, `policy_types: [law, legislation]`.
- **practical**: rate limit not published in the error response; standard REST, no
  documented pagination cap issues. Official successor to the old (deprecated)
  ProPublica Congress API.
- **effort tier**: (c) — new client; clean REST/JSON shape, straightforward to build,
  good candidate to model loosely on `govinfo`.
- **why worth adding**: only structured source of the actual bill-introduction-to-law
  pipeline for US federal legislation with full-text search on bill summaries — GovInfo
  serves finished document collections, not a queryable bill-lifecycle API.
- **verified**: YES. `curl "https://api.congress.gov/v3/bill?limit=1"` (no key) returned
  a real, well-formed JSON error: `{"error":{"code":"API_KEY_MISSING","message":"No
  api_key was supplied. Get one at https://api.congress.gov:443"}}` — confirms the
  service is live and the auth mechanism/signup path are real, not hallucinated.

---

### 2. `federal_register_api` — US Federal Register API
- **base_url**: `https://www.federalregister.gov`
- **level**: national
- **access**: **none** — fully keyless, no signup, no headers
- **format**: JSON
- **endpoints**: `GET /api/v1/documents.json?conditions[term]=<keyword>` (full-text
  search across all Federal Register documents — proposed rules, final rules, notices,
  presidential documents — with agency/date/type filters); `/api/v1/documents/{number}.json`
  for detail; `/api/v1/agencies`.
- **coverage**: distinct from Regulations.gov (which is the *docket/public-comment*
  layer) — the Federal Register is the *official publication* of record for every US
  federal rule and notice. `region: usa`, `category: regulatory`, `policy_types:
  [regulation, notice]`.
- **practical**: no documented rate limit observed; no auth headers needed at all.
  Response includes `html_url` and `pdf_url` per document plus paginated `next_page_url`.
- **effort tier**: (c) — new client; simplest of the three top US finds to build
  (single GET, no auth, clean JSON).
- **why worth adding**: **the highest-value find of this pass**. A live, keyless,
  on-topic query returned exactly the kind of document PolicyPulse targets.
- **verified**: YES, end-to-end with an on-topic result.
  `curl "https://www.federalregister.gov/api/v1/documents.json?per_page=1&conditions%5Bterm%5D=data+center+waste+heat"`
  returned `{"count":2651,...}` with a real, on-topic first result: a DOE "Request for
  Information on Artificial Intelligence Infrastructure on DOE Lands" notice (document
  `2025-05936`, published 2025-04-07) discussing AI/data-center infrastructure siting on
  federal land — squarely in scope.

---

### 3. `openstates_api` — Open States API v3 (all 50 US states + DC + PR)
- **base_url**: `https://v3.openstates.org`
- **level**: subnational (state) — but one integration covers all 50 states at once
- **access**: **api_key** — free registration at `https://openstates.org/account/profile/`.
  Env var: `OPENSTATES_API_KEY`. Pass via `X-API-KEY` header or `?apikey=` query param.
- **format**: JSON
- **endpoints**: `/jurisdictions`, `/people` (legislators, incl. geolocation lookup),
  `/bills` (search by jurisdiction/session/query, returns bill actions, sponsors, and
  linked full-text/version documents), `/committees`, `/events`. Interactive docs at
  `v3.openstates.org/docs/`.
- **coverage**: `region: usa`, `category: legislative`, `policy_types: [law,
  legislation]`. **Distinct from the existing `legiscan` client**: LegiScan's free tier
  is query-limited and full bill text/bulk access sits behind a paid tier; Open States is
  a nonprofit (Plural Policy/Open States Foundation)-run alternative with a free key
  covering the same 50-state bill corpus plus committees/events/geolocation-based
  legislator lookup that LegiScan doesn't expose. Treat as a complementary fallback/
  cross-check source, not a strict duplicate.
- **practical**: no rate-limit figure surfaced in the error response this pass; docs
  page did not state one either — confirm exact limits at key-registration time.
- **effort tier**: (c) — new client; REST/JSON, well-documented (OpenAPI + ReDoc).
- **why worth adding**: single integration for every US state legislature's bill data,
  free-tier key, real full-text-linked bill records — the single best "one integration =
  a whole jurisdiction" multiplier available for US subnational coverage (50 states at
  once).
- **verified**: YES. `curl "https://v3.openstates.org/bills?jurisdiction=Texas&q=energy"`
  (no key) returned the real, documented auth-gate JSON:
  `{"detail":"Must provide API Key as ?apikey or X-API-KEY. Login and visit
  https://openstates.org/account/profile/ for your API key."}` — confirms the live
  service, the exact auth mechanism, and the correct signup URL (more authoritative than
  the docs page, which pointed to a slightly different legacy Plural Policy URL).

---

### 4. `kenya_law_api` — Kenya Law / National Council for Law Reporting search API
- **base_url**: `https://new.kenyalaw.org`
- **level**: national
- **access**: **none** — keyless, no signup
- **format**: JSON (documents modeled in Akoma Ntoso / FRBR URIs — same open-legal-data
  standard used by AfricanLII / Laws.Africa across multiple African jurisdictions)
- **endpoints**: `GET /search/api/documents/?search=<term>` (full-text search across all
  document types); add `&doc_type=legislation` to restrict to Acts/statutes (vs.
  `judgment` for case law). Returns `count`, FRBR work/expression URIs, citation,
  dates.
- **coverage**: Kenyan national legislation (Acts, incl. the Energy Act) and case law.
  `region: kenya`, `category: legislative`, `policy_types: [law, legislation]`.
- **practical**: no documented rate limit found this pass; clean REST, no pagination
  issues observed at `count`-level.
- **effort tier**: (c) — new client; simple REST/JSON, keyless, straightforward.
- **why worth adding**: only verified national gazette/legislation API found in
  sub-Saharan Africa this pass — direct hit on Kenya's Energy Act via a live keyword +
  doc_type filter, and the same AfricanLII/Laws.Africa AKN pattern likely recurs across
  other African LII sites (worth a follow-up pass if African coverage becomes a
  priority).
- **verified**: YES. `curl "https://new.kenyalaw.org/search/api/documents/?search=energy&doc_type=legislation"`
  returned real JSON: `{"count": 492, "results": [{"doc_type": "legislation", "title":
  "Energy Act", "date": "2022-12-31", "citation": "Cap. 314", ...}]}`.

---

### 5. `oparl` — oParl standard (German municipal council information systems)
- **base_url**: per-body (no single root; e.g. Cologne: `https://ratsinformation.stadt-koeln.de/oparl/system`)
- **level**: **local/municipal**, NOT state-level — **important correction to the
  research target**: oParl is implemented by city/county council information systems
  (Ratsinformationssysteme), not by Landtage (German state parliaments). No Landtag
  running an oParl endpoint was found or is known to exist; Landtage run their own
  bespoke parliamentary-documentation systems (the DACH region file already covers
  several via direct Landesrecht/ministry crawl domains instead).
- **access**: none — keyless, standardized JSON-LD schema (`schema.oparl.org`)
- **format**: JSON (JSON-LD)
- **endpoints**: every implementing body exposes the same shape starting from a
  `System` object: `GET /oparl/system` → links to `body` → `organization`, `meeting`,
  `paper` (agenda items/motions/resolutions — this is where waste-heat/district-heating
  council motions would live), `person`. Schema at `schema.oparl.org`.
- **coverage**: hundreds of German municipalities use oParl-compliant "Sitzungsmanagement"
  vendors (e.g. SOMACOS "Session", used by Cologne); no central registry/directory of
  live endpoints was found this pass (the `oparl.org/koerperschaften/` listing page
  redirected but its content wasn't independently enumerated) — a client would need a
  small hardcoded list of known-good municipal endpoints, or a scrape of a third-party
  registry.
- **practical**: no rate limit documented; each municipality's instance is independently
  hosted/maintained (varies in uptime — a Bonn instance tried this pass returned HTTP 500).
- **effort tier**: (c) — new generic oParl client, reusable across any implementing
  municipality once built, but value is capped by the local (not state/national) scope.
- **why worth adding**: real, live, standardized, keyless municipal legislative-motion
  API — but flagged as **lower priority than originally hoped** since it does not reach
  the Landtag level the task asked about. Best used opportunistically for specific
  high-value cities (e.g. a city known to be piloting data-center district heating) once
  a registry of live endpoints is compiled, rather than as blanket "German subnational"
  coverage.
- **verified**: YES (municipal example only). `curl "https://ratsinformation.stadt-koeln.de/oparl/system"`
  returned a real JSON-LD `System` object for "Stadt Köln - OParl 1.1" with a working
  `body` link. A second instance tried (Bonn) returned HTTP 500 (site-side issue, not a
  protocol problem).

---

### 6. `bundesrat_rss` — Bundesrat plenary-document RSS feeds (Germany) — discovery feed, not a query API
- **base_url**: `https://www.bundesrat.de`
- **level**: national
- **access**: none — keyless
- **format**: XML (RSS 2.0)
- **endpoints**: `/SiteGlobals/Functions/RSSFeed/RSSGenerator_Publication.xml`
  (Plenarprotokolle — plenary session transcripts), `RSSGenerator_PBPrintout.xml`
  (Drucksachen/printed matter — the actual bill/resolution documents), `RSSGenerator_Event.xml`,
  `RSSGenerator_Event_Ausschuss.xml` (committee events), `RSSGenerator_Announcement.xml`.
- **coverage**: `region: germany`, `category: legislative`, `policy_types: [legislation,
  report]`. **Note**: no true query/search API was found for the Bundesrat itself (its
  open-data landing page path referenced in earlier research, `/DE/service/opendata/
  opendata-node.html`, 404s — that page no longer exists or was moved). These RSS feeds
  are a chronological publication feed, not a keyword-searchable database.
- **practical**: `ttl: 60` (feed self-declares 60-min refresh); no documented rate limit.
  The site itself was intermittently slow/unreachable during this session (several
  requests timed out before succeeding on retry) — build in generous timeouts.
- **effort tier**: (b) — better suited to the existing crawl-domain/RSS-ingestion
  pattern than a bespoke structured-API client, given it's a plain feed with no query
  parameters.
- **related, likely-better path**: the existing `dip` client (Bundestag/Bundesrat joint
  documentation system, DIP) accepts a `f.zuordnung=BR` filter to restrict results to
  Bundesrat-attributed documents — confirmed the parameter is accepted (a keyless probe
  returned the expected `401 API key required` auth-gate response, not a parameter
  error), meaning **Bundesrat coverage may already be reachable by extending the
  existing `dip` client's query params** rather than building anything new. Flag this
  for the `dip` client maintainer rather than treating Bundesrat as its own new source.
- **why worth adding**: real and live, but of narrow value given the `dip` filter
  option above is likely the better integration path.
- **verified**: YES for the RSS feed. `curl ".../RSSGenerator_Publication.xml"` returned
  real, dated RSS items (e.g. "Plenarprotokoll 1067. Sitzung, 10.07.2026"). The `dip`
  `f.zuordnung=BR` probe returned the standard DIP auth-required JSON error (not a bad-
  parameter error), suggesting the filter is valid.

---

## Unverified / needs-human-check (dropped or blocked this pass)

- **Austria — Parlament Open Data / data.gv.at**: same blocker as wave-2's finding,
  re-confirmed this pass. The human landing page (`parlament.gv.at/recherchieren/
  open-data/`) is live (200) and its subpage confirms JSON/API/download language is
  present, but every guessed direct data endpoint 404'd, and `data.gv.at`'s CKAN-style
  `package_search` call returned the portal's HTML frontend shell rather than JSON even
  with an `Accept: application/json` header. Needs a real browser session to find the
  actual API root (the JSON is very likely fetched client-side by a JS app).
- **Portugal — Assembleia da República (parlamento.pt)**: landing page confirmed live
  (200) and now confirms in its own text that "a AR disponibiliza dados abertos... em
  formatos XML e JSON" — new confirmation beyond wave-2 — but the actual download links
  on the Iniciativas (bills) subpage are obfuscated SharePoint tokens, not stable
  URLs/query endpoints, reachable only via a headed browser session.
- **Italy — Camera dei Deputati (dati.camera.it)**: re-confirmed this pass — every
  direct query (including `?output=json`) returns an Akamai bot-challenge page (SHA1/
  cookie-computation JS), not data. Same blocker as wave-2; still needs a real browser.
- **Belgium — data.gov.be**: new finding this pass — actively blocked by a
  TSPD/Akamai-style bot-challenge script on the Action API (`/api/3/action/
  package_search`), same pattern as Italy above. Not previously confirmed blocked in
  wave-2 ("not confirmed either way"); now confirmed blocked.
- **Lithuania (Seimas/lrs.lt), Latvia (Saeima), Slovenia (DZ-RS), Croatia (Sabor)**:
  main sites confirmed live (200), but no query-able open-data API endpoint was located
  this pass (guessed paths 404'd). Needs a dedicated per-country search pass, not
  dropped outright.
- **Mexico — Cámara de Diputados / Senado**: `datos.gob.mx` portal confirmed live, but
  (same as wave-2) no specific dataset exposing queryable bill text/metadata was found;
  the guessed CKAN path (`/busca/api/3/action/package_search`) 404'd — this portal's API
  root differs from standard CKAN paths and needs a follow-up search from within the
  portal's own UI.
- **Argentina — datos.gob.ar**: portal confirmed live with a real DCAT `data.json`
  catalog, but keyword matches on "congreso"/"senado"/"diputados" in the raw catalog
  were false positives (aviation/conference-related datasets, e.g.
  "negocios_congreso_conferencia") — no actual legislative bill-tracking dataset found.
  Dropping this candidate; not proposing Argentina from this pass.
- **India — Sansad (sansad.in), IndiaCode (indiacode.nic.in)**: both sites live (200),
  but no public API was found — `sansad.in/api` and `/opendata` both 404, and IndiaCode's
  DSpace-based repository does not expose a working OAI-PMH endpoint at the standard
  path (`/oai/request` 404s with a generic error page). PRS Legislative Research
  (prsindia.org, also live) is a private NGO, not a government source, and out of scope
  per the brief. Dropping India from this pass; would need a more targeted search for
  Lok Sabha/Rajya Sabha-specific open-data initiatives.
- **Indonesia (peraturan.go.id), Malaysia (federalgazette.agc.gov.my)**: both
  **unreachable from this research session** — `peraturan.go.id` refused the connection
  outright and `federalgazette.agc.gov.my` failed DNS resolution entirely, from two
  different fetch tools (curl and WebFetch). This looks like a network-level block
  rather than the sites being down — needs a recheck from a different network/session
  before concluding anything either way.
- **Not investigated this pass** (time-boxed out, no findings either way): EU
  TED (Tenders Electronic Daily) and "Have Your Say" portal; Canadian provincial
  legislatures beyond Quebec (already covered via `donneesquebec_ckan` in wave-1).

---

## Summary

- **6 verified, working structured sources**: Congress.gov API, US Federal Register
  API, Open States API v3, Kenya Law API, oParl standard (municipal-only, not Landtag),
  Bundesrat RSS feeds (discovery feed, not a query API).
- **Keyless vs keyed**: 4 of 6 are fully keyless (Federal Register, Kenya Law, oParl,
  Bundesrat RSS). 2 require a free API key (Congress.gov — signup at
  `api.congress.gov/sign-up/`; Open States — signup at `openstates.org/account/profile/`).
- **12 unverified/dropped**: Austria, Portugal, Italy, Belgium (all blocked by
  bot-challenges or JS-only frontends), Lithuania/Latvia/Slovenia/Croatia (live sites,
  no API located yet), Mexico and Argentina (portals live, no relevant dataset found),
  India (no working government API found), Indonesia and Malaysia (network-unreachable
  this session — inconclusive).
- **Highest-value finds**: **US Federal Register API** (`federalregister.gov/api/v1`) —
  fully keyless, and a live on-topic query for "data center waste heat" returned 2,651
  matching documents including a DOE AI-infrastructure RFI, on the first try, with zero
  setup. **Congress.gov API** and **Open States API v3** are the second tier: both
  confirmed live via real (not guessed) auth-gate responses that name the exact signup
  URL, and together they give US federal bill-lifecycle tracking (Congress.gov) plus
  free-tier all-50-state bill tracking (Open States) as a genuine complement to the
  existing `legiscan` client rather than a duplicate of it.
