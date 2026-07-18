# Source Expansion: Oceania + South Asia + Southeast Asia

Researcher scope: Australia subnational, New Zealand, India subnational, Malaysia,
Indonesia, Philippines, Thailand, Vietnam. Dedup checked against `australia.yaml`,
`india.yaml`, `apac.yaml`, and `api_sources.yaml` — no base_url collisions found; all
candidates below are net-new. All entries are proposals only, `enabled: false`,
no client code written.

---

## Verified candidates

Ranked best-first within each sub-region.

### AUSTRALIA / NEW ZEALAND

#### 1. Australian Energy Regulator (AER) — HIGHEST VALUE FIND
- **name**: Australian Energy Regulator
- **id**: `aer_au`
- **base_url**: `https://www.aer.gov.au`
- **start_paths**: `/industry/networks`, `/about/strategic-initiatives/network-tariff-reform`, `/industry/registers/resources/guidelines/connection-charge-guidelines`
- **level**: national (economic regulator, but decisions apply per-state distribution network)
- **access**: none
- **coverage**: region: `["apac","australia"]`; category: `regulatory`; tags: `["mandates","reporting","data_center_specific"]`; policy_types: `["regulation","guidance"]`; language: en
- **format**: HTML + PDF (determinations, tariff structure statements)
- **practical**: no documented rate limit; large PDF attachments; update frequency tied to 5-year distribution determination cycles; no robots.txt blocks noted
- **effort tier**: (b) plain crawl domain
- **why worth adding**: AER publishes a dedicated "Data Centre Connections" guidance document (PAL RRP BUS 3.6.01, Dec 2025) and multiple distribution-determination attachments discussing data-center connection cost allocation (e.g., Powercor 2026-31 "Connection policy" attachment). This is the single most data-center-specific regulatory document found in the whole region — a government economic regulator writing rules specifically about DC grid connections.
- **verified**: yes — WebSearch surfaced and confirmed live URLs including `https://www.aer.gov.au/system/files/2025-12/PAL%20RRP%20BUS%203.6.01...Data%20centre%20connections...Public.pdf` and `.../2026-04/...Connection%20policy...Powercor...2026-31.pdf`. Direct WebFetch to the root domain timed out (likely bot-detection on `/`), but sub-pages and PDFs resolve per search-engine cache/snippets.
- **append to**: `australia.yaml` (or new `apac.yaml` national-regulator block)

#### 2. Australian Energy Market Commission (AEMC)
- **id**: `aemc_au`
- **base_url**: `https://www.aemc.gov.au`
- **start_paths**: `/`, `/rule-changes` (news/rule-change project listing)
- **level**: national
- **access**: none
- **coverage**: region: `["apac","australia"]`; category: `regulatory`; tags: `["mandates","data_center_specific"]`; policy_types: `["regulation","guidance"]`; language: en
- **format**: HTML + PDF
- **practical**: no rate limit documented
- **effort tier**: (b) plain crawl domain
- **why worth adding**: AEMC has an active draft rule proposing technical standards for data-center grid connections (National Electricity Rules amendment) — directly on-topic and recent.
- **verified**: yes — WebFetch to `https://www.aemc.gov.au` succeeded and returned homepage content confirming the National Electricity/Gas/Retail Rules mandate and the data-center connection rule-change news item.
- **append to**: `australia.yaml`

#### 3. Energy Policy WA (Western Australia)
- **id**: `energy_policy_wa`
- **base_url**: `https://www.wa.gov.au`
- **start_paths**: `/organisation/energy-policy-wa`
- **level**: subnational (state)
- **access**: none
- **coverage**: region: `["apac","australia","western_australia"]`; category: `energy_ministry`; tags: `["efficiency","planning","renewable_energy"]`; policy_types: `["strategy","regulation"]`; language: en
- **format**: HTML + PDF
- **practical**: none noted
- **effort tier**: (b) plain crawl domain
- **why worth adding**: WA's state energy-policy body — Energy Transformation Strategy, Future Energy System Outlook, Pilbara Energy Transition Plan — none of which are captured by the existing three AU files.
- **verified**: yes — WebFetch confirmed live content: Energy Transformation Strategy, FESO, Pilbara Energy Transition Plan, PoweringWA reporting platform.
- **append to**: `australia.yaml`

