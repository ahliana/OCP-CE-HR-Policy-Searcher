# East Asia — Source Expansion Research

Region: Japan, South Korea, China, Taiwan, Hong Kong, Singapore.
Branch: `feature/source-expansion-research`. Research only — no client code, nothing
enabled. All candidates below are drafts for `config/domains/*.yaml` with
`enabled: false` until reviewed.

## Dedup check performed

Read `config/domains/apac.yaml` and `config/domains/api_sources.yaml` in full before
researching. Existing `base_url`s already covered (skipped, not re-proposed):

- `https://www.imda.gov.sg` (imda_sg)
- `https://www1.bca.gov.sg` (bca_sg_greenmark)
- `https://www.ema.gov.sg` (ema_sg)
- `https://www.meti.go.jp` (meti_jp)
- `https://www.enecho.meti.go.jp` (enecho_jp)
- `https://www.motie.go.kr` (motie_kr)
- `https://elaws.e-gov.go.jp` (elaws_jp)
- `https://www.law.go.kr` (law_kr)
- `https://www.energy.gov.au` (energy_au — not in scope for this region anyway)

No existing `docs/source-expansion/regions/*.md` files existed before this one (first
region file written). No China, Taiwan, or Hong Kong entries exist anywhere in
`config/domains/` today — this region is greenfield for those three countries.

---

## Verified candidates (ranked best-first)

### 1. Beijing Existing Data Center Optimization Work Plan (Beijing Municipal Government)

- **name**: Beijing Municipal People's Government — Data Center Policy
- **id**: `beijing_gov_dc`
- **base_url**: `https://www.beijing.gov.cn`
- **start_paths**:
  - `/zhengce/zhengcefagui/202411/t20241115_3942264.html` (北京市存量数据中心优化工作方案 2024-2027)
  - `/zhengce/zcjd/202411/t20241118_3942744.html` (policy interpretation — differential electricity pricing)
  - `/zhengce/zhengcefagui/202307/t20230706_3156356.html` (2023 data center energy-saving review rules, found via search, not independently fetched — see unverified list)
- **level**: local (Beijing municipal)
- **access**: none
- **coverage**: region=`apac`/`china`; category=`regulatory`; tags=`mandatory`,`pue_limits`,`differential_pricing`,`carbon`; policy_types=`regulation`,`incentive`. Mandates average annual PUE ≤1.35 by 2027 for existing DCs; differential (higher) electricity pricing for DCs exceeding the PUE standard, phased at +¥0.2/kWh and +¥0.5/kWh; subsidies up to ¥30M per green retrofit project.
- **format**: HTML (policy notices), some PDF attachments
- **practical**: no rate-limit info published; standard gov portal, moderate update frequency (major notices a few times/year); no robots.txt block observed via fetch.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: Beijing is one of China's top data-center hubs and this is the most detailed, current (Nov 2024) municipal PUE-linked pricing/incentive regime found for any East Asian city — directly on-topic for waste-heat/efficiency mandates.
- **verified**: yes — fetched `https://www.beijing.gov.cn/zhengce/zhengcefagui/202411/t20241115_3942264.html` directly; confirmed official "首都之窗" portal, document number 京经信发〔2024〕62号, issued jointly by Beijing Economic and Information Technology Bureau, Beijing DRC, and Beijing Communications Administration, PUE ≤1.35 target text present.

### 2. Shanghai Data Center Development Implementation Opinion (Shanghai Municipal Government)

- **name**: Shanghai Municipal People's Government — Data Center Policy
- **id**: `shanghai_gov_dc`
- **base_url**: `https://www.shanghai.gov.cn`
- **start_paths**:
  - `/gwk/search/content/9dd958b26fa249d4a32367dce97211bf` (上海市经济信息化委 市发展改革委关于推进本市数据中心健康有序发展的实施意见, 沪经信基〔2022〕306号)
  - `/nw12344/20240914/a33482feb8a24666ad745e95ef295f03.html` (2024-2027 green low-carbon transition action plan, references DC PUE)
