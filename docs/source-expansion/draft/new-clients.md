# New Structured Clients Needed (tier-c)

Sixteen tier-c candidates surfaced across the 11 region files — each needs a
NEW `source_type` client under `src/sources/` (registered in
`src/sources/__init__.py`) because none of them fit the shape of the 9
existing clients (`riksdagen`, `uk_bills`, `legisinfo`, `folketing`,
`eurlex_nim`, `legiscan`, `govinfo`, `regulations_gov`, `dip`). No client code
is included here — this is a spec for a future engineer, per the brief.

Each spec below: proposed `source_type` id, API base, auth, response format,
endpoint(s), CrawlResult field mapping, pagination/rate-limit notes. The
draft `api_sources.yaml` entries (all `enabled: false`) follow in one fenced
block at the end of this file.

---

## 1. `donneesquebec_ckan` — Donnees Quebec "Projets de loi" (Assemblee nationale du Quebec)

- **Region**: Canada / Quebec (subnational)
- **API base**: `https://www.donneesquebec.ca` (CKAN Action API:
  `/api/3/action/package_show?id=projets-de-loi`)
- **Auth**: none
- **Format**: CSV via the dataset page today; JSON available through the
  standard CKAN Action API (`package_show`, `datastore_search`)
- **Endpoints to call**: `GET /api/3/action/package_show?id=projets-de-loi`
  for dataset metadata + resource URLs; `GET /api/3/action/datastore_search?
  resource_id=<id>` if the resource is datastore-backed, else download the
  CSV resource URL directly.
- **CrawlResult mapping**: `url` = resource download URL or a constructed
  Assemblee nationale bill-detail URL if the dataset includes a bill number;
  `title` = bill short title field; `content` = bill status/summary fields
  concatenated; `lifecycle_stage` = derive from the dataset's status column
  (introduced / adopted / etc. — exact column names TBD once the CSV schema
  is inspected).
- **Pagination/rate limits**: dataset described as "Frequence de mise a
  jour: Temps reel" (real-time); no documented rate limit. License is
  CC-BY-NC 4.0 (attribution, non-commercial) — MORE RESTRICTIVE than every
  other source already in `api_sources.yaml`; flag for legal review before
  building. Contact: donneesouvertes@assnat.qc.ca.
- **Note**: building a generic CKAN Action-API client here would also unlock
  other Donnees Quebec datasets beyond this one, if useful later.

---

## 2. `stortinget` — Storting Open Data API (Norway)

- **Region**: Nordic / Norway (national)
- **API base**: `https://data.stortinget.no`
- **Auth**: none (attribution requested)
- **Format**: XML/JSON (technical documentation confirmed live on-site;
  exact response format per-endpoint not fully enumerated this pass)
- **Endpoints to call**: cases/bills ("Saker"), votes ("Voteringer"),
  hearings ("Horinger"), publications, committees — exact endpoint paths
  need confirming against the site's own API docs before building (docs
  page was confirmed live but not deeply enumerated).
- **CrawlResult mapping**: `url` = case/bill detail page URL; `title` = case
  title; `content` = case summary/status text; `lifecycle_stage` = case
  status field (proposed / in committee / voted / enacted).
- **Pagination/rate limits**: no published rate limit found — check the API
  docs page directly before building. Historical XML docs/votes back to
  2008. Contact: +47 23 31 33 33 / web@stortinget.no.
- **Why it matters**: Norway is the one Nordic "big three" (Sweden/Denmark/
  Norway) national parliament without a structured API source yet, and it
  passed the data-center waste-heat CBA law amendment.

---

## 3. `eduskunta` — Eduskunta Avoin Data API (Finland)

- **Region**: Nordic / Finland / EU (national)
- **API base**: `https://avoindata.eduskunta.fi`
- **Auth**: none
- **Format**: JSON (confirmed live — a direct table-listing endpoint at
  `/api/v1/tables/` returned a real JSON array of dataset names)
- **Endpoints to call**: confirmed live tables include `MemberOfParliament`,
  `SaliDBIstunto` (sessions), `SaliDBPuheenvuoro` (speeches),
  `SaliDBAanestys`/`SaliDBKohtaAanestys` (votes), `SaliDBAsiakirja`
  (documents), `SaliDBTiedote` (notices), `VaskiData`. Exact query/filter
  parameters per table need confirming against docs.
- **CrawlResult mapping**: `url` = document/session detail page (via
  VaskiData or SaliDBAsiakirja linkage); `title` = document title; `content`
  = document/speech text; `lifecycle_stage` = derive from session/vote
  status fields.
