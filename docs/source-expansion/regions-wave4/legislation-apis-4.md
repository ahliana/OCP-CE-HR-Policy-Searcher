# Structured Legislation / Gazette APIs — Wave 4 (retry + new-country pass)

Retry pass over sources flagged unverified in prior waves, plus new-country
gazette/legislation API targets requested this wave (Austria, Portugal,
Italy, Belgium, Mexico, Argentina, India, Indonesia, Malaysia, plus
national gazette APIs worldwide). Dedup confirmed against BRIEF.md's
already-built client list, `draft/new-clients.md` (wave 1, 16 candidates),
`draft/new-clients-wave2.md` (wave 2, 17 candidates), and
`draft/new-clients-wave3.md` (wave 3, 8 candidates) — no `source_type` or
`base_url` overlaps with any of the 41 prior tier-c candidates or the 9
shipped clients.

**7 net-new verified APIs this wave** (all keyless except India). Each
needs a NEW `source_type` client under `src/sources/` per the brief, except
the two Argentina CKAN instances, which can route through the generic
`ckan_action_api` client already specced in wave 2 (just two more
parameterized instances — no new client code beyond what wave 2 already
called for).

---

## Verified candidates (ranked best-first)

### 1. `italy_senato_sparql` — Senato della Repubblica Linked Open Data SPARQL endpoint (Italy)

- **Level**: national
- **Base URL**: `https://dati.senato.it` (SPARQL endpoint at
  `https://dati.senato.it/sparql`, redirects through CloudFront but resolves
  cleanly)
- **Access**: none — fully keyless, no signup, no headers. CC-BY 3.0 IT
  license.
- **Format**: JSON (`application/sparql-results+json` via `Accept` header
  or content negotiation), also XML/CSV/Turtle
- **Query endpoint**: `GET https://dati.senato.it/sparql?query=<url-encoded
  SPARQL>` — full SPARQL 1.1 over a Virtuoso triple store covering bills
  (`ddl` = disegni di legge), senators, commissions, votes, legislative
  process metadata back to unification-era archives.
- **Coverage**: Italian Senate bills/legislative process — maps to
  `category: legislative`, `tags: [mandates]`, `policy_types: [law,
  legislation]`, `region: [italy, eu, eu_south]`, `language: it`
- **Practical**: no documented rate limit; standard SPARQL courtesy
  throttling recommended. Docs discoverable from `dati.senato.it/sito/23`
  (the "Interroga i dati" / query-the-data page), which links directly to
  the SPARQL endpoint. Companion bulk CSV/JSON/XML downloads described at
  `dati.senato.it/sito/scarica_i_dati` but no concrete per-file download
  URL was resolved this session (JS/session-driven, not a static link) —
  the SPARQL endpoint is the reliable path.
- **Effort tier**: (c) — needs a new SPARQL-query client (would also serve
  as a reference implementation if other SPARQL sources are added later).
- **Why worth adding**: Italy — a top-5 EU economy and a country with
  significant data-center buildout — has ZERO structured legislative API
  in the repo today (only static crawl domains). This closes that gap with
  a real, keyless, on-topic-confirmed source.
- **Verified**: YES. `curl -A "Mozilla/5.0" -H "Accept: application/
  sparql-results+json" -L "https://dati.senato.it/sparql?query=PREFIX+bif:+
  <bif:>+SELECT+?s+?label+WHERE+{?s+?p+?label+.+?label+bif:contains+
  \"energia\"+.}+LIMIT+5"` returned real bindings including
  `http://dati.senato.it/ddl/34715` labeled "Norme per il risparmio
  energetico e lo sviluppo dell'impiego di energia da fonti rinnovabili
  negli edifici pubblici" (Rules for energy savings and renewable-energy
  use in public buildings) — a direct, on-topic hit, first try.
- **Companion NOT verified this pass**: Camera dei Deputati (`dati.camera.it`)
  — see Unverified section. Every endpoint tested there (SPARQL, OCD
  linked-data, plain HTML) returned an F5/TSPD bot-challenge page (a
  client-side SHA1 JS cookie computation), not real data, despite the
  service being genuinely live per public documentation. Do not build a
  Camera client from this session's evidence alone.

---

### 2. `austria_parlament_filter_api` — Austrian Parliament Filter API

