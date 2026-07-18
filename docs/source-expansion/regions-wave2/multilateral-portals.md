# Wave 2 — Multilateral/Regional Bodies + National Open-Data Portal APIs

Two mandates in one file per the task brief:
- **Target 1**: multilateral/regional bodies (development banks, regional energy
  centres, UN/global databases, cooling-specific bodies) not already covered by
  wave-1 supranational finds (IEA 4E EDNA, OECD SDMX, data.europa.eu, C40, ICLEI,
  Euroheat, Energy Community, ASEAN Centre for Energy, RCREEE, AFREC all excluded
  as duplicates).
- **Target 2**: national open-data portal APIs (CKAN/DKAN/Socrata) checked for
  live status, API type, and whether an actual energy/DC-relevant dataset exists.

**Dedup performed**: grepped `docs/source-expansion/draft/crawl/*.yaml`,
`docs/source-expansion/draft/new-clients.md`, and `config/domains/**/*.yaml` for
every candidate base_url/org name before drafting. Key findings:
- `data.gov.uk` is **already in the repo** (`config/domains/uk.yaml`, id
  `uk_hnpd`, `enabled: true`) but only as a single-dataset crawl entry (one HNPD
  dataset page), not the general CKAN Action API. See UK entry below for the
  distinction.
- `data.gov.sg` is already flagged (lowest-confidence, contingent) in
  `new-clients.md` #13 — not re-proposed here, per the brief's explicit dedup note.
- `donneesquebec_ckan` (Quebec CKAN) and `data_gov_cy` (Cyprus DKAN) are already
  tier-c candidates in `new-clients.md` — different portals, not re-proposed.
- World Bank RISE, Climate Policy Radar API, ICLEI, InforMEA/ECOLEX, and OECD PINE
  were already researched and flagged unverified in
  `docs/source-expansion/regions/supranational.md` — not re-litigated here except
  where this pass found new information.
- No existing `config/domains/*.yaml` file contains ECREEE, EACREEE, CCREEE,
  SACREEE, OLADE, Cool Coalition, Climate Watch, Eurostat's own REST API,
  climate-laws.org, France/Germany/Italy/Spain/Ireland/Mexico/Canada CKAN
  endpoints, or SEforALL. All are net-new.

Every candidate below was hit with a live fetch this session (WebFetch or a
direct API call); results are reported as observed, including negative/blocked
results — nothing here is guessed or hallucinated.

---

## Target 1 — Verified candidates (multilateral / regional bodies)

### 1. ECREEE — ECOWAS Centre for Renewable Energy and Energy Efficiency
- **name**: "ECREEE - ECOWAS Centre for Renewable Energy and Energy Efficiency"
- **id**: `ecreee_regional`
- **base_url**: `https://www.ecreee.org`
- **level**: supranational (regional IGO body — energy efficiency + renewables for
  15 ECOWAS West African member states)
- **access**: none (open, no key)
- **format**: HTML + PDF
- **effort tier**: (b) plain crawl domain
- **coverage**: region: `["africa"]` (closest valid bucket; ECOWAS/West Africa not
  in `VALID_REGIONS`), category: `coordination_body`, tags:
  `["efficiency", "planning", "research"]`, policy_types: `["report", "guidance", "directive"]`,
  language: `en`
- **start_paths** (proposed): `/energy-efficiency/`, `/regional-policies/`,
  `/regional-progress-reports/`, `/country-documents/`
- **practical**: no robots.txt blocker hit; standard corporate CMS. Also links out
  to `eis.ecowas.int` (Energy Information System / "ECOWREX" data platform) —
  worth a follow-up pass to check if that sub-domain has its own API.
- **why worth adding**: direct regional counterpart to the already-shipped RCREEE
  (Arab states) and AFREC (AU) entries — this is the ECOWAS-specific one, covering
  a large West African bloc with a dedicated "Energy Efficiency" section holding
  consolidated regional policy documents, not just renewables.
- **verified**: yes. Fetched directly — page title confirmed "ECREEE (ECOWAS
  Centre for Renewable Energy and Energy Efficiency)"; confirmed live
  `/regional-policies/`, `/regional-progress-reports/` (2023 report referenced),
  `/country-documents/` sections.

### 2. EACREEE — East African Centre of Excellence for Renewable Energy and Efficiency
- **name**: "EACREEE - East African Centre of Excellence for Renewable Energy and Efficiency"
- **id**: `eacreee_regional`
- **base_url**: `https://www.eacreee.org`
- **level**: supranational (EAC — East African Community regional energy body)
- **access**: none
- **format**: HTML + PDF
- **effort tier**: (b) plain crawl domain
- **coverage**: region: `["africa"]`, category: `coordination_body`, tags:
  `["efficiency", "planning", "research"]`, policy_types: `["report", "guidance"]`,
  language: `en`
- **start_paths** (proposed): `/content/activities-and-services`, `/publications`,
  `/documents` (Strategic Documents)
- **practical**: no auth; confirmed live content includes Minimum Energy
  Performance Standards (MEPS) for refrigerating appliances and air conditioners
  — directly in-taxonomy (cooling-efficiency standard).
