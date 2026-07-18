# New Structured Clients Needed - Wave 4 (tier-c)

Eight wave-4 tier-c candidates, all from one source file
(`docs/source-expansion/regions-wave4/legislation-apis-4.md`) - a retry pass
over sources flagged unverified in prior waves, plus new-country gazette/
legislation API targets (Italy, Austria, Portugal, Mexico, Argentina, South
Africa, India). Six need a NEW `source_type` client under `src/sources/`
(registered in `src/sources/__init__.py`) because none fit the shape of the 9
existing clients (`riksdagen`, `uk_bills`, `legisinfo`, `folketing`,
`eurlex_nim`, `legiscan`, `govinfo`, `regulations_gov`, `dip`), the 16
wave-1 tier-c clients, the 17 wave-2 tier-c clients, or the 8 wave-3 tier-c
clients. TWO (the Argentina CKAN instances) need NO new client code at all -
they route through the generic `ckan_action_api` client already specced in
`draft/new-clients-wave2.md` (Italy/Ireland/Canada/Mexico/UK instances); these
are simply a sixth and seventh instance of that same client. Dedup confirmed
against all four prior lists plus every existing `api_sources.yaml` entry -
no `source_type` or `base_url` overlaps.

No client code is included here - this is a spec for a future engineer, per
the brief. Each spec below: proposed `source_type` id, base URL, auth,
response format, endpoint(s), coverage mapping, why it matters. The draft
`api_sources.yaml` entries (all `enabled: false`) follow in one fenced block
at the end of this file.

---

## 1. `italy_senato_sparql` - Senato della Repubblica Linked Open Data SPARQL endpoint (Italy)

- **Region**: Italy (national) - highest-value find of wave 4
- **API base**: `https://dati.senato.it` (SPARQL endpoint at
  `https://dati.senato.it/sparql`)
- **Auth**: none - fully keyless, no signup, no headers. CC-BY 3.0 IT
  license.
- **Format**: JSON (`application/sparql-results+json` via `Accept` header
  or content negotiation), also XML/CSV/Turtle
- **Endpoint to call**: `GET https://dati.senato.it/sparql?query=<url-encoded
  SPARQL>` - full SPARQL 1.1 over a Virtuoso triple store covering bills
  (`ddl` = disegni di legge), senators, commissions, votes, legislative
  process metadata back to unification-era archives.
- **Coverage mapping**: `category: legislative`, `tags: [mandates]`,
  `policy_types: [law, legislation]`, `region: [italy, eu, eu_south]`,
  `language: it`
- **Practical**: no documented rate limit; standard SPARQL courtesy
  throttling recommended. Docs discoverable from `dati.senato.it/sito/23`
  ("Interroga i dati"), which links directly to the SPARQL endpoint.
  Companion bulk CSV/JSON/XML downloads described at
  `dati.senato.it/sito/scarica_i_dati` but no concrete per-file download URL
  was resolved this session (JS/session-driven) - the SPARQL endpoint is the
  reliable path.
- **Why it matters**: Italy - a top-5 EU economy and a country with
  significant data-center buildout - had ZERO structured legislative API in
  the repo before this. Verified end-to-end: a `bif:contains` full-text
  query for "energia" returned a real bindings result,
  `http://dati.senato.it/ddl/34715`, labeled "Norme per il risparmio
  energetico e lo sviluppo dell'impiego di energia da fonti rinnovabili
  negli edifici pubblici" (rules for energy savings and renewable-energy use
  in public buildings) - a direct, on-topic hit, first try.
- **Companion NOT verified this pass**: Camera dei Deputati
  (`dati.camera.it`) - every endpoint tested (SPARQL, OCD linked-data, plain
  HTML) returned an F5/TSPD bot-challenge page, not real data, despite the
  service being genuinely live per public documentation. Do not build a
  Camera client from this session's evidence alone.

---

## 2. `austria_parlament_filter_api` - Austrian Parliament Filter API