- **Level**: national
- **Base URL**: `https://www.parlament.gv.at`
- **Access**: none — fully keyless, no signup, no headers
- **Format**: JSON
- **Query endpoint**: `GET /Filter/api/filter/data/{listId}?js=eval&
  showAll=true&export=true` — a generic filtered-list API behind every
  search UI on the site; `listId=101` returned the full parliamentary
  document index (bills, government responses, petitions, etc.) with a
  self-describing `header` field naming every filterable column
  (`GP_CODE`, `ITYP`, `INR`, etc.). Other `listId` values cover different
  document categories (not individually enumerated this session — the
  numeric IDs are visible in each search page's own network calls).
- **Coverage**: Austrian federal legislative process — bills, government
  bill responses, committee reports. Maps to `category: legislative`,
  `tags: [mandates]`, `policy_types: [law, legislation]`, `region:
  [austria, eu, eu_central]`, `language: de`
- **Practical**: no documented rate limit found this pass. `pages`/`count`
  fields in the response support pagination (100,231 total records
  observed for `listId=101` — the site's full historical document index).
  No separate developer docs page found; the API is discovered by
  inspecting the site's own search-page network calls (`js=eval&
  showAll=true&export=true` is the "give me raw JSON" incantation used by
  the site's own frontend).
- **Effort tier**: (c) — needs a new client; the generic `listId`-based
  shape could genericize to one client parameterized by list ID once the
  full set of useful list IDs is enumerated (a follow-up task).
- **Why worth adding**: Austria was explicitly flagged unverified in an
  earlier wave — now confirmed live with a real, large, keyless dataset.
  Complements the existing Austria HTML crawl domains with a structured,
  filterable index of the full legislative document corpus.
- **Verified**: YES. `curl "https://www.parlament.gv.at/Filter/api/filter/
  data/101?js=eval&showAll=true&export=true"` returned HTTP 200 with real
  JSON: `{"pages":2,"lastSync":"2026-07-18 16:56:48.0","count":100231,
  "header":[...]}` — a genuine, current, machine-readable response.
- **Companion NOT verified this pass**: `data.gv.at` (Austria's national
  CKAN-style open-data portal) — see Unverified section. The classic CKAN
  Action API path 404'd; the portal appears to have migrated off CKAN to a
  JS-rendered SPA with no API path discovered via static fetch this
  session.

---

### 3. `datos_gob_ar` (Argentina national CKAN) — Datos Argentina, incl. InfoLEG

- **Level**: national
- **Base URL**: `https://datos.gob.ar`
- **Access**: none — keyless CKAN Action API
- **Format**: JSON
- **Query endpoint**: `GET /api/3/action/package_search?q=<term>&rows=<n>`
  — standard CKAN, confirmed live. The specific InfoLEG dataset
  (`justicia-base-infoleg-normativa-nacional` — Argentina's national
  legislative/regulatory database, laws/decrees/resolutions since 1997) is
  directly fetchable via `GET /api/3/action/package_show?
  id=justicia-base-infoleg-normativa-nacional`.
- **Coverage**: cross-ministry Argentine open data, including the InfoLEG
  normativa-nacional dataset specifically requested this wave. Maps to
  `category: legislation`, `tags: [mandates, reporting]`, `policy_types:
  [law, regulation, report]`, `region: [south_america]` (no dedicated
  `argentina` key in `VALID_REGIONS` — use the broad `south_america`
  group, same pattern the existing config uses for Chile), `language: es`
- **Practical**: no documented hard rate limit; standard CKAN courtesy
  throttling. `metadata_modified` on the InfoLEG package showed
  `2026-07-18` (today) — actively maintained, not a stale mirror.
- **Effort tier**: (a)/(c) hybrid — routes through the generic
  `ckan_action_api` client already specced in `new-clients-wave2.md`
  (Italy/Ireland/Canada/Mexico/UK instances); this is simply a sixth
  instance, no new client code required once that client exists.
- **Why worth adding**: this IS the InfoLEG API the brief asked to
  retry/find — not a standalone InfoLEG-hosted API (InfoLEG itself,
  `infoleg.gob.ar`, has no public API of its own), but the same dataset
  served through Argentina's national open-data CKAN portal, confirmed
  live and current.
- **Verified**: YES. `curl "https://datos.gob.ar/api/3/action/
  package_search?q=energia&rows=3"` returned HTTP 200, `"count": 139`, real
  results. `curl "https://datos.gob.ar/api/3/action/package_show?
  id=justicia-base-infoleg-normativa-nacional"` returned HTTP 200 with a
  real package record maintained by "Ministerio de Justicia. Secretaría de
  Justicia. Dirección Nacional del Sistema Argentino de Información
  Jurídica" (SAIJ), `metadata_modified` dated today.

---

### 4. `datos_hcdn_gob_ar` (Argentina Chamber of Deputies CKAN) — Cámara de Diputados Open Data

- **Level**: national
- **Base URL**: `https://datos.hcdn.gob.ar`
- **Access**: none — keyless CKAN Action API
- **Format**: JSON
- **Query endpoint**: `GET /api/3/action/package_search?q=<term>&rows=<n>`
  — same CKAN shape as #3 above but a distinct instance/portal run
  directly by the lower house (HCDN = Honorable Cámara de Diputados de la
  Nación).
- **Coverage**: Argentine Chamber of Deputies datasets — confirmed hits
  include "Leyes" (Laws) and "Leyes Sancionadas" (Sanctioned/Enacted Laws)
  datasets. Maps to `category: legislative`, `tags: [mandates]`,
  `policy_types: [law, legislation]`, `region: [south_america]`,
  `language: es`
- **Practical**: no documented rate limit; the search term matters —
  `q=energia` returned 0 results, `q=ley` returned 6 real dataset hits
  including the two named above.
- **Effort tier**: (a)/(c) hybrid — same generic `ckan_action_api` client
  as #3, a seventh instance.
- **Why worth adding**: distinct from #3 — this is the legislative-branch's
  own portal (bill text, sanctioned-law datasets) rather than the
  executive-branch national catalog; together they cover both the
  legislative-process side and the cross-ministry regulatory side for
  Argentina.
- **Verified**: YES. `curl "https://datos.hcdn.gob.ar/api/3/action/
  package_search?q=ley&rows=3"` returned HTTP 200, `"count": 6`, with real
  dataset titles "Leyes" and "Leyes Sancionadas".

---

### 5. `dados_gov_pt` — dados.gov.pt (Portugal national open-data portal, udata)

- **Level**: national
- **Base URL**: `https://dados.gov.pt`
- **Access**: none — keyless
- **Format**: JSON. **Not CKAN** — runs on **udata** (the same Etalab
  platform as France's `data.gouv.fr`, already specced as
  `data_gouv_fr_api` in wave 2) — a genuinely different API shape from the
  CKAN family.
- **Query endpoint**: `GET /api/1/datasets/?q=<query>` — confirmed live,
  returns `{"data": [...], "page", "page_size", "total"}`.
- **Coverage**: cross-ministry Portuguese open data, including municipal
  climate-action plans and datasets that explicitly reference Diário da
  República (the official gazette) publication numbers. Maps to
  `category: district_heating`/`environmental_agency` depending on hit,
  `tags: [reporting, efficiency]`, `policy_types: [report]`, `region:
  [portugal, eu, eu_south]`, `language: pt`
- **Practical**: no documented hard rate limit found this pass.
- **Effort tier**: (c) — needs the same udata-shaped client already called
  for by `data_gouv_fr_api` in wave 2; recommend building ONE generic
  `udata_api` client parameterized by base_url (France + Portugal, and any
  future udata-platform country) rather than two bespoke clients — same
  consolidation logic wave 2 applied to the CKAN family.
- **Why worth adding**: fills the Portugal gap this wave specifically
  asked to retry. Distinct base_url from the existing `portugal.yaml`
  crawl entries (which target `parlamento.pt` and ministry sites directly)
  — this is the cross-government open-data catalog, useful as a discovery
  layer the same way `data_gouv_fr_api` was rated in wave 2.
- **Verified**: YES. `curl "https://dados.gov.pt/api/1/datasets/?q=diario+
  da+republica"` returned HTTP 200, `"total": 108`, with real hits
  including gazette-referencing municipal planning datasets. A narrower
  `q=eficiencia+energetica` returned only 2 hits and `q=rede+de+calor`
  (district heating) returned 0 — broader Portuguese energy/climate terms
  work better than literal English-taxonomy translations.
- **NOT independently verified this pass**: a direct `parlamento.pt`
  "Iniciativas" JSON API (community project `parlamentodb` wraps it) and
  `DRE.pt` (Diário da República) itself — no public webservice/API was
  confirmed for either; see Unverified section.

---

### 6. `mx_sidof_gazette_api` — SIDOF (Sistema de Información del Diario Oficial de la Federación, Mexico)

- **Level**: national — **the official federal gazette itself**, distinct
  from the DOF dataset mirror on datos.gob.mx (item below)
- **Base URL**: `https://sidof.segob.gob.mx`
- **Access**: none — keyless, no signup
- **Format**: JSON
- **Query endpoint**: `GET /datos_abiertos/getJSON/{id}` — confirmed live;
  `id=65` returned a real `ListaDiarios` array of gazette editions with
  `codDiario`, `codEdicion` (e.g. "VES" = vespertina/evening edition),
  and `fecha` fields. The `datos_abiertos` landing page
  (`sidof.segob.gob.mx/datos_abiertos`) links several such `getJSON/{id}`
  endpoints (ids 43, 57, 61, 65 observed) — each apparently a different
  slice/dataset of the gazette index; exact per-id schema needs enumerating
  before a client is built.
- **Coverage**: Mexico's Official Gazette (DOF) — the government's
  publication-of-record for laws, decrees, regulations, NOMs (official
  Mexican standards, where data-center energy-efficiency mandates would
  live). Maps to `category: regulatory`, `tags: [mandates, reporting]`,
  `policy_types: [law, regulation]`, `region: [mexico, north_america]`,
  `language: es`
- **Practical**: no documented rate limit found. The `apiStatus` page at
  `/apiStatus` is an HTML "publication alert" page, not itself a JSON
  endpoint — don't confuse it with the real `getJSON/{id}` data endpoints.
- **Effort tier**: (c) — needs a new client; multi-id discovery step
  required before the client can enumerate every available dataset slice.
- **Why worth adding**: this is the actual Mexican federal gazette
  (equivalent to the US Federal Register, already a wave-3 client) — a
  genuinely different, higher-value find than the generic DOF *summary*
  dataset already reachable via the Mexico CKAN instance from wave 2.
- **Verified**: YES. `curl "https://sidof.segob.gob.mx/datos_abiertos/
  getJSON/65"` returned HTTP 200 with real JSON:
  `{"messageCode": 200, "response": "OK", "ListaDiarios": [{"codDiario":
  254661, "codEdicion": "VES", "fecha": "31-10-2013", ...}, ...]}`.
- **Related, already covered**: `datos.gob.mx`'s
  `resumen_diario_oficial_federacion_dof` dataset (maintained by SENASICA)
  is a DOF summary mirror reachable through the wave-2
  `ckan_action_api` (Mexico instance, `www.datos.gob.mx`) already specced
  — confirmed live this pass (`package_show` returned a real record,
  license CC-BY-4.0) but this is a dataset *within* an already-proposed
  source, not a new client.
- **NOT verified this pass**: a clean API for the Mexican Chamber of
  Deputies (SIL — Sistema de Información Legislativa,
  `sil.gobernacion.gob.mx`) — the system is real and browsable but no
  documented REST/JSON API endpoint was found or confirmed; see
  Unverified section.

---

### 7. `za_open_gazettes_archive` — Open Gazettes South Africa (OpenUp / SAFLII)

- **Level**: national (covers national AND all 9 provincial gazette series)
- **Base URL**: `https://archive.opengazettes.org.za` (companion search UI
  at `https://opengazettes.org.za`)
- **Access**: none — keyless, no signup. Nonprofit project (OpenUp +
  SAFLII + African Network of Centers for Investigative Reporting,
  originally Indigo Trust/Code4SA funded).
- **Format**: JSON Lines (`.jsonlines`) bulk index + linked PDF gazette
  documents
- **Query endpoint**: `GET /index/gazette-index-latest.jsonlines` — a
  bulk, newline-delimited-JSON index of every gazette in the archive
  (~40,000 gazettes, national + all 9 provinces, 1958-present per project
  docs), each record with `publication_title`, `jurisdiction_name`,
  `issue_number`, `volume_number`, `archive_url` (direct PDF link),
  `issue_title`, `pagecount`. This is a bulk-download shape (like the
  already-specced `assemblee_nationale_opendata` from wave 2), NOT a
  live keyword-search query endpoint — the companion human search UI at
  `search.opengazettes.org.za` appears to be a JS-rendered SPA that
  redirected to the plain homepage on every automated query attempt this
  session (no working query-string API discovered for it).
- **Coverage**: South African national and provincial government gazettes
  — the actual gazette full-text/PDF-link layer this wave specifically
  asked to retry/find. Maps to `category: regulatory`, `tags: [reporting,
  mandates]`, `policy_types: [law, regulation, report]`, `region:
  [south_africa, africa]`, `language: en`
- **Practical**: no documented rate limit on the bulk index; it is a large
  file (not measured this session, but described as covering ~40,000
  gazette records) — a client should download once and diff/re-poll
  periodically rather than re-fetching per query.
- **Effort tier**: (c) — needs a new client (bulk-index-then-filter shape,
  similar in spirit to the `assemblee_nationale_opendata` bulk-ZIP client
  from wave 2, but JSON Lines instead of a ZIP archive).
- **Why worth adding**: a genuine national+provincial GAZETTE archive (not
  just a legislature bill-tracker) — exactly the "official journal, full
  text or metadata + doc URL" shape the brief called out by name (citing
  South Africa alongside Kenya/Singapore/Ireland). Complements the
  existing `south_africa.yaml` crawl domains (ministry/regulator sites)
  with the actual promulgation-of-record layer.
- **Verified**: YES. `curl "https://archive.opengazettes.org.za/index/
  gazette-index-latest.jsonlines"` returned HTTP 200 with a real first
  record: `{"publication_title": "Provincial Gazette", "archive_url":
  "https://archive.opengazettes.org.za/archive/ZA-NW/2015/
  provincial-gazette-ZA-NW-vol-258-no-7533-dated-2015-09-08.pdf",
  "jurisdiction_name": "North West", "issue_number": 7533, ...}`.
- **NOT re-proposed**: Kenya Gazette — already covered by the wave-3
  `kenya_law_api` client (`new.kenyalaw.org`'s `doc_type` filter includes
  gazette notices alongside legislation), not re-specced here.

---

### 8. `in_data_gov_ogd_api` — Open Government Data (OGD) Platform India

- **Level**: national
- **Base URL**: `https://api.data.gov.in` (portal at `https://www.data.gov.in`)
- **Access**: **api_key** — free self-serve registration at
  `https://www.data.gov.in/user/register` (confirmed the registration path
  resolves, HTTP 302 redirect into the standard signup flow). Env var:
  `DATA_GOV_IN_API_KEY`. Key passed as `?api-key=` query param.
- **Format**: JSON (also XML/CSV per resource)
- **Query endpoint**: `GET /resource/{resource_id}?api-key=<key>&
  format=json&limit=<n>` — the widely-circulated public "DEMO" key from
  online tutorials (`579b464db66ec23bdd000001...`) does NOT work broadly;
  it returned a real, well-formed `{"error": "Key not authorised"}` JSON
  response — this proves the gateway itself is live and enforcing
  per-registration auth, but a personal key is required for real use, not
  a shared demo key as some tutorials imply.
- **Coverage**: India's national open-data catalog — thousands of
  datasets across ministries; would need a follow-up pass, once a real key
  is issued, to identify which specific resource IDs cover energy
  efficiency / data-center policy / Bureau of Energy Efficiency programs.
  Maps to `category: regulatory`, `tags: [reporting, efficiency]`,
  `policy_types: [report]`, `region: [india, apac]`, `language: en`
- **Practical**: rate limits not confirmed (require a real key to test);
  standard courtesy throttling recommended.
- **Effort tier**: (c) — needs a new client; self-disables until
  `DATA_GOV_IN_API_KEY` is set, same pattern as `legiscan`/`govinfo`/
  `congress_gov_api`.
- **Why worth adding**: confirms India's national open-data gateway is
  real and live (the specific ask was "India Code API / eGazette /
  Sansad") — this is the closest verified structured entry point found
  this pass, though it is a general-purpose data catalog, not a
  legislation-specific API.
- **Verified**: PARTIALLY. The gateway itself is confirmed live (real
  auth-gate JSON response, not a network failure or generic 404 page).
  **NOT verified**: no working query against a real dataset was completed
  (blocked on needing a registered personal key); no specific
  energy/data-center-relevant resource ID was identified. Treat as HOLD
  until a real key is issued and a relevant resource is found.
- **NOT found this pass**: a dedicated India Code API (indiacode.nic.in —
  reachable, HTTP 200, but no API reference found in page content) or a
  working eGazette API (`egazette.gov.in` — connection timed out
  repeatedly this session, could not confirm live or dead) or a public
  PRS Legislative Research API (PRS is a respected bill-tracking nonprofit
  but publishes no documented API — data is scraped from parliament/gazette
  sources, not offered as a service). All three flagged in Unverified
  below rather than specced as clients.

---

## Unverified / needs-human-check

Per the brief's instruction: these were checked this session and could
NOT be confirmed live/queryable with real evidence. Do not build clients
against them without a follow-up verification pass (ideally from a
different network / with a real browser for the bot-protected ones).

- **Austria — data.gv.at**: the classic CKAN Action API path
  (`/api/3/action/package_search`) returned HTTP 404 at every base_url
  variant tried (`www.data.gv.at/katalog/api/...`,
  `www.data.gv.at/api/...`, `data.gv.at/api/...`). The portal now appears
  to be a JS-rendered SPA (page fetched with an empty `<title>`, no static
  API links discoverable). It may have migrated off CKAN entirely since
  older documentation was written — needs a real-browser or
  network-inspector pass to find the current API, if any survives.
- **Belgium — data.gov.be**: every request (including the classic CKAN
  path) returned an F5/TSPD bot-challenge page (`bobcmn` JS cookie
  challenge), not real content — same protection pattern seen on Italy's
  Camera dei Deputati site. Cannot confirm the documented CKAN API is
  actually reachable by a scripted client without a headless-browser
  approach.
- **Belgium — dekamer.be (Chamber open data)**: `/kvvcr/opendata/`
  returned HTTP 200 but only 244 bytes of content (likely a
  redirect/placeholder shell) — inconclusive, no dataset or API link
  extracted.
- **Belgium — Senate (senate.be)**: no dedicated open-data/API reference
  found in search results at all; not fetched this pass.
- **Italy — Camera dei Deputati (dati.camera.it)**: portal is
  well-documented in public sources (SPARQL endpoint, "OCD" linked-data
  vocabulary, daily-updated), but every endpoint tried this session
  (SPARQL query, OCD linked-data content-negotiation, plain search page)
  returned the same F5/TSPD SHA1-JS-challenge page. Genuinely live per
  public documentation, but NOT independently confirmed this session —
  do not build a client from this pass's evidence.
- **Mexico — Cámara de Diputados / Senado (SIL, sil.gobernacion.gob.mx)**:
  real, browsable legislative-information system, but no documented
  REST/JSON API endpoint was found or confirmed; the system appears to be
  a traditional server-rendered web app, not an API.
- **India — eGazette (egazette.gov.in)**: connection timed out on every
  attempt this session (`HTTP 000`) — could not confirm live or dead from
  this network.
- **India — India Code (indiacode.nic.in)**: site itself is live (HTTP
  200) but no API reference found in the fetched page content.
- **India — PRS Legislative Research**: respected nonprofit bill-tracking
  site, but publishes no documented public API — it is a research/
  publishing organization, not a data-service provider.
- **Indonesia — peraturan.go.id, jdih.dpr.go.id**: both unreachable from
  this research session — `peraturan.go.id` returned a connection
  failure (`ECONNREFUSED`) via WebFetch and `HTTP 000` (no response) via
  curl; `jdih.dpr.go.id` returned HTTP 403 (Forbidden) consistently. Could
  be geo/network-level blocking rather than the sites being down — needs
  a retry from a different network or a residential-IP fetch service.
- **Malaysia — federalgazette.agc.gov.my, lom.agc.gov.my**: both
  unreachable this session (`getaddrinfo ENOTFOUND` / `HTTP 000`) — same
  caveat as Indonesia; the AGC (Attorney General's Chambers) portal is
  documented as existing in public sources but could not be independently
  reached.
- **Singapore — sso.agc.gov.sg (Singapore Statutes Online), egazette.gov.sg**:
  both returned HTTP 403 on every request this session (including the
  search endpoint) — appears to be active bot-blocking (Singapore Statutes
  Online is known to be heavily protected against scraping) rather than
  the sites being down. No API is publicly documented for either.
- **Ireland — Iris Oifigiúil (irisoifigiuil.ie)**: site is live (HTTP
  200), confirmed NOT running WordPress (`/wp-json/` 404s) or any other
  discoverable API — appears to be a static/legacy gazette site with no
  structured access beyond HTML pages. No API found.
- **Portugal — parlamento.pt Iniciativas API / DRE.pt webservices**: the
  Portuguese Parliament does publish raw JSON/XML files under its own
  "Dados Abertos" section (per its own page and a well-known community
  wrapper, `parlamentodb`, that re-exposes it as a REST API), but no
  concrete, independently-fetchable raw-file URL was resolved this
  session — needs a follow-up pass to find the actual current file paths
  (they appear to be enumerable only by browsing the site's own dados
  abertos page). DRE.pt (the gazette itself) publishes no documented
  webservice/API — access is UI-only per every source checked.

---

## Draft `api_sources.yaml` entries (all `enabled: false`)

```yaml
# =============================================================================
# DRAFT WAVE 4 ADDITIONS — tier-c structured API sources from wave-4
# source-expansion research (retry + new-country gazette/legislation pass).
# Every entry is `enabled: false`. Each NEW source_type needs a client
# under src/sources/ (registered in src/sources/__init__.py) before
# `enabled` can ever be flipped to true. The two `ckan_action_api` entries
# route through the generic client already called for in
# draft/new-clients-wave2.md — no new client code needed for those two.
# =============================================================================

domains:
  - name: "Senato della Repubblica Linked Open Data SPARQL endpoint (Italy)"
    id: "italy_senato_sparql"
    enabled: false
    source_type: "italy_senato_sparql"
    base_url: "https://dati.senato.it"
    region:
      - "italy"
      - "eu"
      - "eu_south"
    category: "legislative"
    tags:
      - "mandates"
    policy_types:
      - "law"
      - "legislation"
    notes: |
      Wave 4 tier-c candidate. Keyless SPARQL 1.1 endpoint (Virtuoso).
      Verified end-to-end: a bif:contains full-text query for "energia"
      returned a real, on-topic Senate bill on energy savings/renewables
      in public buildings (ddl/34715). Italy had zero structured
      legislative API before this. Camera dei Deputati companion
      (dati.camera.it) is bot-protected (F5/TSPD) and NOT verified -
      do not build that client from this pass's evidence.

  - name: "Austrian Parliament Filter API"
    id: "austria_parlament_filter_api"
    enabled: false
    source_type: "austria_parlament_filter_api"
    base_url: "https://www.parlament.gv.at"
    region:
      - "austria"
      - "eu"
      - "eu_central"
    category: "legislative"
    tags:
      - "mandates"
    policy_types:
      - "law"
      - "legislation"
    notes: |
      Wave 4 tier-c candidate. Keyless. Generic Filter/api/filter/data/
      {listId} shape backing every search UI on the site; listId=101
      confirmed live with 100,231 total records. Retried from an earlier
      wave's unverified flag - now confirmed. data.gv.at (Austria's CKAN
      portal) remains unverified this pass (404s on classic CKAN path,
      appears migrated to a JS SPA).

  - name: "Datos Argentina national CKAN (incl. InfoLEG normativa nacional)"
    id: "datos_gob_ar"
    enabled: false
    source_type: "ckan_action_api"
    base_url: "https://datos.gob.ar"
    region:
      - "south_america"
    category: "legislation"
    tags:
      - "mandates"
      - "reporting"
    policy_types:
      - "law"
      - "regulation"
      - "report"
    notes: |
      Wave 4 tier-c candidate. Keyless CKAN - routes through the generic
      ckan_action_api client already specced in new-clients-wave2.md
      (Italy/Ireland/Canada/Mexico/UK instances); this is a sixth
      instance, no new client code needed. Hosts the InfoLEG
      normativa-nacional dataset (laws/decrees/resolutions since 1997) -
      this IS the InfoLEG API retry ask; InfoLEG itself has no standalone
      API. Verified: package_show on
      justicia-base-infoleg-normativa-nacional returned a real,
      actively-maintained record (metadata_modified = today).

  - name: "Camara de Diputados de la Nacion Open Data (Argentina, HCDN)"
    id: "datos_hcdn_gob_ar"
    enabled: false
    source_type: "ckan_action_api"
    base_url: "https://datos.hcdn.gob.ar"
    region:
      - "south_america"
    category: "legislative"
    tags:
      - "mandates"
    policy_types:
      - "law"
      - "legislation"
    notes: |
      Wave 4 tier-c candidate. Keyless CKAN - seventh instance of the
      shared ckan_action_api client. Distinct from datos_gob_ar above -
      this is the legislative branch's own portal (bill/enacted-law
      datasets: "Leyes", "Leyes Sancionadas" confirmed live) vs. the
      cross-ministry executive-branch catalog. Note: q=energia returned
      0 results, q=ley returned 6 real hits - query-term sensitive.

  - name: "dados.gov.pt (Portugal national open-data portal, udata)"
    id: "dados_gov_pt"
    enabled: false
    source_type: "udata_api"
    base_url: "https://dados.gov.pt"
    region:
      - "portugal"
      - "eu"
      - "eu_south"
    category: "district_heating"
    tags:
      - "reporting"
      - "efficiency"
    policy_types:
      - "report"
    notes: |
      Wave 4 tier-c candidate. Keyless udata API (same platform family as
      the wave-2 data_gouv_fr_api) - recommend a shared udata_api client
      parameterized by base_url rather than two bespoke clients. Verified:
      q=diario+da+republica returned 108 real hits referencing the
      official gazette. Direct parlamento.pt Iniciativas API and DRE.pt
      webservices remain unverified this pass - see the unverified
      section in legislation-apis-4.md.

  - name: "SIDOF - Sistema de Informacion del Diario Oficial de la Federacion (Mexico gazette API)"
    id: "mx_sidof_gazette_api"
    enabled: false
    source_type: "mx_sidof_gazette_api"
    base_url: "https://sidof.segob.gob.mx"
    region:
      - "mexico"
      - "north_america"
    category: "regulatory"
    tags:
      - "mandates"
      - "reporting"
    policy_types:
      - "law"
      - "regulation"
    notes: |
      Wave 4 tier-c candidate - the actual Mexican federal gazette (DOF),
      equivalent to the US Federal Register client from wave 3. Keyless
      getJSON/{id} endpoints confirmed live (id=65 returned a real
      ListaDiarios array of gazette editions). Multiple ids (43/57/61/65)
      exist per the datos_abiertos landing page - schema needs
      enumerating per id before building. Distinct and higher-value than
      the DOF summary dataset already reachable via the wave-2
      ckan_action_api Mexico instance (www.datos.gob.mx).

  - name: "Open Gazettes South Africa (OpenUp/SAFLII national + provincial gazette archive)"
    id: "za_open_gazettes_archive"
    enabled: false
    source_type: "za_open_gazettes_archive"
    base_url: "https://archive.opengazettes.org.za"
    region:
      - "south_africa"
      - "africa"
    category: "regulatory"
    tags:
      - "reporting"
      - "mandates"
    policy_types:
      - "law"
      - "regulation"
      - "report"
    notes: |
      Wave 4 tier-c candidate - genuine national + all-9-provincial
      gazette archive (~40,000 gazettes, 1958-present), keyless bulk
      JSONLINES index. Verified: gazette-index-latest.jsonlines returned
      real records with archive_url PDF links. Bulk-then-filter shape
      like the wave-2 assemblee_nationale_opendata client. The live
      keyword-search UI (search.opengazettes.org.za) redirected to the
      homepage on every automated query this pass - not confirmed as a
      working query API, use the bulk index instead. Kenya Gazette NOT
      re-proposed here - already covered by the wave-3 kenya_law_api
      client's doc_type filter.

  - name: "Open Government Data (OGD) Platform India"
    id: "in_data_gov_ogd_api"
    enabled: false
    source_type: "in_data_gov_ogd_api"
    base_url: "https://api.data.gov.in"
    region:
      - "india"
      - "apac"
    category: "regulatory"
    tags:
      - "reporting"
      - "efficiency"
    policy_types:
      - "report"
    notes: |
      Wave 4 tier-c candidate - HOLD, partially verified only. Requires
      DATA_GOV_IN_API_KEY (free self-serve signup at
      www.data.gov.in/user/register, confirmed live). The widely-shared
      public "DEMO" key from tutorials does NOT work (returned a real
      "Key not authorised" JSON error, proving the gateway is live but
      key-enforced). Needs a real registered key AND a follow-up pass to
      find a specific energy/data-center-relevant resource ID before
      building. India Code, eGazette, and PRS Legislative Research were
      all checked this pass and none has a confirmed public API - see
      unverified section.
```