- **why worth adding**: this is the Target-1 EAC ask, fulfilled — a real,
  currently active regional body (not a dead/placeholder page), with a
  region-wide MEPS program for cooling equipment.
- **verified**: yes. Fetched directly — confirmed page content: "Draft Regional
  Renewable Energy Policy and Transboundary" framework, MEPS program, green
  hydrogen strategy, 2025-2030 strategy document.

### 3. CCREEE — Caribbean Centre for Renewable Energy and Energy Efficiency
- **name**: "CCREEE - Caribbean Centre for Renewable Energy and Energy Efficiency"
- **id**: `ccreee_regional`
- **base_url**: `https://ccreee.org`
- **level**: supranational (CARICOM regional energy body — fulfills the brief's
  CARICOM ask directly, more specific than the general CARICOM secretariat site)
- **access**: none
- **format**: HTML + PDF
- **effort tier**: (b) plain crawl domain
- **coverage**: region: `["north_america"]` (closest valid bucket per
  `VALID_REGIONS` docstring "North America (US, Canada, Mexico)" — imperfect;
  Caribbean/CARICOM has no dedicated bucket, flagged below), category:
  `coordination_body`, tags: `["efficiency", "planning", "research"]`,
  policy_types: `["report", "guidance"]`, language: `en`
- **start_paths** (proposed): `/all-strategic-documents/`, `/all-publications/`,
  `/our-work/`
- **practical**: no auth; site describes itself as "The Caribbean's Renewable
  Energy and Energy Efficiency Hub." Energy Report Cards (ERCs) per member state
  and an Integrated Resource and Resilience Plan (IRRP) resource confirmed live.
- **why worth adding**: same regional-hub pattern as RCREEE/ECREEE/AFREC already
  in the repo, filling the Caribbean/CARICOM gap the brief calls out by name.
- **verified**: yes. Fetched directly — page title "Home - CCREEE" confirmed,
  strategic documents / publications / ERC sections all live.

