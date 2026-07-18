# New Structured Clients Needed — Wave 2 (tier-c)

Seventeen wave-2 tier-c candidates, across two source files
(`docs/source-expansion/regions-wave2/legislation-apis.md` and
`docs/source-expansion/regions-wave2/multilateral-portals.md`) — each needs a
NEW `source_type` client under `src/sources/` (registered in
`src/sources/__init__.py`) because none fit the shape of the 9 existing
clients (`riksdagen`, `uk_bills`, `legisinfo`, `folketing`, `eurlex_nim`,
`legiscan`, `govinfo`, `regulations_gov`, `dip`) OR the 16 wave-1 tier-c
clients already specced in `docs/source-expansion/draft/new-clients.md`. No
client code is included here — this is a spec for a future engineer, per the
brief. Dedup confirmed against both of those lists plus every existing
`api_sources.yaml` entry — no `source_type` or `base_url` overlaps.

Each spec below: proposed `source_type` id, API base, auth, response format,
endpoint(s), CrawlResult field mapping, pagination/rate-limit notes. The
draft `api_sources.yaml` entries (all `enabled: false`) follow in one fenced
block at the end of this file.

---

## Legislation APIs (7) — all keyless, all verified end-to-end

### 1. `sejm_api` — Sejm (Polish Parliament) API

- **Region**: Poland (national)
- **API base**: `https://api.sejm.gov.pl`
- **Auth**: none — keyless, no signup
- **Format**: JSON (fully-documented REST, self-describing OpenAPI at the
  base URL)
- **Endpoints to call**: `GET /sejm/term10/proceedings` (session agendas/
  proceedings, full text in `agenda` field); `GET /sejm/term10/prints?
  title=<keyword>` (bill "prints" filterable by title substring, returns
  PDF attachment links); `GET /sejm/term10/proceedings/{num}` for
  per-session detail.
- **CrawlResult mapping**: `url` = constructed Sejm print/proceeding detail
  page; `title` = print/bill title; `content` = agenda text or the PDF
  attachment link + print metadata; `lifecycle_stage` = not directly
  present — would need deriving from print status fields once inspected.
- **Pagination/rate limits**: no documented rate limit observed this
  pass.
- **Why it matters**: keyword-filterable, keyless, modern REST API over
  the full corpus of Polish bills and session records. Verified:
  `curl "https://api.sejm.gov.pl/sejm/term10/prints?title=energetyczn"`
  returned real energy-related bill records (numbers, titles, PDF links,
  dates), HTTP 200.

---

### 2. `tweede_kamer_odata` — Tweede Kamer (Dutch House of Representatives) OData API

- **Region**: Netherlands (national) — **highest-value find of this wave's
  legislation-apis pass**
- **API base**: `https://gegevensmagazijn.tweedekamer.nl`
- **Auth**: none — keyless, no signup
- **Format**: JSON (OData v4)
- **Endpoints to call**: `GET /OData/v4/2.0/Zaak?$filter=contains(Onderwerp,
  '<keyword>')` (legislative "cases" — bills, motions, amendments, written
  questions, title-filterable via OData `contains()`); also `Document`,
  `Activiteit`, `Besluit` entity sets in the same OData service.
- **CrawlResult mapping**: `url` = constructed Zaak/Document detail page;
  `title` = `Onderwerp` (subject) field; `content` = case summary/status
  text from the same response; `lifecycle_stage` = derive from the `Zaak`
  status field (not independently enumerated this pass).
- **Pagination/rate limits**: standard OData v4 `$filter`/`$top`/
  `$orderby` all work; no documented rate limit found.
- **Why it matters**: a live keyword query for "warmtenet" (heat network)
  returned a real parliamentary amendment titled "...over middelen voor
  het verhogen van de Warmtenetten Investeringssubsidie" (heat-network
  investment subsidy funding amendment) — proving the API surfaces
  exactly PolicyPulse's target policy category on the first try, zero
  auth. Verified: `curl "https://gegevensmagazijn.tweedekamer.nl/OData/
  v4/2.0/Zaak?\$filter=contains(Onderwerp,'warmtenet')&\$top=3"` returned
  that real, on-topic amendment record, HTTP 200.

---

### 3. `camara_dos_deputados_api` — Camara dos Deputados API (Brazil)

- **Region**: Brazil (national)
- **API base**: `https://dadosabertos.camara.leg.br`
- **Auth**: none — keyless
- **Format**: JSON (also XML available)
- **Endpoints to call**: `GET /api/v2/proposicoes?keywords=<term>&
  itens=<n>` (bill/proposal keyword search, paginated via a `links` array
  with `next`/`last` rels); `GET /api/v2/proposicoes/{id}` for full
  detail.
- **CrawlResult mapping**: `url` = proposal detail page from the `links`
  field; `title` = proposal ementa/title; `content` = proposal summary
  text; `lifecycle_stage` = proposal status field (not independently
  enumerated this pass).
- **Pagination/rate limits**: clean REST pagination (`pagina`/`itens`
  params); no documented hard rate limit.
