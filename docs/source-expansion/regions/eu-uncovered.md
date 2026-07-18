# Source Expansion Research — EU Uncovered Countries (Central/Eastern/Baltic/Balkan) + Pan-EU APIs

Region assignment: Slovakia, Slovenia, Croatia, Bulgaria, Lithuania, Latvia, Cyprus, Malta,
Serbia, Ukraine — plus pan-EU structured APIs beyond EUR-Lex NIM. Finland/Norway/Iceland are
covered by a separate Nordics agent and are NOT included here.

Dedup check performed against `config/domains/eu.yaml` and `config/domains/api_sources.yaml`
before researching. No `base_url` collisions found — all candidates below are net-new. No
EUR-Lex NIM tracker re-proposed. Existing structured clients (riksdagen, uk_bills, legisinfo,
folketing, eurlex_nim, legiscan, govinfo, regulations_gov, dip) not re-proposed.

All entries are draft-only: `enabled: false` when added to config. Branch:
`feature/source-expansion-research`.

---

## Verified candidates (ranked best-first)

### 1. European Parliament Open Data API v2 (pan-EU)

- **id**: `europarl_opendata_api` (proposed)
- **base_url**: `https://data.europarl.europa.eu`
- **level**: supranational
- **access**: none (no key; rate-limited to 500 requests / 5 minutes)
- **source_type feasibility**: needs a **new** client (tier c) — REST/OpenAPI 3 (OAS3) v2,
  responses in JSON-LD/RDF (Turtle also available). Key endpoints: `/api/v2/documents`,
  `/api/v2/meps`, `/api/v2/controlled-vocabularies/{vocId}`, plenary/committee/question
  documents, adopted texts (resolutions, legislative acts, opinions).
- **coverage**: `region: [eu]`, `category: legislative`, `tags: [mandates, research]`,
  `policy_types: [directive, law, report]`. Language: en (+ all EU languages via
  multilingual metadata). Would let us query EP legislative procedures, committee reports,
  and adopted texts touching the Energy Efficiency Directive, the Data Centre Delegated
  Regulation, and any follow-on Data Centre Energy Efficiency Package — i.e. the
  parliamentary process feeding the EUR-Lex outputs we already track.
- **format**: JSON-LD / RDF (Turtle)
- **practical**: docs at `/en/developer-corner/opendata-api`; rate limit 500 req/5 min;
  release notes at `/release-notes`; portal went live Q4 2022, API v2 is current stable.
- **effort tier**: (c) — needs new client, but well-documented OpenAPI 3 spec makes this a
  reasonably scoped build.
- **why worth adding**: only pan-EU source that exposes the *legislative process itself*
  (amendments, committee reports, plenary votes) rather than just final law text — catches
  proposed changes to data-center/heat-reuse rules before they hit EUR-Lex.
- **verified**: yes. Fetched `https://data.europarl.europa.eu/api/v2/documents?limit=1` via
  curl — returned live RDF/XML with a real EP document (`eli:Work` for
  `A-10-0034-0034-AM-001-001`). Also fetched developer-corner docs confirming endpoint list,
  OAS3 basis, and rate limit via search-engine cache (direct WebFetch of the docs page
  itself returned empty content, so docs URL is in the "needs human recheck" list below,
  but the API itself is confirmed live).

### 2. EU Open Data Portal (data.europa.eu) Search API (pan-EU)

- **id**: `data_europa_eu_search_api` (proposed)
- **base_url**: `https://data.europa.eu`
- **level**: supranational
- **access**: none — read-only, no key
- **source_type feasibility**: needs a **new** client (tier c). Confirmed endpoints:
  Search API `https://data.europa.eu/api/hub/search/`, SPARQL endpoint
  `https://data.europa.eu/sparql`, Registry API `https://data.europa.eu/api/hub/repo/`.
- **coverage**: `region: [eu]`, `category: legislative`, `tags: [reporting, research]`,
  `policy_types: [report, guidance]`. Aggregates open datasets from all 27 member states
  (1,015,339+ datasets indexed at verification time) including national energy-efficiency
  and municipal energy datasets.
- **format**: JSON (search API), RDF/SPARQL
- **practical**: no auth; can filter by country + category, e.g. energy datasets from
  Ireland's CSO, Belgian municipal energy indicators, etc. Query syntax for
  policy-domain filtering needs its own scoping.
- **effort tier**: (c) — new client; a thin wrapper around the search API is
  straightforward, but the taxonomy mapping (dataset "categories" -> our `policy_types`)
  needs design work.