### 4. SACREEE — SADC Centre for Renewable Energy and Energy Efficiency
- **name**: "SACREEE - SADC Centre for Renewable Energy and Energy Efficiency"
- **id**: `sacreee_regional`
- **base_url**: `https://www.sacreee.org`
- **level**: supranational (SADC — Southern African Development Community regional
  energy body; fulfills the brief's SADC ask)
- **access**: none
- **format**: HTML + PDF
- **effort tier**: (b) plain crawl domain
- **coverage**: region: `["africa"]`, category: `coordination_body`, tags:
  `["efficiency", "planning", "research"]`, policy_types: `["report", "guidance"]`,
  language: `en`
- **start_paths** (proposed): `/services/policy-advisory`, `/resources/publications`,
  `/sekh` (Sustainable Energy Knowledge Hub)
- **practical**: no auth; the SADC Industrial Energy Efficiency Programme (SIEEP)
  is its flagship policy/regulatory-framework project per its own site.
- **why worth adding**: completes the Africa regional-body set alongside
  ECREEE/EACREEE/AFREC/RCREEE — one per major African regional economic
  community.
- **verified**: yes. Fetched directly — page title "Homepage | SACREEE Community"
  confirmed; Vision & Mission, Services > Policy Advisory, SEKH, and Publications
  sections all live.

### 5. OLADE — Latin American and Caribbean Energy Organization
- **name**: "OLADE - Latin American and Caribbean Energy Organization"
- **id**: `olade_regional`
- **base_url**: `https://www.olade.org`
- **level**: supranational (27-member-country Ibero-American/LatAm energy IGO,
  headquartered Quito, Ecuador — the brief's explicit OLADE ask)
- **access**: none for the site/publications; SieLAC statistical portal is also
  free/open per OLADE's own description
- **format**: HTML + PDF; SieLAC is a separate statistical data portal (not
  independently confirmed as an API this pass — likely a web UI, not REST)
- **effort tier**: (b) plain crawl domain (SieLAC itself would need a follow-up
  pass to confirm any API/export shape before considering tier-c)
- **coverage**: region: `["south_america"]`, category: `coordination_body`, tags:
  `["efficiency", "research", "reporting"]`, policy_types: `["report", "guidance"]`,
  language: `es` (site has an English section, `/en/`)
  , note: primary content is Spanish
- **start_paths** (proposed): `/en/` (English section), `/publicaciones/` or
  equivalent publications index, `/sielac/` (statistics portal landing)
- **practical**: no robots.txt blocker hit on the English homepage.
- **why worth adding**: the single Ibero-American/LatAm-wide energy IGO the brief
  names directly — publishes Energy Outlook reports, ENERLAC journal, and
  cross-country statistical series (economic-energy indicators, 1970-present)
  across all 27 member states, not just one country.
- **verified**: yes. Fetched `/en/` directly — page title "Home English - OLACDE"
  confirmed; SieLAC statistical portal, ENERLAC journal, and Energy Outlook
  reports all referenced as live resources.
- **append to**: new file `config/domains/supranational.yaml` (already recommended
  in wave-1 for IEA 4E EDNA etc. — OLADE and the four regional centres above
  should join that same file rather than force-fitting into a single-country
  file).

### 6. UNEP Cool Coalition — District cooling / cooling-efficiency policy hub
- **name**: "Cool Coalition (UNEP) - Cooling Policy Hub"
- **id**: `cool_coalition`
- **base_url**: `https://coolcoalition.org`
- **level**: supranational (UNEP-hosted global coalition — governments,
  cities, business — the brief's explicit district-cooling ask)
- **access**: none
- **format**: HTML + PDF
- **effort tier**: (b) plain crawl domain
- **coverage**: region: `["supranational", "global"]` (same enum caveat as
  wave-1's IEA/C40/ISO entries — not in `VALID_REGIONS`, flagged not force-mapped),
  category: `district_cooling` (existing category, used by apac.yaml/uae.yaml
  today), tags: `["efficiency", "planning", "carbon"]`, policy_types:
  `["guidance", "report", "standard"]`, language: `en`
- **start_paths** (proposed): `/knowledge-hub`, `/working-groups` (nine thematic
  groups including Cooling Efficiency Standards / MEPS and Urban Heat & District
  Cooling), `/global-cooling-pledge`
- **practical**: no auth wall observed; standard corporate CMS.
- **why worth adding**: this is precisely the district-cooling/cooling-specific
  body the brief calls out — tracks National Cooling Action Plans (NCAPs) by
  country, a Policy Toolkit for Sustainable Cooling, and MEPS/procurement working
  groups — the closest global equivalent to a district-cooling regulator index.
- **verified**: yes. Fetched directly — page title "Homepage | Cool Coalition"
  confirmed; NCAP working group, Policy Toolkit (Knowledge Hub), MEPS/procurement
  working group, and Global Cooling Pledge (250+ signatories) all live.
- **append to**: new file `config/domains/supranational.yaml`.

### 7. Climate Change Laws of the World (Grantham Research Institute / LSE)
- **name**: "Climate Change Laws of the World"
- **id**: `climate_laws_lse`
- **base_url**: `https://climate-laws.org`
- **level**: supranational (196-country climate-law database, LSE Grantham
  Research Institute, now powered by Climate Policy Radar's NLP search — the
  brief's explicit "LSE Grantham... has data" ask)
- **access**: none for browsing/search (a "Download our data" bulk-export form
  exists but was not tested this pass)
- **format**: HTML (search UI); underlying documents are PDF/HTML
- **effort tier**: (b) plain crawl domain. **Not** tier-c: wave-1's
  `supranational.md` already confirmed Climate Policy Radar's own **API is
  explicitly "coming soon," not live** — this entry proposes crawling the public
  search/browse website itself, which is a different thing from that unlaunched
  API and does not conflict with the wave-1 finding.
- **coverage**: region: `["supranational", "global"]` (enum caveat as above),
  category: `legislative`, tags: `["mandates", "research", "reporting"]`,
  policy_types: `["law", "report"]`, language: `en` (site auto-translates
  non-English documents)
- **start_paths** (proposed): `/` (search landing), a filtered search URL such as
  `/search?q=energy+efficiency` or `/search?q=data+centre` (exact query-string
  shape not independently confirmed this pass — confirm the site's real search
  URL pattern via a browser session before building start_paths)
- **practical**: over 7,000 climate laws/policies/UNFCCC submissions indexed;
  no visible topic tag specifically for "energy efficiency" or "data centres" in
  the landing-page content fetched this pass — full-text search would need to
  carry the load rather than a pre-built topic filter. Likely JS-rendered search
  results (React-style app) — **requires_playwright: true** is a reasonable
  default assumption pending confirmation.
- **why worth adding**: exactly the "one integration, many jurisdictions" climate
  law source the brief names, and — unlike the not-yet-live API — the website
  itself is confirmed live and searchable today.
- **verified**: yes, with caveat. Fetched `https://climate-laws.org/` directly —
  page title and "Search over 7000 climate laws..." copy confirmed live. Did NOT
  confirm the exact filtered-search URL pattern or whether search results render
  without JS — flag for one more pass before finalizing `start_paths`.
- **append to**: new file `config/domains/supranational.yaml`.

### 8. SEforALL — Sustainable Energy for All (Research & Analysis hub)
- **name**: "SEforALL - Research and Analysis"
- **id**: `seforall_research`
- **base_url**: `https://www.seforall.org`
- **level**: supranational (UN-affiliated global SDG7 body — the brief's
  explicit SEforALL ask)
- **access**: none
- **format**: HTML + PDF
- **effort tier**: (b) plain crawl domain
- **coverage**: region: `["supranational", "global"]`, category: `standards`,
  tags: `["efficiency", "research"]`, policy_types: `["report", "guidance"]`,
  language: `en`
- **start_paths** (proposed): `/our-work/research-analysis`
- **practical**: confirmed 181 research outputs, filterable by programme
  area/SDG7 target/region/country — but this is a **publication hub, not a
  queryable database or API**; no downloadable structured dataset or policy
  tracker found on this page.
- **why worth adding**: lower priority than the district-cooling-specific Cool
  Coalition entry above, but still a legitimate, currently-updated global
  energy-access/efficiency knowledge hub (cooling-sector "Chilling Prospects"
  series, eCooking guidance) worth indexing at low crawl depth.
- **verified**: yes. Fetched directly — page title "Research & analysis |
  Sustainable Energy for All" confirmed; 181 outputs and cooling/eCooking
  publications named explicitly.
- **append to**: new file `config/domains/supranational.yaml`.

---

## Target 1 — Structured API candidates (tier-c, new client needed)

### 9. Climate Watch — NDC Content API (World Resources Institute)
- **name**: "Climate Watch NDC Content API"
- **proposed id**: `climatewatch_ndc`
- **API base**: `https://www.climatewatchdata.org`
- **access**: none — keyless, confirmed live
- **source_type feasibility**: needs a NEW client. Confirmed working, keyless
  endpoints: `GET /api/v1/data/historical_emissions?source_ids[]=<id>` (returned
  a real 200 JSON response with country/sector/gas columns) and
  `GET /api/v1/data/ndc_content?location=<ISO3>&category_ids[]=<id>` (also
  returned a real 200 JSON response with `id, source, iso_code3, country,
  sector, subsector, indicator_slug, value, indicator_name` columns) — both
  calls in this session used guessed parameter IDs and returned empty `data`
  arrays, so the endpoints are live and the schema is confirmed, but the exact
  category/indicator IDs relevant to energy efficiency/buildings/waste heat
  still need to be enumerated from Climate Watch's own category list before a
  client can pull real content.
- **format**: JSON
- **CrawlResult mapping**: `url` = constructed NDC country page
  (`climatewatchdata.org/ndcs/country/<ISO3>`); `title` = country + indicator
  name; `content` = indicator value/text from the `ndc_content` response;
  `lifecycle_stage` = not applicable (NDC submissions are the lifecycle stage
  itself, not further staged).
- **pagination/rate limits**: none documented; no hard rate limit encountered
  this pass.
- **why it matters**: NDCs (Paris Agreement national commitments) are exactly
  the "policy commitment" layer the brief's taxonomy covers, across 171+
  countries in one API, with 150+ structured indicators — some of which cover
  energy efficiency and buildings sectors per Climate Watch's own indicator
  taxonomy. Needs one more pass to enumerate the specific
  `category_ids`/indicator slugs for energy efficiency before building.
- **append to**: `config/domains/api_sources.yaml` as a new `source_type:
  "climatewatch_ndc"`.

### 10. Eurostat REST Dissemination API (energy balance statistics)
- **name**: "Eurostat REST Dissemination API - Energy Balances"
- **proposed id**: `eurostat_energy`
- **API base**: `https://ec.europa.eu/eurostat/api/dissemination`
- **access**: none — keyless, EU open-data terms
- **source_type feasibility**: needs a NEW client (SDMX-JSON, distinct shape
  from every existing client and from the `data_europa` tier-c spec already
  drafted in wave-1 — this is Eurostat's own statistics API, not the
  data.europa.eu cross-catalog search). Confirmed working endpoint pattern:
  `GET /statistics/1.0/data/{dataset_code}?format=JSON&lang=EN&{dimension
  filters}` — tested against `nrg_bal_c` (Complete Energy Balances), which
  returned valid SDMX-JSON structural metadata (35 years of data, 1990-2024,
  for Germany) confirming the dataset and endpoint are both real and live; the
  specific waste-heat product/flow code combination queried happened to return
  no populated observations, meaning the exact SIEC/NRG_BAL code for "waste
  heat" needs to be looked up in Eurostat's own code-list browser before a
  client can reliably pull that specific series (the dataset and gateway
  themselves are not in question).
- **format**: JSON (SDMX-JSON 2.0), also CSV/XML available via `format=` param
- **CrawlResult mapping**: `url` = Eurostat's own dataset browser page for the
  queried code; `title` = dataset name + country + indicator; `content` =
  observation values + metadata description; `lifecycle_stage` = not applicable
  (statistical series, not a legislative lifecycle).
- **pagination/rate limits**: no documented hard limit; standard EU API courtesy
  throttling recommended.
- **why it matters**: Eurostat is the EU's own statistical office (distinct from
  the data.europa.eu meta-catalog already drafted in wave-1) with a real,
  documented, keyless REST API for energy statistics across all 27 EU member
  states plus EFTA/candidate countries in one call — the brief's explicit
  "Eurostat energy" ask. Treat as a discovery/context layer alongside legal
  text sources, same caveat wave-1 gave data.europa.eu (statistical, not
  primarily legislative).
- **append to**: `config/domains/api_sources.yaml` as a new `source_type:
  "eurostat_energy"`.

---

## Target 1 — Unverified / needs-human-check (blocked or inconclusive this session)

All of the following were attempted with a live fetch and returned HTTP 403 or
404 to this session's automated tooling (consistent with enterprise
Cloudflare/Akamai bot-protection commonly used by multilateral development
banks) — existence and real content were confirmed only indirectly via web
search of their own published pages, not by an independent direct fetch. Do
not add to `config/domains/` until a human/browser session confirms
reachability, per the brief's verification standard.

- **World Bank ESMAP** (`esmap.org`) — 403 on `/energy_efficiency` and the
  bare homepage both attempts. Web search confirms ESMAP is real and active on
  energy efficiency broadly, but no data-center/waste-heat-specific ESMAP page
  was surfaced even via search. Recommend a browser-session recheck before any
  further work.
- **GlobalABC** (`globalabc.org`) — 403 on both the Global Status Report path
  and the bare homepage. Known to be real (UNEP-hosted Global Alliance for
  Buildings and Construction, publishes the annual Global Status Report for
  Buildings and Construction) but not independently reachable this session.
- **African Development Bank (AfDB)** (`afdb.org`) — 403 on
  `/en/topics-and-sectors/sectors/energy-power`. Web search confirms a real,
  active Sustainable Energy Fund for Africa (SEFA) and energy-efficiency
  publications, but page content not independently fetched.
- **Asian Development Bank (ADB)** (`adb.org`) — 403 on `/what-we-do/topics/
  energy/overview`. Web search independently confirmed real, on-topic ADB
  documents — "District Heating Business Models and Policy Solutions:
  Financing Utilization of Low-Grade Industrial Excess Heat in the PRC" and the
  "Heilongjiang Energy Efficient District Heating Project" — genuinely
  on-topic (industrial waste heat + district heating policy), but the page
  itself was not independently fetched this session; recheck via browser
  before adding.
- **EBRD Green Cities / Green Economy Transition** (`ebrd.com`) — both
  `/green-cities` and `/what-we-do/sectors/green-economy` returned 404
  (URL paths guessed, likely stale/incorrect), and
  `/green-economy-transition` also 404'd. EBRD's Green Cities program is real
  and well-documented externally, but the correct current URL path was not
  found this session — needs a fresh site-map/search pass, not just a retry.
- **Inter-American Development Bank (IDB)** (`iadb.org`) — 403 on
  `/en/topics/energy`. Not independently confirmed this session beyond its
  well-known public existence.
- **European Investment Bank (EIB)** (`eib.org`) — 403 on the energy-efficiency
  priorities page. Not independently confirmed this session.
- **Pacific Community (SPC)** (`spc.int`) — 403 on `/our-work/energy`. Not
  independently confirmed this session; the brief's Pacific/SPC ask remains
  open for a follow-up pass.
- **International Institute of Refrigeration (IIR/IIF)** (`iifiir.org`) —
  homepage DID load successfully (confirmed live, "International Institute of
  Refrigeration (IIR)" title, FRIDOC bibliographic database, technical/policy
  briefs section, a "files on regulations" nav link). However, the homepage
  content fetched did not show district-cooling- or data-center-specific
  policy material prominently — the "files on regulations" link and FRIDOC
  database need a dedicated follow-up pass to confirm whether they carry
  actual government regulation text (vs. just a bibliographic index of
  technical papers) before this is upgraded to a ranked candidate. Provisional
  ranking: low priority pending that check.
- **World Bank RISE, Climate Policy Radar API, OECD PINE dataflow ID, ICLEI,
  InforMEA/ECOLEX** — already flagged unverified in wave-1's
  `docs/source-expansion/regions/supranational.md`; not re-tested this pass,
  no new information to add.

---

## Target 2 — National open-data portal APIs

Every portal below was hit with a real query for an energy/data-center-relevant
keyword against the portal's own action/search API this session. Result counts
and titles are copy-pasted from what the API actually returned, not invented.

### 11. France — data.gouv.fr (verified, best find in Target 2)
- **name**: "data.gouv.fr Open Data API (France)"
- **proposed id**: `data_gouv_fr_api`
- **base_url**: `https://www.data.gouv.fr`
- **API type**: **not CKAN** — France's portal runs on **udata** (Etalab's own
  open-source platform), with its own REST API at `/api/1/`. Distinct shape
  from the CKAN/DKAN clients discussed elsewhere in this file.
- **access**: none — keyless
- **format**: JSON
- **level**: national
- **effort tier**: (c) needs a NEW client (udata's `/api/1/datasets/` shape does
  not match any existing client or the CKAN pattern used elsewhere)
- **coverage**: region: `["france", "eu"]`, category: `district_heating`, tags:
  `["efficiency", "planning"]`, policy_types: `["report", "regulation"]`,
  language: `fr`
- **endpoint tested**: `GET /api/1/datasets/?q=<query>` — confirmed live,
  returns `{"data": [...], "page", "page_size", "total"}`.
- **practical**: `q=chaleur+fatale` (the French policy term for "waste heat")
  returned 0 results, but `q=réseau+de+chaleur` (district heating network)
  returned a rich, genuinely on-topic set of **actual government datasets**,
  not just statistics: "Zone de développement prioritaire du réseau de
  chaleur" (Paris priority-development zones), "Périmètre de raccordement
  obligatoire au réseau de chaleur urbain" (Bordeaux mandatory-connection
  zones — a real regulatory/zoning instrument), "Part de chaleur décarbonée
  produite (ENR&R renouvelable et de récupération)" (tracks recovered/reused
  heat share in district networks — directly maps to this project's waste-heat
  taxonomy).
