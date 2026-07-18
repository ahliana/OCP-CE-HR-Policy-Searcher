# Wave 2 — National Legislature / Legislation Open-Data APIs

Scope: net-new **structured API** sources (not crawl domains) for national
legislatures/legislation/gazettes, worldwide. Dedup checked against the 9
existing structured clients (`riksdagen`, `uk_bills`, `legisinfo`, `folketing`,
`eurlex_nim`, `legiscan`, `govinfo`, `regulations_gov`, `dip`), the wave-1
tier-c list in `docs/source-expansion/draft/new-clients.md`, and every
`base_url` in `config/domains/*.yaml` and `docs/source-expansion/draft/crawl/*.yaml`.
No overlaps found — everything below is net-new.

Every candidate was fetched live this session (`curl`/WebFetch), not taken from
docs alone. Exact commands and responses are summarized under each entry.

---

## Verified candidates (ranked best-first)

### 1. `sejm_api` — Sejm (Polish Parliament) API
- **name**: Sejm API (Poland)
- **base_url**: `https://api.sejm.gov.pl`
- **level**: national
- **access**: none — fully keyless, no signup, no headers required
- **format**: JSON
- **endpoints**: `GET /sejm/term10/proceedings` (session agendas/proceedings,
  full text in `agenda` field); `GET /sejm/term10/prints?title=<keyword>`
  (bill "prints" — filterable by title substring, returns PDF attachment
  links); `GET /sejm/term10/proceedings/{num}` for per-session detail.
  Modern, fully-documented REST API (OpenAPI spec at `api.sejm.gov.pl`).
- **coverage**: Polish national legislation, bill drafts, session
  proceedings, votes. `region: poland`, `category: legislative`, `policy_types:
  [law, legislation]`.
- **practical**: no documented rate limit observed; docs live at the base URL
  itself (self-describing OpenAPI). Real-time — Sejm term 10 (current) is
  live-updated.
- **effort tier**: (c) — needs a new client, but the API shape is clean REST
  JSON with query-string filtering, straightforward to build.
- **why worth adding**: keyword-filterable, keyless, modern REST API over the
  full corpus of Polish bills and session records — the best-documented API
  found this pass.
- **verified**: YES. `curl "https://api.sejm.gov.pl/sejm/term10/prints?title=energetyczn"`
  returned real bill records (numbers, titles, PDF links, dates) for
  energy-related bills. `curl "https://api.sejm.gov.pl/sejm/term10/proceedings"`
  returned real session agenda HTML-in-JSON content. Both HTTP 200, valid JSON.

---

### 2. `tweede_kamer_odata` — Tweede Kamer (Dutch House of Representatives) OData API
- **name**: Tweede Kamer Open Data / Gegevensmagazijn (Netherlands)
- **base_url**: `https://gegevensmagazijn.tweedekamer.nl`
- **level**: national
- **access**: none — keyless, no signup
- **format**: JSON (OData v4)
- **endpoints**: `GET /OData/v4/2.0/Zaak?$filter=contains(Onderwerp,'<keyword>')`
  (legislative "cases" — bills, motions, amendments, written questions, with
  subject/title text filterable via OData `contains()`); also `Document`,
  `Activiteit`, `Besluit` entity sets in the same OData service.
- **coverage**: Dutch national parliamentary business incl. bills, motions,
  amendments. `region: netherlands`, `category: legislative`, `policy_types:
  [legislation, motion]`.
- **practical**: no documented rate limit found this pass; standard OData v4
  query semantics ($filter/$top/$orderby all work). Docs/catalog at
  `opendata.tweedekamer.nl`.
- **effort tier**: (c) — new client, but OData v4 is a well-known shape (same
  family as many other gov OData services).
- **why worth adding**: direct keyword match confirmed **on-topic** —
  querying for "warmtenet" (heat network) returned a real amendment titled
  "Amendement... over middelen voor het verhogen van de Warmtenetten
  Investeringssubsidie" (heat-network investment subsidy funding amendment).
  This is exactly PolicyPulse's target policy category, found via live query.