- **why worth adding**: single query surface across every EU member state's open-data
  catalog — a fallback discovery layer for any of the 10 target countries whose national
  agencies don't have direct APIs (which is most of them here).
- **verified**: yes. Fetched
  `https://data.europa.eu/api/hub/search/search?q=district+heating` — returned HTTP 200
  with valid JSON (`result.count`, `result.results[]` with `identifier`, `title`,
  `description`, `distributions`, `publisher`).

### 3. Croatia — Ministry of Physical Planning, Construction and State Assets: Energy Efficiency in Buildings Regulations

- **id**: `mpgi_hr_energy_efficiency` (proposed)
- **base_url**: `https://mpgi.gov.hr`
- **start_paths**: `/about-the-ministry-139/scope-of-the-ministry/energy-efficiency-in-the-buildings-sector/regulations-in-the-field-of-energy-efficiency-8679/8679`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, croatia]`, `category: standards`,
  `tags: [mandates, efficiency]`, `policy_types: [law, regulation, standard]`. Language: hr
  (some EN summaries).
- **format**: HTML with linked PDFs (Official Gazette laws/ordinances)
- **practical**: no robots.txt issue observed; static government content, low update
  frequency (legislative amendments).
- **effort tier**: (b) plain crawl domain — file this under a new `croatia.yaml`.
- **why worth adding**: directly lists Croatia's Energy Efficiency Act (OG 127/14, 116/18,
  25/20, 41/21), the Building Act, the "Technical regulation on energy economy and heat
  retention in buildings," and transposition of EPBD (EU) 2024/1275 — exactly the
  building/efficiency mandate layer our taxonomy targets.
- **verified**: yes. Fetched directly — confirmed live page listing the Energy Efficiency
  Act, Building Act, multiple ordinances (energy audits/certification, renewable installer
  certification), long-term renovation strategy to 2050, and EPBD reference.

### 4. Croatia — Croatian Energy Regulatory Agency (HERA)

- **id**: `hera_hr` (proposed)
- **base_url**: `https://www.hera.hr`
- **start_paths**: `/en/html/index.html`, `/en/html/activities.html`, `/en/html/eu_lex.html`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, croatia]`, `category: district_heating`,
  `tags: [mandates, reporting]`, `policy_types: [regulation, guidance]`. Language: en/hr.
- **format**: HTML + PDF decisions
- **practical**: publishes dated regulatory decisions (e.g. district heating discount/
  multiplier/seasonal-factor decisions) and an EU-legislation cross-reference page.
- **effort tier**: (b) plain crawl — append to new `croatia.yaml`.
- **why worth adding**: HERA is Croatia's independent energy regulator and the direct
  authority for district-heating tariff/pricing decisions — a heat-network regulator entry
  the region was missing entirely.
- **verified**: yes. Confirmed live homepage with a dated 2026 district-heating decision
  PDF, news archive, and an EU-legislation ("eu_lex") cross-reference section.

### 5. Croatia — Ministry of Economy (mingo.gov.hr)

- **id**: `mingo_gov_hr` (proposed)
- **base_url**: `https://mingo.gov.hr`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, croatia]`, `category: energy_ministry`,
  `tags: [mandates, planning]`, `policy_types: [law, guidance]`. Language: hr (no English
  version found on the main site).
- **format**: HTML
- **practical**: note the domain moved: `mzozt.gov.hr` (Environmental Protection ministry
  — do NOT use, wrong ministry, handles nature/habitat protection only) → the energy
  portfolio actually sits at `mingo.gov.hr` (redirected from a since-abandoned
  `mingor.gov.hr`), under an "Uprava za energetiku" (Energy Directorate) section.
- **effort tier**: (b) plain crawl, but needs a human pass to pick exact `start_paths`
  under the Energy Directorate before enabling — homepage only was verified, not the
  directorate's specific policy subpages.
- **why worth adding**: primary national energy ministry for Croatia.
- **verified**: partial. Confirmed the corrected base_url resolves (301 mingor.gov.hr ->
  mingo.gov.hr, 200 OK) and that an "Uprava za energetiku" section exists in the site nav.
  Have NOT yet located/verified the specific energy-efficiency or district-heating policy
  subpage — flagged in the unverified section for a human to pick exact start_paths.

### 6. Slovenia — Portal Energetika