- **Why it matters**: genuinely different, complementary source to the
  existing crawl entries in `config/domains/brazil.yaml`
  (gov.br/epe.gov.br energy-ministry pages) — this is the national
  legislative-bill side. Verified: `curl "https://dadosabertos.
  camara.leg.br/api/v2/proposicoes?keywords=energia&itens=2"` returned 2
  real bill records with full pagination metadata, HTTP 200; a keyword
  search surfaced a bill "Dispoe sobre a instalacao de sistema de
  aquecimento solar em edificacoes" (solar heating mandate).

---

### 4. `au_legislation_frl_api` — Federal Register of Legislation API (Australia)

- **Region**: Australia (national)
- **API base**: `https://api.prod.legislation.gov.au`
- **Auth**: none — keyless (companion human site is `legislation.gov.au`)
- **Format**: JSON (OData-flavored, `@odata.context` envelope)
- **Endpoints to call**: `GET /v1/titles?text=<keyword>` — full-text
  search across Acts, legislative instruments, regulations, returning
  title, collection type, in-force status, and status/amendment history.
- **CrawlResult mapping**: `url` = title's canonical legislation.gov.au
  page; `title` = title field; `content` = status-history text (repeal/
  amendment reasons) from the same response; `lifecycle_stage` = in-force
  vs. repealed status field, directly present in the response.
- **Pagination/rate limits**: no documented hard rate limit found.
- **Why it matters**: only true national full-text legislation search API
  found for Australia, covering Acts AND subordinate regulations (where
  technical energy-efficiency mandates usually live) — complements the
  existing `australia.yaml` crawl entries (state energy agencies) with a
  national index. Shape resembles the existing `eurlex_nim` client
  conceptually (title/status/history) — a possible implementation
  reference. Verified: `curl "https://api.prod.legislation.gov.au/v1/
  titles?text=energy"` returned real titles with full status history,
  HTTP 200.

---

### 5. `congreso_es_opendata` — Congreso de los Diputados Open Data (Spain)

- **Region**: Spain (national)
- **API base**: `https://www.congreso.es`
- **Auth**: none — keyless (a bare `curl` with no `User-Agent` gets a
  standard WAF 403; any normal browser UA string succeeds — not real auth)
- **Format**: JSON, XML, and CSV (all three offered per dataset)
- **Endpoints to call**: bulk files regenerated on a schedule and linked
  from `GET /es/opendata/iniciativas`, e.g.
  `/webpublica/opendata/iniciativas/ProyectosDeLey__<timestamp>.json`,
  `.../ProposicionesDeLey__<timestamp>.json`,
  `.../PropuestasDeReforma__<timestamp>.json`,
  `.../IniciativasLegislativasAprobadas__<timestamp>.json`. The
  `<timestamp>` in the filename changes on each regeneration — a client
  must first fetch the HTML index page to discover the current filename
  before downloading (an unusual "discover-then-download" shape, not a
  query endpoint).
- **CrawlResult mapping**: `url` = the discovered timestamped file URL;
  `title` = bill title field from the downloaded JSON; `content` = bill
  summary/status fields; `lifecycle_stage` = derived from which dataset
  category the bill appears in (Proyectos/Proposiciones/enacted).
- **Pagination/rate limits**: files regenerate multiple times daily
  (3 different timestamps observed within seconds across dataset types);
  no documented rate limit; robots.txt not checked this pass — flag for a
  quick check before building.
- **Why it matters**: real-time-generated structured JSON/XML/CSV of every
  bill category in the Spanish Congress, complementing the existing
  `spain.yaml` crawl entries (`boe.es` gazette, `miteco.gob.es` ministry).
  Verified: `curl -A "Mozilla/5.0" "https://www.congreso.es/es/opendata/
  iniciativas"` returned HTTP 200 with live `href` links to `.json`/
  `.xml`/`.csv` files timestamped with the current session date.

---

### 6. `curia_vista_odata` — Curia Vista / Swiss Parliament Web Services (OData)

- **Region**: Switzerland (national)
- **API base**: `https://ws.parlament.ch`
- **Auth**: none — keyless. Note: `ws-old.parlament.ch` (referenced in
  some older third-party docs) now 404s — the live host is
  `ws.parlament.ch`, not the "-old" one.
- **Format**: JSON (`application/json;odata=verbose`) or XML, OData v2/v3
  style
- **Endpoints to call**: `GET /odata.svc/Business?$top=<n>` and
  `$filter=substringof('<term>',Title)` for keyword search across
  parliamentary business items (motions, postulates, bills —
  "Geschaefte").
- **CrawlResult mapping**: `url` = constructed Business-item detail page;
  `title` = `Title` field; `content` = business item description/status
  from the same response; `lifecycle_stage` = business-item status field
  (not independently enumerated this pass).
- **Pagination/rate limits**: no documented hard rate limit found;
  standard OData `$top`/`$filter` pagination.