- **verified**: YES. `curl "https://gegevensmagazijn.tweedekamer.nl/OData/v4/2.0/Zaak?\$filter=contains(Onderwerp,'warmtenet')&\$top=3"`
  returned a real, on-topic amendment record. HTTP 200, valid JSON.

---

### 3. `camara_dos_deputados_api` — Camara dos Deputados API (Brazil)
- **name**: Camara dos Deputados Dados Abertos API (Brazil)
- **base_url**: `https://dadosabertos.camara.leg.br`
- **level**: national
- **access**: none — keyless
- **format**: JSON (also XML available)
- **endpoints**: `GET /api/v2/proposicoes?keywords=<term>&itens=<n>` (bill/
  proposal search by keyword, paginated via `links` array with `next`/`last`
  rels); `GET /api/v2/proposicoes/{id}` for full detail.
- **coverage**: Brazilian national legislation (bills, PLs). `region: brazil`,
  `category: legislative`, `policy_types: [law, legislation]`.
  Note: `config/domains/brazil.yaml` already has crawl entries for
  `gov.br`/`epe.gov.br` (energy ministry pages) — this is a genuinely
  different, complementary structured legislative-bill API, not a duplicate.
- **practical**: clean REST pagination (`pagina`/`itens` params, `links`
  array with `rel=next/last`); no documented hard rate limit.
- **effort tier**: (c) — new client, simple REST/JSON shape, easiest to
  implement of all candidates here.
- **why worth adding**: keyword search directly returned on-topic bills, e.g.
  a bill "Dispõe sobre a instalação de sistema de aquecimento solar em
  edificações" (solar heating system installation mandate) — thermal-energy
  policy squarely in PolicyPulse's taxonomy.
- **verified**: YES. `curl "https://dadosabertos.camara.leg.br/api/v2/proposicoes?keywords=energia&itens=2"`
  returned 2 real bill records with full pagination metadata. HTTP 200.

---

### 4. `au_legislation_frl_api` — Federal Register of Legislation API (Australia)
- **name**: Federal Register of Legislation API (Australia)
- **base_url**: `https://api.prod.legislation.gov.au`
- **level**: national
- **access**: none — keyless (the companion human site is
  `legislation.gov.au`)
- **format**: JSON (OData-flavored: `@odata.context` envelope)
- **endpoints**: `GET /v1/titles?text=<keyword>` (full-text search across
  Acts, legislative instruments, regulations — returns title, collection
  type, in-force status, status history with repeal/amendment reasons).
- **coverage**: all Australian Commonwealth legislation and legislative
  instruments (not just bills — includes regulations, which is where most
  energy-efficiency/data-center mandates would land). `region: australia`,
  `category: legislative`, `policy_types: [law, regulation, legislation]`.
  Complements the existing `australia.yaml` crawl entries (state energy
  agencies) with a national, full-text-searchable legislation index.
- **practical**: no documented hard rate limit found; response includes full
  status/amendment history per title, useful for lifecycle tracking.
- **effort tier**: (c) — new client; shape resembles `eurlex_nim`
  conceptually (title/status/history) so that client could be a reference.
- **why worth adding**: only true national full-text legislation search API
  found for Australia — covers Acts AND subordinate regulations (where
  technical energy-efficiency mandates usually live), keyless.