- **id**: `energetika_portal_si` (proposed)
- **base_url**: `https://www.energetika-portal.si`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, slovenia]`, `category: energy_ministry`,
  `tags: [incentives, efficiency, mandates]`, `policy_types: [guidance, report, regulation]`.
  Language: sl.
- **format**: HTML
- **practical**: run directly by the Ministry for Infrastructure and Energy's Energy
  Directorate; covers building renovation grants (e.g. EUR 92.7M public-building program),
  renewables, gas/fuel pricing.
- **effort tier**: (b) plain crawl — new `slovenia.yaml`.
- **why worth adding**: Slovenia's central energy-policy news/document hub, ministry-run,
  directly covers energy-efficiency incentive programs.
- **verified**: yes. Fetched directly — confirmed ministry ownership (footer: Direktorat za
  energijo, Ministry for Infrastructure and Energy) and live content on building renovation
  funding and renewables.

### 7. Slovenia — Ministry of the Environment, Climate and Energy: Energy Directorate

- **id**: `gov_si_energy_directorate` (proposed)
- **base_url**: `https://www.gov.si`
- **start_paths**: `/en/state-authorities/ministries/ministry-of-the-environment-climate-and-energy/about-the-ministry/direktorat-za-energijo/`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, slovenia]`, `category: energy_ministry`,
  `tags: [mandates, efficiency, planning]`, `policy_types: [guidance, regulation]`.
  Language: en/sl.
- **format**: HTML
- **practical**: note the ministry's general "about-the-ministry" landing page is
  environment/climate-only (no energy content) — the Energy Directorate lives at this
  specific sub-path, confirmed separately.
- **effort tier**: (b) plain crawl — new `slovenia.yaml`.
- **why worth adding**: official Slovenian ministry page for the unit that implements
  national energy-efficiency and renewable-energy incentive programs.
- **verified**: yes. Fetched the Energy Directorate sub-path directly — confirmed content
  on national energy programs, energy-efficiency/RES policy coordination.

### 8. Slovenia — Agencija za energijo (Slovenian Energy Agency)

- **id**: `agen_rs_si` (proposed)
- **base_url**: `https://www.agen-rs.si`
- **start_paths**: `/web/en/about-the-agency`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, slovenia]`, `category: district_heating`,
  `tags: [mandates, reporting]`, `policy_types: [regulation]`. Language: en/sl.
- **format**: HTML
- **practical**: independent regulator, funded via network charges (not state budget).
- **effort tier**: (b) plain crawl.
- **why worth adding**: national regulator explicitly confirmed to regulate "heating and
  other energy gases" — the heat-network regulator entry for Slovenia.
- **verified**: yes. Fetched directly — confirmed regulatory mandate over heating-sector
  operators.

### 9. Slovenia — ARSO Environmental Indicators (district heating efficiency)

- **id**: `arso_kazalci_district_heating` (proposed)
- **base_url**: `https://kazalci.arso.gov.si`
- **start_paths**: `/en/content/share-heat-produced-energy-efficient-district-heating-systems`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, slovenia]`, `category: environmental_agency`,
  `tags: [efficiency, research]`, `policy_types: [report]`. Language: en/sl.
- **format**: HTML with exportable data tables (per-indicator "Export Table Data")
- **practical**: Slovenian Environment Agency (ARSO), data compiled with the Jožef Stefan
  Institute Energy Efficiency Centre; indicator PO28 specifically tracks % of heat from
  efficient DH systems and waste-heat/RES share.
- **effort tier**: (b) plain crawl.
- **why worth adding**: rare case of a government source publishing actual structured
  waste-heat-share numbers (87% efficient DH, ~21% RES+waste-heat in 2022) with exportable
  tables — good ground-truth data alongside the policy text elsewhere.
- **verified**: yes. Fetched directly — confirmed indicator PO28 data, export buttons, and
  2024-02-01 update date.

### 10. Bulgaria — Sustainable Energy Development Agency (SEDA, formerly EEA)

- **id**: `seea_government_bg` (proposed)
- **base_url**: `https://www.seea.government.bg`
- **start_paths**: `/en/`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, bulgaria]`, `category: energy_ministry`,
  `tags: [mandates, efficiency, reporting]`, `policy_types: [law, guidance, report]`.
  Language: en/bg.
- **format**: HTML
- **practical**: executive agency within the Ministry of Energy; runs Bulgaria's National
  Information System for energy-efficiency reporting.
- **effort tier**: (b) plain crawl — new `bulgaria.yaml`.
- **why worth adding**: Bulgaria's dedicated energy-efficiency implementation agency —
  administers the national efficiency-obligation scheme that would cover any Bulgarian
  data-center EED Article 12 reporting.
- **verified**: yes (home page only). Fetched `/en/` directly — confirmed agency mandate.
  The deeper `/en/about-seda-en` subpage returned a TLS certificate error on fetch; flagged
  below for a human recheck, not used as the verified start_path.

### 11. Bulgaria — Energy and Water Regulatory Commission (EWRC / KEVR)

- **id**: `dker_bg` (proposed)
- **base_url**: `https://www.dker.bg`
- **start_paths**: `/en/home.html`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, bulgaria]`, `category: district_heating`,
  `tags: [mandates, reporting]`, `policy_types: [regulation, law]`. Language: en/bg.
- **format**: HTML + PDF
- **practical**: independent, reports to Parliament; publishes directives, regulations,
  laws, resolutions, and REMIT compliance documents; dedicated heat-energy sector page.
- **effort tier**: (b) plain crawl.
- **why worth adding**: Bulgaria's heat-network/tariff regulator — direct source for
  district-heating pricing rules and licensing decisions.
- **verified**: yes. Fetched directly — confirmed sector pages (electricity, heat energy,
  gas, water) and a "Documents" section with directives/regulations/laws/resolutions.

### 12. Bulgaria — Ministry of Energy

- **id**: `me_government_bg` (proposed)
- **base_url**: `https://www.me.government.bg`
- **start_paths**: `/en/`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, bulgaria]`, `category: energy_ministry`,
  `tags: [mandates, planning]`, `policy_types: [law, guidance]`. Language: en/bg.
- **format**: HTML
- **practical**: main visible content at verification time was nuclear/renewables/
  restructuring news; efficiency-specific subpages not yet located.
- **effort tier**: (b) plain crawl — homepage confirmed, deeper efficiency/DH-specific
  paths need a follow-up pass.
- **why worth adding**: primary national ministry of record for Bulgaria.
- **verified**: yes (homepage; confirmed "Ministry of Energy of the Republic of Bulgaria"
  branding and live navigation). Specific efficiency/DH document paths not yet confirmed —
  noted for human follow-up.

### 13. Latvia — Public Utilities Commission (SPRK) — District Heating

- **id**: `sprk_gov_lv` (proposed)
- **base_url**: `https://www.sprk.gov.lv`
- **start_paths**: `/en/content/district-heating`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, latvia]`, `category: district_heating`,
  `tags: [mandates, reporting]`, `policy_types: [regulation]`. Language: en/lv.
- **format**: HTML
- **practical**: regulates heat supply above 5000 MWh/year; ~100 regulated companies,
  62 urban areas, ~93% market coverage, ~5.5 TWh/year regulated.
- **effort tier**: (b) plain crawl — new `latvia.yaml`.
- **why worth adding**: Latvia's heat-network regulator with genuinely detailed, current
  scope-of-regulation content (concrete thresholds and market-coverage numbers).
- **verified**: yes. Fetched directly — confirmed the 5000 MWh/year threshold, ~100
  companies, 62 urban areas, and regulatory scope description.

### 14. Latvia — Ministry of Climate and Energy

- **id**: `em_gov_lv` (proposed)
- **base_url**: `https://www.em.gov.lv`
- **start_paths**: `/en/`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, latvia]`, `category: energy_ministry`,
  `tags: [mandates, planning, efficiency]`, `policy_types: [guidance, regulation]`.
  Language: en/lv.
- **format**: HTML
- **practical**: ministry reorganized Jan 2023 (merged energy functions from the old
  Ministry of Economics with climate functions from Environmental Protection/Regional
  Development); site is mid-transition — some climate content still lives on
  `www.varam.gov.lv` rather than `em.gov.lv`. Use `em.gov.lv` as the primary base_url for
  the energy side.
- **effort tier**: (b) plain crawl.
- **why worth adding**: Latvia's national energy ministry, explicitly tasked with
  promoting waste-heat recovery in district heating/cooling per its NECP.
- **verified**: yes. Fetched directly (via a related news article on the same domain) —
  confirmed ministry structure and mandate. Home page navigation not separately re-fetched;
  low risk since the domain and organizational facts are corroborated by multiple sources.

### 15. Serbia — Energy Agency of the Republic of Serbia (AERS)

- **id**: `aers_rs` (proposed)
- **base_url**: `http://www.aers.rs`
- **start_paths**: `/laws`, `/regulations`, `/secondary-legislation`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, serbia]`, `category: regulatory`,
  `tags: [mandates, efficiency]`, `policy_types: [law, regulation]`. Language: en/sr.
  (Serbia is not an EU member but is an Energy Community Contracting Party transposing EU
  energy acquis — tagged `eu` for policy-alignment purposes per this region's remit.)
- **format**: HTML + PDF
- **practical**: site is plain HTTP (no HTTPS) at the verified URL — note for crawler TLS
  config.
- **effort tier**: (b) plain crawl — new `serbia.yaml`.
- **why worth adding**: Serbia's energy regulator, explicit "Laws" and "Secondary
  Legislation" sections covering the Energy Law and the Law on Energy Efficiency and
  Rational Use of Energy.
- **verified**: yes. Fetched `/laws` directly — confirmed live listing (Energy Law No.
  145/14 & 95/18, Pipeline Transportation Law, Planning and Construction Law, etc.).

### 16. Serbia — Ministry of Mining and Energy

- **id**: `mre_gov_rs` (proposed)
- **base_url**: `https://mre.gov.rs`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, serbia]`, `category: energy_ministry`,
  `tags: [mandates, incentives, efficiency]`, `policy_types: [law, guidance]`.
  Language: en/sr.
