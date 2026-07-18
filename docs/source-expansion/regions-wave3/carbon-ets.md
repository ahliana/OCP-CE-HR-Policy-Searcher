# Wave 3 — Carbon Pricing / Emissions Trading / Climate-Compliance Bodies

Scope: government carbon-pricing, ETS, and emissions-registry bodies, plus mandatory
corporate GHG/energy reporting schemes that bind data-center energy and emissions.
Net-new only — dedup checked against `config/domains/*.yaml` (all 34 files, incl.
`us/*.yaml`), `docs/source-expansion/draft/crawl/**/*.yaml`,
`docs/source-expansion/draft/new-clients.md` + `new-clients-wave2.md`, and every
`docs/source-expansion/regions-wave2/*.md`. 227 crawl domains + 9 APIs already ship;
none of them are ETS/carbon-pricing-authority bodies. A few base_urls below are
already used by an *unrelated* page on the same domain (e.g. `ww2.arb.ca.gov`,
`meti.go.jp`, `bafu.admin.ch`, `alberta.ca`, `gov.uk`, `environnement.gouv.qc.ca` vs.
the sibling `transitionenergetique.gouv.qc.ca`) — same precedent as the existing
`eur-lex.europa.eu` (4 entries) and `gov.uk` (30+ entries) reuse pattern already in
the codebase. Each such case is called out explicitly below with the existing
sibling id so it's clear this is an addition, not a duplicate.

Every URL below was fetched live this session (`curl -L` with a browser
User-Agent, cross-checked with WebFetch/WebSearch where a bot-block required it).
Exact HTTP results are noted per entry.

---

## Verified candidates (ranked best-first)

### 1. `eu_ets_main` — EU Emissions Trading System (European Commission, DG CLIMA)
- **name**: EU Emissions Trading System (EU ETS)
- **base_url**: `https://climate.ec.europa.eu`
- **start_paths**: `/eu-action/eu-emissions-trading-system-eu-ets_en`
- **level**: supranational
- **access**: none
- **coverage**: the flagship EU carbon market — power/heat generation, energy-
  intensive industry, aviation; from 2027 EU ETS2 extends carbon pricing to
  buildings, road transport and additional fuel-combustion sectors (data-center
  grid electricity in ETS-covered member states is priced indirectly through
  generator compliance costs; large on-site combustion at a DC would fall
  directly under scope). `region: ["eu"]`, `category: "environmental_agency"`,
  `tags: ["carbon", "mandates", "reporting"]`, `policy_types: ["regulation",
  "directive", "guidance"]`, `language: en` (all EU languages available via
  `_xx` suffix).
  Distinct from the existing `ec_energy_datacentres`/`jrc_coc_datacentres`
  entries in `eu.yaml` (those are EED-driven efficiency/reporting rules on
  `energy.ec.europa.eu` and `joint-research-centre.ec.europa.eu` — different
  subdomain, different legal instrument, no ETS content).
- **format**: HTML + linked PDF (Directive 2003/87/EC consolidated text, annual
  reports)
- **practical**: no rate limit observed; `requires_playwright` not needed
  (plain HTML). Page is a hub — recommend `max_depth: 2` to reach the "Scope of
  the EU ETS" and "Union Registry" sub-pages.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: the single largest carbon market bound to affect
  EU electricity prices data centers pay, and the legal basis for EU ETS2
  (below) and the Union Registry (below).
- **verified**: yes. `curl -L` → HTTP 200. WebFetch confirmed page content is
  the DG CLIMA EU ETS hub page (background, caps, revenue use, monitoring/
  verification, international carbon markets sections); noted the detailed
  sector-scope table lives one click deeper on a linked "Scope of the EU ETS"
  page (not separately fetched this session).

---

### 2. `eu_ets2_buildings_transport` — EU ETS2 (Buildings, Road Transport, Additional Sectors)
- **name**: EU ETS2 — Buildings, Road Transport and Additional Sectors
- **base_url**: `https://climate.ec.europa.eu`
- **start_paths**: `/eu-action/eu-emissions-trading-system-eu-ets/ets2-buildings-road-transport-and-additional-sectors_en`
- **level**: supranational
- **access**: none
- **coverage**: new (2027-effective) EU carbon-pricing scheme covering fuel
  combustion in buildings, road transport, and other sectors not in EU ETS1 —
  directly prices the fossil-fuel heating/backup-generation side of data
  centers in scope member states. `region: ["eu"]`, `category:
  "environmental_agency"`, `tags: ["carbon", "mandates"]`, `policy_types:
  ["regulation", "directive"]`, `language: en`.
- **format**: HTML
- **practical**: same host/rate profile as #1; note the correct slug is
  `ets2-...` not `eu-ets2-...` (a naive guess 404s).
- **effort tier**: (b)
- **why worth adding**: this is the scheme most likely to newly bind
  data-center on-site fossil combustion (backup generation, gas heating) that
  EU ETS1 never covered.
- **verified**: yes. `curl -L` → HTTP 200 (after correcting the slug from an
  initial 404 on a guessed URL).

---

### 3. `eu_ets_union_registry` — EU ETS Union Registry
- **name**: EU ETS Union Registry
- **base_url**: `https://climate.ec.europa.eu`
- **start_paths**: `/eu-action/eu-emissions-trading-system-eu-ets/union-registry_en`
- **level**: supranational
- **access**: none (the registry account/transaction system itself needs
  login; this page is the public-facing description + links to public data)