- **Region**: Austria (national)
- **API base**: `https://www.parlament.gv.at`
- **Auth**: none - fully keyless, no signup, no headers
- **Format**: JSON
- **Endpoint to call**: `GET /Filter/api/filter/data/{listId}?js=eval&
  showAll=true&export=true` - a generic filtered-list API behind every
  search UI on the site; `listId=101` returned the full parliamentary
  document index (bills, government responses, petitions, etc.) with a
  self-describing `header` field naming every filterable column
  (`GP_CODE`, `ITYP`, `INR`, etc.). Other `listId` values cover different
  document categories (not individually enumerated this session - the
  numeric IDs are visible in each search page's own network calls).
- **Coverage mapping**: `category: legislative`, `tags: [mandates]`,
  `policy_types: [law, legislation]`, `region: [austria, eu, eu_central]`,
  `language: de`
- **Practical**: no documented rate limit found this pass. `pages`/`count`
  fields support pagination (100,231 total records observed for
  `listId=101` - the site's full historical document index). No separate
  developer docs page found; the API is discovered by inspecting the site's
  own search-page network calls.
- **Why it matters**: Austria was explicitly flagged unverified in an
  earlier wave - now confirmed live with a real, large, keyless dataset.
  Complements the existing Austria HTML crawl domains with a structured,
  filterable index of the full legislative document corpus. Retried from an
  earlier wave's unverified flag - now confirmed.
- **Companion NOT verified this pass**: `data.gv.at` (Austria's national
  CKAN-style open-data portal) - the classic CKAN Action API path 404'd; the
  portal appears to have migrated off CKAN to a JS-rendered SPA with no API
  path discovered via static fetch this session.

---

## 3. `datos_gob_ar` (routes through existing `ckan_action_api` client - NO NEW CLIENT CODE) - Datos Argentina national CKAN, incl. InfoLEG

- **Region**: Argentina (national) - tagged `region: [south_america]` per
  the source research (no dedicated `argentina` key in `VALID_REGIONS` or
  `config/jurisdictions.yaml` today; the broad `south_america` group already
  exists and is the pattern the live config uses for Chile). Note for the
  registry team: if Argentina coverage grows, a dedicated `argentina`
  country row (iso3 ARG, iso_numeric 032) would let this render on the map
  as its own country rather than only inside the `south_america` group tray
  - flagged as an observation, not drafted here since no wave-4 entry
  actually requests that specific slug.
- **API base**: `https://datos.gob.ar`
- **Auth**: none - keyless CKAN Action API
- **Format**: JSON
- **Endpoint to call**: `GET /api/3/action/package_search?q=<term>&
  rows=<n>` - standard CKAN, confirmed live. The InfoLEG dataset
  (`justicia-base-infoleg-normativa-nacional` - Argentina's national
  legislative/regulatory database, laws/decrees/resolutions since 1997) is
  directly fetchable via `GET /api/3/action/package_show?
  id=justicia-base-infoleg-normativa-nacional`.
- **Coverage mapping**: `category: legislation`, `tags: [mandates,
  reporting]`, `policy_types: [law, regulation, report]`, `region:
  [south_america]`, `language: es`
- **Practical**: no documented hard rate limit; standard CKAN courtesy
  throttling. `metadata_modified` on the InfoLEG package showed
  `2026-07-18` (the day of this research) - actively maintained, not a
  stale mirror.
- **Effort tier**: (a)/(c) hybrid, per the task's instruction - USES THE
  EXISTING `ckan_action_api` client already specced in
  `draft/new-clients-wave2.md` (Italy/Ireland/Canada/Mexico/UK instances);
  this is simply a sixth instance, parameterized only by `base_url`. NO NEW
  CLIENT CODE REQUIRED.
- **Why it matters**: this IS the InfoLEG API the brief asked to
  retry/find - not a standalone InfoLEG-hosted API (InfoLEG itself,
  `infoleg.gob.ar`, has no public API of its own), but the same dataset
  served through Argentina's national open-data CKAN portal, confirmed live
  and current.

---

## 4. `datos_hcdn_gob_ar` (routes through existing `ckan_action_api` client - NO NEW CLIENT CODE) - Camara de Diputados de la Nacion Open Data (Argentina, HCDN)

- **Region**: Argentina (national) - same `region: [south_america]` tagging
  rationale as #3 above
- **API base**: `https://datos.hcdn.gob.ar`
- **Auth**: none - keyless CKAN Action API
- **Format**: JSON
- **Endpoint to call**: `GET /api/3/action/package_search?q=<term>&
  rows=<n>` - same CKAN shape as #3 but a distinct instance/portal run
  directly by the lower house (HCDN = Honorable Camara de Diputados de la
  Nacion).
- **Coverage mapping**: `category: legislative`, `tags: [mandates]`,
  `policy_types: [law, legislation]`, `region: [south_america]`,
  `language: es`
- **Practical**: no documented rate limit; the search term matters -
  `q=energia` returned 0 results, `q=ley` returned 6 real dataset hits
  including "Leyes" and "Leyes Sancionadas" (Sanctioned/Enacted Laws).
- **Effort tier**: (a)/(c) hybrid - same generic `ckan_action_api` client
  as #3, a SEVENTH instance. NO NEW CLIENT CODE REQUIRED.
- **Why it matters**: distinct from #3 - this is the legislative-branch's
  own portal (bill text, sanctioned-law datasets) rather than the
  executive-branch national catalog; together they cover both the
  legislative-process side and the cross-ministry regulatory side for
  Argentina.

---

## 5. `udata_api` (generic, first instance `dados_gov_pt`) - dados.gov.pt (Portugal national open-data portal)

- **Region**: Portugal (national)
- **API base**: `https://dados.gov.pt`
- **Auth**: none - keyless
- **Format**: JSON. NOT CKAN - runs on udata (the same Etalab platform as
  France's `data.gouv.fr`, already specced as `data_gouv_fr_api` in wave 2)
  - a genuinely different API shape from the CKAN family.
- **Endpoint to call**: `GET /api/1/datasets/?q=<query>` - confirmed live,
  returns `{"data": [...], "page", "page_size", "total"}`.
- **Coverage mapping**: cross-ministry Portuguese open data, including
  municipal climate-action plans and datasets that explicitly reference
  Diario da Republica (the official gazette) publication numbers. Maps to
  `category: district_heating`/`environment_ministry` depending on hit,
  `tags: [reporting, efficiency]`, `policy_types: [report]`, `region:
  [portugal, eu, eu_south]`, `language: pt`
- **Practical**: no documented hard rate limit found this pass.
- **Effort tier**: (c) - RECOMMEND building ONE generic `udata_api` client
  parameterized by `base_url` (France + Portugal, and any future
  udata-platform country) rather than two bespoke clients - same
  consolidation logic wave 2 applied to the CKAN family.
- **Why it matters**: fills the Portugal gap this wave specifically asked
  to retry. Distinct `base_url` from the existing `portugal.yaml` crawl
  entries (which target `parlamento.pt` and ministry sites directly) - this
  is the cross-government open-data catalog, useful as a discovery layer
  the same way `data_gouv_fr_api` was rated in wave 2. Verified:
  `q=diario+da+republica` returned 108 real hits referencing the official
  gazette. A narrower `q=eficiencia+energetica` returned only 2 hits and
  `q=rede+de+calor` (district heating) returned 0 - broader Portuguese
  energy/climate terms work better than literal English-taxonomy
  translations.
- **NOT independently verified this pass**: a direct `parlamento.pt`
  "Iniciativas" JSON API (community project `parlamentodb` wraps it) and
  `DRE.pt` (Diario da Republica) itself - no public webservice/API was
  confirmed for either; see unverified appendix.

---

## 6. `mx_sidof_gazette_api` - SIDOF (Sistema de Informacion del Diario Oficial de la Federacion, Mexico)

- **Region**: Mexico (national) - the official federal gazette itself,
  distinct from the DOF dataset mirror on datos.gob.mx (already reachable
  via the wave-2 `ckan_action_api` Mexico instance)
- **API base**: `https://sidof.segob.gob.mx`
- **Auth**: none - keyless, no signup
- **Format**: JSON
- **Endpoint to call**: `GET /datos_abiertos/getJSON/{id}` - confirmed
  live; `id=65` returned a real `ListaDiarios` array of gazette editions
  with `codDiario`, `codEdicion` (e.g. "VES" = vespertina/evening
  edition), `fecha` fields. The `datos_abiertos` landing page links several
  such `getJSON/{id}` endpoints (ids 43, 57, 61, 65 observed) - each
  apparently a different slice/dataset of the gazette index; exact per-id
  schema needs enumerating before a client is built.
- **Coverage mapping**: Mexico's Official Gazette (DOF) - the publication-
  of-record for laws, decrees, regulations, NOMs (official Mexican
  standards, where data-center energy-efficiency mandates would live). Maps
  to `category: regulatory`, `tags: [mandates, reporting]`, `policy_types:
  [law, regulation]`, `region: [mexico, north_america]`, `language: es`
- **Practical**: no documented rate limit found. The `/apiStatus` page is
  an HTML "publication alert" page, not itself a JSON endpoint - don't
  confuse it with the real `getJSON/{id}` data endpoints.
- **Effort tier**: (c) - needs a new client; multi-id discovery step
  required before the client can enumerate every available dataset slice.
- **Why it matters**: this is the actual Mexican federal gazette
  (equivalent to the US Federal Register, already a wave-3 client) - a
  genuinely different, higher-value find than the generic DOF summary
  dataset already reachable via the Mexico CKAN instance from wave 2.
  Verified: `curl "https://sidof.segob.gob.mx/datos_abiertos/getJSON/65"`
  returned HTTP 200 with real JSON: `{"messageCode": 200, "response": "OK",
  "ListaDiarios": [{"codDiario": 254661, "codEdicion": "VES", "fecha":
  "31-10-2013", ...}, ...]}`.
- **NOT verified this pass**: a clean API for the Mexican Chamber of
  Deputies (SIL - Sistema de Informacion Legislativa,
  `sil.gobernacion.gob.mx`) - real and browsable but no documented
  REST/JSON API endpoint found; see unverified appendix.

---

## 7. `za_open_gazettes_archive` - Open Gazettes South Africa (OpenUp / SAFLII)

- **Region**: South Africa (national, covers national AND all 9 provincial
  gazette series)
- **API base**: `https://archive.opengazettes.org.za` (companion search UI
  at `https://opengazettes.org.za`)
- **Auth**: none - keyless, no signup. Nonprofit project (OpenUp + SAFLII +
  African Network of Centers for Investigative Reporting, originally Indigo
  Trust/Code4SA funded).
- **Format**: JSON Lines (`.jsonlines`) bulk index + linked PDF gazette
  documents
- **Endpoint to call**: `GET /index/gazette-index-latest.jsonlines` - a
  bulk, newline-delimited-JSON index of every gazette in the archive
  (~40,000 gazettes, national + all 9 provinces, 1958-present per project
  docs), each record with `publication_title`, `jurisdiction_name`,
  `issue_number`, `volume_number`, `archive_url` (direct PDF link),
  `issue_title`, `pagecount`. This is a bulk-download shape (like the
  already-specced `assemblee_nationale_opendata` from wave 2), NOT a live
  keyword-search query endpoint - the companion human search UI at
  `search.opengazettes.org.za` appears to be a JS-rendered SPA that
  redirected to the plain homepage on every automated query attempt this
  session (no working query-string API discovered for it).
- **Coverage mapping**: South African national and provincial government
  gazettes - the actual gazette full-text/PDF-link layer this wave
  specifically asked to retry/find. Maps to `category: regulatory`, `tags:
  [reporting, mandates]`, `policy_types: [law, regulation, report]`,
  `region: [south_africa, africa]`, `language: en`
- **Practical**: no documented rate limit on the bulk index; it is a large
  file (not measured this session) - a client should download once and
  diff/re-poll periodically rather than re-fetching per query.
- **Effort tier**: (c) - needs a new client (bulk-index-then-filter shape,
  similar in spirit to the `assemblee_nationale_opendata` bulk-ZIP client
  from wave 2, but JSON Lines instead of a ZIP archive).
- **Why it matters**: a genuine national+provincial GAZETTE archive (not
  just a legislature bill-tracker) - exactly the "official journal, full
  text or metadata + doc URL" shape the brief called out by name. Verified:
  `curl "https://archive.opengazettes.org.za/index/
  gazette-index-latest.jsonlines"` returned HTTP 200 with a real first
  record. Complements the existing `south_africa.yaml` crawl domains
  (ministry/regulator sites) with the actual promulgation-of-record layer.
- **NOT re-proposed**: Kenya Gazette - already covered by the wave-3
  `kenya_law_api` client's `doc_type` filter, not re-specced here.

---

## 8. `in_data_gov_ogd_api` - Open Government Data (OGD) Platform India (HOLD)

- **Region**: India (national)
- **API base**: `https://api.data.gov.in` (portal at
  `https://www.data.gov.in`)
- **Auth**: **api_key** - free self-serve registration at
  `https://www.data.gov.in/user/register` (confirmed the registration path
  resolves, HTTP 302 redirect into the standard signup flow). Env var:
  `DATA_GOV_IN_API_KEY`. Key passed as `?api-key=` query param.
- **Format**: JSON (also XML/CSV per resource)
- **Endpoint to call**: `GET /resource/{resource_id}?api-key=<key>&
  format=json&limit=<n>` - the widely-circulated public "DEMO" key from
  online tutorials does NOT work broadly; it returned a real, well-formed
  `{"error": "Key not authorised"}` response - this proves the gateway
  itself is live and enforcing per-registration auth, but a personal key is
  required for real use, not a shared demo key.
- **Coverage mapping**: India's national open-data catalog - thousands of
  datasets across ministries; would need a follow-up pass, once a real key
  is issued, to identify which specific resource IDs cover energy
  efficiency/data-center policy/Bureau of Energy Efficiency programs. Maps
  to `category: regulatory`, `tags: [reporting, efficiency]`,
  `policy_types: [report]`, `region: [india, apac]`, `language: en`
- **Practical**: rate limits not confirmed (require a real key to test);
  standard courtesy throttling recommended.
- **Effort tier**: (c) - needs a new client; self-disables until
  `DATA_GOV_IN_API_KEY` is set, same pattern as `legiscan`/`govinfo`/
  `congress_gov_api`.
- **STATUS: HOLD.** PARTIALLY verified only. The gateway itself is
  confirmed live (real auth-gate JSON response, not a network failure or
  generic 404 page). NOT verified: no working query against a real dataset
  was completed (blocked on needing a registered personal key); no specific
  energy/data-center-relevant resource ID was identified. Do not build
  until a real key is issued and a relevant resource is found.
- **Why it matters (if it clears the hold)**: confirms India's national
  open-data gateway is real and live (the specific ask was "India Code
  API/eGazette/Sansad") - closest verified structured entry point found
  this pass, though it is a general-purpose data catalog, not a
  legislation-specific API.
- **NOT found this pass**: a dedicated India Code API (indiacode.nic.in -
  reachable, HTTP 200, but no API reference found in page content), a
  working eGazette API (`egazette.gov.in` - connection timed out
  repeatedly), or a public PRS Legislative Research API (PRS is a
  respected bill-tracking nonprofit but publishes no documented API - data
  is scraped from parliament/gazette sources, not offered as a service).
  All three flagged in the unverified appendix.

---

## Wave 4 unverified appendix (legislation-apis-4.md, 14 items)

Per the brief's instruction: these were checked this session and could NOT
be confirmed live/queryable with real evidence. Do not build clients against
them without a follow-up verification pass.

| Item | Reason |
|---|---|
| Austria - data.gv.at | Classic CKAN Action API path 404'd at every base_url variant tried; portal appears to have migrated off CKAN to a JS-rendered SPA |
| Belgium - data.gov.be | Every request (incl. the classic CKAN path) returned an F5/TSPD bot-challenge page, not real content |
| Belgium - dekamer.be (Chamber open data) | `/kvvcr/opendata/` returned HTTP 200 but only 244 bytes (likely a redirect/placeholder shell) - inconclusive |
| Belgium - Senate (senate.be) | No dedicated open-data/API reference found in search results at all; not fetched this pass |
| Italy - Camera dei Deputati (dati.camera.it) | Well-documented in public sources (SPARQL endpoint, "OCD" linked-data vocabulary) but every endpoint tried returned the same F5/TSPD SHA1-JS-challenge page |
| Mexico - Camara de Diputados/Senado (SIL, sil.gobernacion.gob.mx) | Real, browsable legislative-information system, but no documented REST/JSON API endpoint found |
| India - eGazette (egazette.gov.in) | Connection timed out on every attempt (`HTTP 000`) - could not confirm live or dead |
| India - India Code (indiacode.nic.in) | Site is live (HTTP 200) but no API reference found in the fetched page content |
| India - PRS Legislative Research | Respected bill-tracking site, but publishes no documented public API |
| Indonesia - peraturan.go.id, jdih.dpr.go.id | Both unreachable this session (`ECONNREFUSED`/`HTTP 000` and HTTP 403 respectively) - could be geo/network-level blocking |
| Malaysia - federalgazette.agc.gov.my, lom.agc.gov.my | Both unreachable this session (`getaddrinfo ENOTFOUND`/`HTTP 000`) - same caveat as Indonesia |
| Singapore - sso.agc.gov.sg (Singapore Statutes Online), egazette.gov.sg | Both returned HTTP 403 on every request - appears to be active bot-blocking rather than the sites being down |
| Ireland - Iris Oifigiuil (irisoifigiuil.ie) | Site is live (HTTP 200), confirmed NOT running WordPress or any other discoverable API - appears to be a static/legacy gazette site |
| Portugal - parlamento.pt Iniciativas API / DRE.pt webservices | Parliament does publish raw JSON/XML under "Dados Abertos", per its own page and a community wrapper (`parlamentodb`), but no concrete fetchable raw-file URL was resolved this session; DRE.pt itself publishes no documented webservice |

---

## Draft `api_sources.yaml` entries (all `enabled: false`)

```yaml
# =============================================================================
# DRAFT WAVE 4 ADDITIONS - tier-c structured API sources from wave-4
# source-expansion research (retry + new-country gazette/legislation pass).
# Every entry is `enabled: false`. Each NEW source_type needs a client
# under src/sources/ (registered in src/sources/__init__.py) before
# `enabled` can ever be flipped to true. The two `ckan_action_api` entries
# and the `dados_gov_pt` udata entry route through generic clients already
# called for in draft/new-clients-wave2.md - no bespoke new client code
# needed for the two ckan_action_api entries; dados_gov_pt should share a
# generalized `udata_api` client with wave-2's data_gouv_fr_api.
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
      Wave 4 tier-c candidate. USES EXISTING ckan_action_api CLIENT -
      no new client code required. Keyless CKAN, sixth instance
      (Italy/Ireland/Canada/Mexico/UK already specced in
      new-clients-wave2.md). Hosts the InfoLEG normativa-nacional dataset
      (laws/decrees/resolutions since 1997) - this IS the InfoLEG API
      retry ask; InfoLEG itself has no standalone API. Verified:
      package_show on justicia-base-infoleg-normativa-nacional returned a
      real, actively-maintained record (metadata_modified = today).

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
      Wave 4 tier-c candidate. USES EXISTING ckan_action_api CLIENT -
      no new client code required. Keyless CKAN, seventh instance of the
      shared client. Distinct from datos_gob_ar above - this is the
      legislative branch's own portal (bill/enacted-law datasets: "Leyes",
      "Leyes Sancionadas" confirmed live) vs. the cross-ministry
      executive-branch catalog. Note: q=energia returned 0 results, q=ley
      returned 6 real hits - query-term sensitive.

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
      webservices remain unverified this pass.

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
      all checked this pass and none has a confirmed public API.
```