- **format**: HTML + PDF
- **practical**: has a dedicated "Sector for Energy Efficiency and Climate Change" and an
  internal "Energy Portal" link; references district-heating building-renovation programs
  (SURCE project).
- **effort tier**: (b) plain crawl.
- **why worth adding**: Serbia's national energy ministry — Law on Energy Efficiency and
  Rational Use of Energy (2021) originates here.
- **verified**: yes. Fetched directly — confirmed sector pages and district-heating
  building-renovation program reference. Exact start_paths for the efficiency sector need
  a follow-up pass (Cyrillic/Latin URL variants observed).

### 17. Ukraine — National Energy and Utilities Regulatory Commission (NEURC)

- **id**: `nerc_gov_ua` (proposed)
- **base_url**: `https://www.nerc.gov.ua`
- **start_paths**: `/en`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, ukraine]`, `category: district_heating`,
  `tags: [mandates, reporting]`, `policy_types: [regulation]`. Language: en/uk. (Ukraine is
  an EU candidate country transposing the Energy Community/EU acquis — tagged `eu` for
  policy-alignment purposes.)
- **format**: HTML + PDF (resolutions, orders)
- **practical**: site blocks generic bot user-agents (curl got HTTP 403) but resolves fine
  through a browser-rendering fetch — crawler will likely need `requires_playwright: true`
  or a realistic user-agent header.
- **effort tier**: (b) plain crawl (with Playwright) — new `ukraine.yaml`.
- **why worth adding**: Ukraine's heat-sector regulator, dedicated "Heat" (Тепло) section
  covering consumer regulations, supplier licensing, and "stimulative regulation" for
  district heating — directly on-topic and previously uncovered.
- **verified**: yes, via rendered fetch. Confirmed live "Heat" regulatory section,
  resolutions/orders archive. Plain curl returned 403 (bot-blocked, not evidence the site
  is down) — noted as a practical/crawler-config caveat, not a verification failure.

### 18. Ukraine — Ministry of Energy

- **id**: `mev_gov_ua` (proposed)
- **base_url**: `https://www.mev.gov.ua`
- **start_paths**: `/en`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, ukraine]`, `category: energy_ministry`,
  `tags: [mandates, efficiency]`, `policy_types: [regulation, guidance]`. Language: en/uk.
- **format**: HTML
- **practical**: dedicated "Energy Efficiency" (Енергоефективність) nav section with
  news/regulatory-acts subsections; no dedicated district-heating section found (heat
  falls to NEURC + the Ministry for Communities and Territories Development instead).
- **effort tier**: (b) plain crawl.
- **why worth adding**: Ukraine's national energy ministry, active energy-efficiency
  regulatory-acts publisher, directly relevant given the country's ongoing district-heating
  reform legislation (draft law No. 14067, passed second reading in parliament).
- **verified**: yes. Fetched directly — confirmed live energy-efficiency nav section.

### 19. Ukraine — Verkhovna Rada (Parliament) Open Data Portal

- **id**: `rada_opendata_ua` (proposed)
- **base_url**: `https://data.rada.gov.ua`
- **level**: national
- **access**: none (Creative Commons; no key)
- **source_type feasibility**: needs a **new** client (tier c). API section confirmed at
  `/open/main/en/api`; datasets cover legislation ("Normative-legal base of Ukraine"),
  agenda items, registered bills, and MP data.