- **coverage**: the account/allowance-tracking system of record for EU ETS —
  publishes verified emissions and allocation data per installation.
  `region: ["eu"]`, `category: "environmental_agency"`, `tags: ["carbon",
  "reporting"]`, `policy_types: ["regulation", "report"]`, `language: en`.
- **format**: HTML (page) linking to downloadable installation-level data
- **practical**: no rate limit observed.
- **effort tier**: (b) for this page; the underlying registry transaction data
  is a candidate tier-c open-data API for a later pass (not scoped/tested this
  session — flagging for follow-up, not proposing as a client yet).
- **why worth adding**: facility-level EU ETS allocation/emissions data,
  useful to cross-reference any EU data-center operator with on-site
  combustion covered installations.
- **verified**: yes. `curl -L` → HTTP 200.

---

### 4. `eurlex_csrd_2022_2464` — EU Corporate Sustainability Reporting Directive
- **name**: EUR-Lex Corporate Sustainability Reporting Directive (CSRD) 2022/2464
- **base_url**: `https://eur-lex.europa.eu`
- **start_paths**:
  - `/eli/dir/2022/2464/oj/eng`
  - `/legal-content/EN/TXT/HTML/?uri=CELEX:32022L2464`
- **level**: supranational
- **access**: none
- **coverage**: mandatory sustainability reporting (via ESRS, incl. ESRS E1
  Climate Change — energy consumption/mix and GHG Scope 1/2/3 disclosure) for
  large EU companies and listed SMEs; directly captures large data-center
  operators/colocation groups headquartered or operating in the EU.
  `region: ["eu"]`, `category: "legislation"`, `tags: ["reporting",
  "mandates", "carbon"]`, `policy_types: ["directive", "law"]`, `language: en`.
  Confirmed net-new: neither "CSRD" nor CELEX `32022L2464` appears anywhere in
  `config/domains/` or prior source-expansion docs — the existing `eu.yaml`
  EUR-Lex entries (`eurlex_eed_2023`, `eurlex_dc_regulation`,
  `eurlex_eed_recommendation`) are EED/data-centre-regulation only, not CSRD.
- **format**: HTML (consolidated directive text)
- **practical**: same eur-lex.europa.eu host already crawled 3x elsewhere in
  `eu.yaml` — no new rate-limit concern. `max_depth: 1` per existing eurlex
  pattern.
- **effort tier**: (b)
- **why worth adding**: the broadest EU mandatory climate-disclosure regime
  touching data-center corporate groups — complements the existing
  DC-specific EED/delegated-regulation entries with the company-level
  financial-reporting angle (ESRS E1 energy/emissions disclosures).
- **verified**: yes. Both `curl -L` URLs → HTTP 200.

---

### 5. `uk_ets_participating` — UK Emissions Trading Scheme (participation guidance)
- **name**: Participating in the UK Emissions Trading Scheme (UK ETS)
- **base_url**: `https://www.gov.uk`
- **start_paths**: `/government/publications/participating-in-the-uk-ets`
- **level**: national
- **access**: none
- **coverage**: UK's post-Brexit domestic carbon market (replaced UK
  participation in EU ETS from 1 Jan 2021); covers power, industry, and
  (since 2024) waste incineration, with aviation/maritime added through 2025.
  `region: ["uk"]`, `category: "environmental_agency"`, `tags: ["carbon",
  "mandates", "reporting"]`, `policy_types: ["regulation", "guidance"]`,
  `language: en`.
  `gov.uk` is already a base_url for 8+ existing `uk.yaml` entries
  (`uk_desnz`, `uk_environment_agency`, `uk_opss`, `uk_hndu`, `uk_ghnf`,
  `uk_hn_zoning`, `uk_desnz_heat_networks`, `uk_ofgem_cap`, etc.) — this is a
  new, distinct start_path/topic (carbon-market participation, not heat
  networks or efficiency funds), same reuse pattern as those entries.
- **format**: HTML + linked PDFs (allocation tables, MRR guidance)
- **practical**: no rate limit issue beyond gov.uk's existing crawl profile.
- **effort tier**: (b)
- **why worth adding**: the national ETS authority page — direct compliance
  obligations for any UK-based large energy user/generator; also the
  jumping-off point to per-installation allocation data.
- **verified**: yes. First guess (`/guidance/participating-in-the-uk-ets`)
  404'd; `curl -L` on the corrected URL → HTTP 200. WebFetch confirmed content:
  describes UK ETS scope (installations, hospitals, small/ultra-small
  emitters, aviation, and — as of July 2025 — maritime operators) and links to
  allocation tables.

---

### 6. `uk_secr` — UK Streamlined Energy and Carbon Reporting (SECR)
- **name**: Environmental Reporting Guidelines incl. Streamlined Energy and
  Carbon Reporting (SECR)
- **base_url**: `https://www.gov.uk`
- **start_paths**: `/government/publications/environmental-reporting-guidelines-including-mandatory-greenhouse-gas-emissions-reporting-guidance`
- **level**: national
- **access**: none
- **coverage**: mandatory UK energy-use and GHG disclosure in annual reports
  for quoted companies and large unquoted companies/LLPs exceeding statutory
  size thresholds (in force since April 2019) — captures large UK data-center
  operators as "large unquoted companies." `region: ["uk"]`, `category:
  "environmental_agency"`, `tags: ["reporting", "mandates", "carbon"]`,
  `policy_types: ["regulation", "guidance"]`, `language: en`.