- **why worth adding**: unlike most open-data-portal hits in this file (mostly
  statistical tables), several of these ARE regulatory instruments —
  mandatory-connection perimeters and priority-development zones are
  government policy decisions with real legal force, not just data. Highest
  policy-relevance hit of any Target-2 portal tested this session.
- **verified**: yes, both empty and populated queries tested directly against
  the live API.
- **rate limits**: no documented hard limit found this pass.

### 12. Italy — dati.gov.it (verified, CKAN)
- **name**: "dati.gov.it Open Data API (Italy)"
- **proposed id**: `dati_gov_it_api`
- **base_url**: `https://www.dati.gov.it`
- **API type**: **CKAN** — confirmed via the standard `package_search` action
  and `"success": true` response shape.
- **access**: none — keyless
- **format**: JSON
- **level**: national
- **effort tier**: (c) needs a NEW client, OR could reuse a generic CKAN client
  if one gets built for the France/other CKAN entries in this file (Italy,
  Australia-attempted, Ireland, and the already-drafted Cyprus DKAN entry all
  share the CKAN Action API shape closely enough that ONE generic
  `ckan_action_api` client parameterized by base_url could serve all of them —
  recommend this consolidation over five separate bespoke clients).
- **coverage**: region: `["italy", "eu"]`, category: `energy_ministry`, tags:
  `["efficiency", "reporting"]`, policy_types: `["report"]`, language: `it`