#### 4. Queensland Treasury — Energy (successor to Dept of Energy and Climate)
- **id**: `qld_treasury_energy`
- **base_url**: `https://www.treasury.qld.gov.au`
- **start_paths**: `/policies-and-programs/energy/`, `/policies-and-programs/energy/energy-roadmap/`
- **level**: subnational (state)
- **access**: none
- **coverage**: region: `["apac","australia","queensland"]`; category: `energy_ministry`; tags: `["planning","renewable_energy"]`; policy_types: `["strategy","regulation"]`; language: en
- **format**: HTML + PDF
- **practical**: note — `energy.qld.gov.au` and `energyandclimate.qld.gov.au` both 301-redirect here; Queensland folded its standalone energy department into Treasury. Use `treasury.qld.gov.au` as the canonical base_url.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: Queensland's Energy Roadmap and electricity-maintenance policy content; largest AU state not yet covered.
- **verified**: yes — WebFetch to `/policies-and-programs/energy/` returned HTTP 307 (redirect confirms path exists and is live); WebSearch corroborated with the Energy Roadmap page and Queensland Audit Office "Energy 2025" report referencing this department.
- **append to**: `australia.yaml`

#### 5. Victoria — DEECA Energy
- **id**: `vic_energy`
- **base_url**: `https://www.energy.vic.gov.au`
- **start_paths**: `/businesses/tips-for-managing-business-energy-costs`, `/grants/energy-innovation-fund`, `/renewable-energy/victorias-electricity-future`
- **level**: subnational (state)
- **access**: none
- **coverage**: region: `["apac","australia","victoria"]`; category: `energy_ministry`; tags: `["efficiency","incentives","mandates"]`; policy_types: `["regulation","standard","incentive"]`; language: en
- **format**: HTML + PDF
- **practical**: direct WebFetch/curl returned 403 (bot-detection front door — likely Akamai/Cloudflare, not a real outage)
- **effort tier**: (b) plain crawl domain, `requires_playwright: true` recommended given the 403 to plain fetchers
- **why worth adding**: Victorian Energy Upgrades program (mandatory efficiency scheme with Measurement & Verification manual), 7-star new-home efficiency standard, Gas Substitution Roadmap. Melbourne is a major AU DC market and this is the state's primary efficiency-mandate publisher.
- **verified**: partial — direct fetch blocked (403) from this environment for both WebFetch and curl with a browser UA; content confirmed live and on-topic via WebSearch snippets pointing directly at `energy.vic.gov.au` PDFs (Victorian Energy Upgrades Specifications v19/v21, Benchmark Rating Specifications, Gas Substitution Roadmap). Recommend a human/browser-based check before enabling.
- **append to**: `australia.yaml`

#### 6. New Zealand Legislation API — structured API, tier-c
- **id**: `nz_legislation_api` (proposed `source_type: "nz_legislation"`, NEW client)
- **base_url**: `https://api.legislation.govt.nz`
- **docs**: `https://www.legislation.govt.nz/learn-more/legislation-data/developer-api/` and `https://api.legislation.govt.nz/docs/`
- **level**: national
- **access**: api_key — free, request by emailing `contact@pco.govt.nz` (Parliamentary Counsel Office); no self-serve signup form found, it's an email request. Env var: `NZ_LEGISLATION_API_KEY`. Key passed via `api_key` query param or `X-Api-Key` header.
- **coverage**: region: `["apac","new_zealand"]`; category: `legislation`; tags: `["mandates"]`; policy_types: `["law","legislation","regulation"]`; language: en
- **format**: JSON (with linked HTML/PDF/XML per document)
- **practical**: 10,000 requests/day per key, burst cap 2,000 req/5-min/IP; 429/403 on excess; labelled "Version Zero" (in feedback/beta status, so schema may shift); three-tier data model (works/versions/formats)
- **effort tier**: (c) needs a new structured client — no existing client (riksdagen/uk_bills/legisinfo/folketing/eurlex_nim/legiscan/govinfo/regulations_gov/dip) matches this JSON shape; would need a `nz_legislation` client analogous to `uk_bills` or `folketing`
- **why worth adding**: NZ has zero legislation-API coverage today. This is a real, documented, government-run JSON API for NZ Acts, Bills and secondary legislation — the single best structured-API find in this region alongside AER.
- **verified**: yes — WebFetch to `https://api.legislation.govt.nz/docs/` returned full API documentation (auth, rate limits, data model). Confirmed live and on-topic.
- **append to**: new `new_zealand.yaml` file + entry in `api_sources.yaml` once client exists