- **format**: HTML (page) + PDF (the Environmental Reporting Guidelines
  document itself, ~150pp incl. SECR chapter)
- **practical**: same gov.uk crawl profile as #5.
- **effort tier**: (b)
- **why worth adding**: distinct from EU CSRD/ESRS — this is the UK's own
  standing mandatory energy/carbon reporting regime, predates and remains
  separate post-Brexit.
- **verified**: yes. `curl -L` → HTTP 200.

---

### 7. `uk_esos` — UK Energy Savings Opportunity Scheme (ESOS)
- **name**: Complying with the Energy Savings Opportunity Scheme (ESOS)
- **base_url**: `https://www.gov.uk`
- **start_paths**: `/guidance/energy-savings-opportunity-scheme-esos`
- **level**: national
- **access**: none
- **coverage**: mandatory energy audits every 4 years for large UK
  undertakings (250+ employees or turnover/balance-sheet thresholds) — directly
  covers large data-center operators; ESOS Phase 4 (2024) added mandatory
  net-zero action-plan reporting. `region: ["uk"]`, `category:
  "environmental_agency"`, `tags: ["mandates", "reporting", "efficiency"]`,
  `policy_types: ["regulation", "guidance"]`, `language: en`.
- **format**: HTML + PDF
- **practical**: same gov.uk profile.
- **effort tier**: (b)
- **why worth adding**: the mandatory-audit sibling to SECR — where SECR is
  disclosure, ESOS forces the underlying efficiency audit; large DC operators
  are squarely in scope.
- **verified**: yes. First guess 404'd twice; `curl -L` on the corrected slug
  → HTTP 200.

---

### 8. `de_dehst_nehs` — DEHSt National Emissions Trading (nEHS / BEHG)
- **name**: DEHSt — National Emissions Trading System (nEHS) under the Fuel
  Emissions Trading Act (BEHG)
- **base_url**: `https://www.dehst.de`
- **start_paths**: `/EN/Topics/nEHS/nehs_node.html`
- **level**: national
- **access**: none
- **coverage**: Germany's national carbon price on heating/transport fuels
  (since 2021, under BEHG), gradually merging into EU ETS2 from 2027 — DEHSt
  (housed at the German Environment Agency, UBA) is also Germany's competent
  authority for EU ETS installations. `region: ["germany", "eu"]`, `category:
  "environmental_agency"`, `tags: ["carbon", "mandates", "reporting"]`,
  `policy_types: ["regulation", "guidance"]`, `language: en` (German original
  also available, same domain).
- **format**: HTML + PDF (factsheets, sales/auction reports)
- **practical**: no rate limit observed; note `/EN/Home/home_node.html` (the
  bare homepage) also resolves but the nEHS-specific path above is the
  on-topic one — a generic `/EN/Topics/EU-ETS/eu-ets_node.html` guess 404'd.
- **effort tier**: (b)
- **why worth adding**: the German national ETS authority — BEHG carbon
  costs flow into industrial energy prices and the KTF climate fund that
  finances (per DEHSt's own page) "transformation of heating networks" —
  directly adjacent to PolicyPulse's district-heating taxonomy.
- **verified**: yes. `curl -L` → HTTP 200. WebSearch + page confirmed content:
  nEHS/BEHG mechanism description, EU ETS2 transition, KTF revenue use.

---

### 9. `ca_carb_cap_trade` — California Cap-and-Trade Program (CARB)
- **name**: California Air Resources Board — Cap-and-Trade Program
- **base_url**: `https://ww2.arb.ca.gov`
- **start_paths**: `/our-work/programs/cap-and-trade-program`
- **level**: subnational (state)
- **access**: none
- **coverage**: California's economy-wide cap-and-trade system (linked with
  Quebec's SPEDE, see #17) covering large industrial and power-sector
  emitters — directly relevant to California data centers' grid-electricity
  carbon cost pass-through and to any DC operator with large on-site
  generation. `region: ["us", "us_states", "california"]`, `category:
  "environmental_agency"`, `tags: ["carbon", "mandates", "reporting"]`,
  `policy_types: ["regulation", "report"]`, `language: en`.
  Note: `ww2.arb.ca.gov` is already a base_url in
  `config/domains/us/california.yaml` via the existing `carb_generators`
  entry (backup-generator emissions rules, a completely different
  topic/start_path) — this is a new, additive entry, not a duplicate.
- **format**: HTML + linked PDF/XLSX (allowance prices, compliance
  instrument reports)
- **practical**: plain `curl` (no User-Agent) got HTTP 403 — CARB's site
  blocks default-UA bot traffic; a browser User-Agent string resolved cleanly
  to HTTP 200. Recommend the crawler send a standard browser UA. WebFetch's
  own fetcher was also 403'd for the same reason (confirms this is a UA/bot
  check, not a dead page — curl with a spoofed UA is the only method that
  succeeded this session).