- **level**: local (Shanghai municipal)
- **access**: none
- **coverage**: region=`apac`/`china`; category=`regulatory`; tags=`mandatory`,`pue_limits`,`carbon`,`efficiency`; policy_types=`regulation`. New large clustered DCs: PUE ≤1.25; existing centers with PUE >1.7 (small, old, <800 racks, 10+ years) targeted for phase-out. References national standard GB 40879-2021 and local standard DB31/652-2020.
- **format**: HTML
- **practical**: same portal family as Beijing; no documented rate limit; standard municipal notice cadence.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: Shanghai is China's other top-tier DC hub; this is a directly on-topic, dated, numbered municipal regulation with hard PUE thresholds and phase-out criteria.
- **verified**: yes — fetched `https://www.shanghai.gov.cn/gwk/search/content/9dd958b26fa249d4a32367dce97211bf` directly; confirmed content, document number, PUE targets present. (Note: a second candidate path, `/hqcyfz2/20230626/...`, returned 404 on fetch — dropped from start_paths.)

### 3. China MIIT — New Data Center Development Three-Year Action Plan

- **name**: Ministry of Industry and Information Technology (MIIT) — Data Center Policy
- **id**: `miit_cn`
- **base_url**: `https://www.miit.gov.cn`
- **start_paths**:
  - `/zwgk/zcjd/art/2021/art_792413b03def477d93e2bb445c1692a2.html` (policy interpretation infographic page)