- **endpoint tested**: `GET /opendata/api/3/action/package_search?q=efficienza+
  energetica&rows=5` — confirmed live, 5 real results returned.
- **practical**: results returned are mostly regional/provincial statistical
  tables (Umbria energy-efficiency-report counts, Trento Energy Performance
  Certificates, provincial energy-efficiency incentive programs, ENEA agency
  news feed) — mixed statistical/administrative, with at least one real
  incentive-program dataset ("Incentivi Legge Provinciale 14/80 -
  Efficientamento energetico").
- **verified**: yes, direct live query confirmed.
- **rate limits**: not documented this pass; standard CKAN courtesy throttling
  recommended.

### 13. Spain — datos.gob.es (verified, DCAT/linked-data API — not CKAN)
- **name**: "datos.gob.es apidata (Spain)"
- **proposed id**: `datos_gob_es_api`
- **base_url**: `https://datos.gob.es`
- **API type**: **not CKAN** — a Linked Data API (DCAT-AP-ES, "apidata")
  supporting JSON/XML/RDF/Turtle/CSV via file-extension content negotiation.
- **access**: none — keyless
- **format**: JSON (default), also XML/RDF/Turtle/CSV
- **level**: national
- **effort tier**: (c) needs a NEW client (linked-data-api shape, distinct from
  CKAN)
- **coverage**: region: `["spain", "eu"]`, category: `energy_ministry`, tags:
  `["efficiency", "reporting"]`, policy_types: `["report"]`, language: `es`
- **endpoint tested**: `GET /apidata/catalog/dataset/title/<keyword>` — this is
  an **exact/substring title match, not a full-text search** (a full free-text
  query like "eficiencia energetica" returned 0 results; the single word
  "energia" returned 2 real hits) — important implementation detail for a
  future client: it will need either exact known titles or a broader
  crawl-then-filter strategy, not a keyword search the way CKAN's
  `package_search` works.
- **practical**: confirmed real datasets: "Estadísticas delegadas de petróleo,
  gas y energía eléctrica" and "Registro de productores de energía eléctrica"
  (electricity producer registry) — statistical/administrative, not
  legislative text.
- **verified**: yes, both the empty and populated query shapes confirmed live.
- **rate limits**: not documented this pass.

### 14. Ireland — data.gov.ie (verified, CKAN)
- **name**: "data.gov.ie Open Data API (Ireland)"
- **proposed id**: `data_gov_ie_api`
- **base_url**: `https://data.gov.ie`
- **API type**: CKAN — confirmed via `package_search`, `"success": true`
- **access**: none — keyless
- **format**: JSON
- **level**: national
- **effort tier**: (c), same generic-CKAN-client consolidation note as Italy
  above
- **coverage**: region: `["ireland"]`, category: `energy_ministry`, tags:
  `["efficiency", "reporting"]`, policy_types: `["report"]`, language: `en`
- **endpoint tested**: `GET /api/3/action/package_search?q=energy+efficiency&
  rows=5` — 19 total results.
- **practical**: results are local-authority housing-retrofit data (Fingal
  County Council) and CSO (Central Statistics Office) household
  energy-efficiency-installation statistics — statistical, not legislative.
  Lower priority than the already-shipped `oireachtas` tier-c candidate
  (new-clients.md #8) for actual Irish legislative text, since this portal
  is statistics-only for this query.
- **verified**: yes.
- **rate limits**: not documented this pass.

### 15. Canada — open.canada.ca (verified, CKAN)
- **name**: "Open Government Canada CKAN API"
- **proposed id**: `open_canada_ca_api`
- **base_url**: `https://open.canada.ca`
- **API type**: CKAN — confirmed
- **access**: none — keyless
- **format**: JSON
- **level**: national
- **effort tier**: (c), same generic-CKAN-client consolidation note
- **coverage**: region: `["canada", "north_america"]`, category:
  `energy_ministry`, tags: `["efficiency", "reporting"]`, policy_types:
  `["report"]`, language: `en`
- **endpoint tested**: `GET /data/api/3/action/package_search?q=data+centre+
  energy+efficiency&rows=5` — 100 results (rows capped, likely far more total).
- **practical**: results include Natural Resources Canada's "Survey of
  Commercial and Institutional Energy Use," "Canada's Energy Future 2026:
  Energy Supply and Demand Projections to 2050," and EnerGuide appliance-label
  data — statistical/administrative, not legislative. Complements (does not
  replace) the existing `legisinfo_api` client already in
  `config/domains/api_sources.yaml`.
- **verified**: yes.
- **rate limits**: not documented this pass.

### 16. Mexico — datos.gob.mx (verified, CKAN)
- **name**: "datos.gob.mx Open Data API (Mexico)"
- **proposed id**: `datos_gob_mx_api`
- **base_url**: `https://www.datos.gob.mx` (note: **www prefix required** — the
  bare `datos.gob.mx/api/...` and `datos.gob.mx/busca/api/...` paths both
  404'd; only `https://www.datos.gob.mx/api/3/action/...` resolved)
- **API type**: CKAN — confirmed
- **access**: none — keyless
- **format**: JSON
- **level**: national
- **effort tier**: (c), same generic-CKAN-client consolidation note
- **coverage**: region: `["mexico"]`, category: `energy_ministry`, tags:
  `["efficiency", "reporting"]`, policy_types: `["report"]`, language: `es`
- **endpoint tested**: `GET /api/3/action/package_search?q=energia&rows=5` — 81
  results.
- **practical**: real datasets from CFE (Federal Electricity Commission) and
  CENACE (National Energy Control Center) — electricity consumption, marginal
  energy prices, an "Energy-Saving Technologies Evaluation" (ETA) program.
  Statistical/administrative rather than legislative.
- **verified**: yes.
- **rate limits**: not documented this pass.

### 17. United States — data.gov (verified — requires an api_key, corrects the brief's assumption)
- **name**: "Data.gov (GSA gateway to CKAN Action API)"
- **proposed id**: `data_gov_us_api`
- **base_url**: `https://api.gsa.gov/technology/datagov/v3` (the GSA API
  gateway now fronts the underlying CKAN instance at catalog.data.gov — a
  direct hit to `catalog.data.gov/api/3/action/...` 404'd this session,
  confirming the gateway is now the only working path)
- **access**: **api_key** — a shared `DEMO_KEY` worked for this session's test
  query (rate-limited, shared across all api.data.gov demo users), but
  production use needs a free personal key from `https://api.data.gov/signup/`.
  Env var: `DATA_GOV_API_KEY`.
- **format**: JSON
- **level**: national
- **effort tier**: (c) needs a NEW client (CKAN-shaped payload, but the auth
  layer — api_key as a query param through a GSA gateway rather than a bare
  CKAN instance — is a real difference from the plain-CKAN entries above)
- **coverage**: region: `["us"]`, category: `energy_ministry`, tags:
  `["efficiency", "reporting"]`, policy_types: `["report"]`, language: `en`
- **endpoint tested**: `GET /action/package_search?q=data+center+energy+
  efficiency&rows=5&api_key=DEMO_KEY` — confirmed live, 4,363 total results.
- **practical**: results include DOE's FuelEconomy.gov, alternative-fueling
  station data, and "NYC Building Energy and Water Data Disclosure for Local
  Law 84" (a real municipal energy-benchmarking-law compliance dataset — the
  closest thing to actual policy-adjacent data found in this US query).
  Mostly statistical/disclosure data, not primary legislative text.
- **why the correction matters**: the brief listed data.gov generically among
  keyless CKAN/DKAN portals; this session confirmed that assumption is now
  wrong for the US specifically — data.gov requires registering for a free key
  through the GSA's api.data.gov program, unlike the UK/Italy/Ireland/Canada/
  Mexico entries above which are all fully keyless.
- **verified**: yes, live call with a working (shared demo) key.
- **rate limits**: DEMO_KEY is explicitly rate-limited/shared; a registered
  personal key raises the limit (exact numbers in api.data.gov's own docs, not
  independently re-confirmed this pass).

### 18. UK — data.gov.uk CKAN Action API (verified — broader than the existing single-dataset entry)
- **name**: "data.gov.uk CKAN Action API (general query, beyond the existing HNPD dataset)"
- **proposed id**: `data_gov_uk_ckan_api`
- **base_url**: `https://www.data.gov.uk` (redirects to the underlying instance
  at `ckan.publishing.service.gov.uk` — confirmed via a live 301)
- **access**: none — keyless
- **format**: JSON
- **level**: national
- **effort tier**: (c) needs a NEW client for the *general* CKAN Action API —
  **dedup note**: `config/domains/uk.yaml` already has `uk_hnpd` (`enabled:
  true`) pointed at `https://www.data.gov.uk`, but that entry is a plain crawl
  domain scoped to ONE dataset page (the DESNZ Heat Networks Planning
  Database). This candidate is a different kind of integration — the general
  `package_search` action, which would surface ALL matching datasets on the
  portal, not just the one already hardcoded. Not a duplicate in function, but
  shares a base_url with an existing entry — flagging explicitly per the
  brief's dedup instructions rather than silently adding a second
  same-base_url entry.
- **coverage**: region: `["uk"]`, category: `district_heating`, tags:
  `["efficiency", "reporting"]`, policy_types: `["report"]`, language: `en`
- **endpoint tested**: `GET /api/3/action/package_search?q=heat+network+data+
  centre&rows=5` (via the redirect target) — confirmed live, **1,793 total
  results**, with the existing `uk_hnpd` dataset itself appearing in the top
  results ("DESNZ: Heat Networks Planning Database"), alongside others like
  "Heat Network Locations (Existing and Planned) - Scotland" and "Heat
  Networks Polling - January 2026."
- **why worth adding**: the existing crawl entry only ever sees the ONE
  dataset it's hardcoded to; a real CKAN Action API client would
  automatically pick up new/updated UK heat-network and energy datasets as
  they're published, at essentially the same access cost (keyless, same
  host).
- **verified**: yes, live query confirmed 1,793 results including datasets
  already known to be relevant.
- **rate limits**: UK's own guidance states no rate limit on this API (per a
  `guidance.data.gov.uk` doc page surfaced during research, not independently
  re-fetched this pass).