- **Pagination/rate limits**: no published rate limit found this pass.
  Docs referenced at `parliament.fi/fi/avoin-data/mita-on-avoin-data` and
  `eduskunta.fi/avoin-data` both returned 403 to automated fetch in the
  research session (likely bot-blocking) — confirm manually before building.
- **Why it matters**: completes structured API coverage for all three
  largest Nordic national parliaments (Sweden/Denmark already covered,
  Norway via #2 above, Finland here).

---

## 4. `europarl_opendata` — European Parliament Open Data API v2 (pan-EU)

- **Region**: EU (supranational)
- **API base**: `https://data.europarl.europa.eu`
- **Auth**: none (rate-limited to 500 requests / 5 minutes)
- **Format**: JSON-LD / RDF (Turtle also available); REST/OpenAPI 3 (OAS3)
  v2
- **Endpoints to call**: `/api/v2/documents` (plenary/committee/question
  documents, adopted texts — resolutions, legislative acts, opinions),
  `/api/v2/meps`, `/api/v2/controlled-vocabularies/{vocId}`.
- **CrawlResult mapping**: `url` = document's `eli:Work` identifier resolved
  to its canonical EP document page; `title` = document title metadata;
  `content` = document abstract/full text where available; `lifecycle_stage`
  = document type/procedure stage (amendment / committee report / adopted
  text).
- **Pagination/rate limits**: 500 req / 5 min. Docs at
  `/en/developer-corner/opendata-api` (returned empty content to a plain
  text fetch — likely JS-rendered; confirm via real browser before
  building). Release notes at `/release-notes`.
- **Why it matters**: only pan-EU source exposing the legislative process
  itself (amendments, committee reports, plenary votes) rather than just
  final law text — catches proposed changes to data-center/heat-reuse rules
  before they hit EUR-Lex. Verified end-to-end: `curl
  https://data.europarl.europa.eu/api/v2/documents?limit=1` returned a real
  EP document (`A-10-0034-0034-AM-001-001`).

---

## 5. `data_europa` — data.europa.eu Search API (pan-EU open-data meta-catalog)

- **Region**: EU (supranational) — **cross-listed candidate**: this exact
  source was independently proposed in both `regions/eu-uncovered.md` and
  `regions/supranational.md`; the two write-ups are merged into this single
  spec.
- **API base**: `https://data.europa.eu`
- **Auth**: none — keyless, no signup, no rate-limit key required
- **Format**: JSON (Search API), RDF/SPARQL (semantic endpoint)
- **Endpoints to call**: Search API `GET /api/hub/search/search?q=<query>&
  limit=<n>`; SPARQL endpoint `/sparql` for precise DCAT-AP metadata queries
  (e.g. filter by `dcat:theme = energy`); Registry API `/api/hub/repo/`.
- **CrawlResult mapping**: `url` = dataset `distributions[].access_url` (the
  actual downloadable resource, not the catalog page); `title` = dataset
  title; `content` = dataset description; `lifecycle_stage` = not
  applicable/N/A for most hits — this catalog mostly surfaces statistical
  datasets (e.g. "Share of renewable energy and waste heat" energy-balance
  tables), not laws/directives with a lifecycle. Treat as a **discovery
  layer**, not primarily a legislation database.
- **Pagination/rate limits**: no documented hard rate limit; use courtesy
  throttling. Docs: `dataeuropa.gitlab.io/data-provider-manual/api-
  documentation/` and `data.europa.eu/en/which-apis-are-available-and-
  where-can-i-find-information-about-them`.
- **Why it matters**: one integration surfaces energy/waste-heat datasets
  from every EU member state's national open-data portal simultaneously —
  fallback discovery layer for the many target countries whose national
  agencies don't have direct APIs. Verified twice independently: query
  `?q=district+heating` returned 1,015,339+ total results; query
  `?q=waste%20heat%20data%20centre` returned 1,012,093 total results with
  live Austrian/Dutch energy-dataset hits.

---

## 6. `rada_opendata` — Verkhovna Rada (Ukraine Parliament) Open Data Portal

- **Region**: EU-aligned / Ukraine (national, EU-candidate/Energy Community
  transposition context)
- **API base**: `https://data.rada.gov.ua`
- **Auth**: none (Creative Commons; no key)
- **Format**: NOT FULLY CONFIRMED — the `/open/main/en/api` link was located
  but not fetched this pass; needs one more verification pass before
  building.
- **Endpoints to call**: portal's four dataset categories: "Normative-legal
  base of Ukraine" (legislation), agenda items, registered bills, MP data.
  Exact endpoint paths/parameters TBD.
- **CrawlResult mapping**: `url` = bill/law detail page; `title` = bill/law
  title; `content` = bill/law text or summary; `lifecycle_stage` = bill
  status from the registered-bills dataset (registered / first reading /
  second reading / enacted).
- **Pagination/rate limits**: portal explicitly labeled "in test operation
  mode" — schema may still change. Built jointly by the Rada apparatus,
  OPORA, the e-governance agency, and UNDP Ukraine.
- **Why it matters**: would let PolicyPulse track Ukraine's
  district-heating reform bill (draft law No. 14067, passed second reading)
  and any future data-center/efficiency legislation through the
  bill-registration dataset rather than only reading finished law text.
  **BLOCKED on one more verification step**: confirm the `/open/main/en/api`
  page's actual request/response format before writing this client.

---

## 7. `dkan_cy` — data.gov.cy Open Data Portal (Cyprus, Ministry of Energy group)

- **Region**: EU / Cyprus (national)
- **API base**: `https://data.gov.cy`
- **Auth**: none
- **Format**: JSON (DKAN REST) — platform is DKAN, not CKAN
- **Endpoints to call**: portal exposes a "Dataset REST API" and a
  "Datastore API" per its own developer page
  (`data.gov.cy/en/support-developers`); dataset group for Ministry of
  Energy, Commerce and Industry at `/en/group/29`. Developer docs point to
  upstream DKAN documentation rather than hosting full endpoint specs
  in-portal — consult upstream DKAN API docs when building.
- **CrawlResult mapping**: `url` = dataset resource download URL; `title` =
  dataset title; `content` = dataset description/metadata; `lifecycle_stage`
  = not applicable (statistical/report datasets, not legislative lifecycle
  items).
- **Pagination/rate limits**: not documented this pass.
- **Why it matters**: government-run open-data catalog specifically grouped
  by publishing ministry, letting PolicyPulse pull Cyprus energy datasets
  without a bespoke scraper. Verified both `/en/group/29` (Ministry of
  Energy, Commerce and Industry group confirmed) and `/en/support-
  developers` (DKAN REST + Datastore API references confirmed) directly.

---

## 8. `oireachtas` — Houses of the Oireachtas Open Data API (Ireland)

- **Region**: Ireland (national) — **highest-value UK/Ireland-region find**
- **API base**: `https://api.oireachtas.ie/v1` (Swagger docs at
  `https://data.oireachtas.ie`)
- **Auth**: none — open, no key. Public "Oireachtas (Open Data) PSI Licence"
  (CC-based). Support contact: open.data@oireachtas.ie.
- **Format**: JSON (OAS 2.0 / Swagger v1.1.0), with linked XML (Akoma Ntoso
  debates, parliamentary questions) and PDF (bills, acts) via
  `data.oireachtas.ie`
- **Endpoints to call**: `/constituencies`, `/debates`, `/houses`,
  `/legislation` (filterable by `heading=` keyword, e.g. `heat`/`energy`),
  `/members`, `/parties`, `/questions`, `/votes`.
- **CrawlResult mapping**: `url` = bill/debate/question detail page from the
  JSON response's own link field; `title` = bill short title / debate
  topic; `content` = bill summary or debate/question text; `lifecycle_stage`
  = bill stage field (First Stage / Committee / Enacted, etc.) directly
  present in the `/legislation` response.
- **Pagination/rate limits**: no documented rate limit found — use standard
  courtesy throttling (2s).
- **Why it matters**: Ireland currently has ZERO structured legislative API
  anywhere in the repo — everything Irish is HTML crawl. Verified
  end-to-end, not just documented: `curl
  "https://api.oireachtas.ie/v1/legislation?heading=heat&limit=10"` returned
  a well-formed 57KB JSON response including the Heat (Networks and
  Miscellaneous Provisions) Bill 2024, Ireland's first dedicated
  district-heating law. Closely analogous in shape to the existing
  `uk_bills` client (`bills-api.parliament.uk`) — a good implementation
  reference.

---

## 9. `scottish_parliament` — Scottish Parliament Open Data API

- **Region**: UK / Scotland (subnational)
- **API base**: `https://data.parliament.scot`
- **Auth**: none — open data, no key, no auth headers
- **Format**: JSON
- **Endpoints to call**: `/api/bills` (every SP Bill since devolution, with
  reference number, short/full name, sponsoring member), `/api/events`
  (motions/members' business). No single index/root API page (it 404s) —
  endpoints were found via the Open Data Scotland catalogue, not in-site
  navigation; more endpoints (questions, committees) likely exist but were
  not enumerated this pass.
- **CrawlResult mapping**: `url` = the bill's page on the existing
  `uk_scotland_parliament` HTML crawl domain (this API supplies structured
  metadata for matching/filtering, the HTML site carries full bill
  text/stages/committee reports — the two are complementary, not
  redundant); `title` = bill short/full name; `content` = bill reference +
  sponsoring-member metadata; `lifecycle_stage` = not directly present in
  the tested response — would need to be inferred or fetched from the
  companion HTML page.
- **Pagination/rate limits**: no rate-limit documentation found.
- **Why it matters**: Scotland has the UK's most advanced heat-network
  legislation (Heat Networks (Scotland) Act 2021, forthcoming Heat in
  Buildings Bill) but is currently HTML-crawl-only for its Parliament,
  unlike Westminster (`uk_bills` HTML + `uk_bills_api` structured client).
  Verified: both `/api/bills` and `/api/events` returned live JSON this
  pass. NOT verified: whether a keyword-filterable query parameter (e.g.
  searching bills by title substring) is supported — confirm before
  building a client that relies on server-side filtering.

---

## 10. `egov_law_jp` — e-Gov Law Search API v2 (Japan, Digital Agency)

- **Region**: APAC / Japan (national)
- **API base**: `https://laws.e-gov.go.jp`
- **Auth**: none — no API key, no registration (official guidance: avoid
  high-frequency bursts)
- **Format**: JSON, XML
- **Endpoints to call**: `/api/2/laws` (search/list), `/api/2/law_data/
  {law_id}` (full law text/amendment history). OpenAPI/Swagger spec at
  `/api/2/swagger-ui`, ReDoc at `/api/2/redoc/`, PDF spec at
  `/file/houreiapi_shiyosyo.pdf`.
- **CrawlResult mapping**: `url` = law's canonical e-Gov page (constructed
  from `law_id`); `title` = law name; `content` = full law text from
  `/law_data/{law_id}`; `lifecycle_stage` = enacted/amended status +
  amendment history from the same response.
- **Pagination/rate limits**: no documented hard rate limit; avoid
  high-frequency bursts per official guidance. Docs at
  `laws.e-gov.go.jp/docs/law-data-basic/`.
- **Why it matters**: same underlying corpus as the existing `elaws_jp`
  crawl entry (Energy Efficiency Act / Rationalizing Energy Use Act) but via
  a real structured, keyless API instead of a Playwright-scraped search UI
  — different base_url from `elaws.e-gov.go.jp` (the older system), not a
  duplicate. **BLOCKED on one more verification step**: the Swagger UI is
  client-rendered — a developer should open `/api/2/redoc/` in a real
  browser or `curl` it directly to confirm the exact endpoint/parameter
  schema before writing this client (a text fetch of the swagger-ui page
  returned only a page shell this pass).

---

## 11. `open_assembly_kr` — Open National Assembly Information OpenAPI (South Korea)

- **Region**: APAC / South Korea (national)
- **API base**: `https://open.assembly.go.kr`
- **Auth**: **api_key** — free registration required through the portal
  (browsable without login, but calling any endpoint requires a
  per-endpoint authentication key). Env var: `ASSEMBLY_API_KEY`.
- **Format**: JSON/XML (per-API, typically XML by default with a JSON
  option)
- **Endpoints to call**: portal exposes dozens of named APIs — 18 for
  bills (uian), 11 for legislation (beopryul), plus member voting records.
  Each named API issues its own key at registration time.
- **CrawlResult mapping**: `url` = bill detail page constructed from the
  bill ID in the response; `title` = bill title; `content` = bill
  summary/status text; `lifecycle_stage` = bill stage field (introduced /
  committee / passed, etc.).
- **Pagination/rate limits**: no documented rate limit found. Each named
  API being a separate key request raises integration complexity — a
  client would need to manage multiple per-endpoint keys.
- **Why it matters**: complements the existing `law_kr` (enacted-law) crawl
  entry with pre-enactment bill tracking — closes the loop from proposed to
  enacted energy/DC legislation. Verified: `open.assembly.go.kr/portal/
  openapi/main.do` confirmed free browsing, registration-gated key
  issuance, bill/legislation API categories present.

---

## 12. `open_law_kr` — Open Law API (South Korea, Ministry of Government Legislation)

- **Region**: APAC / South Korea (national)
- **API base**: `https://open.law.go.kr`
- **Auth**: **api_key** — registration required through the Ministry of
  Government Legislation (beopjecheo) portal, by phone/email per the guide
  page. Env var: `LAW_GO_KR_API_KEY`.
- **Format**: XML
- **Endpoints to call**: 191 named APIs covering current/historical
  legislation, administrative rules, local ordinances, case law, treaties.
  Exact endpoint needed (likely a current-legislation search/detail API) to
  be selected from the 191-API guide list at build time.
- **CrawlResult mapping**: `url` = law detail page constructed from the law
  ID; `title` = law name; `content` = full law text; `lifecycle_stage` =
  current/historical status flag.
- **Pagination/rate limits**: no published rate limit; registration by
  phone/email (not self-serve).
- **Why it matters**: same upgrade rationale as the Japan e-Gov API (#10) —
  trades a `requires_playwright: true` crawl (the existing `law_kr` entry,
  `www.law.go.kr`) for a documented, key-based API over the identical
  statutory corpus (Rational Energy Utilization Act, etc.). Different
  base_url from `law_kr`, so net-new, not a duplicate — recommended future
  replacement/companion for `law_kr`. Verified: `open.law.go.kr/LSO/
  openApi/guideList.do` confirmed the 191-API count, XML format statement,
  registration requirement.

---

## 13. `data_gov_sg` — Singapore Open Data Portal (contingent / lowest confidence)

- **Region**: APAC / Singapore (national)
- **API base**: `https://www.data.gov.sg`
- **Auth**: none for the portal itself; per-agency dataset tokens not
  confirmed either way.
- **Format**: JSON (API), CSV
- **Endpoints to call**: NOT YET IDENTIFIED. The portal (4,500+ datasets
  across 70+ agencies) was confirmed live and API-driven, but no
  energy-efficiency, data-center, or district-cooling-specific dataset was
  located from the landing page's featured categories (Arts & Culture,
  Education, Economy, Environment, Geospatial, Housing, Health, Social,
  Transport).
- **CrawlResult mapping**: cannot be specified until a relevant dataset is
  found.
- **Pagination/rate limits**: unknown, contingent on dataset found.
- **Why it matters / status**: lowest-confidence tier-c entry in the whole
  project — included for completeness as a "worth a deeper look," not a
  ready candidate. **BEFORE any client work**: do a dataset-search pass
  within the portal (e.g. site search for "energy" or "PUE") to confirm a
  relevant dataset exists at all. If none is found, drop this candidate
  entirely rather than build a client with nothing to query.

---

## 14. `nz_legislation` — New Zealand Legislation API

- **Region**: APAC / New Zealand (national)
- **API base**: `https://api.legislation.govt.nz`
- **Auth**: **api_key** — free, but no self-serve signup form; request by
  emailing `contact@pco.govt.nz` (Parliamentary Counsel Office). Env var:
  `NZ_LEGISLATION_API_KEY`. Key passed via `api_key` query param or
  `X-Api-Key` header.
- **Format**: JSON, with linked HTML/PDF/XML per document. Three-tier data
  model: works / versions / formats.
- **Endpoints to call**: docs at `legislation.govt.nz/learn-more/
  legislation-data/developer-api/` and `api.legislation.govt.nz/docs/` (both
  confirmed live and fully documented this pass — auth, rate limits, data
  model all confirmed).
- **CrawlResult mapping**: `url` = the "work" canonical URL; `title` = Act/
  Bill/regulation title; `content` = full text via the "format" tier
  (HTML/PDF/XML linked from the work record); `lifecycle_stage` = the
  work's status field (Bill / Act / secondary legislation, in-force vs.
  repealed).