- **effort tier**: (b)
- **why worth adding**: CARB is the model program most other North American
  systems reference (RGGI, Quebec, Washington's program) — high-value,
  frequently updated (auction results, compliance data).
- **verified**: yes, with caveat. `curl -L -A "<browser UA>"` → HTTP 200.
  Default UA and WebFetch both got HTTP 403 (bot-detection, not a broken
  page) — flag `requires_playwright: true` or a custom UA header at
  crawl-config time so the production crawler doesn't silently skip this
  domain.

---

### 10. `us_rggi` — Regional Greenhouse Gas Initiative (RGGI)
- **name**: Regional Greenhouse Gas Initiative (RGGI)
- **base_url**: `https://www.rggi.org`
- **start_paths**: `/`
- **level**: subnational (multi-state — 11 Northeast/Mid-Atlantic US states)
- **access**: none
- **coverage**: the first (2009) US cap-and-invest program, covering CO2 from
  fossil power generation across 11 states — relevant to data-center
  grid-electricity carbon cost in RGGI states (NY, MA, CT, NJ, VA before its
  2023 withdrawal, etc.). `region: ["us", "us_states"]`, `category:
  "environmental_agency"`, `tags: ["carbon", "mandates", "reporting"]`,
  `policy_types: ["regulation", "report"]`, `language: en`.
- **format**: HTML + PDF/XLSX (auction results, COATS allowance-tracking
  data, model rule text, state regulations)
- **practical**: no rate limit observed.
- **effort tier**: (b)
- **why worth adding**: the multi-state carbon program covering the
  US Northeast data-center corridor (northern Virginia is technically
  outside current RGGI membership, but NY/NJ/MA capacity is directly priced).
- **verified**: yes. `curl -L` → HTTP 200. WebFetch confirmed content: 11-state
  cap-and-invest description, auction/allowance-tracking (COATS), investment
  reports.

---

### 11. `au_cer_safeguard` — Australia Safeguard Mechanism (Clean Energy Regulator)
- **name**: Safeguard Mechanism (Clean Energy Regulator, Australia)
- **base_url**: `https://cer.gov.au`
- **start_paths**: `/schemes/safeguard-mechanism`
- **level**: national
- **access**: none
- **coverage**: mandatory emissions-intensity baseline-and-credit scheme for
  facilities emitting >100,000 tCO2e/year (mining, oil & gas, manufacturing,
  transport, waste) — a large Australian data-center campus with substantial
  on-site generation could approach this threshold; more directly, it caps
  the carbon intensity of large grid-connected generators supplying DC load.
  `region: ["australia", "apac"]`, `category: "environmental_agency"`,
  `tags: ["carbon", "mandates", "reporting"]`, `policy_types: ["regulation",
  "guidance"]`, `language: en`.
- **format**: HTML + PDF (rule instruments, facility baseline data)
- **practical**: no rate limit observed.
- **effort tier**: (b)
- **why worth adding**: Australia's primary industrial carbon-pricing
  instrument; complements the existing `australia.yaml` state energy-agency
  entries (NSW/SA) with the national emissions-cap regulator.
- **verified**: yes. `curl -L` → HTTP 200. WebFetch confirmed the
  100,000 tCO2e/year threshold and covered-sector list directly from the page.

---

### 12. `au_cer_nger` — Australia National Greenhouse and Energy Reporting Scheme (NGER)
- **name**: National Greenhouse and Energy Reporting (NGER) Scheme
- **base_url**: `https://cer.gov.au`
- **start_paths**: `/schemes/national-greenhouse-and-energy-reporting-scheme`
- **level**: national
- **access**: none
- **coverage**: mandatory annual corporate GHG-emissions and energy
  consumption/production reporting for entities exceeding facility or
  corporate-group thresholds; feeds the Safeguard Mechanism, national policy,
  and (above a publication threshold) publicly published facility data.
  `region: ["australia", "apac"]`, `category: "environmental_agency"`,
  `tags: ["reporting", "mandates", "carbon"]`, `policy_types: ["regulation",
  "report"]`, `language: en`. Same `cer.gov.au` host as #11, distinct topic/
  start_path — additive, not duplicate.
- **format**: HTML + downloadable facility-level datasets (CSV/XLSX)
- **practical**: annual reporting deadline 31 October; public data release
  cadence documented on-page.
- **effort tier**: (b) crawl now; the published facility-level NGER dataset
  itself (if it has a stable machine-readable endpoint) is a tier-c follow-up
  worth scoping later.
- **why worth adding**: the underlying mandatory reporting regime that feeds
  Safeguard — this is where facility-level Australian energy/emissions data
  (potentially including large DCs) becomes public.
- **verified**: yes. `curl -L` → HTTP 200. WebFetch confirmed mandatory
  reporting thresholds exist (exact figures on a linked sub-page) and that
  facility data is public only above a publication threshold.

---

### 13. `nz_epa_ets` — New Zealand Emissions Trading Scheme (NZ EPA)
- **name**: New Zealand Emissions Trading Scheme (NZ ETS) / NZ Emissions Unit
  Register
- **base_url**: `https://www.epa.govt.nz`
- **start_paths**:
  - `/industry-areas/emissions-trading-scheme/`
  - `/industry-areas/emissions-trading-scheme/about-the-emissions-trading-scheme/nz-emissions-unit-register/`
- **level**: national
- **access**: none
- **coverage**: NZ's economy-wide cap-and-trade system (forestry, energy,
  industry, waste) administered by the NZ Environmental Protection Authority;
  covers grid-electricity generation and any large industrial energy user.
  `region: ["apac", "new_zealand"]`, `category: "environmental_agency"`,
  `tags: ["carbon", "mandates", "reporting"]`, `policy_types: ["regulation",
  "guidance"]`, `language: en`.