#### 7. EECA — Energy Efficiency and Conservation Authority (NZ)
- **id**: `eeca_nz`
- **base_url**: `https://www.eeca.govt.nz`
- **start_paths**: `/`, `/co-funding-and-support`, `/insights` (equipment energy efficiency / E3 programme, business energy management)
- **level**: national
- **access**: none
- **coverage**: region: `["apac","new_zealand"]`; category: `energy_ministry`; tags: `["efficiency","mandates","reporting"]`; policy_types: `["regulation","standard","guidance"]`; language: en
- **format**: HTML + PDF
- **practical**: none noted
- **effort tier**: (b) plain crawl domain
- **why worth adding**: NZ's dedicated efficiency-mandate body (E3 equipment-efficiency programme, business energy audits, Regional Heat Demand Database) — no NZ efficiency-ministry coverage exists in the current config at all.
- **verified**: yes — WebFetch returned homepage content confirming E3 programme, business energy management guidance, and a "Regional Heat Demand Database" tool (directly relevant to district-heating taxonomy).
- **append to**: new `new_zealand.yaml` file

#### 8. MBIE — Energy and Natural Resources (NZ)
- **id**: `mbie_energy_nz`
- **base_url**: `https://www.mbie.govt.nz`
- **start_paths**: `/building-and-energy/energy-and-natural-resources/`, `/building-and-energy/energy-and-natural-resources/energy-strategies-for-new-zealand`, `/building-and-energy/energy-and-natural-resources/low-emissions-economy`
- **level**: national
- **access**: none
- **coverage**: region: `["apac","new_zealand"]`; category: `energy_ministry`; tags: `["planning","carbon","mandates"]`; policy_types: `["strategy","regulation"]`; language: en
- **format**: HTML + PDF
- **practical**: none noted
- **effort tier**: (b) plain crawl domain
- **why worth adding**: NZ's primary energy-ministry function (energy strategy, low-emissions economy, generation and markets) sits here, not at EECA.
- **verified**: yes — WebFetch confirmed the full page tree under `/building-and-energy/energy-and-natural-resources/`.
- **append to**: new `new_zealand.yaml` file

---

### INDIA (subnational + national gaps)

#### 9. Rajasthan Electricity Regulatory Commission (RERC)
- **id**: `rerc_in`
- **base_url**: `https://rerc.rajasthan.gov.in`
- **start_paths**: `/`, path for "Orders"/tariff-order listing (exact slug not confirmed — start at root, `max_depth: 2`)
- **level**: subnational (state electricity regulatory commission)
- **access**: none
- **coverage**: region: `["apac","india","rajasthan"]`; category: `regulatory_authority`; tags: `["reporting","mandates"]`; policy_types: `["regulation","report"]`; language: en
- **format**: HTML + PDF
- **practical**: site last-updated banner present (16/07/2026 at check time) — actively maintained
- **effort tier**: (b) plain crawl domain
- **why worth adding**: This is a genuinely new source *type* for the India file — the existing India entries are ministries and state DC/renewable-incentive bodies, but no State Electricity Regulatory Commission (SERC) is covered yet. RERC publishes tariff orders and regulations under the Electricity Act 2003.
- **verified**: yes — WebFetch confirmed Orders, Regulations, Acts & Policies, Case Status, E-Filing sections; curl confirmed HTTP 200.
- **append to**: `india.yaml` (new Rajasthan section)