- **Why it matters**: Swiss federal-level motions/postulates on
  data-center energy efficiency and waste-heat reuse are only visible
  through this API, not through the extensive cantonal crawl domains
  already in the repo (which cover enacted law, not in-progress federal
  motions). A newer community wrapper (`openparldata.ch`) exists but the
  official OData service is the primary source. Verified:
  `curl "https://ws.parlament.ch/odata.svc/Business?\$top=1"` returned
  HTTP 200 with a real JSON body (3363 bytes); a keyword filter query
  returned a valid empty-result OData envelope (`{"d":[]}`), confirming
  the filter syntax is accepted by the live service.

---

### 7. `assemblee_nationale_opendata` — Assemblee Nationale Open Data (France)

- **Region**: France (national)
- **API base**: `https://data.assemblee-nationale.fr`
- **Auth**: none — keyless
- **Format**: JSON and XML (bulk ZIP archives per data category, not a
  query API)
- **Endpoints to call**: bulk downloads such as
  `/static/openData/repository/17/loi/dossiers_legislatifs/
  Dossiers_Legislatifs.json.zip` (all legislative dossiers for the
  current 17th legislature — bills under examination, adopted texts,
  committee reports, rapporteur assignments) and the equivalent `.xml.zip`;
  similar archives exist for amendments (~1hr update latency per the
  site's own FAQ) and prior legislatures under `/archives-16e/`,
  `/archives-15e/`.
- **CrawlResult mapping**: `url` = constructed dossier detail page on
  assemblee-nationale.fr; `title` = dossier title from the archive;
  `content` = dossier summary/status text; `lifecycle_stage` = dossier
  status field within the JSON (bill under examination / adopted /
  committee stage).
- **Pagination/rate limits**: no documented rate limit (static file
  download, not a query endpoint); `dossiers_legislatifs` archive
  confirmed regenerated same-day (`Last-Modified` header dated the
  research session's date).
- **Why it matters**: full legislative-dossier TEXT (not just metadata)
  for every French bill in progress, machine-readable, zero auth. Distinct
  base_url from the existing `legifrance.gouv.fr` crawl entries in
  `france.yaml` (enacted-law text) — this is the legislative-process
  side. **Related, higher-effort companion NOT independently specced
  here**: the PISTE/Legifrance API (`api.piste.gouv.fr`) — confirmed
  reachable (sandbox returned HTTP 400, i.e. live but rejecting
  unauthenticated calls) but requires free OAuth2 client registration via
  `https://piste.gouv.fr` (env vars would be `PISTE_CLIENT_ID` /
  `PISTE_CLIENT_SECRET`) and was not registered/tested end-to-end.
  Verified: `curl -I "https://data.assemblee-nationale.fr/static/openData/
  repository/17/loi/dossiers_legislatifs/Dossiers_Legislatifs.json.zip"`
  returned HTTP 200, `Content-Type: application/zip`,
  `Content-Length: 10095333` (~10MB), current `Last-Modified`.

---

## Multilateral / Regional (2) — keyless, needs indicator/dataflow ID follow-up

### 8. `climatewatch_ndc` — Climate Watch NDC Content API (World Resources Institute)

- **Region**: Supranational / global (171+ countries)
- **API base**: `https://www.climatewatchdata.org`
- **Auth**: none — keyless, confirmed live
- **Format**: JSON
- **Endpoints to call**: `GET /api/v1/data/historical_emissions?
  source_ids[]=<id>` (confirmed live, real 200 JSON with country/sector/
  gas columns); `GET /api/v1/data/ndc_content?location=<ISO3>&
  category_ids[]=<id>` (confirmed live, real 200 JSON with `id, source,
  iso_code3, country, sector, subsector, indicator_slug, value,
  indicator_name` columns). Both calls this pass used guessed
  parameter IDs and returned empty `data` arrays — endpoints/schema are
  confirmed live, but the exact energy-efficiency/buildings/waste-heat
  `category_ids`/indicator slugs still need enumerating from Climate
  Watch's own category list before a client can pull real content.
- **CrawlResult mapping**: `url` = constructed NDC country page
  (`climatewatchdata.org/ndcs/country/<ISO3>`); `title` = country +
  indicator name; `content` = indicator value/text from the `ndc_content`
  response; `lifecycle_stage` = not applicable (NDC submissions are the
  lifecycle stage itself).
- **Pagination/rate limits**: none documented; no hard rate limit hit
  this pass.
- **Why it matters**: NDCs (Paris Agreement national commitments) are
  exactly the "policy commitment" layer this project's taxonomy covers,
  across 171+ countries in one API with 150+ structured indicators, some
  of which cover energy efficiency/buildings sectors. **HOLD**: needs one
  more pass to enumerate the specific `category_ids`/indicator slugs for
  energy efficiency before building.

---

### 9. `eurostat_energy` — Eurostat REST Dissemination API (energy balance statistics)

- **Region**: EU (27 member states) + EFTA/candidate countries
- **API base**: `https://ec.europa.eu/eurostat/api/dissemination`
- **Auth**: none — keyless, EU open-data terms
- **Format**: JSON (SDMX-JSON 2.0), also CSV/XML via `format=` param
- **Endpoints to call**: `GET /statistics/1.0/data/{dataset_code}?
  format=JSON&lang=EN&{dimension filters}` — tested against `nrg_bal_c`
  (Complete Energy Balances), which returned valid SDMX-JSON structural
  metadata (35 years of data, 1990-2024, for Germany) confirming the
  dataset/gateway are both real and live. The specific waste-heat
  product/flow code combination queried returned no populated
  observations — the exact SIEC/NRG_BAL code for "waste heat" needs
  looking up in Eurostat's own code-list browser before a client can
  reliably pull that specific series (the dataset/gateway themselves are
  not in question).
- **CrawlResult mapping**: `url` = Eurostat's own dataset browser page for
  the queried code; `title` = dataset name + country + indicator;
  `content` = observation values + metadata description;
  `lifecycle_stage` = not applicable (statistical series, not a
  legislative lifecycle).
- **Pagination/rate limits**: no documented hard limit; standard EU API
  courtesy throttling recommended.
- **Why it matters**: the EU's own statistical office (distinct from the
  `data_europa` meta-catalog already drafted wave 1) with a real,
  documented, keyless REST API for energy statistics across all 27 EU
  member states in one call. Treat as a discovery/context layer alongside
  legal-text sources, same caveat wave 1 gave `data_europa` (statistical,
  not primarily legislative).

---

## National Open-Data Portal APIs (8) — Target 2 of multilateral-portals.md

**Consolidation recommendation**: Italy, Ireland, Canada, Mexico, and UK
below all share an identical CKAN Action API request/response shape
(`package_search`, `"success": true` envelope). Recommend building ONE
generic `ckan_action_api` client parameterized by `base_url`, rather than
five bespoke `source_type`s — each entry below still gets its own
`api_sources.yaml` row (different base_url/region/notes) but all five can
route through the same client code. France (udata), Spain (linked-data/
DCAT-AP-ES), and the US (GSA-gated CKAN) each need their OWN client due to
genuinely different API shapes or auth.

### 10. `data_gouv_fr_api` — data.gouv.fr Open Data API (France)

- **Region**: France (national)
- **API base**: `https://www.data.gouv.fr`
- **Auth**: none — keyless
- **Format**: JSON. **Not CKAN** — France's portal runs on **udata**
  (Etalab's own open-source platform), own REST API at `/api/1/`.
- **Endpoints to call**: `GET /api/1/datasets/?q=<query>` — confirmed
  live, returns `{"data": [...], "page", "page_size", "total"}`.
- **CrawlResult mapping**: `url` = dataset's own page/resource URL from
  the response; `title` = dataset title; `content` = dataset description;
  `lifecycle_stage` = not applicable for most hits, though several
  results ARE regulatory instruments (see below) rather than pure
  statistics.
- **Pagination/rate limits**: no documented hard limit found this pass.
- **Why it matters**: unlike most open-data-portal hits in this file
  (mostly statistical tables), several results here ARE regulatory
  instruments with real legal force — "Zone de developpement prioritaire
  du reseau de chaleur" (Paris priority-development zones), "Perimetre de
  raccordement obligatoire au reseau de chaleur urbain" (Bordeaux
  mandatory-connection zoning), "Part de chaleur decarbonee produite
  (ENR&R renouvelable et de recuperation)" (tracks recovered/reused heat
  share — directly maps to this project's waste-heat taxonomy). Highest
  policy-relevance hit of any Target-2 portal tested. Verified:
  `q=reseau+de+chaleur` returned the datasets above; `q=chaleur+fatale`
  (French for "waste heat") returned 0 results — use the district-heating
  French term, not a literal translation.

---

### 11. `ckan_action_api` (Italy instance) — dati.gov.it Open Data API

- **Region**: Italy (national)
- **API base**: `https://www.dati.gov.it`
- **Auth**: none — keyless
- **Format**: JSON (CKAN Action API — confirmed via `package_search`,
  `"success": true`)
- **Endpoints to call**: `GET /opendata/api/3/action/package_search?
  q=efficienza+energetica&rows=5` — confirmed live, 5 real results.
- **CrawlResult mapping**: `url` = dataset resource download URL;
  `title` = dataset title; `content` = dataset notes/description;
  `lifecycle_stage` = not applicable (statistical/administrative
  datasets).
- **Pagination/rate limits**: not documented this pass; standard CKAN
  courtesy throttling recommended.
- **Why it matters**: results are mostly regional/provincial statistical
  tables (Umbria EE-report counts, Trento Energy Performance
  Certificates, provincial EE incentive programs, ENEA agency news feed),
  with at least one real incentive-program dataset ("Incentivi Legge
  Provinciale 14/80 - Efficientamento energetico"). Build as a parameterized
  instance of the shared `ckan_action_api` client (see consolidation note
  above).

---

### 12. `datos_gob_es_api` — datos.gob.es apidata (Spain, linked-data API)

- **Region**: Spain (national)
- **API base**: `https://datos.gob.es`
- **Auth**: none — keyless
- **Format**: JSON (default), also XML/RDF/Turtle/CSV via content
  negotiation. **Not CKAN** — a Linked Data API (DCAT-AP-ES, "apidata").
- **Endpoints to call**: `GET /apidata/catalog/dataset/title/<keyword>` —
  this is an EXACT/SUBSTRING title match, NOT full-text search (a
  free-text query like "eficiencia energetica" returned 0 results; the
  single word "energia" returned 2 real hits) — a client needs either
  exact known titles or a broader crawl-then-filter strategy.
- **CrawlResult mapping**: `url` = dataset's catalog page; `title` =
  dataset title field; `content` = dataset description; `lifecycle_stage`
  = not applicable (statistical/administrative datasets).
- **Pagination/rate limits**: not documented this pass.
- **Why it matters**: confirmed real datasets: "Estadisticas delegadas de
  petroleo, gas y energia electrica" and "Registro de productores de
  energia electrica" (electricity producer registry) — statistical/
  administrative, not legislative. Needs its OWN client (distinct from
  the CKAN shape) due to the exact-title-match search behavior.

---

### 13. `ckan_action_api` (Ireland instance) — data.gov.ie Open Data API

- **Region**: Ireland (national)
- **API base**: `https://data.gov.ie`
- **Auth**: none — keyless
- **Format**: JSON (CKAN — confirmed via `package_search`,
  `"success": true`)
- **Endpoints to call**: `GET /api/3/action/package_search?q=energy+
  efficiency&rows=5` — 19 total results.
- **CrawlResult mapping**: same as the Italy CKAN instance above.
- **Pagination/rate limits**: not documented this pass.
- **Why it matters**: results are local-authority housing-retrofit data
  (Fingal County Council) and CSO household energy-efficiency-
  installation statistics — statistical, not legislative. LOWER priority
  than the already-specced `oireachtas` tier-c candidate (wave-1
  new-clients.md #8) for actual Irish legislative text, since this
  portal is statistics-only for this query. Build as a parameterized
  instance of the shared `ckan_action_api` client.

---

### 14. `ckan_action_api` (Canada instance) — Open Government Canada CKAN API

- **Region**: Canada (national)
- **API base**: `https://open.canada.ca`
- **Auth**: none — keyless
- **Format**: JSON (CKAN — confirmed)
- **Endpoints to call**: `GET /data/api/3/action/package_search?q=data+
  centre+energy+efficiency&rows=5` — 100 results (rows capped, likely far
  more total).
- **CrawlResult mapping**: same as the Italy CKAN instance above.
- **Pagination/rate limits**: not documented this pass.
- **Why it matters**: results include NRCan's "Survey of Commercial and
  Institutional Energy Use," "Canada's Energy Future 2026," EnerGuide
  appliance-label data — statistical/administrative, complements (does
  not replace) the existing `legisinfo_api` client already in
  `config/domains/api_sources.yaml`. Build as a parameterized instance of
  the shared `ckan_action_api` client.

---

### 15. `ckan_action_api` (Mexico instance) — datos.gob.mx Open Data API

- **Region**: Mexico (national)
- **API base**: `https://www.datos.gob.mx` (note: **www prefix required**
  — the bare `datos.gob.mx/api/...` and `/busca/api/...` paths both
  404'd; only `https://www.datos.gob.mx/api/3/action/...` resolved)
- **Auth**: none — keyless
- **Format**: JSON (CKAN — confirmed)
- **Endpoints to call**: `GET /api/3/action/package_search?q=energia&
  rows=5` — 81 results.
- **CrawlResult mapping**: same as the Italy CKAN instance above.
- **Pagination/rate limits**: not documented this pass.
- **Why it matters**: real datasets from CFE (Federal Electricity
  Commission) and CENACE (National Energy Control Center) — electricity
  consumption, marginal energy prices, an "Energy-Saving Technologies
  Evaluation" (ETA) program. Statistical/administrative. Build as a
  parameterized instance of the shared `ckan_action_api` client — but
  hardcode the `www.` prefix for this instance specifically.

---

### 16. `data_gov_us_gsa_api` — Data.gov (GSA gateway to CKAN Action API)

- **Region**: United States (national)
- **API base**: `https://api.gsa.gov/technology/datagov/v3` (the GSA API
  gateway now fronts the underlying CKAN instance at catalog.data.gov —
  a direct hit to `catalog.data.gov/api/3/action/...` 404'd this session,
  confirming the gateway is now the only working path)
- **Auth**: **api_key** — a shared `DEMO_KEY` worked for this session's
  test query (rate-limited, shared across all api.data.gov demo users);
  production use needs a free personal key from
  `https://api.data.gov/signup/`. Env var: `DATA_GOV_API_KEY`.
- **Format**: JSON (CKAN-shaped payload through the GSA gateway)
- **Endpoints to call**: `GET /action/package_search?q=data+center+
  energy+efficiency&rows=5&api_key=DEMO_KEY` — confirmed live, 4,363
  total results.
- **CrawlResult mapping**: same shape as the plain-CKAN instances above,
  but the auth layer (api_key as a query param through a GSA gateway
  rather than a bare CKAN instance) is a real difference — needs its OWN
  client, not a `ckan_action_api` instance.
- **Pagination/rate limits**: DEMO_KEY is explicitly rate-limited/shared;
  a registered personal key raises the limit (exact numbers in
  api.data.gov's own docs, not independently re-confirmed).
- **Why it matters / correction**: the wave-2 research corrects an
  assumption that data.gov is keyless like the other national CKAN
  portals in this file — it is NOT, for the US specifically. Results
  include DOE's FuelEconomy.gov, alternative-fueling station data, and
  "NYC Building Energy and Water Data Disclosure for Local Law 84" (a
  real municipal energy-benchmarking-law compliance dataset — the
  closest thing to actual policy-adjacent data found in this US query).

---

### 17. `ckan_action_api` (UK instance, general query) — data.gov.uk CKAN Action API

- **Region**: United Kingdom (national)
- **API base**: `https://www.data.gov.uk` (redirects to the underlying
  instance at `ckan.publishing.service.gov.uk` — confirmed via a live
  301)
- **Auth**: none — keyless
- **Format**: JSON (CKAN — confirmed)
- **Endpoints to call**: `GET /api/3/action/package_search?q=heat+
  network+data+centre&rows=5` (via the redirect target) — confirmed
  live, **1,793 total results**.
- **CrawlResult mapping**: same as the Italy CKAN instance above.
- **Pagination/rate limits**: UK guidance states no rate limit on this
  API (per a `guidance.data.gov.uk` doc page surfaced during research,
  not independently re-fetched).
- **DEDUP NOTE**: `config/domains/uk.yaml` already has `uk_hnpd`
  (`enabled: true`) pointed at `https://www.data.gov.uk`, but that entry
  is a plain crawl domain scoped to ONE dataset page (the DESNZ Heat
  Networks Planning Database). This candidate is the general
  `package_search` action surfacing ALL matching datasets on the portal
  — not a duplicate in function, though it shares a base_url with an
  existing entry (flagged explicitly rather than silently added as a
  second same-base_url crawl entry).
  Verified: the existing `uk_hnpd` dataset itself appeared in the top
  results ("DESNZ: Heat Networks Planning Database"), alongside others
  like "Heat Network Locations (Existing and Planned) - Scotland" and
  "Heat Networks Polling - January 2026" — a real client here would
  automatically pick up new/updated UK heat-network datasets as they
  publish, at the same access cost. Build as a parameterized instance of
  the shared `ckan_action_api` client.

---

## Target 2 portals checked but NOT specced above (unreachable/uncertain this pass)

Per `multilateral-portals.md`'s own "Unverified" section — do not build
clients against these without a follow-up verification pass:

- **Germany — govdata.de**: CKAN API shape is real/documented but every
  fetch this session returned `ECONNREFUSED` (networking-layer failure,
  not a confirmed-down site).
- **Australia — data.gov.au**: every attempt (CKAN API, HTML search page,
  even `/robots.txt`) returned HTTP 403 — session-level bot-blocking
  suspected, not confirmed down.
- **Netherlands — data.overheid.nl**: CKAN API IS reachable
  (`"success": true` confirmed), but the query tried
  (`energie+efficiency`) returned 0 results — try Dutch-language terms
  ("energie-efficientie", "warmtenet") before ranking this candidate.
- **Brazil — dados.gov.br**: classic CKAN path returned HTTP 401
  Unauthorized; the portal's own help article describes a "consumer
  profile" registration step — likely `api_key`-gated now, not `none` as
  the brief originally assumed. Needs a human pass to confirm the
  registration process before treating as a `none`-access candidate.

---

## Draft `api_sources.yaml` entries (all `enabled: false`)

```yaml
# =============================================================================
# DRAFT WAVE 2 ADDITIONS — tier-c structured API sources from wave-2
# source-expansion research. Every entry is `enabled: false`. Each
# `source_type` needs a NEW client under src/sources/ (registered in
# src/sources/__init__.py) before `enabled` can ever be flipped to true —
# see docs/source-expansion/draft/new-clients-wave2.md for the full spec of
# each. None of these route through an existing (wave-1 or shipped) client.
#
# Consolidation note: the five `ckan_action_api` rows below (Italy, Ireland,
# Canada, Mexico, UK) are recommended to share ONE client implementation
# parameterized by base_url — see new-clients-wave2.md's consolidation note.
# =============================================================================

domains:
  - name: "Sejm API (Poland)"
    id: "sejm_api"
    enabled: false
    source_type: "sejm_api"
    base_url: "https://api.sejm.gov.pl"
    region:
      - "poland"
    category: "legislative"
    tags:
      - "mandates"
    policy_types:
      - "law"
      - "legislation"
    notes: |
      Wave 2 tier-c candidate from docs/source-expansion/regions-wave2/
      legislation-apis.md #1. Keyless, self-describing OpenAPI. Verified
      end-to-end with a keyword query against energy-related bills. See
      new-clients-wave2.md #1 for full spec.

  - name: "Tweede Kamer Open Data / Gegevensmagazijn (Netherlands)"
    id: "tweede_kamer_odata"
    enabled: false
    source_type: "tweede_kamer_odata"
    base_url: "https://gegevensmagazijn.tweedekamer.nl"
    region:
      - "netherlands"
      - "eu"
      - "eu_west"
    category: "legislative"
    tags:
      - "mandates"
    policy_types:
      - "legislation"
    notes: |
      Wave 2 tier-c candidate, HIGHEST-VALUE find in
      legislation-apis.md (#2). Keyless OData v4. Verified end-to-end:
      a live "warmtenet" (heat network) query returned a real
      heat-network-subsidy amendment. See new-clients-wave2.md #2.

  - name: "Camara dos Deputados Dados Abertos API (Brazil)"
    id: "camara_dos_deputados_api"
    enabled: false
    source_type: "camara_dos_deputados_api"
    base_url: "https://dadosabertos.camara.leg.br"
    region:
      - "brazil"
      - "south_america"
    category: "legislative"
    tags:
      - "mandates"
    policy_types:
      - "law"
      - "legislation"
    notes: |
      Wave 2 tier-c candidate from legislation-apis.md #3. Keyless REST.
      Complements (not a duplicate of) the existing brazil.yaml crawl
      entries. See new-clients-wave2.md #3.

  - name: "Federal Register of Legislation API (Australia)"
    id: "au_legislation_frl_api"
    enabled: false
    source_type: "au_legislation_frl_api"
    base_url: "https://api.prod.legislation.gov.au"
    region:
      - "australia"
      - "apac"
    category: "legislative"
    tags:
      - "mandates"
    policy_types:
      - "law"
      - "regulation"
      - "legislation"
    notes: |
      Wave 2 tier-c candidate from legislation-apis.md #4. Keyless. Only
      true national full-text legislation search for Australia, covers
      Acts and subordinate regulations. See new-clients-wave2.md #4.

  - name: "Congreso de los Diputados Open Data (Spain)"
    id: "congreso_es_opendata"
    enabled: false
    source_type: "congreso_es_opendata"
    base_url: "https://www.congreso.es"
    region:
      - "spain"
      - "eu"
      - "eu_south"
    category: "legislative"
    tags:
      - "mandates"
    policy_types:
      - "law"
      - "legislation"
    notes: |
      Wave 2 tier-c candidate from legislation-apis.md #5. Keyless
      (bare-curl 403 is a WAF UA check, not real auth). Unusual
      discover-then-download shape (index page -> timestamped file). See
      new-clients-wave2.md #5.

  - name: "Curia Vista OData Web Services (Switzerland)"
    id: "curia_vista_odata"
    enabled: false
    source_type: "curia_vista_odata"
    base_url: "https://ws.parlament.ch"
    region:
      - "switzerland"
      - "eu_central"
    category: "legislative"
    tags:
      - "mandates"
    policy_types:
      - "legislation"
    notes: |
      Wave 2 tier-c candidate from legislation-apis.md #6. Keyless
      OData v2/verbose. Surfaces federal-level motions/postulates not
      visible through the extensive cantonal crawl domains already in
      the repo. See new-clients-wave2.md #6.

  - name: "Assemblee Nationale Open Data (France)"
    id: "assemblee_nationale_opendata"
    enabled: false
    source_type: "assemblee_nationale_opendata"
    base_url: "https://data.assemblee-nationale.fr"
    region:
      - "france"
      - "eu"
      - "eu_central"
    category: "legislative"
    tags:
      - "mandates"
    policy_types:
      - "legislation"
      - "law"
    notes: |
      Wave 2 tier-c candidate from legislation-apis.md #7. Keyless bulk
      ZIP archives, distinct base_url from the existing legifrance.gouv.fr
      crawl entries. See new-clients-wave2.md #7.

  - name: "Climate Watch NDC Content API (World Resources Institute)"
    id: "climatewatch_ndc"
    enabled: false
    source_type: "climatewatch_ndc"
    base_url: "https://www.climatewatchdata.org"
    region:
      - "supranational"
      - "global"
    category: "regulatory"
    tags:
      - "research"
      - "reporting"
    policy_types:
      - "report"
    notes: |
      Wave 2 tier-c candidate from
      docs/source-expansion/regions-wave2/multilateral-portals.md
      Target 1 #9. Keyless. HOLD until the energy-efficiency/buildings
      category_ids are enumerated from Climate Watch's own category
      list. See new-clients-wave2.md #8.

  - name: "Eurostat REST Dissemination API - Energy Balances"
    id: "eurostat_energy"
    enabled: false
    source_type: "eurostat_energy"
    base_url: "https://ec.europa.eu/eurostat/api/dissemination"
    region:
      - "eu"
    category: "regulatory"
    tags:
      - "research"
      - "reporting"
    policy_types:
      - "report"
    notes: |
      Wave 2 tier-c candidate from multilateral-portals.md Target 1 #10.
      Keyless SDMX-JSON. Distinct from the wave-1 data_europa meta-catalog
      client. HOLD until the exact SIEC/NRG_BAL waste-heat code is
      confirmed. See new-clients-wave2.md #9.

  - name: "data.gouv.fr Open Data API (France)"
    id: "data_gouv_fr_api"
    enabled: false
    source_type: "data_gouv_fr_api"
    base_url: "https://www.data.gouv.fr"
    region:
      - "france"
      - "eu"
    category: "district_heating"
    tags:
      - "efficiency"
      - "planning"
    policy_types:
      - "report"
      - "regulation"
    notes: |
      Wave 2 tier-c candidate from multilateral-portals.md Target 2 #11.
      Keyless udata API (not CKAN) — needs its own client. Highest
      policy-relevance Target-2 hit: several results are real regulatory
      instruments (mandatory district-heating connection zones), not just
      statistics. See new-clients-wave2.md #10.

  - name: "dati.gov.it Open Data API (Italy)"
    id: "dati_gov_it_api"
    enabled: false
    source_type: "ckan_action_api"
    base_url: "https://www.dati.gov.it"
    region:
      - "italy"
      - "eu"
    category: "energy_ministry"
    tags:
      - "efficiency"
      - "reporting"
    policy_types:
      - "report"
    notes: |
      Wave 2 tier-c candidate from multilateral-portals.md Target 2 #12.
      Keyless CKAN. Recommend building as one instance of a shared
      generic ckan_action_api client (see new-clients-wave2.md
      consolidation note) rather than a bespoke client.

  - name: "datos.gob.es apidata (Spain)"
    id: "datos_gob_es_api"
    enabled: false
    source_type: "datos_gob_es_api"
    base_url: "https://datos.gob.es"
    region:
      - "spain"
      - "eu"
    category: "energy_ministry"
    tags:
      - "efficiency"
      - "reporting"
    policy_types:
      - "report"
    notes: |
      Wave 2 tier-c candidate from multilateral-portals.md Target 2 #13.
      Keyless Linked Data API (DCAT-AP-ES), NOT CKAN — needs its own
      client (exact/substring title match only, not full-text search).
      See new-clients-wave2.md #12.

  - name: "data.gov.ie Open Data API (Ireland)"
    id: "data_gov_ie_api"
    enabled: false
    source_type: "ckan_action_api"
    base_url: "https://data.gov.ie"
    region:
      - "ireland"
    category: "energy_ministry"
    tags:
      - "efficiency"
      - "reporting"
    policy_types:
      - "report"
    notes: |
      Wave 2 tier-c candidate from multilateral-portals.md Target 2 #14.
      Keyless CKAN. Same shared ckan_action_api client recommendation as
      dati_gov_it_api. Lower priority than the wave-1 oireachtas client
      for actual Irish legislative text — this portal is statistics-only.

  - name: "Open Government Canada CKAN API"
    id: "open_canada_ca_api"
    enabled: false
    source_type: "ckan_action_api"
    base_url: "https://open.canada.ca"
    region:
      - "canada"
      - "north_america"
    category: "energy_ministry"
    tags:
      - "efficiency"
      - "reporting"
    policy_types:
      - "report"
    notes: |
      Wave 2 tier-c candidate from multilateral-portals.md Target 2 #15.
      Keyless CKAN. Same shared ckan_action_api client recommendation.
      Complements (does not replace) the existing legisinfo_api client.

  - name: "datos.gob.mx Open Data API (Mexico)"
    id: "datos_gob_mx_api"
    enabled: false
    source_type: "ckan_action_api"
    base_url: "https://www.datos.gob.mx"
    region:
      - "mexico"
      - "north_america"
    category: "energy_ministry"
    tags:
      - "efficiency"
      - "reporting"
    policy_types:
      - "report"
    notes: |
      Wave 2 tier-c candidate from multilateral-portals.md Target 2 #16.
      Keyless CKAN. NOTE: www prefix required in base_url — bare
      datos.gob.mx 404s. Same shared ckan_action_api client
      recommendation.

  - name: "Data.gov (GSA gateway to CKAN Action API, US)"
    id: "data_gov_us_api"
    enabled: false
    source_type: "data_gov_us_gsa_api"
    base_url: "https://api.gsa.gov/technology/datagov/v3"
    region:
      - "us"
    category: "energy_ministry"
    tags:
      - "efficiency"
      - "reporting"
    policy_types:
      - "report"
    notes: |
      Wave 2 tier-c candidate from multilateral-portals.md Target 2 #17.
      Requires api_key (free DATA_GOV_API_KEY via api.data.gov/signup/;
      DEMO_KEY works for low-volume testing, shared/rate-limited).
      CORRECTS the assumption that data.gov is keyless like peer national
      CKAN portals. See new-clients-wave2.md #16.

  - name: "data.gov.uk CKAN Action API (general query)"
    id: "data_gov_uk_ckan_api"
    enabled: false
    source_type: "ckan_action_api"
    base_url: "https://www.data.gov.uk"
    region:
      - "uk"
    category: "district_heating"
    tags:
      - "efficiency"
      - "reporting"
    policy_types:
      - "report"
    notes: |
      Wave 2 tier-c candidate from multilateral-portals.md Target 2 #18.
      Keyless CKAN. DEDUP FLAG: shares base_url with the existing
      enabled `uk_hnpd` crawl entry in config/domains/uk.yaml, but is
      functionally different (general package_search vs. one hardcoded
      dataset page) — not a duplicate, flagged per the brief's dedup
      instructions. Same shared ckan_action_api client recommendation.
```