- **coverage**: `region: [eu, ukraine]`, `category: legislative`,
  `tags: [mandates]`, `policy_types: [law, legislation]`. Language: en/uk.
- **format**: structured data via API (format not fully confirmed — needs a follow-up
  fetch of the `/open/main/en/api` page itself)
- **practical**: portal explicitly labeled "in test operation mode" — schema may still
  change; built jointly by the Rada apparatus, OPORA, the e-governance agency, and UNDP
  Ukraine.
- **effort tier**: (c) new client.
- **why worth adding**: would let us track Ukraine's district-heating reform bill (and any
  future data-center/efficiency legislation) through the bill-registration dataset rather
  than only reading finished law text.
- **verified**: partial. Fetched the portal's `/open/main/en/` landing page directly —
  confirmed the four dataset categories and an `/open/main/en/api` link, but did not fetch
  the API sub-page itself to confirm request/response format. Flagged below for one more
  verification pass before building a client.

### 20. Cyprus — Energy Service, Ministry of Energy, Commerce and Industry

- **id**: `energy_gov_cy` (proposed)
- **base_url**: `https://www.energy.gov.cy`
- **start_paths**: `/en/`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, cyprus]`, `category: energy_ministry`,
  `tags: [mandates, efficiency, incentives]`, `policy_types: [law, guidance]`.
  Language: en/el.
- **format**: HTML
- **practical**: legal basis is the Energy Efficiency Laws of 2009–2021 plus secondary
  legislation, per the site's own framing.
- **effort tier**: (b) plain crawl — new `cyprus.yaml`.
- **why worth adding**: Cyprus's national energy-efficiency policy authority; no
  data-center-specific content found yet, but this is the correct ministry for any future
  EED Article 12/26 transposition.
- **verified**: yes. Fetched directly — confirmed ministry mandate and legal-basis
  statement.

### 21. Cyprus — data.gov.cy Open Data Portal (Ministry of Energy group + DKAN API)

- **id**: `data_gov_cy_energy` (proposed)
- **base_url**: `https://data.gov.cy`
- **start_paths**: `/en/group/29`
- **level**: national
- **access**: none
- **source_type feasibility**: needs a **new** client (tier c) — platform is DKAN (not
  CKAN), exposing a "Dataset REST API" and a "Datastore API" per the portal's own developer
  page.