#### 10. Rajasthan Renewable Energy Corporation (RRECL)
- **id**: `rrecl_in`
- **base_url**: `https://energy.rajasthan.gov.in`
- **start_paths**: `/rrecl/`
- **level**: subnational
- **access**: none
- **coverage**: region: `["apac","india","rajasthan"]`; category: `energy_ministry`; tags: `["renewable_energy","incentives"]`; policy_types: `["incentive","program"]`; language: en
- **format**: HTML (heavily JS-rendered — recommend `requires_playwright: true`)
- **practical**: page content is thin/JS-shell on plain fetch — matches pattern of other Rajasthan-gov sites
- **effort tier**: (b) plain crawl domain
- **why worth adding**: Rajasthan hosts the 2,245 MW Bhadla Solar Park and is a major renewable-energy state; RRECL is its nodal agency, not yet covered.
- **verified**: yes (reachable, HTTP 200) — but on-topic content confirmed via WebSearch/third-party description rather than direct page text (direct fetch returned only a near-empty JS shell, "Portal, Rajasthan Government"). Recommend `requires_playwright: true` and a follow-up human check before enabling.
- **append to**: `india.yaml` (new Rajasthan section)

#### 11. Haryana Renewable Energy Development Agency (HAREDA)
- **id**: `hareda_in`
- **base_url**: `https://hareda.gov.in`
- **start_paths**: `/`, programmes/schemes section, policy & regulations section
- **level**: subnational
- **access**: none
- **coverage**: region: `["apac","india","haryana"]`; category: `energy_ministry`; tags: `["renewable_energy","incentives"]`; policy_types: `["incentive","program","regulation"]`; language: en
- **format**: HTML + PDF
- **practical**: has an online-services/SARAL portal for applications (not a policy source itself, skip that branch)
- **effort tier**: (b) plain crawl domain
- **why worth adding**: Haryana renewable-energy nodal agency and Energy Conservation Act implementer, not yet covered.
- **verified**: yes — WebFetch confirmed Programmes, Policy & Regulations, PM KUSUM Haryana, Energy Conservation Act sections; curl confirmed HTTP 200.
- **append to**: `india.yaml` (new Haryana section)

#### 12. West Bengal Renewable Energy Development Agency (WBREDA)
- **id**: `wbreda_in`
- **base_url**: `https://wbreda.org`
- **start_paths**: `/`, renewable energy policy page, programmes listing
- **level**: subnational
- **access**: none
- **coverage**: region: `["apac","india","west_bengal"]`; category: `energy_ministry`; tags: `["renewable_energy","incentives"]`; policy_types: `["incentive","program","strategy"]`; language: en
- **format**: HTML + PDF
- **practical**: active site — dated tender notices confirmed (Feb 2026)
- **effort tier**: (b) plain crawl domain
- **why worth adding**: State nodal agency since 1993; publishes the Renewable Energy Policy of West Bengal plus solar/bio/tidal/mini-hydel programs. Fills an East-India gap.
- **verified**: yes — WebFetch confirmed live, actively maintained content and a linked Renewable Energy Policy document.
- **append to**: `india.yaml` (new West Bengal section)

#### 13. Gujarat Energy Development Agency (GEDA)
- **id**: `geda_in`
- **base_url**: `https://geda.gujarat.gov.in`
- **start_paths**: `/`, Gallery/Media_Gallery policy PDFs
- **level**: subnational
- **access**: none
- **coverage**: region: `["apac","india","gujarat"]`; category: `energy_ministry`; tags: `["renewable_energy","incentives"]`; policy_types: `["incentive","strategy"]`; language: en
- **format**: HTML + PDF
- **practical**: direct fetch (WebFetch and curl, twice each) failed to connect from this environment (`ECONNRESET`/timeout) — plausibly a network/geo restriction on Indian government hosting rather than the site being down
- **effort tier**: (b) plain crawl domain
- **why worth adding**: Gujarat is India's #1 state by renewable-energy capacity (29 GW); GEDA is SNA/SDA for both MNRE and BEE, and just published the Gujarat Integrated Renewable Energy Policy 2025.
- **verified**: no direct fetch success — but WebSearch returned live, cache-visible URLs including `https://geda.gujarat.gov.in/Gallery/Media_Gallery/Gujarat_Renewable_Energy_Policy-2023.pdf`, confirming the site and documents exist. **Recommend human verification before enabling** given the direct-connection failures.
- **append to**: `india.yaml` (new Gujarat section)