- **Pagination/rate limits**: 10,000 requests/day per key, burst cap 2,000
  req/5-min/IP; returns 429/403 on excess. Labelled "Version Zero" (beta/
  feedback status — schema may shift).
- **Why it matters**: NZ has zero legislation-API coverage today. Real,
  documented, government-run JSON API for NZ Acts, Bills and secondary
  legislation — the single best structured-API find in the Oceania/South
  Asia region alongside the Australian Energy Regulator crawl-domain find.
  Verified: `api.legislation.govt.nz/docs/` returned full API documentation
  directly.

---

## 15. `leychile` — LeyChile / BCN Legislative Web Service (Chile)

- **Region**: South America / Chile (national)
- **API base**: `https://www.leychile.cl`
- **Auth**: none — fully open, no API key, no auth
- **Format**: XML
- **Endpoints to call**: `GET /Consulta/obtxml?opt=7&idLey=<id>` (also
  accepts `idNorma`) — returns the full norm (`Ley`, `Decreto`,
  `Resolucion`, etc.) as XML with promulgation/publication dates, issuing
  body, and full consolidated text (always the current in-force version,
  footnoted for amendments). Docs:
  `leychile.cl/Consulta/legislacion_abierta_web_service` (mirrored at
  `bcn.cl/leychile/consulta/legislacion_abierta_web_service`); spec PDF at
  `leychile.cl/esquemas/accesoLeyesChilenas4.pdf`.