- **coverage**: `region: [eu, cyprus]`, `category: legislative`,
  `tags: [reporting]`, `policy_types: [report]`. Language: en/el.
- **format**: JSON (DKAN REST)
- **practical**: developer docs point out to external DKAN documentation rather than
  hosting full endpoint specs in-portal — a client would need to consult upstream DKAN API
  docs.
- **effort tier**: (c) new client.
- **why worth adding**: government-run open-data catalog specifically grouped by
  publishing ministry, letting us pull Cyprus energy datasets without a bespoke scraper.
- **verified**: yes. Fetched both `/en/group/29` (confirmed Ministry of Energy, Commerce
  and Industry group) and `/en/support-developers` (confirmed DKAN REST + Datastore API
  references) directly.

### 22. Malta — Energy and Water Agency (EWA)

- **id**: `energywateragency_gov_mt` (proposed)
- **base_url**: `https://energywateragency.gov.mt`
- **start_paths**: `/energy-efficiency/`, `/2030-necp/`, `/schemes-1/`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, malta]`, `category: energy_ministry`,
  `tags: [incentives, efficiency, mandates]`, `policy_types: [guidance, incentive]`.
  Language: en.
- **format**: HTML
- **practical**: page explicitly confirms Malta has **no district-heating/cooling
  networks** (island grid) — do not tag `district_heating`; this source is relevant only
  for the data-center-energy-efficiency/EED-audit-obligation angle (>10 TJ consumption
  triggers mandatory audits per Directive (EU) 2023/1791 Art. 11, per the page).
  Value is specifically the data-center/large-consumer efficiency-mandate angle, not heat
  reuse.
- **effort tier**: (b) plain crawl — new `malta.yaml`.
- **why worth adding**: national energy-efficiency authority; directly cites the EED
  Article 11 large-consumer audit obligation relevant to data centers.
- **verified**: yes. Fetched directly — confirmed EED Art. 11 (>10TJ) audit-obligation
  language and explicit "no district heating/cooling networks" statement.

### 23. Malta — Regulator for Energy and Water Services (REWS)

- **id**: `rews_org_mt` (proposed)
- **base_url**: `https://www.rews.org.mt`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, malta]`, `category: regulatory`,
  `tags: [mandates, incentives]`, `policy_types: [regulation, incentive]`. Language: en.