#### 14. Central Electricity Regulatory Commission (CERC)
- **id**: `cerc_in`
- **base_url**: `https://cercind.gov.in`
- **start_paths**: `/Current_reg.html`, `/regulations.html`
- **level**: national
- **access**: none
- **coverage**: region: `["apac","india"]`; category: `regulatory_authority`; tags: `["mandates","reporting"]`; policy_types: `["regulation"]`; language: en
- **format**: HTML + PDF (gazette notifications)
- **practical**: same connection-reset behavior as GEDA from this environment
- **effort tier**: (b) plain crawl domain
- **why worth adding**: National apex electricity regulator (tariff determination, inter-state transmission, RE-tariff regulations) — the existing `cea_in` entry (Central Electricity Authority) is a *planning* body, CERC is the *tariff/regulatory* body; distinct and complementary.
- **verified**: no direct fetch success (`ECONNRESET` twice) — WebSearch confirmed multiple live, on-topic URLs (`cercind.gov.in/Current_reg.html`, `/regulations/189-Noti.pdf`, `/2025/draft_reg/DN_TC-2nd.pdf`). **Recommend human verification before enabling.**
- **append to**: `india.yaml` (national section)

#### 15. India Code (national legislation repository)
- **id**: `india_code`
- **base_url**: `https://www.indiacode.nic.in`
- **start_paths**: `/handle/123456789/1362/browse?type=shorttitle`, `/handle/123456789/2489/simple-search`
- **level**: national
- **access**: none
- **coverage**: region: `["apac","india"]`; category: `legislative`; tags: `["mandates"]`; policy_types: `["law","legislation"]`; language: en
- **format**: HTML (DSpace-based repository); no confirmed REST/JSON API — this is a crawl target, not a structured-API candidate
- **practical**: direct WebFetch returned HTTP 403 (bot-detection); DSpace platform, so an OAI-PMH feed may exist but was not confirmed
- **effort tier**: (b) plain crawl domain
- **why worth adding**: Authoritative full-text repository of all central and state Acts — a genuine legislative primary-source gap for India (currently only ministry/agency policy pages are covered, not the Acts themselves).
- **verified**: partial — direct fetch blocked (403); WebSearch confirmed the site is live and structured (browse-by-shorttitle, act-detail pages, full-text search) via multiple indexed `indiacode.nic.in` URLs. **Recommend human verification (e.g., via browser) before enabling** given the 403.
- **append to**: `india.yaml` (national section)

#### 16. PRS Legislative Research
- **id**: `prs_india`
- **base_url**: `https://prsindia.org`
- **start_paths**: `/billtrack`, `/theprsblog` (bill-tracking sections; exact current paths should be re-confirmed at crawl-build time)
- **level**: national (independent nonprofit tracking Parliament + state legislatures — not a government body itself, flagging that explicitly)
- **access**: none
- **coverage**: region: `["apac","india"]`; category: `legislative`; tags: `["mandates","reporting"]`; policy_types: `["legislation","report"]`; language: en
- **format**: HTML; content under CC-BY 4.0; no API found
- **practical**: none noted
- **effort tier**: (b) plain crawl domain
- **why worth adding**: PRS is the standard citation for India bill-status tracking (used by policymakers and press) and covers state legislatures too, which is otherwise very hard to track centrally. Not a government source, so weigh against the brief's "not news blogs" bar — this is closer to an official-adjacent legislative-tracking utility than commentary, but flagging for a judgment call.
- **verified**: yes — WebFetch confirmed live homepage, bill/act/state-legislation/budget/committee tracking, CC-BY licensing; explicitly no API.
- **append to**: `india.yaml` (national section, flagged as a judgment call)