---

## Target 2 — Unverified / needs-human-check

- **Germany — govdata.de** — the CKAN Action API shape is real and documented
  (confirmed via search: `https://www.govdata.de/ckan/api/3/action/
  package_search`, matching third-party references), but every direct fetch
  attempt this session returned `connect ECONNREFUSED` rather than an HTTP
  error — a networking-layer failure from this session's environment, not a
  confirmed-down site. Needs a recheck from a normal network/browser before
  either confirming or dropping.
- **Australia — data.gov.au** — every attempt (the CKAN API at both `/api/3/
  action/...` and `/data/api/3/action/...`, the plain dataset-search HTML page,
  and even `/robots.txt`) returned HTTP 403 this session, suggesting
  session-level bot-blocking (Australia's portal is known publicly to run
  CKAN, per search results showing `data.gov.au/data/api/1/util/snippet/
  api_info.html` resource pages) rather than the site being down. Needs a
  browser-session recheck; do not add until reachability is independently
  confirmed.
- **Netherlands — data.overheid.nl** — the CKAN API IS reachable and returns
  `"success": true` (confirmed live, unlike Germany/Australia above), but the
  specific query tried (`energie+efficiency`) returned **0 results** — either
  the search terms need adjustment (try Dutch-language terms like
  "energie-efficiëntie" or "warmtenet" for district heating) or this portal's
  index genuinely has nothing matching yet. Recommend a follow-up query pass
  with Dutch search terms before ranking this candidate either way — the API
  itself is confirmed live and keyless, which is the harder part.