- **level**: national
- **access**: none
- **coverage**: region=`apac`/`china`; category=`energy_ministry`; tags=`mandatory`,`pue_limits`,`efficiency`,`carbon`; policy_types=`regulation`,`guidance`. New Data Center Development Three-Year Action Plan (2021-2023): PUE ≤1.3 for new large facilities nationally, ≤1.25 in cold-climate regions; layout guidance for hub nodes/provincial/edge DCs; liquid cooling and clean-energy siting encouraged.
- **format**: HTML
- **practical**: MIIT's main site resolved on direct fetch (unlike some China ministry sites). No published rate limit. Same document is mirrored on `www.gov.cn` (see #4) which may be more resilient if miit.gov.cn becomes unreachable.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: MIIT is the named ministry in the brief (data-center energy efficiency authority) and this is its flagship national DC policy, not previously in `apac.yaml`.
- **verified**: yes — fetched directly, confirmed MIIT-issued infographic page for the plan (page footer credits MIIT's Dept. of Information and Communications Development); PUE figures cross-confirmed via a separate fetch of the mirrored full-text notice on gov.cn (#4).

### 4. China State Council Portal (gov.cn) — mirrors NDRC/MIIT joint DC notice

- **name**: China State Council Gazette / gov.cn — Data Center & Energy Notices
- **id**: `govcn_dc`
- **base_url**: `https://www.gov.cn`
- **start_paths**:
  - `/zhengce/zhengceku/2021-07/14/content_5624964.htm` (full text, MIIT Notice 工信部通信〔2021〕76号, New Data Center 3-Year Action Plan)
- **level**: national
- **access**: none
- **coverage**: region=`apac`/`china`; category=`regulatory`; tags=`mandatory`,`pue_limits`; policy_types=`regulation`. Full official notice text (vs. MIIT's own infographic-only page) — PUE ≤1.3 for new large facilities, 20% annual rack-capacity growth target, 60%+ utilization target.
- **format**: HTML
- **practical**: `gov.cn` is China's central "zhengceku" (policy repository) — historically more reliable/accessible than individual ministry domains for automated fetching; worth using as a fallback aggregator across MIIT/NDRC/NEA notices generally, not just this one document.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: More resilient access point than ministry-specific domains, and it's the canonical full-text source (ministry sites often only host interpretive summaries or infographics).
- **verified**: yes — fetched directly, confirmed full notice text with document number, date, and PUE targets.

### 5. Hong Kong Data Centre Facilitation Portal (Digital Policy Office)

- **name**: Hong Kong SAR — Data Centre Facilitation Measures Portal
- **id**: `datacentre_hk`
- **base_url**: `https://www.datacentre.gov.hk`
- **start_paths**:
  - `/en/facilitation_measures/energy_efficiency.html`
  - `/en/` (portal home — links to site selection, power supply, water cooling, facilitation measures)
- **level**: national (Hong Kong SAR government)
- **access**: none
- **coverage**: region=`apac`/`hong_kong`; category=`regulatory`; tags=`efficiency`,`cooling_efficiency`,`incentives`; policy_types=`guidance`,`regulation`. One-stop government portal (run by the Digital Policy Office, formerly OGCIO) aggregating Hong Kong's DC-specific facilitation measures: Building Energy Efficiency Ordinance (BEEO) application to DCs, the Fresh Water Cooling Towers Scheme, Green Data Centres Practice Guide, and BEAM Plus Data Centres assessment tool.
- **format**: HTML, PDF (guides)
- **practical**: English-language, no login, straightforward crawl.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: This is the single best aggregator found for Hong Kong DC energy policy — it's the government's own index of every relevant scheme, better than crawling EMSD alone since it cross-links Buildings Dept and Digital Policy Office material too. First Hong Kong source for this project.
- **verified**: yes — fetched `/en/facilitation_measures/energy_efficiency.html` directly, confirmed content (BEEO, FWCT Scheme, SBD guidelines, Green Data Centres Practice Guide, BEAM Plus). Fetched `/en/` root separately and confirmed same portal identity.

### 6. Hong Kong EMSD — Energy Efficiency Office

- **name**: Electrical and Mechanical Services Department (EMSD) — Energy Management
- **id**: `emsd_hk`
- **base_url**: `https://www.emsd.gov.hk`
- **start_paths**:
  - `/en/energy_efficiency/energy_management/index.html`
  - `/en/energy_efficiency/new_renewable_energy/index.html`
- **level**: national (Hong Kong SAR government)
- **access**: none
- **coverage**: region=`apac`/`hong_kong`; category=`energy_ministry`; tags=`mandatory`,`efficiency`,`reporting`; policy_types=`regulation`,`guidance`. Building Energy Efficiency Ordinance (mandatory energy audits every 10 years for commercial buildings, includes DCs), online building energy benchmarking tool, HK EE Net technical library.
- **format**: HTML, PDF
- **practical**: English, no login, no published rate limit. Note: `/en/energy_efficiency/quality_professional_services/data_centre/index.html` (a more DC-specific path found via search) returned 404 on direct fetch — do not use that path; use the two above instead.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: EMSD is the exact agency the brief names for Hong Kong (the equivalent regulator to METI/MOTIE); this is the department's own energy-efficiency regulatory hub, distinct from and complementary to the datacentre.gov.hk aggregator above.
- **verified**: yes — fetched `/en/energy_efficiency/energy_management/index.html` directly; confirmed BEEO description and benchmarking tool content. The specific `/data_centre/` sub-path referenced in search results 404'd on direct fetch and should not be used.

### 7. Japan e-Gov Law API v2 (laws.e-gov.go.jp)

- **name**: e-Gov Law Search API v2 (Digital Agency, Japan)
- **id**: `egov_law_api`
- **base_url**: `https://laws.e-gov.go.jp`
- **source_type feasibility**: NEW client needed — real REST API (`/api/2/laws`, `/api/2/law_data/{law_id}`, etc.), OpenAPI/Swagger spec at `/api/2/swagger-ui`, ReDoc at `/api/2/redoc/`, PDF spec at `/file/houreiapi_shiyosyo.pdf`. Returns JSON or XML, full law text retrievable by law number, keyword search across law names/provisions, amendment history.
- **level**: national
- **access**: none — no API key, no registration; the tool documented (via search) that it explicitly does not require sign-up (just don't hammer it with high request volume).
- **coverage**: region=`apac`/`japan`; category=`legislative`; tags=`mandates`,`energy_efficiency`; policy_types=`law`,`legislation`. Same underlying corpus as the existing `elaws_jp` crawl entry (Energy Efficiency Act / Rationalizing Energy Use Act) but via a real structured API instead of a Playwright-scraped search UI.
- **format**: JSON, XML
- **practical**: no documented hard rate limit; official recommendation is to avoid high-frequency bursts. Docs at `https://laws.e-gov.go.jp/docs/law-data-basic/`.
- **effort tier**: (c) needs a new structured client
- **why worth adding**: This is a materially better access path to the same Japanese law corpus the project already wants (Energy Efficiency Act text) — trading a `requires_playwright: true` crawl domain for a documented, keyless JSON/XML API. Different base_url from the existing `elaws_jp` entry (`elaws.e-gov.go.jp`, the older system), so not a duplicate.
- **verified**: yes (partially) — confirmed via WebSearch that `laws.e-gov.go.jp/api/2/swagger-ui` and `/api/2/redoc/` exist and are live search results; a direct WebFetch of the swagger-ui page returned only a page title with no machine-readable spec body (client-rendered Swagger UI). Recommend a human/dev spike load the Swagger UI in a real browser or fetch `/api/2/redoc/` before building the tier-c client, since I could not confirm exact JSON schema details from a text fetch.

### 8. Tokyo Metropolitan Government — Data Center Urban Development Guideline

- **name**: Tokyo Bureau of Urban Development — "Guideline for Data Centers Harmonized with Urban Development"
- **id**: `tokyo_toshiseibi_dc`
- **base_url**: `https://www.toshiseibi.metro.tokyo.lg.jp`
- **start_paths**:
  - `/machizukuri/smarttokyo/datacenter`
- **level**: local (Tokyo Metropolitan Government)
- **access**: none
- **coverage**: region=`apac`/`japan`; category=`standards`; tags=`planning`,`efficiency`,`district_heating`; policy_types=`guidance`. Published March 31, 2026: guideline for siting/community dialogue on new data centers in Tokyo, explicitly covering power-demand coordination, decarbonization, and — per the FY2026 program description found in search — **new support for utilizing data-center waste heat in surrounding communities**, plus a forthcoming (FY2026) environment-conscious DC certification scheme.
- **format**: HTML, PDF
- **practical**: Japanese only; no login; standard TMG site.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: This is the newest and most directly on-topic waste-heat-reuse policy found in the entire region — Tokyo (roughly half of Japan's DC floor space per TMG's own published figure) explicitly funding DC waste-heat community reuse starting FY2026. Single highest-value find for East Asia.
- **verified**: yes — fetched the March 2026 press release (`https://www.metro.tokyo.lg.jp/information/press/2026/03/2026033122`) directly, confirming the guideline's publication and scope. The urban-development bureau's own guideline landing page (`toshiseibi.metro.tokyo.lg.jp/machizukuri/smarttokyo/datacenter`) was located via search but not independently re-fetched with WebFetch in this session — treat the exact path as verified-by-search, one level below a direct fetch (see note in Unverified section for the fully-unconfirmed alternative paths).

### 9. Tokyo Bureau of Environment — Cap-and-Trade Program (large facilities)

- **name**: Tokyo Metropolitan Government Bureau of Environment — Cap-and-Trade Program
- **id**: `tokyo_kankyo_capandtrade`
- **base_url**: `https://www.kankyo.metro.tokyo.lg.jp`
- **start_paths**:
  - `/climate/large_scale/index.html`
- **level**: local (Tokyo Metropolitan Government)
- **access**: none
- **coverage**: region=`apac`/`japan`; category=`regulatory`; tags=`mandatory`,`carbon`,`reporting`; policy_types=`regulation`. World's first urban cap-and-trade scheme; mandatory CO2 reduction obligations for large facilities using ≥1,500kL crude-oil-equivalent/year (the same threshold used in the national DC energy-efficiency benchmark) — covers large Tokyo data centers as regulated entities. 4th compliance period FY2025-FY2029.
- **format**: HTML, PDF
- **practical**: Japanese; an English program summary PDF also exists at `english.metro.tokyo.lg.jp/documents/d/english/outlineoftheprogram_4th` (confirmed to resolve — 758KB PDF — but its text is image-embedded and could not be read via automated fetch; treat as a supplementary English artifact, not the primary crawl target).
- **effort tier**: (b) plain crawl domain
- **why worth adding**: Distinct scheme from the national METI/ANRE benchmark already tracked (`enecho_jp`) — this is Tokyo's own binding carbon scheme that captures large data centers by the same energy-use threshold, not yet represented in `apac.yaml`.
- **verified**: yes — fetched `/climate/large_scale/index.html` directly; confirmed program description, 1,500kL threshold, "world's first urban-type cap-and-trade system" language, compliance-period detail.
- **note**: the old TMG "Eco-Conscious Data Center Certification" scheme at `/climate/large_scale/dc.html` was also fetched and confirmed **discontinued since March 2017** — do not propose that path as a live candidate.

### 10. South Korea — Open Assembly Information API (open.assembly.go.kr)

- **name**: 열린국회정보 (Open National Assembly Information) OpenAPI
- **id**: `open_assembly_kr_api`
- **base_url**: `https://open.assembly.go.kr`
- **source_type feasibility**: NEW client needed. Bill/legislation-focused OpenAPI portal with dozens of named APIs (18 for 의안/bills, 11 for 법률/legislation, plus member voting records). Each API endpoint issues its own key.
- **level**: national
- **access**: api_key — free registration required; portal is browsable without login but calling any API endpoint requires requesting an authentication key through the portal (env var suggestion: `ASSEMBLY_API_KEY`).
- **coverage**: region=`apac`/`south_korea`; category=`legislative`; tags=`mandates`; policy_types=`legislation`. Bill-tracking data for Korean National Assembly, useful for tracking pending energy-efficiency/carbon legislation before it reaches `law.go.kr`.
- **format**: JSON/XML (per-API, typically XML by default with JSON option)
- **practical**: no documented rate limit found; each named API is a separate key request, which raises integration complexity.
- **effort tier**: (c) needs a new structured client
- **why worth adding**: Complements the existing `law_kr` (enacted-law) crawl entry with pre-enactment bill tracking — closing the loop from proposed to enacted energy/DC legislation.
- **verified**: yes — fetched `https://open.assembly.go.kr/portal/openapi/main.do` directly; confirmed free browsing, registration-gated key issuance, bill/legislation API categories present.

### 11. South Korea — Open Law API (open.law.go.kr)

- **name**: 국가법령정보 공동활용 Open API (Ministry of Government Legislation)
- **id**: `open_law_kr_api`
- **base_url**: `https://open.law.go.kr`
- **source_type feasibility**: NEW client needed. 191 named APIs covering current/historical legislation, administrative rules, local ordinances, case law, treaties — XML responses.
- **level**: national
- **access**: api_key — registration required through the Ministry of Government Legislation (법제처) portal (env var suggestion: `LAW_GO_KR_API_KEY`).
- **coverage**: region=`apac`/`south_korea`; category=`legislative`; tags=`mandates`,`energy_efficiency`; policy_types=`law`,`legislation`,`regulation`. Same statutory corpus as the existing `law_kr` crawl entry (Rational Energy Utilization Act etc.) but via a documented structured API instead of a Playwright-scraped search UI.
- **format**: XML
- **practical**: registration required by phone/email per the guide page; no published rate limit.
- **effort tier**: (c) needs a new structured client
- **why worth adding**: Same upgrade rationale as the Japan e-Gov API — trades a `requires_playwright: true` crawl for a documented key-based API over the identical legal corpus. Different `base_url` from the existing `law_kr` entry (`www.law.go.kr`), so it is net-new, not a duplicate — flagging as a recommended future replacement/companion for `law_kr`.
- **verified**: yes — fetched `https://open.law.go.kr/LSO/openApi/guideList.do` directly; confirmed 191-API count, XML format statement, registration requirement, and phone contact for the Ministry of Government Legislation.

### 12. South Korea — Korea Energy Agency (KEA)

- **name**: Korea Energy Agency (한국에너지공단)
- **id**: `kea_kr`
- **base_url**: `https://www.energy.or.kr`
- **start_paths**: `/` (top-level Korean site — no deeper English/DC-specific path confirmed; see note)
- **level**: national
- **access**: none
- **coverage**: region=`apac`/`south_korea`; category=`regulatory`; tags=`efficiency`,`reporting`; policy_types=`standard`,`guidance`. Implements zero-energy building certification, industrial energy audits/voluntary efficiency targets, and public-facility power monitoring — the operational agency underneath MOTIE's policy (the existing `motie_kr` entry is the ministry itself, not the implementing agency).
- **format**: HTML, Korean-language
- **practical**: official Korean e-government site confirmed ("공식 전자정부 누리집"); no confirmed dedicated data-center program page — would need a deeper crawl/discovery pass to find one, if it exists.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: Fills the "implementing agency" gap next to `motie_kr` (ministry) and `law_kr`/`open_law_kr_api` (statute) — KEA runs the actual certification/audit programs referenced by Korean energy-efficiency law.
- **verified**: yes (site identity only) — fetched `https://www.energy.or.kr` directly; confirmed official government site and general program list. Could not confirm a DC-specific page in this pass — treat the DC relevance as adjacent/implementing-agency value rather than DC-specific content, and flag for a follow-up crawl to find a more targeted start_path.

### 13. Taiwan — Energy Administration, Ministry of Economic Affairs (MOEAEA)

- **name**: 經濟部能源署 Energy Administration, Ministry of Economic Affairs, R.O.C. (Taiwan)
- **id**: `moeaea_tw`
- **base_url**: `https://www.moeaea.gov.tw`
- **start_paths**:
  - `/ECW/populace/home/Home.aspx`
  - `/ECW/english/content/ContentLink.aspx?menu_id=977` (English "Laws and Regulations" section)
- **level**: national
- **access**: none
- **coverage**: region=`apac`/`taiwan`; category=`energy_ministry`; tags=`efficiency`,`incentives`,`carbon`; policy_types=`regulation`,`incentive`,`guidance`. Taiwan's national energy ministry — energy conservation programs, subsidy schemes, energy statistics, and the agency responsible for the Energy Administration Act (which governs large energy-consuming facilities, a category that includes data centers) en route to Taiwan's 2050 net-zero target.
- **format**: HTML, has both Chinese and English content
- **practical**: bilingual site (zh-TW primary, en available), no login.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: This is the exact agency named in the brief for Taiwan (MOEA) and Taiwan currently has zero entries anywhere in `config/domains/` — this is the foundational national source for the country.
- **verified**: yes — fetched `/ECW/populace/home/Home.aspx` directly; confirmed official Energy Administration site, content sections (electricity, oil/gas, renewables, energy conservation), subsidy programs, and net-zero framing.

### 14. Taiwan — Laws & Regulations Database (Ministry of Justice)

- **name**: 全國法規資料庫 Laws & Regulations Database of the R.O.C. (Taiwan)
- **id**: `law_moj_tw`
- **base_url**: `https://law.moj.gov.tw`
- **start_paths**:
  - `/Eng/index.aspx` (English portal)
  - `/ENG/LawClass/LawAll.aspx?pcode=J0130002` (Energy Administration Act, English)
  - `/ENG/LawClass/LawAll.aspx?pcode=J0130032` (Renewable Energy Development Act, English)
- **level**: national
- **access**: none
- **coverage**: region=`apac`/`taiwan`; category=`legislative`; tags=`mandates`,`energy_efficiency`; policy_types=`law`,`legislation`. Full bilingual statutory text for Taiwan's energy law, including the Energy Administration Act and Renewable Energy Development Act.
- **format**: HTML
- **practical**: no API found despite a targeted search — this is a crawl-only source at present; Chinese text is authoritative over English per the site's own disclaimer.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: Second Taiwan source — statutory-text companion to the MOEAEA ministry site above, again filling a country with zero current coverage.
- **verified**: yes — fetched `/Eng/index.aspx` directly; confirmed database identity, law/convention/search navigation, and traffic disclaimer text. Individual law pages (`LawAll.aspx?pcode=...`) confirmed live via WebSearch result snippets showing real article text, not independently re-fetched with WebFetch in this pass.

### 15. Singapore — data.gov.sg (open data portal)

- **name**: Singapore Open Data Portal
- **id**: `data_gov_sg`
- **base_url**: `https://www.data.gov.sg`
- **source_type feasibility**: possible NEW client if a relevant dataset/API exists (4,500+ datasets across 70+ agencies, general-purpose API layer) — **not confirmed** to carry an energy-efficiency, data-center, or district-cooling-specific dataset; the landing page's featured categories (Arts & Culture, Education, Economy, Environment, Geospatial, Housing, Health, Social, Transport) do not obviously include one.
- **level**: national
- **access**: none (open data portal; some datasets may require API tokens per-agency, not confirmed either way)
- **coverage**: region=`apac`/`singapore`; category=`regulatory`; policy_types=`report`. Lower confidence than other candidates — general-purpose portal, DC/energy relevance unconfirmed.
- **format**: JSON (API), CSV
- **practical**: would need a follow-up dataset-search pass (e.g., site search for "energy" or "PUE" within the portal) before this is actionable.
- **effort tier**: (c) needs a new structured client, contingent on finding a relevant dataset first
- **why worth adding**: Lowest-confidence entry included for completeness — flagging as a "worth a deeper look" rather than a ready candidate.
- **verified**: yes (portal exists and is live) / no (relevant dataset not confirmed) — fetched `https://www.data.gov.sg` directly and confirmed the portal is real and API-driven, but could not confirm energy/DC/district-cooling datasets from the landing page alone. **Recommend treating as needs-human-check for dataset relevance before building anything.**

---

## Unverified / needs-human-check

- **Guizhou Provincial Big Data Development and Management Bureau** (`https://dsj.guizhou.gov.cn`) — Guizhou is one of China's "national hub node" computing regions (东数西算 program) with its own big-data industry legislation (Guizhou Province Big Data Development and Application Promotion Regulations, effective Jan 1 2026) and a page of policy documents at `/zwgk/xxgkml/zcwj/zcfg/index.html`. **Could not verify**: every direct WebFetch attempt (root domain and two sub-paths) returned `connect ECONNREFUSED` from this environment. Content described above is from WebSearch result snippets only, not a direct fetch. This is exactly the kind of site the brief warns may be hard to reach — recommend a human check from a China-reachable network before adding.

- **Beijing DRC 2023 data-center energy-review rules** (`https://www.beijing.gov.cn/zhengce/zhengcefagui/202307/t20230706_3156356.html`, "关于进一步加强数据中心项目节能审查若干规定") — found via WebSearch, on-topic (DC project energy-conservation review rules), but not independently fetched in this session. Likely resolves given the same portal's other pages verified cleanly, but not confirmed directly — treat as probable, not certain.

- **Tokyo Bureau of Urban Development guideline landing page** (`https://www.toshiseibi.metro.tokyo.lg.jp/machizukuri/smarttokyo/datacenter`) — the guideline's *existence and content* were confirmed via a direct fetch of the March 2026 TMG press release, but this specific bureau subdomain path itself was only seen in WebSearch result titles, not independently re-fetched with WebFetch. Recommend a quick confirmation fetch before finalizing the `start_paths` list for entry #8.

- **Korea District Heating Corporation (KDHC)** (`https://www.kdhc.co.kr`) — state-run district heating utility (est. 1985), directly matches the brief's "district heating/cooling authorities" ask for Korea. WebFetch of the English business-overview page returned `connect ECONNREFUSED`. Not confirmed reachable in this session; worth a retry, as it may be a transient network issue rather than a block.

- **e-Gov Law API v2 machine-readable schema** — the API's existence, docs, and Swagger/ReDoc URLs are confirmed live (see candidate #7), but a direct WebFetch of the Swagger UI page returned only the page shell (client-side rendered), so the exact endpoint/parameter schema was not independently confirmed. A developer should open `/api/2/redoc/` in a real browser (or `curl` it) before writing the tier-c client.

---

## Summary of level distribution

- National: e-Gov API, Open Assembly API, Open Law API, KEA, MIIT, gov.cn, MOEAEA, law.moj.gov.tw, datacentre.gov.hk, EMSD, data.gov.sg
- Local/subnational: Beijing municipal government, Shanghai municipal government, Tokyo Bureau of Urban Development, Tokyo Bureau of Environment
- Unverified: Guizhou provincial bureau, KDHC