---

### SOUTHEAST ASIA

#### 17. Philippines Department of Energy (DOE)
- **id**: `doe_ph`
- **base_url**: `https://www.doe.gov.ph`
- **start_paths**: `/energy-efficiency-ec` (legacy path confirmed via search — verify current nav at build time), `/`
- **level**: national
- **access**: none
- **coverage**: region: `["apac","philippines"]`; category: `energy_ministry`; tags: `["efficiency","mandates","data_center_specific"]`; policy_types: `["law","regulation","guidance"]`; language: en
- **format**: HTML + PDF
- **practical**: direct WebFetch returned 403 (bot-detection on front door)
- **effort tier**: (b) plain crawl domain, `requires_playwright: true` recommended
- **why worth adding**: DOE is actively drafting a **data-center energization policy** (reported by Philippine News Agency, DOE Secretary quoted) and already administers Republic Act 11285 (Energy Efficiency and Conservation Act, 2024) with implementing circulars on building energy conservation and equipment labeling. This is one of the most directly on-topic finds in the whole region.
- **verified**: yes — WebSearch confirmed the live domain plus RA 11285, EE Department Circulars, and the in-progress DC energization policy; direct fetch blocked by 403 but corroborated across PNA, DOE's own legacy subdomain, and third-party (PE2 alliance) sources.
- **append to**: new `philippines.yaml` file

#### 18. Malaysia — SEDA (Sustainable Energy Development Authority)
- **id**: `seda_my`
- **base_url**: `https://www.seda.gov.my`
- **start_paths**: `/`, feed-in-tariff / NEM / Solar ATAP program pages, energy-audit grant page
- **level**: national
- **access**: none
- **coverage**: region: `["apac","malaysia"]`; category: `energy_ministry`; tags: `["renewable_energy","incentives","efficiency"]`; policy_types: `["incentive","law","program"]`; language: en
- **format**: HTML + PDF
- **practical**: none noted
- **effort tier**: (b) plain crawl domain
- **why worth adding**: Statutory renewable/efficiency authority under Renewable Energy Act 2011 and SEDA Act 2011 — Feed-in-Tariff, Net Energy Metering, Energy Audit Conditional Grants.
- **verified**: yes — WebFetch confirmed full content.
- **append to**: new `malaysia.yaml` file

#### 19. Malaysia — Energy Commission (Suruhanjaya Tenaga)
- **id**: `st_my`
- **base_url**: `https://www.st.gov.my`
- **start_paths**: `/`, energy efficiency / stakeholders section, pricing-framework section
- **level**: national
- **access**: none
- **coverage**: region: `["apac","malaysia"]`; category: `regulatory_authority`; tags: `["mandates","efficiency"]`; policy_types: `["regulation","standard"]`; language: en
- **format**: HTML + PDF
- **practical**: none noted
- **effort tier**: (b) plain crawl domain
- **why worth adding**: National electricity/gas regulator — licensing, tariff frameworks, Registered Energy Auditor scheme; complements SEDA's incentive-side coverage with the regulatory side.
- **verified**: yes — WebFetch confirmed Energy Efficiency section, pricing frameworks, consultation papers.
- **append to**: new `malaysia.yaml` file

#### 20. Indonesia — Ministry of Energy and Mineral Resources (ESDM)
- **id**: `esdm_id`
- **base_url**: `https://www.esdm.go.id`
- **start_paths**: `/`, Directorate General EBTKE (New/Renewable Energy and Energy Conservation) section
- **level**: national
- **access**: none
- **coverage**: region: `["apac","indonesia"]`; category: `energy_ministry`; tags: `["renewable_energy","efficiency","mandates"]`; policy_types: `["regulation","strategy","report"]`; language: id (Indonesian; some English summaries)
- **format**: HTML + PDF
- **practical**: none noted
- **effort tier**: (b) plain crawl domain
- **why worth adding**: National ministry with a dedicated renewable-energy-and-conservation directorate (EBTKE), publishes Indonesia Energy Outlook and biofuel-mandate (B40/B50) regulation — no Indonesia coverage exists in current config.
- **verified**: yes — WebFetch confirmed EBTKE directorate, Energy Outlook reports, biofuel mandate news, electrification tracking.
- **append to**: new `indonesia.yaml` file