- **Brazil — dados.gov.br** — the classic CKAN Action API path
  (`/api/3/action/package_search`) returned **HTTP 401 Unauthorized** this
  session, and the portal's own help article is literally titled "Como
  acessar a API do Portal de Dados Abertos com o perfil de consumidor" (how
  to access the API with a "consumer profile") — strongly suggesting Brazil's
  portal has moved away from fully-open CKAN access to a registration-gated
  model, unlike every other CKAN portal tested in this file. The help page's
  actual content (signup steps, key format) could not be extracted this
  session (JS-rendered, empty on fetch). Needs a human pass to confirm the
  registration process and whether it's free/self-serve before treating this
  as a `none`-access candidate — provisionally reclassify as likely
  `api_key`-gated, not `none`, contrary to the brief's assumption for this
  portal.

---

## Summary of proposed new/updated files

- **New file** `config/domains/supranational.yaml`: entries #1-8 (ECREEE,
  EACREEE, CCREEE, SACREEE, OLADE, Cool Coalition, Climate Change Laws of the
  World, SEforALL) join the four wave-1 entries already recommended for this
  file (IEA 4E EDNA, Energy Community, C40 Knowledge Hub, ISO/IEC 30134).
- **New `api_sources.yaml` entries** (tier-c, hold for client-build): #9-10
  (Climate Watch NDC Content API, Eurostat REST Dissemination API) alongside
  wave-1's already-drafted `data_europa` and `oecd_sdmx`.
- **New `api_sources.yaml` entries**, Target 2 CKAN/DCAT portals #11-18 (France
  udata, Italy CKAN, Spain linked-data, Ireland CKAN, Canada CKAN, Mexico CKAN,
  US GSA-gated CKAN, UK CKAN) — recommend building ONE generic
  `ckan_action_api` client parameterized by base_url for the five plain-CKAN
  entries (Italy, Ireland, Canada, Mexico, UK) rather than five bespoke
  clients, since they share an identical request/response shape; France
  (udata) and Spain (linked-data-api) and the US (GSA-gated) each need their
  own client due to genuinely different API shapes/auth.
- Region-value gaps to flag alongside wave-1's existing "supranational"/
  "global" recommendation: Caribbean/CARICOM has no `VALID_REGIONS` bucket
  (CCREEE mapped to the imperfect `north_america`); ECOWAS/EAC/SADC have no
  sub-Saharan-regional buckets narrower than `africa` (acceptable per the
  existing RCREEE/AFREC precedent, which used the same broad bucket).