- **format**: HTML + PDF
- **practical**: publishes legislation, decision notices, consultations, and support
  schemes (e.g. Heat Pump Water Heater Scheme); no data-center-specific content found.
- **effort tier**: (b) plain crawl.
- **why worth adding**: Malta's energy/water regulator — completes the ministry+regulator
  pair for the country.
- **verified**: yes. Fetched directly — confirmed legislation/decision-notice/scheme
  sections.

### 24. Slovakia — Ministry of Economy (MHSR)

- **id**: `economy_gov_sk` (proposed)
- **base_url**: `https://www.economy.gov.sk`
- **start_paths**: `/en/ministry`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, slovakia]`, `category: energy_ministry`,
  `tags: [mandates, planning]`, `policy_types: [law, guidance]`. Language: en/sk.
- **format**: HTML
- **practical**: `mhsr.sk` now redirects/aliases to `economy.gov.sk`; use the latter as
  base_url. Site has a dedicated "Energy" nav item but efficiency/DH-specific subpages not
  yet located.
- **effort tier**: (b) plain crawl — new `slovakia.yaml`.
- **why worth adding**: Slovakia's national energy ministry, responsible for the energy-
  efficiency action plan and district-heating-relevant CHP tenders per prior research.
- **verified**: yes (homepage/ministry page). Fetched directly — confirmed live "Energy"
  nav section. Deeper efficiency-specific paths not yet confirmed (follow-up needed).

### 25. Slovakia — Regulatory Office for Network Industries (ÚRSO) — District Heating

- **id**: `urso_gov_sk` (proposed)
- **base_url**: `https://www.urso.gov.sk`
- **start_paths**: `/district-heating/`, `/legislation/`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, slovakia]`, `category: district_heating`,
  `tags: [mandates, reporting]`, `policy_types: [regulation]`. Language: sk only on the
  actual documents (page chrome is bilingual en/sk).
- **format**: HTML + XLS (price-calculation annexes to Decree No. 248/2016 Coll.)
- **practical**: page states explicitly the annex documents are "available in Slovak
  language only" — no English document set; low priority relative to other sources unless
  a Slovak-language keyword pass is added.
- **effort tier**: (b) plain crawl, lower priority given the language/format barrier
  (spreadsheet annexes, not prose policy text).
- **why worth adding**: still the only heat-network regulator entry for Slovakia; rounds
  out ministry+regulator coverage even though the specific documents found are compliance
  forms rather than narrative policy.
- **verified**: yes. Fetched `/district-heating/` directly — confirmed 21 XLS annexes tied
  to Decree No. 248/2016 Coll. and the Slovak-only caveat.

### 26. Lithuania — National Energy Regulatory Council (VERT)

- **id**: `vert_lt` (proposed)
- **base_url**: `https://www.vert.lt`
- **start_paths**: `/en/Pages/prices.aspx`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, lithuania]`, `category: district_heating`,
  `tags: [mandates, reporting]`, `policy_types: [regulation]`. Language: en/lt.
- **format**: HTML
- **practical**: **site returns HTTP 403 to both curl and the WebFetch tool** — it is
  real and content-bearing (confirmed via search-engine cache/snippet showing live district
  -heating price data and contact details), but blocks this session's automated fetchers,
  likely on user-agent/bot-detection grounds. A production crawler with a normal browser
  user-agent (or `requires_playwright: true`) should get through; a human should
  double-check before enabling.
- **effort tier**: (b) plain crawl, pending fetch-access recheck.
- **why worth adding**: Lithuania's district-heating and energy price regulator (45
  municipal/regional DH companies, >85% biomass fuel share per NERC/VERT data) — the
  heat-network regulator entry the region was missing.
- **verified**: partial — confirmed live via search snippet only; direct fetch blocked
  (403) by both curl and WebFetch in this session. Flagged in unverified section too.

### 27. Lithuania — Ministry of Energy

- **id**: `enmin_lrv_lt` (proposed)
- **base_url**: `https://enmin.lrv.lt`
- **start_paths**: `/en/`
- **level**: national
- **access**: none
- **coverage**: `region: [eu, lithuania]`, `category: energy_ministry`,
  `tags: [mandates, planning]`, `policy_types: [law, guidance]`. Language: en/lt.