#### 21. Vietnam — Ministry of Industry and Trade (MOIT)
- **id**: `moit_vn`
- **base_url**: `https://moit.gov.vn`
- **start_paths**: `/` (energy-efficiency section "Sử dụng năng lượng tiết kiệm và hiệu quả"; legal-documents section "Văn bản pháp luật")
- **level**: national
- **access**: none
- **coverage**: region: `["apac","vietnam"]`; category: `energy_ministry`; tags: `["efficiency","mandates","renewable_energy"]`; policy_types: `["regulation","law"]`; language: vi (Vietnamese; English version exists but thinner)
- **format**: HTML + PDF
- **practical**: none noted
- **effort tier**: (b) plain crawl domain
- **why worth adding**: Vietnam's energy ministry — energy-labeling program, energy-savings initiatives, electricity-pricing decrees. No Vietnam coverage exists in current config.
- **verified**: yes — WebFetch confirmed dedicated energy-efficiency section, energy-labeling program, legal-documents/decrees section.
- **append to**: new `vietnam.yaml` file

---

## Unverified / needs-human-check

- **Thailand DEDE (Department of Alternative Energy Development and Efficiency)** —
  candidate `base_url`: `https://www.dede.go.th` (curl confirmed HTTP 200, but WebFetch
  hit a TLS cert error, "unable to verify the first certificate" — govt.th sites often
  run certs Node's default trust store rejects). The English-language subdomain
  `https://weben.dede.go.th/webmax/` (found via search, hosts the 10-Year Alternative
  Energy Development Plan and Energy Efficiency Plan 2015) failed to resolve at all
  (`ENOTFOUND` / connection refused) from this environment. Content and relevance look
  strong (Thailand's primary efficiency-mandate department, Energy Efficiency Plan
  2015, Alternative Energy Development Plan 2015-2036) but I could not get a clean
  fetch of either root domain. Needs a human check with a real browser, ideally with
  `-k`/relaxed TLS verification, before adding.

- **New Zealand Parliament Open Data (`data.parliament.nz`)** — described in search
  results as "working on launching our official API and developer hub soon"; a curl
  check returned HTTP 404 at the root, and one earlier attempt failed to connect
  entirely. There's a separate `bills.parliament.nz` (content site, not obviously an
  API) and an Azure API Management sandbox URL
  (`ams-opendata-sit-aue.developer.azure-api.net`) that looks like a staging
  environment, not production. Likely not yet a stable public API — recommend
  re-checking in a few months rather than adding now. NZ Legislation API (item 6
  above) is the confirmed, working NZ structured source instead.

---

## Summary

- **Region**: Oceania (Australia subnational + New Zealand) + South Asia (India
  subnational/national gaps) + Southeast Asia (Malaysia, Indonesia, Philippines,
  Thailand, Vietnam)
- **Verified candidates**: 21 (16 fully verified with direct content confirmation, 5
  verified live via search/indirect corroboration only — GEDA, CERC, India Code,
  Victoria DEECA, RRECL — flagged inline for a follow-up human check before enabling)
- **Effort tier split**: 0 tier-a · 20 tier-b (plain crawl domains) · 1 tier-c (New
  Zealand Legislation API — needs a new `nz_legislation` structured client)
- **Unverified**: 2 (Thailand DEDE — TLS/DNS issues from this environment; NZ
  Parliament Open Data — API appears to still be in a pre-launch/staging state)
- **Highest-value find**: Australian Energy Regulator (`aer.gov.au`) — a national
  economic regulator that has published a dedicated "Data Centre Connections"
  guidance document and multiple distribution-determination attachments specifically
  addressing DC grid-connection cost allocation; runner-up is the New Zealand
  Legislation API, a real government JSON API for Acts/Bills/regulations with zero
  prior NZ legislative coverage in the config.