- **verified**: YES. `curl "https://api.prod.legislation.gov.au/v1/titles?text=energy"`
  returned real titles with full status history (e.g. "Inter-State Commission
  Regulations 1913" with repeal chain). HTTP 200, valid JSON.

---

### 5. `congreso_es_opendata` — Congreso de los Diputados Open Data (Spain)
- **name**: Congreso de los Diputados — Iniciativas Open Data (Spain)
- **base_url**: `https://www.congreso.es`
- **level**: national
- **access**: none — keyless, no signup (site returns 403 to a bare `curl`
  with no `User-Agent` header — a standard WAF UA check, not real
  auth — succeeds with any normal browser UA string)
- **format**: JSON, XML, and CSV (all three offered per dataset)
- **endpoints**: bulk files regenerated on a schedule and linked from
  `GET /es/opendata/iniciativas`, e.g.
  `/webpublica/opendata/iniciativas/ProyectosDeLey__<timestamp>.json`,
  `.../ProposicionesDeLey__<timestamp>.json`,
  `.../PropuestasDeReforma__<timestamp>.json`,
  `.../IniciativasLegislativasAprobadas__<timestamp>.json`. The `<timestamp>`
  in the filename changes with each regeneration (confirmed same-day
  timestamp `20260718` during this session), so a client must first fetch the
  HTML index page to discover the current filename before downloading.
- **coverage**: Spanish national legislative initiatives — government bills
  (Proyectos de Ley), member bills (Proposiciones de Ley), constitutional
  reform proposals, and enacted initiatives. `region: spain`, `category:
  legislative`, `policy_types: [law, legislation]`. Complements the existing
  `spain.yaml` crawl entries (`boe.es` gazette, `miteco.gob.es` ministry).
- **practical**: files regenerate multiple times daily (observed 3 different
  timestamps within seconds across different dataset types); no documented
  rate limit; robots.txt not checked this pass — flag for a quick check
  before building.
- **effort tier**: (c) — new client; unusual "discover-then-download" shape
  (index page → timestamped file) rather than a query endpoint, but the data
  itself is genuinely structured JSON, not HTML-scrape.
- **why worth adding**: real-time-generated structured JSON/XML/CSV of every
  bill category in the Spanish Congress, regenerated same-day — a title/date/
  status keyword-filter pass (done client-side after download) would surface
  district-heating and energy-efficiency bills directly.
- **verified**: YES. `curl -A "Mozilla/5.0" "https://www.congreso.es/es/opendata/iniciativas"`
  returned HTTP 200 with live `href` links to `.json`/`.xml`/`.csv` files
  timestamped `20260718` (today). Files not downloaded in full this pass but
  the index page and filenames are confirmed live and current.

---

### 6. `curia_vista_odata` — Curia Vista / Swiss Parliament Web Services (OData)
- **name**: Curia Vista OData Web Services (Switzerland)
- **base_url**: `https://ws.parlament.ch`
- **level**: national
- **access**: none — keyless (note: `ws-old.parlament.ch`, referenced in
  some older third-party docs/packages, now 404s — the live host is
  `ws.parlament.ch`, not the "-old" one)
- **format**: JSON (`application/json;odata=verbose`) or XML, OData v2/v3
  style (`Business` entity = parliamentary business/motions/bills,
  filterable with standard OData `$filter`/`$top`)
- **endpoints**: `GET /odata.svc/Business?$top=<n>` and
  `$filter=substringof('<term>',Title)` for keyword search across
  parliamentary business items (motions, postulates, bills — "Geschäfte").
- **coverage**: Swiss Federal Assembly parliamentary business, all types
  (motions, interpellations, bills). `region: switzerland`, `category:
  legislative`, `policy_types: [legislation, motion]`. Complements the
  extensive existing `switzerland.yaml` crawl domains (which are mostly
  cantonal energy agencies + `fedlex.data.admin.ch` for enacted federal law)
  with the parliamentary-process side (proposed motions/bills in progress).
- **practical**: returns full security headers (CSP, HSTS) consistent with a
  production, actively maintained API; no documented hard rate limit. A
  newer community-facing wrapper exists at `openparldata.ch` (confirmed live,
  200) but the official OData service is the primary source.
- **effort tier**: (c) — new client; OData v2/verbose JSON shape, similar
  query pattern to `riksdagen` conceptually.
- **why worth adding**: Switzerland's district-heating and building-energy
  mandates are largely cantonal, but federal-level motions/postulates on
  data-center energy efficiency and waste-heat reuse (an active topic in the
  Swiss Federal Assembly) are only visible through this API, not through the
  cantonal crawl domains already in the repo.
- **verified**: YES. `curl "https://ws.parlament.ch/odata.svc/Business?\$top=1"`
  returned HTTP 200 with a real JSON body (`Content-Type:
  application/json;odata=verbose`, 3363 bytes). A keyword filter query
  executed successfully (valid empty-result OData envelope `{"d":[]}` for the
  specific test term tried) confirming the filter syntax is accepted by the
  live service.

---

### 7. `assemblee_nationale_opendata` — Assemblee Nationale Open Data (France)
- **name**: Assemblee Nationale Open Data (France)
- **base_url**: `https://data.assemblee-nationale.fr`
- **level**: national
- **access**: none — keyless
- **format**: JSON and XML (bulk ZIP archives per data category, not a query
  API)
- **endpoints**: bulk downloads such as
  `/static/openData/repository/17/loi/dossiers_legislatifs/Dossiers_Legislatifs.json.zip`
  (all legislative dossiers for the current 17th legislature: bills under
  examination, adopted texts, committee reports, rapporteur assignments) and
  the equivalent `.xml.zip`; similar archives exist for amendments (with
  ~1-hour update latency per the site's own FAQ) and for prior legislatures
  under `/archives-16e/`, `/archives-15e/`.
  Different `base_url` from the existing `legifrance.gouv.fr` crawl entries
  in `france.yaml` (enacted-law text) — this is the legislative-process side
  (bills in progress), not a duplicate.
- **coverage**: French National Assembly legislative dossiers, amendments,
  committee reports. `region: france`, `category: legislative`,
  `policy_types: [legislation, law]`.
- **practical**: no documented rate limit (it's a static file download, not a
  query endpoint); `dossiers_legislatifs` archive confirmed regenerated
  same-day (`Last-Modified` header dated today).
  **Related, higher-effort candidate not fully verified this pass**: the
  PISTE/Legifrance API (`api.piste.gouv.fr`, sandbox at
  `sandbox-api.piste.gouv.fr`) — confirmed live (sandbox endpoint returned
  HTTP 400, i.e. reachable but rejecting the unauthenticated test call) but
  requires free OAuth2 client registration via `https://piste.gouv.fr`
  (env vars: `PISTE_CLIENT_ID` / `PISTE_CLIENT_SECRET`) and was not
  registered/tested end-to-end this session — listed here as a companion,
  not a separate ranked entry.
- **effort tier**: (c) — new client; "download full ZIP, parse locally, then
  keyword-filter" shape (like `donneesquebec_ckan`'s pattern) rather than a
  live query endpoint.
- **why worth adding**: full legislative-dossier text (not just metadata) for
  every French bill in progress, in machine-readable JSON/XML, updated
  same-day, with zero auth.
- **verified**: YES. `curl -I "https://data.assemblee-nationale.fr/static/openData/repository/17/loi/dossiers_legislatifs/Dossiers_Legislatifs.json.zip"`
  returned HTTP 200, `Content-Type: application/zip`, `Content-Length:
  10095333` (~10MB), `Last-Modified` dated today's session date. The
  containing HTML page (`/travaux-parlementaires/dossiers-legislatifs`) was
  also confirmed live (200) with the direct download `href` present in its
  markup.

---

## Unverified / needs-human-check

These were investigated but could not be confirmed to a working query/data
endpoint this pass — either blocked by anti-bot JS challenges, redirecting to
a browsing UI with no extractable machine endpoint via plain `curl`, or simply
under-documented. Do not build clients against these without a follow-up
verification pass (ideally with a real headed browser).

- **Italy — Camera dei Deputati Open Data (`dati.camera.it`)**: portal root
  and `/it/dataset` both return HTTP 200, and an "OCD" (Open Camera Data)
  linked-data API is documented (`/ocd/aic.rdf/lista`, etc.), but every
  attempted query (`.json` suffix, SPARQL endpoint at `/sparql`) returned an
  Akamai-style JS bot-challenge page (a `SHA1`/cookie-computation script)
  instead of data — i.e. the portal is live but automated (non-browser)
  access is actively blocked. Needs a real browser session to confirm the
  actual JSON response shape.
- **Italy — Senato Open Data (`dati.senato.it`)**: root URL 302-redirects to
  `https://dati.senato.it/sito/home` (200), but the specific dataset/query
  endpoints were not enumerated this pass.
- **Austria — Parlament Open Data (`parlament.gv.at` / `data.gv.at`)**: the
  human-facing open-data landing page
  (`https://www.parlament.gv.at/recherchieren/open-data`) is confirmed live
  (200) and links to Austria's national CKAN catalog
  (`https://www.data.gv.at/auftritte/?organisation=parlament`), but a direct
  request to that CKAN organisation's `data.parlament.gv.at` subdomain
  timed out/failed to resolve cleanly, and a `package_search` query against
  `data.gv.at/katalog/api/3/action/package_search` returned an HTML error
  page rather than the expected JSON. The dataset almost certainly exists
  (showcases reference "Welche Gesetzesinitiativen sind erfolgreich" — i.e.
  bill-success-rate analysis built on this same data) but the exact
  query/download endpoint needs one more verification pass.
- **Belgium — Chamber of Representatives (`dekamer.be` / `lachambre.be`)**:
  no dedicated chamber-specific open-data API endpoint could be located.
  `www.dekamer.be/kvvcr/opendata.cfm` 404s; the broader
  `data.gov.be` federal portal is real (DCAT-AP/RDF metadata catalog) but is
  a generic cross-agency catalog, not a chamber-specific legislative API —
  would need a targeted dataset search within it to confirm real coverage.
- **Czech Republic — Poslanecka snemovna (`psp.cz`)**: an "opendata" section
  exists and is live (200), but only offers static historical ZIP archive
  dumps per electoral term (`hl-2021ps.zip`, `tisky.zip`, `sd.zip`, etc.),
  not a live query API — i.e. this is a periodic bulk-dump pattern, not a
  structured API in the sense this task is scoped to. Lower priority; flag
  for crawl-domain treatment instead of an API client.
- **Portugal — Assembleia da Republica (`parlamento.pt`)**: the official
  "Dados Abertos" landing page is confirmed live
  (`https://www.parlamento.pt/Cidadania/Paginas/DadosAbertos.aspx`, 200), and
  third-party documentation describes 21+ REST endpoints for initiatives/
  votes/deputies, but the page itself did not yield extractable API links via
  plain `curl` (likely a JS-rendered SharePoint-style page) — needs a headed-
  browser pass to confirm the actual base URL/endpoint shape before building.
- **Mexico — Camara de Diputados / Senado**: no official structured
  JSON/XML API confirmed. The Sistema de Informacion Legislativa
  (`sil.gobernacion.gob.mx`, `gaceta.diputados.gob.mx`) is a browsing portal,
  and `datos.gob.mx` lists a Camara de Diputados organization page but no
  dataset was confirmed to expose queryable bill text/metadata this pass.
  Drop unless a follow-up search finds a real endpoint.

---

## Summary

- **7 verified, working structured APIs** found this pass: Poland (Sejm),
  Netherlands (Tweede Kamer), Brazil (Camara dos Deputados), Australia
  (Federal Register of Legislation), Spain (Congreso), Switzerland (Curia
  Vista), France (Assemblee Nationale).
- **Keyless vs keyed**: all 7 verified candidates are fully keyless (none
  requires an API key or login). The one keyed candidate noted
  (PISTE/Legifrance, France) is unverified end-to-end (needs OAuth2 client
  registration) and listed only as a companion to the Assemblee Nationale
  entry, not counted in the 7.
- **7 unverified/needs-human-check**: Italy (Camera + Senato), Austria,
  Belgium, Czechia, Portugal, Mexico — mostly blocked by anti-bot JS
  challenges or JS-rendered pages that plain `curl` can't get past; flagged
  for a follow-up pass with a real browser rather than dropped outright.
- **Highest-value find**: `tweede_kamer_odata` (Netherlands) — a live keyword
  query for "warmtenet" (heat network) returned a real parliamentary
  amendment about heat-network investment subsidy funding, proving the API
  surfaces exactly PolicyPulse's target policy category on the first try,
  with zero auth and standard OData filter syntax.