- **format**: HTML
- **practical**: same caveat as VERT above — HTTP 403 to curl and WebFetch in this
  session; site's existence and ministry identity are well-corroborated by multiple
  independent sources (IEA country reports, NECP filing, government directory listings)
  but content itself was not directly inspectable this session.
- **effort tier**: (b) plain crawl, pending fetch-access recheck.
- **why worth adding**: Lithuania's national energy ministry — completes ministry+
  regulator coverage for the country.
- **verified**: no — could not fetch content directly (403 both tools). Real/live per
  third-party corroboration only. Listed here rather than purely in "unverified" because
  the domain and organizational identity are well-established, but flagged for a human to
  confirm actual page content before enabling in config.

---

## Unverified / needs-human-check

- **Bulgaria SEEA subpage** `https://www.seea.government.bg/en/about-seda-en` — TLS
  certificate error on fetch (`unable to verify the first certificate`). The parent
  `/en/` homepage verified fine; this specific subpage needs a human/browser check.
- **Croatia `mingo.gov.hr` energy-directorate subpages** — only the homepage/redirect was
  verified. Need a human pass to find and confirm the actual "Uprava za energetiku" policy
  URLs before setting `start_paths`.
- **Bulgaria Ministry of Energy (`me.government.bg`) efficiency/DH-specific paths** —
  homepage confirmed live; deeper policy subpages not yet located.
- **Serbia Ministry of Mining and Energy (`mre.gov.rs`) exact efficiency-sector URL** —
  Cyrillic/Latin URL variants observed in search results; homepage/domain confirmed, exact
  `start_paths` need confirmation.
- **Slovakia `economy.gov.sk` energy-efficiency-specific subpages** — homepage/ministry
  page confirmed; deeper efficiency/DH paths not yet located.
- **Lithuania VERT (`vert.lt`) and Ministry of Energy (`enmin.lrv.lt`)** — both return
  HTTP 403 to automated fetch (curl and WebFetch) in this session. Sites are real
  (corroborated by search snippets and third-party sources) but a human/browser session
  should confirm actual content and robots.txt before these go into a crawl config.
- **Ukraine `data.rada.gov.ua` API format** — portal and `/open/main/en/api` link
  confirmed to exist; the API sub-page's actual request/response format was not fetched
  this session. Needed before scoping a tier-c client.
- **European Parliament developer-corner docs page**
  (`https://data.europarl.europa.eu/en/developer-corner/opendata-api`) — WebFetch returned
  empty content twice (likely a JS-rendered page); the underlying API itself (item #1
  above) was independently verified via a direct curl call to a live endpoint, so this is a
  documentation-page rendering issue, not doubt about the API's existence.
- **Serbia `energetskiportal.com`** — appears to be a privately-run energy news/
  information portal (not confirmed as an official government site), despite listing real
  Serbian energy laws. Excluded from the ranked list per the brief's "not news blogs"
  guidance; noting it here in case a human judges its legislation-tracker page useful as a
  secondary/aggregator source.
- **TED (Tenders Electronic Daily, ted.europa.eu)** — considered per the brief's prompt to
  look at pan-EU structured APIs, but TED exposes procurement/tender notices, not policy
  documents (laws, regulations, directives, guidance, standards, reports) per the project's
  own definition of in-scope content. Not proposed as a candidate; noting the exclusion
  rationale so it isn't re-researched by a future pass.

---

## Suggested config file placement

- New country files: `croatia.yaml`, `slovenia.yaml`, `bulgaria.yaml`, `latvia.yaml`,
  `serbia.yaml`, `ukraine.yaml`, `cyprus.yaml`, `malta.yaml`, `slovakia.yaml`,
  `lithuania.yaml` (Lithuania currently has zero coverage; not to be confused with the
  existing `nordic.yaml`, which is Nordic-only).
- Pan-EU structured API candidates (EP Open Data API v2, data.europa.eu Search API, and —
  pending format confirmation — the Rada Open Data API) belong in
  `config/domains/api_sources.yaml` alongside the existing riksdagen/uk_bills/eurlex_nim
  entries, each requiring a new `source_type` client under `src/sources/`.
- Cyprus's `data.gov.cy` DKAN API is a national (not pan-EU) structured source; it would
  get its own `source_type` (e.g. `dkan_cy`) but lives in a new `cyprus.yaml` alongside the
  crawl-domain entry for `energy.gov.cy`.