- **CrawlResult mapping**: `url` = the leychile.cl page for that idLey/
  idNorma; `title` = norm title/number from the `<Norma>` XML root; `content`
  = the consolidated full text (with amendment footnotes) from the same
  response; `lifecycle_stage` = "in force" (this API always returns the
  current in-force version) vs. historical, derivable from the promulgation/
  publication date fields.
- **Pagination/rate limits**: no documented rate limit; the research pass
  used ~3s between calls without issue and hit one transient 429 — throttle
  client-side. The API takes a known `idLey`/`idNorma`, NOT a keyword-search
  endpoint — an ID-discovery strategy is needed (BCN also exposes a search
  UI at `leychile.cl/Navegar` that a client could scrape or paginate to
  build an ID list, or IDs could be sourced from known law numbers like Ley
  21.305, the Energy Efficiency Law).
- **Why it matters**: only genuine open-data legislative API found across
  all six LatAm countries in scope (Chile/Colombia/Argentina/Peru/Uruguay/
  Costa Rica) — full-text, always-current Chilean law (energy efficiency
  law Ley 21.305, 2050 energy policy framework, decarbonization decrees,
  green hydrogen/renewables rules) in structured XML rather than crawled
  HTML/PDF. Verified: `curl "https://www.leychile.cl/Consulta/
  obtxml?opt=7&idLey=18575"` returned a well-formed `<Norma>` XML document
  with real legislative metadata and text.