- **format**: HTML + PDF
- **practical**: no rate limit observed.
- **effort tier**: (b)
- **why worth adding**: the only Oceania ETS besides Australia's Safeguard
  Mechanism — rounds out APAC carbon-pricing coverage.
- **verified**: yes. Both URLs → HTTP 200 via `curl -L`. Note: a guessed
  dedicated register subdomain (`eur.govt.nz`) did not resolve (DNS failure,
  `curl` exit "000") — the EPA page above (which describes and links the
  register) is the confirmed-live source; the register subdomain itself is
  listed under Unverified below for a human to locate if a dedicated
  machine-readable endpoint exists.

---

### 14. `ch_bafu_ets` — Switzerland Emissions Trading System (FOEN/BAFU)
- **name**: Swiss Emissions Trading System (BAFU/FOEN — Federal Office for
  the Environment)
- **base_url**: `https://www.bafu.admin.ch`
- **start_paths**: `/bafu/en/home/topics/climate/info-specialists/climate-policy/emissions-trading.html`
- **level**: national
- **access**: none
- **coverage**: Switzerland's ETS (linked to EU ETS since 2020) covering
  large industrial/power installations; complements Switzerland's CO2 levy on
  fossil fuels for non-ETS entities. `region: ["switzerland", "eu"]`,
  `category: "environmental_agency"`, `tags: ["carbon", "mandates",
  "reporting"]`, `policy_types: ["regulation", "guidance"]`, `language: en`
  (de/fr/it also available on the same domain).
  Note: `bafu.admin.ch` is already a base_url in `switzerland.yaml` via the
  existing `bafu_buildings` entry (building-sector climate rules, different
  start_path/topic) — additive, not duplicate, same pattern as the EU/UK
  reuse cases above.
- **format**: HTML + PDF
- **practical**: no rate limit observed.
- **effort tier**: (b)
- **why worth adding**: fills the gap in `switzerland.yaml`, which currently
  has cantonal (Zurich) building/energy-code entries and federal
  building-climate rules but nothing on Switzerland's EU-linked ETS.
- **verified**: yes. `curl -L` → HTTP 200.

---

### 15. `jp_meti_gx_ets` — Japan GX-ETS (Emissions Trading System, METI)
- **name**: METI — Emissions Trading System (排出量取引制度 / GX-ETS)
- **base_url**: `https://www.meti.go.jp`
- **start_paths**: `/policy/energy_environment/global_warming/ets.html`
- **level**: national
- **access**: none
- **coverage**: Japan's national mandatory emissions trading system, entering
  its binding phase from FY2026 for businesses with direct CO2 emissions
  ≥100,000 t/year (large industrial facilities, and — via ERMS, the
  Emission Reporting & Management System going live ~June 2026 — the
  compliance/reporting mechanism itself). `region: ["apac", "japan"]`,
  `category: "environmental_agency"`, `tags: ["carbon", "mandates",
  "reporting"]`, `policy_types: ["regulation", "guidance"]`, `language: ja`.
  Note: `meti.go.jp` is already a base_url in `apac.yaml` via `meti_jp`
  (English-language GX growth-strategy page,
  `/english/policy/energy_environment/green_growth`) — this is a different,
  Japanese-language, ETS-specific path; additive, not duplicate.
- **format**: HTML + PDF (setup manuals, leaflets, subcommittee materials)
- **practical**: plain `curl` (no UA) got HTTP 403; a browser UA resolved
  cleanly to HTTP 200. Same bot-check pattern as CARB above — flag
  UA/`requires_playwright` consideration.