---

## 16. `oecd_sdmx` — OECD SDMX Statistics API

- **Region**: Supranational / global (OECD + selected non-member economies)
- **API base**: `https://sdmx.oecd.org`
- **Auth**: none — keyless, "free of charge... subject to OECD Terms and
  Conditions" per OECD's own API documentation
- **Format**: XML/JSON/CSV (SDMX standard, format selectable via a `format=`
  query param)
- **Endpoints to call**: `GET /public/rest/data/{agency},{dataset},
  {version}/{selection}`. Confirmed the gateway itself is live/keyless via
  `GET /public/rest/dataflow/all?references=none` (returned a valid SDMX
  2.1 structure message tested against a climate/cities dataflow list).
  **NOT confirmed**: the specific dataflow ID for **PINE (Policy
  Instruments for the Environment)** — 4,600+ environmental policy
  instruments across 150 countries, the dataset most relevant to this
  project, mainly disseminated via a Shiny dashboard
  (`oecd-main.shinyapps.io/pinedatabase`) rather than a confirmed clean SDMX
  flow. Docs: `data.oecd.org/api/sdmx-json-documentation/` and
  `oecd.org/en/data/insights/data-explainers/2024/09/api.html`.
- **CrawlResult mapping**: cannot be fully specified until the PINE dataflow
  ID (if it exists through this gateway) is confirmed — would map to
  `url`=source document URL from the PINE record, `title`=policy instrument
  name, `content`=instrument description/scope, `lifecycle_stage`=not
  applicable (these are catalogued instruments, not bills with a
  legislative lifecycle).
- **Pagination/rate limits**: general statistics gateway, not a policy-text
  search — expect standard SDMX pagination via the `{selection}` path
  segment; no documented hard rate limit found.
- **Why it matters / status**: keyless, well-documented, genuinely global
  API gateway worth building eventually — but **PINE's practical
  reachability through it needs a follow-up session** testing the actual
  PINE dataflow ID against `sdmx.oecd.org` before committing engineering
  time. Hold this client until that's confirmed.

---

## Draft `api_sources.yaml` entries (all `enabled: false`)

```yaml
# =============================================================================
# DRAFT ADDITIONS — tier-c structured API sources from source-expansion
# research. Every entry is `enabled: false`. Each `source_type` needs a NEW
# client under src/sources/ (registered in src/sources/__init__.py) before
# `enabled` can ever be flipped to true — see new-clients.md for the full
# spec of each. None of these route through an existing client.
# =============================================================================

domains:
  - name: "Donnees Quebec - Projets de loi (Assemblee nationale du Quebec)"
    id: "donneesquebec_bills"
    enabled: false
    source_type: "donneesquebec_ckan"
    base_url: "https://www.donneesquebec.ca"
    region:
      - "north_america"
      - "canada"
      - "quebec"
    category: "legislative"
    tags:
      - "mandates"
    policy_types:
      - "legislation"
    notes: |
      Tier-c candidate from docs/source-expansion/regions/canada.md.
      CKAN Action API. License CC-BY-NC 4.0 (non-commercial) — flag for
      legal review, more restrictive than other sources in this file.
      See docs/source-expansion/draft/new-clients.md #1 for full spec.

  - name: "Storting Open Data API (Norway)"
    id: "stortinget_api"
    enabled: false
    source_type: "stortinget"
    base_url: "https://data.stortinget.no"
    region:
      - "norway"
      - "nordic"
    category: "legislation"
    tags:
      - "mandates"
    policy_types:
      - "legislation"
    notes: |
      Tier-c candidate from docs/source-expansion/regions/nordic.md.
      No API key required. See new-clients.md #2 for full spec.

  - name: "Eduskunta Open Data API (Finland)"
    id: "eduskunta_api"
    enabled: false
    source_type: "eduskunta"
    base_url: "https://avoindata.eduskunta.fi"
    region:
      - "finland"
      - "nordic"
      - "eu"
    category: "legislation"
    tags:
      - "mandates"
    policy_types:
      - "legislation"
    notes: |
      Tier-c candidate from docs/source-expansion/regions/nordic.md.
      No API key required. See new-clients.md #3 for full spec.

  - name: "European Parliament Open Data API v2"
    id: "europarl_opendata_api"
    enabled: false
    source_type: "europarl_opendata"
    base_url: "https://data.europarl.europa.eu"
    region:
      - "eu"
    category: "legislative"
    tags:
      - "mandates"
      - "research"
    policy_types:
      - "directive"
      - "law"
      - "report"
    notes: |
      Tier-c candidate from docs/source-expansion/regions/eu-uncovered.md.
      No API key required, rate-limited to 500 req/5min. See
      new-clients.md #4 for full spec.

  - name: "data.europa.eu Search API"
    id: "data_europa_eu_search_api"
    enabled: false
    source_type: "data_europa"
    base_url: "https://data.europa.eu"
    region:
      - "eu"
    category: "regulatory"
    tags:
      - "research"
      - "reporting"
    policy_types:
      - "report"
    notes: |
      CROSS-LISTED candidate: independently proposed in both
      docs/source-expansion/regions/eu-uncovered.md (#2) and
      docs/source-expansion/regions/supranational.md (#8) — merged into
      one entry here. No API key required. See new-clients.md #5 for
      the merged spec.

  - name: "Verkhovna Rada Open Data Portal (Ukraine)"
    id: "rada_opendata_ua"
    enabled: false
    source_type: "rada_opendata"
    base_url: "https://data.rada.gov.ua"
    region:
      - "eu"
      - "eu_east"
    category: "legislative"
    tags:
      - "mandates"
    policy_types:
      - "law"
      - "legislation"
    notes: |
      Tier-c candidate from docs/source-expansion/regions/eu-uncovered.md.
      No API key required (Creative Commons). PARTIALLY VERIFIED — request/
      response format not confirmed, needs one more pass before building.
      See new-clients.md #6 for full spec.

  - name: "data.gov.cy Open Data Portal (Cyprus, Ministry of Energy group)"
    id: "data_gov_cy_energy"
    enabled: false
    source_type: "dkan_cy"
    base_url: "https://data.gov.cy"
    region:
      - "eu"
      - "eu_south"
    category: "legislative"
    tags:
      - "reporting"
    policy_types:
      - "report"
    notes: |
      Tier-c candidate from docs/source-expansion/regions/eu-uncovered.md.
      No API key required (DKAN REST + Datastore API). See new-clients.md
      #7 for full spec.

  - name: "Houses of the Oireachtas Open Data API (Ireland)"
    id: "oireachtas_api"
    enabled: false
    source_type: "oireachtas"
    base_url: "https://api.oireachtas.ie"
    region:
      - "ireland"
    category: "legislation"
    tags:
      - "mandates"
    policy_types:
      - "legislation"
    notes: |
      Tier-c candidate from docs/source-expansion/regions/uk-ireland.md.
      HIGHEST-VALUE find in that region. No API key required. Verified
      end-to-end including a working keyword query against the Heat
      (Networks and Miscellaneous Provisions) Bill 2024. See
      new-clients.md #8 for full spec.

  - name: "Scottish Parliament Open Data API"
    id: "scottish_parliament_api"
    enabled: false
    source_type: "scottish_parliament"
    base_url: "https://data.parliament.scot"
    region:
      - "uk"
      - "scotland"
    category: "legislation"
    tags:
      - "mandates"
    policy_types:
      - "legislation"
    notes: |
      Tier-c candidate from docs/source-expansion/regions/uk-ireland.md.
      No API key required. Complements (does not replace) the existing
      uk_scotland_parliament HTML crawl domain. See new-clients.md #9 for
      full spec.

  - name: "e-Gov Law Search API v2 (Japan)"
    id: "egov_law_api"
    enabled: false
    source_type: "egov_law_jp"
    base_url: "https://laws.e-gov.go.jp"
    region:
      - "apac"
      - "japan"
    category: "legislative"
    tags:
      - "mandates"
      - "efficiency"
    policy_types:
      - "law"
      - "legislation"
    notes: |
      Tier-c candidate from docs/source-expansion/regions/east-asia.md.
      No API key required. Different base_url from the existing elaws_jp
      crawl entry — not a duplicate. See new-clients.md #10 for full spec.

  - name: "Open National Assembly Information OpenAPI (South Korea)"
    id: "open_assembly_kr_api"
    enabled: false
    source_type: "open_assembly_kr"
    base_url: "https://open.assembly.go.kr"
    region:
      - "apac"
      - "south_korea"
    category: "legislative"
    tags:
      - "mandates"
    policy_types:
      - "legislation"
    notes: |
      Tier-c candidate from docs/source-expansion/regions/east-asia.md.
      Requires api_key (free registration per-endpoint); env var
      ASSEMBLY_API_KEY. See new-clients.md #11 for full spec.

  - name: "Open Law API (South Korea, Ministry of Government Legislation)"
    id: "open_law_kr_api"
    enabled: false
    source_type: "open_law_kr"
    base_url: "https://open.law.go.kr"
    region:
      - "apac"
      - "south_korea"
    category: "legislative"
    tags:
      - "mandates"
      - "energy_efficiency"
    policy_types:
      - "law"
      - "legislation"
      - "regulation"
    notes: |
      Tier-c candidate from docs/source-expansion/regions/east-asia.md.
      Requires api_key (registration via phone/email); env var
      LAW_GO_KR_API_KEY. Different base_url from the existing law_kr
      crawl entry — recommended future companion/replacement. See
      new-clients.md #12 for full spec.

  - name: "Singapore Open Data Portal (data.gov.sg)"
    id: "data_gov_sg"
    enabled: false
    source_type: "data_gov_sg"
    base_url: "https://www.data.gov.sg"
    region:
      - "apac"
      - "singapore"
    category: "regulatory"
    tags: []
    policy_types:
      - "report"
    notes: |
      LOWEST-CONFIDENCE tier-c candidate from
      docs/source-expansion/regions/east-asia.md. No relevant
      energy/DC/district-cooling dataset confirmed yet — do a
      dataset-search pass before any client work; drop if none found.
      See new-clients.md #13 for full spec.

  - name: "New Zealand Legislation API"
    id: "nz_legislation_api"
    enabled: false
    source_type: "nz_legislation"
    base_url: "https://api.legislation.govt.nz"
    region:
      - "apac"
    category: "legislation"
    tags:
      - "mandates"
    policy_types:
      - "law"
      - "legislation"
      - "regulation"
    notes: |
      Tier-c candidate from docs/source-expansion/regions/oceania-south-
      asia.md. Requires api_key (request by email to contact@pco.govt.nz,
      no self-serve signup); env var NZ_LEGISLATION_API_KEY. Labelled
      "Version Zero" (beta). See new-clients.md #14 for full spec.

  - name: "LeyChile / BCN Legislative Web Service (Chile)"
    id: "leychile_api"
    enabled: false
    source_type: "leychile"
    base_url: "https://www.leychile.cl"
    region:
      - "south_america"
    category: "legislative"
    tags:
      - "mandates"
      - "efficiency"
      - "reporting"
    policy_types:
      - "law"
      - "regulation"
    notes: |
      Tier-c candidate from docs/source-expansion/regions/latam.md. Only
      genuine open-data legislative API found across all 6 LatAm countries
      in scope. No API key required. See new-clients.md #15 for full spec.

  - name: "OECD SDMX Statistics API"
    id: "oecd_sdmx_api"
    enabled: false
    source_type: "oecd_sdmx"
    base_url: "https://sdmx.oecd.org"
    region:
      - "supranational"
      - "global"
    category: "regulatory"
    tags:
      - "research"
      - "carbon"
      - "efficiency"
    policy_types:
      - "report"
    notes: |
      Tier-c candidate from docs/source-expansion/regions/supranational.md.
      No API key required. HOLD until the PINE (Policy Instruments for the
      Environment) dataflow ID is confirmed reachable through this gateway
      — see new-clients.md #16 for full spec and the open question.
```