- **effort tier**: (b)
- **why worth adding**: Japan's mandatory ETS is new and directly threshold-
  relevant (100,000 t CO2e/year is in reach for large hyperscale campuses
  with on-site backup/cogeneration); this is the primary-source regulator
  page, distinct from the GX League industry forum (#16).
- **verified**: yes, with caveat. `curl -L -A "<browser UA>"` → HTTP 200;
  default-UA curl and WebFetch both 403'd (bot-detection). Content confirmed
  via WebSearch snippets of the same METI page: FY2026 mandatory-phase
  threshold (100,000 t direct CO2/yr), free-allocation methodology, ERMS
  reporting system launch.

---

### 16. `jp_gx_league` — Japan GX League
- **name**: GX League (Green Transformation League)
- **base_url**: `https://gx-league.go.jp`
- **start_paths**: `/en/`
- **level**: national
- **access**: none
- **coverage**: the government-industry forum (est. 2022) that piloted
  Japan's voluntary emissions trading ahead of the FY2026 mandatory phase;
  publishes market-rule design documents and disclosure guidelines used to
  shape GX-ETS. `region: ["apac", "japan"]`, `category: "environmental_agency"`,
  `tags: ["carbon", "guidance"]`, `policy_types: ["guidance", "report"]`,
  `language: en`.
- **format**: HTML + PDF
- **practical**: no rate limit observed. Note the page itself states GX
  League operations ceased as of FY2025 with activities transferred to a "GX
  Future Consortium" — a human should confirm whether a successor domain
  needs tracking instead/in addition.
- **effort tier**: (b)
- **why worth adding**: primary source for the market-design documents behind
  GX-ETS (#15); English-language, unlike the METI ETS page.
- **verified**: yes. `curl -L` → HTTP 200. WebFetch confirmed content: GX
  League background, market rule-making role, FY2025 wind-down notice,
  climate-disclosure working-group guidelines 2023-2024.

---

### 17. `qc_spede` — Quebec Cap-and-Trade System for GHG Emission Allowances (SPEDE)
- **name**: Système de plafonnement et d'échange de droits d'émission (SPEDE),
  Ministère de l'Environnement du Québec
- **base_url**: `https://www.environnement.gouv.qc.ca`
- **start_paths**:
  - `/changements/carbone/inscription-spede.htm`
  - `/changementsclimatiques/marche-carbone.asp`
- **level**: subnational (province)
- **access**: none
- **coverage**: Quebec's cap-and-trade system (since 2013, linked with
  California's since 2014 under the Western Climate Initiative — together
  the largest carbon market in North America), covering ~80% of Quebec's GHG
  emissions from large emitters and fuel distributors. `region: ["north_america",
  "canada", "quebec"]`, `category: "environmental_agency"`, `tags": ["carbon",
  "mandates", "reporting"]`, `policy_types: ["regulation", "report"]`,
  `language: fr`.
  Note: this is a **different base_url** from the existing `quebec_energy`
  entry in `canada.yaml` (`transitionenergetique.gouv.qc.ca`) — genuinely
  net-new domain, not a reuse.
- **format**: HTML + PDF (regulation text, participant registries)
- **practical**: no rate limit observed. A 2026 draft regulation amendment
  was open for public consultation May 20 - July 3, 2026 per the ministry's
  own news page — an active, currently-updating source.
- **effort tier**: (b)
- **why worth adding**: fills a real gap in `canada.yaml` — the existing
  Quebec/BC/Alberta entries cover energy ministries generically but no entry
  currently crawls a dedicated provincial carbon-market registry page.
- **verified**: yes. Both URLs → HTTP 200 via `curl -L`. Content confirmed via
  WebSearch: SPEDE mechanism description (annual caps, declining allowances,
  WCI linkage with California, 2026 draft-regulation consultation).

---

### 18. `ab_tier` — Alberta Technology Innovation and Emissions Reduction (TIER) Regulation
- **name**: Technology Innovation and Emissions Reduction (TIER) Regulation,
  Government of Alberta
- **base_url**: `https://www.alberta.ca`
- **start_paths**: `/technology-innovation-and-emissions-reduction-regulation`
- **level**: subnational (province)
- **access**: none
- **coverage**: Alberta's industrial carbon-pricing and output-based
  allocation system for large emitters (facilities ≥100,000 tCO2e/year must
  comply; smaller/opt-in facilities can join) — the specific regulation
  underlying the "TIER" name already referenced only in a notes field on the
  existing `alberta_energy` entry in `canada.yaml`. `region: ["north_america",
  "canada", "alberta"]`, `category: "environmental_agency"`, `tags":
  ["carbon", "mandates", "reporting"]`, `policy_types: ["regulation",
  "report"]`, `language: en`.
  Note: `alberta.ca` is already a base_url via `alberta_energy` (generic
  energy-and-environment landing pages) — this is the specific TIER
  regulation page, a new start_path filling in what that entry's notes field
  only mentioned in passing.
- **format**: HTML + PDF (regulation text, compliance reports)
- **practical**: no rate limit observed.
- **effort tier**: (b)
- **why worth adding**: turns an existing passing mention ("TIER system," no
  URL) into an actual crawlable source — Alberta is a growing Canadian
  data-center market with a real industrial-carbon-price obligation.
- **verified**: yes. `curl -L` → HTTP 200.

---

### 19. `us_epa_ghgrp` — US EPA Greenhouse Gas Reporting Program (GHGRP)
- **name**: US EPA Greenhouse Gas Reporting Program (GHGRP)
- **base_url**: `https://www.epa.gov`
- **start_paths**: `/ghgreporting`
- **level**: national
- **access**: none
- **coverage**: mandatory annual GHG reporting for ~8,000 large US facilities
  (fossil generators, refineries, large industrial sources, fuel/industrial-
  gas suppliers) emitting above regulatory thresholds; publishes facility-
  level data via FLIGHT and Envirofacts (see tier-c API, #21). `region:
  ["us"]`, `category: "environmental_agency"`, `tags: ["reporting",
  "mandates", "carbon"]`, `policy_types: ["regulation", "report"]`,
  `language: en`.
- **format**: HTML (guidance pages) + the underlying dataset (see #21)
- **practical**: no rate limit observed on the guidance pages.
- **effort tier**: (b) for this page; #21 is the paired tier-c API for the
  actual facility data.
- **why worth adding**: the US federal mandatory-reporting backbone —
  distinct from EPA ENERGY STAR (already referenced elsewhere in this
  codebase per `standards-bodies.md`) and from any state cap-and-trade page;
  this is the reporting *requirement* itself.
- **verified**: yes. `curl -L` → HTTP 200. WebFetch confirmed mandatory
  reporting scope (~8,000 facilities), and a pending Sept-2025 proposal to
  remove 46 source categories from the reporting requirement (active,
  currently-contested regulation — good crawl target for change tracking).

---

### 20. `cn_mee_ghg` — China Ministry of Ecology and Environment — GHG/Carbon Market Section
- **name**: Ministry of Ecology and Environment (MEE) — Climate Change/Carbon
  Market section
- **base_url**: `https://www.mee.gov.cn`
- **start_paths**: `/ywgz/ydqhbh/wsqtkz/`
- **level**: national
- **access**: none
- **coverage**: MEE is the competent national authority for China's national
  ETS (world's largest by covered emissions, ~8 billion tCO2/year, power
  sector currently, with cement/steel/aluminum expansion underway per 2024-25
  MEE progress reports); this section publishes allocation methodology,
  compliance rules, and the annual "Progress Report of China's National
  Carbon Market." `region: ["apac", "china"]`, `category:
  "environmental_agency"`, `tags: ["carbon", "mandates", "reporting"]`,
  `policy_types: ["regulation", "report"]`, `language: zh`.
- **format**: HTML + PDF (progress reports, e.g. the 2024/2025 editions found
  this session)
- **practical**: no rate limit observed against this path.
- **effort tier**: (b)
- **why worth adding**: China's national ETS is the largest in the world by
  covered emissions and is expanding sector coverage — MEE is the only
  reliably-resolving official government entry point found this session (see
  Unverified for the registry/exchange operator, which did not resolve
  cleanly).
- **verified**: yes. `curl -L` → HTTP 200 (also verified during initial dedup
  pass). Actual annual progress-report PDFs (2024, 2025 editions) located via
  WebSearch, hosted under `mee.gov.cn` and a provincial mirror
  (`xcoss.henan.gov.cn`) — not independently re-fetched this session, listed
  here as evidence the section is actively publishing, not as a separate
  candidate.

---

## Tier-C: Structured API / open-data source

### 21. `epa_ghgrp_envirofacts_api` — EPA Envirofacts GHGRP RESTful Data Service
- **name**: EPA Envirofacts Greenhouse Gas RESTful Data Service
- **base_url**: `https://data.epa.gov` (API); documented at
  `https://www.epa.gov/enviro/greenhouse-gas-restful-data-service`
- **source_type feasibility**: no existing client fits this shape (a generic
  Oracle-table-passthrough REST API, one URL segment per table name, e.g.
  `/efservice/PUB_DIM_FACILITY/JSON/rows/0:10`). Would need a **new**
  `source_type` (tier-c per the brief).
- **level**: national
- **access**: none — fully keyless, no signup, no headers required
- **coverage**: facility-level GHGRP data — the `PUB_DIM_FACILITY` table alone
  returns facility name/address/lat-long/NAICS code/year for every reporting
  facility; other tables (not individually tested this session, but same
  `/efservice/<TABLE>/<FORMAT>` shape) cover reported emissions by
  subpart/gas. `region: ["us"]`, `category: "environmental_agency"`, `tags:
  ["reporting", "carbon"]`, `policy_types: ["report"]`.
- **format**: JSON (also XML, CSV, HTML, JSONP, Parquet, PDF via URL suffix)
- **practical**: no documented hard rate limit found this session; the
  `/JSON/` suffix in the URL path did not change the actual response format
  in this session's test (came back as XML regardless) — a human/engineer
  should confirm the correct format-selector syntax before building a client
  (docs page above has the full syntax reference).
- **effort tier**: (c) — needs a new client; the API shape itself is simple
  (bare REST, no auth) but is a generic table-passthrough rather than a
  purpose-built search API, so response parsing will be table-schema-specific.
- **why worth adding**: the only true open-data API found in this entire
  carbon/ETS pass — live, keyless, facility-level US GHG emissions data
  updated annually. Directly flaggable per the brief's tier-c/open-data-API
  callout.
- **verified**: YES — live query executed this session:
  `curl "https://data.epa.gov/efservice/PUB_DIM_FACILITY/JSON/rows/0:2"` →
  HTTP 200, returned real facility records (e.g. FACILITY_ID 1000001, "PSE
  Ferndale Generating Station," Ferndale WA, NAICS 221112, YEAR 2010) with
  full address/lat-long/NAICS/program fields.

---

### 22. `kr_etrs_registry` — Korea Emission Trade Registry System (ETRS, GIR)
- **name**: Emission Trade Registry System (배출권등록부시스템, ETRS) — Greenhouse
  Gas Inventory and Research Center (GIR)
- **base_url**: `https://etrs.gir.go.kr`
- **start_paths**: `/etrs/main.do`
- **level**: national
- **access**: none (public info pages); the transactional registry itself
  needs an account, out of scope
- **coverage**: the operational registry for Korea's K-ETS — records
  allowance issuance, holding, trading, and retirement per covered entity.
  `region: ["apac", "south_korea"]`, `category: "environmental_agency"`,
  `tags: ["carbon", "reporting", "mandates"]`, `policy_types: ["regulation",
  "report"]`, `language: ko` — **Korean-language only**; no English version
  found this session (GIR's English site, `www.gir.go.kr/eng/...`, does not
  surface K-ETS content — tested and confirmed empty of ETS references).
- **format**: HTML (session-ID-bearing URLs — `;jsessionid=...` — observed on
  several GIR sub-pages during this search, a sign the site may not tolerate
  a stateless crawler well)
- **practical**: unknown rate limit; `jsessionid` URL pattern suggests
  `requires_playwright: true` may be needed for a stable crawl, and URLs
  found via search included session tokens that will not be stable
  long-term — only the bare `/etrs/main.do` entry path (no session token) is
  recommended as the crawl seed.
- **effort tier**: (b), Korean-language, moderate crawl risk (session-based
  URLs) — recommend a human confirm crawlability before enabling.
- **why worth adding**: Korea's K-ETS (4th allocation phase, EITE
  free-allocation rules) is a mature, large Asian carbon market with no
  existing PolicyPulse coverage of `gir.go.kr`/`etrs.gir.go.kr` at all.
- **verified**: partial. `curl -L` on the bare `/etrs/main.do` path → HTTP
  200. Content not independently re-fetched via WebFetch this session (site
  navigation only confirmed via WebSearch snippets identifying ETRS as GIR's
  K-ETS registry system, plus a companion NGMS/target-management system and
  ORS offset registry on the same GIR domain family). GIR's English-language
  homepage (`www.gir.go.kr/eng/main.do`) was separately WebFetched and
  confirmed to have **no** K-ETS content — flagging so a human doesn't
  mistake the English GIR homepage for K-ETS coverage.

---

## Unverified / needs-human-check

- **China CEA registry/exchange operator — `cets.org.cn`** (China Carbon
  Emissions Registration and Clearing Co. / Shanghai Environment and Energy
  Exchange). `curl -L` (both http/https, both with and without a browser UA)
  returned **HTTP 412** consistently — the server is up but rejecting the
  request (likely a header/cert requirement this session's curl didn't
  satisfy, or region-gating). This would be a stronger candidate than the
  generic MEE page (#20) if a human can get past the 412 — it's the actual
  registry/exchange operator, not just the ministry.
- **UK ETS Registry (dedicated subdomain)** — searched for a distinct
  `ets-registry.gov.uk`-style domain; nothing resolved (`curl` exit code
  "000" / DNS failure on the guessed hostname, and no working `gov.uk` guidance
  slug found for "UK ETS registry" specifically in the time available). The
  UK ETS registry is very likely reached through a `gov.uk`
  `sign-in`/service-portal path rather than a separate marketing page — a
  human with more search time should locate the correct guidance URL before
  this is added.
- **NZ Emissions Unit Register (dedicated subdomain)** — guessed
  `eur.govt.nz` did not resolve (DNS failure). The EPA page listed as #13
  (`epa.govt.nz/.../nz-emissions-unit-register/`) is confirmed live and
  describes the register; a human should check whether the register itself
  (as opposed to the EPA's descriptive page) lives at a different,
  correctly-spelled subdomain.
- **Korea GIR English-language K-ETS page** — `www.gir.go.kr/eng/main.do`
  loads (confirmed via WebFetch) but has zero K-ETS content; several guessed
  English ETS-specific paths (`/eng/site/emissionTradingScheme.do`,
  `/eng/main/main.do`) both 404'd. If GIR publishes an English K-ETS
  overview, its URL was not found this session — #22 (Korean-language ETRS)
  is the best confirmed substitute.
- **Voluntary carbon-credit registries (Verra, Gold Standard, ICVCM)** —
  explicitly out of scope per the brief ("government carbon-pricing, ETS, and
  emissions-registry bodies"); these are private/NGO-run registries, not
  government bodies, so they were not researched or proposed here. Flagging
  the exclusion explicitly in case a future pass wants voluntary-market
  coverage under a different brief.

---

## Dedup summary

No candidate's `base_url` duplicates an existing entry's **topic** in
`config/domains/*.yaml`. Several candidates share a **domain** with an
existing unrelated entry (`ww2.arb.ca.gov`, `meti.go.jp`, `bafu.admin.ch`,
`alberta.ca`, `gov.uk`, `eur-lex.europa.eu`) — each is called out above with
the existing sibling `id` so this is legible as additive, consistent with how
`eu.yaml` already carries 4 separate `eur-lex.europa.eu` entries and `uk.yaml`
carries 30+ separate `gov.uk` entries for different topics.

## Summary table

| # | id | Country/body | Tier | Verified |
|---|----|----|------|----------|
| 1 | eu_ets_main | EU ETS | b | yes |
| 2 | eu_ets2_buildings_transport | EU ETS2 | b | yes |
| 3 | eu_ets_union_registry | EU Union Registry | b | yes |
| 4 | eurlex_csrd_2022_2464 | EU CSRD | b | yes |
| 5 | uk_ets_participating | UK ETS | b | yes |
| 6 | uk_secr | UK SECR | b | yes |
| 7 | uk_esos | UK ESOS | b | yes |
| 8 | de_dehst_nehs | Germany nEHS/BEHG | b | yes |
| 9 | ca_carb_cap_trade | California CARB | b | yes (UA needed) |
| 10 | us_rggi | RGGI | b | yes |
| 11 | au_cer_safeguard | Australia Safeguard | b | yes |
| 12 | au_cer_nger | Australia NGER | b | yes |
| 13 | nz_epa_ets | NZ ETS | b | yes |
| 14 | ch_bafu_ets | Switzerland ETS | b | yes |
| 15 | jp_meti_gx_ets | Japan GX-ETS | b | yes (UA needed) |
| 16 | jp_gx_league | Japan GX League | b | yes |
| 17 | qc_spede | Quebec SPEDE | b | yes |
| 18 | ab_tier | Alberta TIER | b | yes |
| 19 | us_epa_ghgrp | US EPA GHGRP | b | yes |
| 20 | cn_mee_ghg | China MEE | b | yes |
| 21 | epa_ghgrp_envirofacts_api | US EPA Envirofacts API | c | yes |
| 22 | kr_etrs_registry | Korea ETRS | b | partial |
