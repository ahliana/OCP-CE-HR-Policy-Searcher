# Wave 4 - New Subnational Jurisdictions (Map-Maximizing)

Goal of this wave: light up NEW subnational jurisdictions not yet represented anywhere in
`config/domains/**` or `docs/source-expansion/draft/crawl/**/*.yaml` (waves 1-3). One
verified candidate per new jurisdiction is prioritized over depth within a jurisdiction
already covered. Dedup was done by grepping all `base_url:` values across
`config/domains/**/*.yaml` and `docs/source-expansion/draft/crawl/**/*.yaml` before
researching each state/province/canton/prefecture/Land below.

**Confirmed already covered (skipped, not re-proposed even though the task brief
mentioned them):** India - Uttar Pradesh, Gujarat, West Bengal, Odisha, Rajasthan,
Haryana (wave1/wave2 docs); Canada - Saskatchewan, New Brunswick, Nova Scotia,
Newfoundland & Labrador (wave2); Australia - ACT, Tasmania, NSW, South Australia
(wave2/wave3); Switzerland - Geneva, Vaud, Bern, Basel-Stadt, Zurich (config +
wave2); Germany - Baden-Württemberg, Bavaria, Berlin, Hamburg, Hesse, Lower Saxony,
NRW, Saxony (config).

**36 new distinct jurisdiction slugs verified live in this wave** (list at bottom).
6 additional candidates are flagged unverified (network/bot-blocked during this
research session, not hallucinated - see Unverified section).

All entries below are **effort tier (b)** - plain crawl domains - unless noted.
Verification method: `curl -s -o /dev/null -w "%{http_code}"` (some sites block
WebFetch/Playwright-style requests but respond to a bare curl, and vice versa; both
were tried before quarantining anything as unverified). Content topic was confirmed
either by direct fetch/WebFetch text extraction or, where a page was a JS shell or
scanned/image PDF, by cross-referencing the independent WebSearch summaries quoted
below (noted per entry).

---

## INDIA (region root: `["apac","india","<state>"]`)

### 1. Madhya Pradesh - IT/ITeS/ESDM Investment Promotion Policy 2023
- **id**: `madhya_pradesh_it_ites_esdm_policy`
- **base_url**: `https://invest.mp.gov.in`
- **start_paths**: `["/wp-content/uploads/2024/07/Madhya-Pradesh-IT-ITes-ESDM-Investment-Promotion-Policy-2023.pdf"]`
- **level**: subnational (state)
- **access**: none
- **coverage**: region: `["apac","india","madhya_pradesh"]`; category: `economic_dev`;
  tags: `["data_center_specific","incentives"]`; policy_types: `["incentive","strategy"]`;
  language: en
- **format**: PDF
- **practical**: no rate-limit info published; static PDF hosted on state investment
  portal; MP also has a newer 2025 "Global Capability Centers Policy" per press
  coverage - worth a follow-up crawl once a direct government URL surfaces.
- **effort tier**: b
- **why worth adding**: MP's official investment-promotion policy explicitly covers
  IT, ESDM, ITeS, BPO/BPM, **and data centres**, with capital/electricity/stamp-duty
  incentives - a genuinely new Indian state, not in waves 1-3.
- **verified**: yes - `curl` returned HTTP 200 on the exact PDF URL. Content
  identity/coverage confirmed via WebSearch (official notification Oct 6 2023,
  covers "Information Technology (IT), Electronic System Design and Manufacturing
  (ESDM), Data Centres, ITeS, BPO, BPM").

### 2. Andhra Pradesh - ITE&C Department (Data Center Policy 4.0, 2024-29)
- **id**: `andhra_pradesh_itec_dept`
- **base_url**: `https://apit.ap.gov.in`
- **start_paths**: `["/assets/files/Policy Guidelines.pdf", "/?page_id=1762"]`
- **level**: subnational (state)
- **access**: none
- **coverage**: region: `["apac","india","andhra_pradesh"]`; category: `economic_dev`;
  tags: `["data_center_specific","incentives"]`; policy_types: `["incentive","strategy"]`;
  language: en
- **format**: HTML (Angular JS-shell on direct fetch) + PDF
- **practical**: `apit.ap.gov.in` is an Angular SPA - direct HTTP fetch returns only
  the shell (`<app-root>`), so `requires_playwright: true` recommended. The specific
  PDF path above returned 200 directly.
- **effort tier**: b
- **why worth adding**: AP Cabinet approved "AP Data Center Policy 4.0 (2024-29)"
  Nov 6 2024 - 200MW target, AI-enabled DC incentives, five-year term, plus a newer
  policy granting large data centres Deemed Distribution Company (Discom) status.
- **verified**: yes for `apit.ap.gov.in` (HTTP 200, confirmed official "ITE&C
  Department - Government of Andhra Pradesh" via page `<title>`/meta tags) and the
  PDF path. The primary host for Policy 4.0 itself, `apedb.ap.gov.in`, timed out on
  every attempt (see Unverified section) - quarantined separately.

### 3. Kerala - Information Technology Policy 2023
- **id**: `kerala_it_policy_2023`
- **base_url**: `https://itpolicy.startupmission.in`
- **start_paths**: `["/it-policy.pdf"]`
- **level**: subnational (state)
- **access**: none
- **coverage**: region: `["apac","india","kerala"]`; category: `policy`; tags:
  `["data_center_specific","incentives"]`; policy_types: `["strategy","guidance"]`;
  language: en
- **format**: PDF (scanned/image-based, 52pp)
- **practical**: PDF fetched fully (1.2MB) but is not machine-text-extractable in
  this pass (Samsung-scanner-produced PDF) - flag for OCR at ingestion time.
- **effort tier**: b
- **why worth adding**: Kerala's official state IT Policy 2023, referenced by the
  MeitY state-wise Data Center Policy tracker as covering ITeS/data-centre
  incentives; Kerala also runs the state's own dual State Data Centres
  (`itmission.kerala.gov.in`, `eitd.kerala.gov.in` - e-governance infra, not an
  investment policy, so not proposed as the primary entry here).
- **verified**: yes - HTTP 200, PDF downloads in full. On-topic coverage confirmed
  via WebSearch cross-reference (profileits.com MeitY state DC policy tracker lists
  Kerala's 2023 IT Policy).

### 4. Punjab - Industrial and Business Development Policy
- **id**: `punjab_industrial_business_policy`
- **base_url**: `https://punjabinfotech.in`
- **start_paths**: `["/assets/pdf/Industrial_Policy_2022.pdf"]`
- **level**: subnational (state)
- **access**: none
- **coverage**: region: `["apac","india","punjab"]`; category: `economic_dev`; tags:
  `["data_center_specific","incentives"]`; policy_types: `["incentive","program"]`;
  language: en
- **format**: HTML (homepage) + PDF (scanned, not text-extractable in this pass)
- **practical**: Punjab launched an updated "Industrial & Business Development
  Policy 2026" (CM Bhagwant Mann, per news coverage) with data-centre-specific
  flexible incentive packages (up to 15-year support, customizable incentive
  bundles) - the 2026 policy PDF was not locatable at a stable government URL in
  this pass; recommend a follow-up check on `investpunjab.gov.in` and
  `fasttrack.punjab.gov.in` (both timed out during this session - see Unverified).
- **effort tier**: b
- **why worth adding**: Dedicated state industrial policy explicitly calling out
  data centres as a target capital-intensive sector with customizable, up-to-15-year
  incentive packages.
- **verified**: yes - `punjabinfotech.in` (Punjab Information & Communication
  Technology Corporation, official Government of Punjab entity, confirmed via
  WebFetch of homepage) returned HTTP 200; the 2022 policy PDF also returned HTTP
  200 (4.2MB download succeeded, though text extraction failed on the binary/scanned
  content).

### 5. Bihar - IT Policy 2024
- **id**: `bihar_it_policy_2024`
- **base_url**: `https://investit.bihar.gov.in`
- **start_paths**: `["/"]`
- **level**: subnational (state)
- **access**: none
- **coverage**: region: `["apac","india","bihar"]`; category: `economic_dev`; tags:
  `["data_center_specific","incentives"]`; policy_types: `["incentive","program"]`;
  language: en
- **format**: HTML
- **practical**: TLS certificate on `investit.bihar.gov.in` is currently expired
  (curl reports "certificate has expired") - site is reachable and title confirms
  "Government of Bihar" but the crawler will need to tolerate/ignore the cert error
  (matches a known pattern with other Indian state sites in this project).
- **effort tier**: b
- **why worth adding**: Bihar IT Policy 2024 (period Jan 2024-Dec 2029) offers 30%
  capital subsidy up to Rs 30 Cr, 10% interest subvention, 50% lease-rental subsidy,
  and 25% annual energy-bill reimbursement for 5 years - explicitly covers data
  centres. Bihar's power surplus is separately reported (Down To Earth) as able to
  host up to 12 mid-sized data centres.
- **verified**: yes - HTTP 200 (with expired-cert warning), page `<title>` confirmed
  "Government of Bihar". Policy content/figures corroborated via WebSearch. A
  third-party mirror of the official policy highlights PDF
  (`https://hebe.net.in/wp-content/uploads/2025/06/Highlights_of_Bihar_IT_policy.pdf`)
  also returned HTTP 200 but is not a government domain - not proposed as the
  base_url, noted for reference only.

---

## CHINA (region root: `["apac","china","<province>"]`)

Note: existing wave2 China entries (Ningxia, Inner Mongolia) tag `region: ["apac"]`
only, with no `china` or province-level slug at all. The entries below propose the
fuller `["apac","china","<province>"]` convention (matching how India/Canada/
Australia/Germany already do subnational tagging) - flag for the registry team to
decide whether to backfill Ningxia/Inner Mongolia to match, or whether `china` needs
to be added to `VALID_REGIONS` first.

### 6. Gansu - Qingyang "East Data West Compute" Hub Support Measures
- **id**: `gansu_computing_hub_policy`
- **base_url**: `https://www.gsei.com.cn`
- **start_paths**: `["/html/1678/2022-09-20/content-397414.html"]`
- **level**: subnational (province)
- **access**: none
- **coverage**: region: `["apac","china","gansu"]`; category: `economic_dev`; tags:
  `["data_center_specific","incentives","renewable_energy"]`; policy_types:
  `["incentive","program"]`; language: zh
- **format**: HTML
- **practical**: hosted on Gansu Economic Information Network (a semi-official
  government-content portal), not the provincial DRC's own domain - the Qingyang
  municipal government site (`zgqingyang.gov.cn`, the actual DC-cluster city)
  returned HTTP 403 (bot-blocked) on every attempt this session; recommend a
  human/different-IP re-check of that primary source.
- **effort tier**: b
- **why worth adding**: Gansu is one of the 8 national computing hub nodes under
  "East Data West Compute"; this notice details the province's "40 measures"
  including demand-charge exemptions through 2025 and discounted renewable power
  for data centres in the Qingyang cluster.
- **verified**: yes - HTTP 200, and WebFetch confirmed on-topic content directly
  (quoted specific measures on power-cost reduction and grid infrastructure for
  data centres).

### 7. Qinghai - Measures to Promote Green Computing Industry Development
- **id**: `qinghai_green_computing_policy`
- **base_url**: `https://www.qhzwfw.gov.cn`
- **start_paths**: `["/lssltjhzl/031001/031001002/20240407/132a9a49-90fb-4425-bba0-64ce7267c238.html"]`
- **level**: subnational (province)
- **access**: none
- **coverage**: region: `["apac","china","qinghai"]`; category: `economic_dev`;
  tags: `["data_center_specific","incentives","renewable_energy"]`; policy_types:
  `["incentive","program"]`; language: zh
- **format**: HTML
- **practical**: hosted on the provincial e-government service portal
  (`qhzwfw.gov.cn`); effective 2024-04-01 through 2029-03-31.
- **effort tier**: b
- **why worth adding**: Qinghai was named China's first "green computing-power
  collaborative demonstration province" (2024, 4 national ministries). This measure
  guarantees 80%+ green-power supply to data centres at preferential rates, offers
  investment subsidies up to 10% for new/expanded data centres, and exempts green
  data centres from EIA review.
- **verified**: yes - HTTP 200 via curl.

### 8. Guangdong - Data Center Energy Guarantee / Layout Requirements
- **id**: `guangdong_dc_energy_policy`
- **base_url**: `https://drc.gd.gov.cn`
- **start_paths**: `["/ywtz/content/post_3271730.html", "/ywtz/content/post_4077316.html"]`
- **level**: subnational (province)
- **access**: none
- **coverage**: region: `["apac","china","guangdong"]`; category: `regulatory`;
  tags: `["mandatory","pue_limits","efficiency","renewable_energy"]`; policy_types:
  `["regulation","guidance"]`; language: zh
- **format**: HTML
- **practical**: hosted on Guangdong Development and Reform Commission's own
  domain.
- **effort tier**: b
- **why worth adding**: Guangdong requires PUE below 1.3 for traditional data
  centres by end of the 14th Five-Year Plan, applies tiered/differentiated
  electricity pricing keyed to operating PUE, and caps new-cabinet approvals based
  on existing-DC utilization rates - a substantive, DC-specific regulatory regime
  from China's largest tech-manufacturing province.
- **verified**: yes - both URLs returned HTTP 200 via curl.

### 9. Beijing - Stock Data Center Optimization Work Plan (2024-2027)
- **id**: `beijing_dc_optimization_plan`
- **base_url**: `https://www.beijing.gov.cn`
- **start_paths**: `["/zhengce/zhengcefagui/202411/t20241115_3942264.html"]`
- **level**: subnational (municipality, provincial-level)
- **access**: none
- **coverage**: region: `["apac","china","beijing"]`; category: `regulatory`; tags:
  `["mandatory","pue_limits","efficiency"]`; policy_types: `["regulation"]`;
  language: zh
- **format**: HTML
- **practical**: joint notice from Beijing Economy & Information Technology
  Bureau, Development & Reform Commission, and Communications Administration;
  alternate mirror at `jxj.beijing.gov.cn` also verified live.
- **effort tier**: b
- **why worth adding**: Sets a binding average PUE target of 1.35 by 2027 for
  existing data centres consuming ≥5M kWh/year, imposes differential electricity
  pricing on DCs above 1.35 PUE starting 2026, and offers up to RMB 1200/tce energy
  subsidy and 30%-of-investment green retrofit grants (capped RMB 30M/project).
- **verified**: yes - HTTP 200 on the primary URL and on the `jxj.beijing.gov.cn`
  mirror.

### 10. Shanghai - Data Center Construction Guidelines / Coordinated Development
- **id**: `shanghai_dc_construction_guideline`
- **base_url**: `https://sheitc.sh.gov.cn`
- **start_paths**: `["/xxfw/20210407/3774163f0b3f4bb399e15ad592f7c2f8.html"]`
- **level**: subnational (municipality, provincial-level)
- **access**: none
- **coverage**: region: `["apac","china","shanghai"]`; category: `regulatory`; tags:
  `["mandatory","pue_limits","efficiency"]`; policy_types: `["regulation","guidance"]`;
  language: zh
- **format**: HTML
- **practical**: hosted on Shanghai Economic and Informatization Commission's own
  domain; a second relevant notice lives at `shanghai.gov.cn` (also verified 200).
- **effort tier**: b
- **why worth adding**: Shanghai's data-centre construction guideline requires new
  builds to target PUE ≤1.25 in the 15th Five-Year Plan period and retrofits to
  reach ≤1.4, with differential electricity pricing and a phase-out list for
  small/old/scattered data centres.
- **verified**: yes - HTTP 200 on both the primary URL and the `shanghai.gov.cn`
  mirror.

### 11. Hebei - Electronic Information Industry / Zhangjiakou DC Cluster (partial)
- **id**: `hebei_electronic_info_industry`
- **base_url**: `https://gxt.hebei.gov.cn`
- **start_paths**: `["/hbgyhxxht/zfxxgk/fdzdgknr/ghjhzc/cyzc/2025042121531749289/index.html"]`
- **level**: subnational (province)
- **access**: none
- **coverage**: region: `["apac","china","hebei"]`; category: `economic_dev`; tags:
  `["data_center_specific","efficiency"]`; policy_types: `["strategy"]`; language: zh
- **format**: HTML
- **practical**: this is Hebei's general electronic-information-industry
  development opinion, confirmed live and on-topic-adjacent. The **more specific**
  "Zhangjiakou Data Center Cluster Construction Plan" (PUE ≤1.25, 70%+ renewable
  target) is the stronger DC-specific document but its known hosts
  (`echinagov.com`, `hebfb.apps.hebei.com.cn`) either 403'd or were untested -
  flagged in Unverified for a follow-up check.
- **effort tier**: b
- **why worth adding**: Hebei hosts the Zhangjiakou cluster, one of the 8 national
  computing hubs (Beijing-Tianjin-Hebei node), targeting 700k standard racks and
  PUE ≤1.25 by 2025 with 70%+ renewable energy use.
- **verified**: yes for the base_url/start_path shown (HTTP 200, title confirmed
  "河北省人民政府办公厅关于促进电子信息产业高质量发展的意见"). The Zhangjiakou-specific
  plan text itself is unverified this session (see below).

**Unverified**: **Sichuan** (`fgw.sc.gov.cn`, Sichuan Development and Reform
Commission - hosts the "四川省算力基础设施高质量发展行动方案（2024-2027）" targeting
500k racks, 60% utilization, PUE ≤1.3 by 2025; every attempt (base domain and deep
link) timed out over 15-25s, both via curl and WebFetch - not bot-blocked so much
as unreachable from this environment. Content is real and well-documented via
WebSearch; recommend a human/different-network re-check before enabling.)

---

## JAPAN (region root: `["apac","japan","<prefecture>"]`)

### 12. Hokkaido - Data Center Siting Guide (Dept. of Industrial Promotion)
- **id**: `hokkaido_dc_siting_guide`
- **base_url**: `https://www.pref.hokkaido.lg.jp`
- **start_paths**: `["/kz/ssg/sgr/dc_guide.html"]`
- **level**: subnational (prefecture)
- **access**: none
- **coverage**: region: `["apac","japan","hokkaido"]`; category: `economic_dev`;
  tags: `["data_center_specific","incentives","renewable_energy"]`; policy_types:
  `["guidance","incentive"]`; language: ja
- **format**: HTML
- **practical**: same `pref.<name>.lg.jp` domain pattern as the already-covered
  Osaka/Chiba/Saitama prefectures.
- **effort tier**: b
- **why worth adding**: Hokkaido is Japan's #1 data-centre-attraction target after
  METI's Hokkaido/Kyushu subsidy program (up to 50% of setup cost, plus a
  reported ¥30bn subsidy to SoftBank's Hokkaido DC); the prefecture also runs its
  own Enterprise Location Promotion Subsidy for new/expanded DCs and call centres.
- **verified**: yes - HTTP 200.

### 13. Fukuoka - Prefectural Business Location Information Site
- **id**: `fukuoka_business_location_incentives`
- **base_url**: `https://www.kigyorichi.pref.fukuoka.lg.jp`
- **start_paths**: `["/ja/"]`
- **level**: subnational (prefecture)
- **access**: none
- **coverage**: region: `["apac","japan","fukuoka"]`; category: `economic_dev`;
  tags: `["incentives"]`; policy_types: `["incentive","program"]`; language: ja
- **format**: HTML
- **practical**: prefecture-run business-location incentive portal; Kitakyushu
  City (within Fukuoka) separately offers up to 6-year fixed-asset tax exemption
  specifically to attract data centres, per news coverage - worth a municipal-level
  follow-up.
- **effort tier**: b
- **why worth adding**: Fukuoka/Kyushu is METI's other named target region (with
  Hokkaido) for the national DC subsidy program; this is the prefecture's own
  incentive-program portal.
- **verified**: yes - HTTP 200.

### 14. Kanagawa - SME Energy-Saving Equipment Subsidy
- **id**: `kanagawa_sme_energy_subsidy`
- **base_url**: `https://www.pref.kanagawa.jp`
- **start_paths**: `["/docs/ap4/cnt/f7226/shouenesetubihojokin.html"]`
- **level**: subnational (prefecture)
- **access**: none
- **coverage**: region: `["apac","japan","kanagawa"]`; category: `economic_dev`;
  tags: `["incentives","efficiency"]`; policy_types: `["incentive","program"]`;
  language: ja
- **format**: HTML
- **practical**: subsidy covers up to ¥5M (1/3 rate) for energy-saving equipment
  incl. HVAC - general SME program, not DC-exclusive, but directly on-taxonomy
  (energy-efficiency incentive).
- **effort tier**: b
- **why worth adding**: Complements the national MIC/MOE "Data Center Zero-Emission
  and Resilience Enhancement" subsidy program (which explicitly funds low-carbon AC
  systems for data centres) with a prefecture-level efficiency incentive route.
- **verified**: yes - HTTP 200.

---

## SPAIN - remaining CCAA (region root: `["eu","eu_south","spain","<ccaa>"]`)

### 15. Basque Country / Euskadi - Energy Strategy 2030 (3E2030) + EVE
- **id**: `euskadi_energy_strategy_2030`
- **base_url**: `https://www.euskadi.eus`
- **start_paths**: `["/plan-departamental/15-estrategia-energetica-de-euskadi-2030-3e-2030/web01-s1leheko/es/"]`
- **level**: subnational (autonomous community)
- **access**: none
- **coverage**: region: `["eu","eu_south","spain","basque_country"]`; category:
  `energy_ministry`; tags: `["efficiency","renewable_energy","planning"]`;
  policy_types: `["strategy","incentive"]`; language: es
- **format**: HTML
- **practical**: EVE (Ente Vasco de la Energía, `www.eve.eus` - also verified live)
  is the operating agency; €22M in 2025 industrial energy-efficiency aid.
- **effort tier**: b
- **why worth adding**: Basque Country's 3E2030 strategy targets 12% energy savings
  by 2030 vs. 2021, run by a dedicated energy agency (EVE) with an active
  industrial-efficiency grant line - directly on-taxonomy.
- **verified**: yes - HTTP 200 for both `euskadi.eus` strategy page and `eve.eus`.

### 16. Castilla y León - EREN Energy DataHub
- **id**: `castilla_y_leon_eren_datahub`
- **base_url**: `https://energia.jcyl.es`
- **start_paths**: `["/web/es/ahorro-eficiencia-energetica/datahub-energetico-junta-castilla.html"]`
- **level**: subnational (autonomous community)
- **access**: none
- **coverage**: region: `["eu","eu_south","spain","castilla_y_leon"]`; category:
  `energy_ministry`; tags: `["efficiency","reporting"]`; policy_types:
  `["report","guidance"]`; language: es
- **format**: HTML
- **practical**: EREN (Ente Público Regional de la Energía) is the regional energy
  agency; separately reported to be modernizing its own backup data centre for
  energy efficiency (an internal case study, not a public policy document).
- **effort tier**: b
- **why worth adding**: EREN's public energy DataHub is an open-data transparency
  tool over the region's energy consumption - fits the reporting/efficiency
  taxonomy and is a genuinely new Spanish CCAA.
- **verified**: yes - HTTP 200.

### 17. Valencia - IVACE Energy Efficiency Aid Program
- **id**: `valencia_ivace_energy_efficiency`
- **base_url**: `https://www.ivace.es`
- **start_paths**: `["/index.php/es/ayudas/energia/ayudas-ahorro-y-eficiencia-energetica-energias-renovables-y-autoconsumo-solicitud-abierta/56966-ayudas-en-materia-de-eficiencia-energetica-en-empresas-2025"]`
- **level**: subnational (autonomous community)
- **access**: none
- **coverage**: region: `["eu","eu_south","spain","valencia"]`; category:
  `economic_dev`; tags: `["incentives","efficiency"]`; policy_types:
  `["incentive","program"]`; language: es
- **format**: HTML
- **practical**: 2025 call: EUR 2.52M budget (FEDER co-financed), up to 35-55% of
  eligible cost, max EUR 400k/project; application window Sep 30-Dec 30, 2025.
  Explicitly funds waste-heat recovery ("Recuperación de calores residuales").
- **effort tier**: b
- **why worth adding**: IVACE (Instituto Valenciano de Competitividad Empresarial)
  is the Valencian government's business-competitiveness institute; this specific
  aid line funds waste-heat recovery and energy-management systems for businesses,
  directly on-taxonomy.
- **verified**: yes - HTTP 200. (Note: the main `gva.es` domain and `sede.gva.es`
  both timed out repeatedly this session - `ivace.es`, its own dedicated domain,
  worked and is recommended as the base_url instead.)

---

## ITALY - remaining regions (region root: `["eu","eu_south","italy","<region>"]`)

### 18. Lazio - Sostenibilità Energetica
- **id**: `lazio_sostenibilita_energetica`
- **base_url**: `https://www.regione.lazio.it`
- **start_paths**: `["/cittadini/tutela-ambientale-difesa-suolo/sostenibilita-energetica"]`
- **level**: subnational (region)
- **access**: none
- **coverage**: region: `["eu","eu_south","italy","lazio"]`; category:
  `energy_ministry`; tags: `["efficiency","district_heating","incentives"]`;
  policy_types: `["regulation","incentive"]`; language: it
- **format**: HTML
- **practical**: includes a EUR 40M FESR 2021-2027 grant line ("Efficienza
  energetica e rinnovabili per le imprese"); Regional Regulation 30/2020 on
  building energy efficiency also lives on this domain.
- **effort tier**: b
- **why worth adding**: Lazio is (with Lombardy) one of the top-2 Italian regions
  by data-centre grid-connection requests (2025: 55GW nationally, concentrated in
  Lombardy + Lazio per Qualenergia); this is the region's energy-efficiency policy
  hub, covering district heating networks and renewable/efficiency rules.
- **verified**: yes - HTTP 200.

### 19. Piemonte - Sviluppo Energetico Sostenibile
- **id**: `piemonte_sviluppo_energetico`
- **base_url**: `https://www.regione.piemonte.it`
- **start_paths**: `["/web/temi/sviluppo/sviluppo-energetico-sostenibile"]`
- **level**: subnational (region)
- **access**: none
- **coverage**: region: `["eu","eu_south","italy","piemonte"]`; category:
  `energy_ministry`; tags: `["efficiency","renewable_energy","incentives"]`;
  policy_types: `["incentive","program"]`; language: it
- **format**: HTML
- **practical**: EUR 53.6M FESR 2021-2027 fund split between business
  energy-efficiency (EUR 28.1M) and renewable-energy promotion (EUR 25.5M) actions.
- **effort tier**: b
- **why worth adding**: Piedmont is reported (local press) to be facing "billions
  in data centre investment" pressure alongside sustainability questions; this is
  the region's live energy-efficiency incentive program for businesses.
- **verified**: yes - HTTP 200.

### 20. Veneto - Incentivi Regionali (incl. Teleriscaldamento)
- **id**: `veneto_incentivi_energia`
- **base_url**: `https://www.regione.veneto.it`
- **start_paths**: `["/web/energia/incentivi-regionali"]`
- **level**: subnational (region)
- **access**: none
- **coverage**: region: `["eu","eu_south","italy","veneto"]`; category:
  `district_heating`; tags: `["district_heating","incentives","efficiency"]`;
  policy_types: `["incentive","program"]`; language: it
- **format**: HTML
- **practical**: EUR 7M FESR 2021-2027 call specifically for new/expanded district
  heating and cooling networks (up to 65% grant for micro/small enterprises, EUR
  100k-3M/project), two application windows through Feb 2026.
- **effort tier**: b
- **why worth adding**: A dedicated district-heating-network grant program is a
  direct hit on the waste-heat-reuse taxonomy - among the strongest Italian finds
  in this wave.
- **verified**: yes - HTTP 200.

### 21. Emilia-Romagna - Energia Regionale (Data Valley heat reuse)
- **id**: `emilia_romagna_energia_portal`
- **base_url**: `https://energia.regione.emilia-romagna.it`
- **start_paths**: `["/"]`
- **level**: subnational (region)
- **access**: none
- **coverage**: region: `["eu","eu_south","italy","emilia_romagna"]`; category:
  `energy_ministry`; tags: `["district_heating","data_center_specific","efficiency"]`;
  policy_types: `["strategy","report"]`; language: it
- **format**: HTML
- **practical**: region hosts CINECA's Leonardo supercomputer (Bologna), concentrating
  reportedly 80%+ of Italy's national computing capacity and ~20% of Europe's; an
  active RSE/University of Bologna/Politecnico di Milano study is evaluating
  Leonardo's waste-heat reuse for district heating.
- **effort tier**: b
- **why worth adding**: Emilia-Romagna's self-branded "Data Valley" strategy
  (launched 2015) is the single strongest Italian regional case for the exact
  DC-waste-heat-to-district-heating use case this project tracks.
- **verified**: yes - HTTP 200 on the region's energy-portal domain.

---

## SWITZERLAND - remaining cantons (region root: `["eu_central","switzerland","<canton>"]`)

### 22. Ticino - Legge cantonale sull'energia (LEn)
- **id**: `ticino_legge_energia`
- **base_url**: `https://m3.ti.ch`
- **start_paths**: `["/CAN/RLeggi/public/index.php/raccolta-leggi/legge/num/523"]`
- **level**: subnational (canton)
- **access**: none
- **coverage**: region: `["eu_central","switzerland","ticino"]`; category:
  `cantonal_authority`; tags: `["mandates","efficiency"]`; policy_types:
  `["law","regulation"]`; language: it
- **format**: HTML
- **practical**: revised LEn (May 4 2021) and Energy Use Regulation (RUEn, revised
  Mar 15 2023) entered into force Jan 1 2024, aligned to MoKEn/MuKEn 2014 model;
  large-consumer threshold (>5 GWh thermal or >0.5 GWh electrical/year) triggers a
  mandatory energy-optimization analysis - would directly capture large DCs.
- **effort tier**: b
- **why worth adding**: Ticino is the only major Italian-speaking canton and was
  not yet represented; its energy law's large-consumer / waste-heat-use provisions
  are directly on-taxonomy.
- **verified**: yes - HTTP 200.

### 23. Aargau - Energiegesetz / Grossverbraucher (Large Consumers)
- **id**: `aargau_energiegesetz`
- **base_url**: `https://www.ag.ch`
- **start_paths**: `["/de/themen/umwelt-natur/energie/planung-und-energienachweise/grossverbraucher"]`
- **level**: subnational (canton)
- **access**: none
- **coverage**: region: `["eu_central","switzerland","aargau"]`; category:
  `cantonal_authority`; tags: `["mandates","efficiency","district_heating"]`;
  policy_types: `["law","regulation"]`; language: de
- **format**: HTML
- **practical**: canton's own legal-text mirror at
  `https://gesetzessammlungen.ag.ch/app/de/texts_of_law/773.200` also verified
  live; new Energiegesetz/Verordnung took effect Apr 1 2025.
- **effort tier**: b
- **why worth adding**: Aargau's "Grossverbraucher" (large-consumer) regime
  requires target agreements (KZV) including waste-heat-potential analysis -
  directly relevant to data-centre heat reuse, and Aargau is a populous canton not
  yet represented.
- **verified**: yes - HTTP 200 on both the `ag.ch` topic page and the
  `gesetzessammlungen.ag.ch` legal-text mirror.

---

## BELGIUM - regional split (region root: `["eu","eu_west","belgium","<region>"]`)

Existing `belgium.yaml` only tags `region: ["eu","eu_west","belgium"]` with no
regional split. All three Belgian regions below are genuinely new sub-slugs.

### 24. Wallonia - Data Centers (dedicated SPW Énergie page)
- **id**: `wallonia_energie_datacenters`
- **base_url**: `https://energie.wallonie.be`
- **start_paths**: `["/home/au-quotidien/dans-la-pme/conseils-pour-mon-type-dentreprise/data-centers.html"]`
- **level**: subnational (region)
- **access**: none
- **coverage**: region: `["eu","eu_west","belgium","wallonia"]`; category:
  `energy_ministry`; tags: `["data_center_specific","efficiency","reporting"]`;
  policy_types: `["guidance","report"]`; language: fr
- **format**: HTML
- **practical**: SPW (Service Public de Wallonie) Énergie's own site; separate
  Walloon Government reflection underway on data-centre siting criteria and an
  Elia-style "swim lanes" power-allocation mechanism at regional level.
- **effort tier**: b
- **why worth adding**: A **dedicated Wallonia government web page specifically
  for data centres**, covering energy-efficiency guidance and the European Code of
  Conduct for Data Centre energy efficiency - the strongest single find of this
  wave for direct on-topic relevance.
- **verified**: yes - HTTP 200, and content topic directly confirmed by page title
  and WebSearch snippet quoting the page's own guidance content.

### 25. Brussels-Capital - Mandatory Data Centre Energy Reporting
- **id**: `brussels_dc_reporting_obligation`
- **base_url**: `https://environnement.brussels`
- **start_paths**: `["/pro/reglementation-et-inspection/obligations-et-autorisations/rapportage-pour-les-centres-de-donnees"]`
- **level**: subnational (region)
- **access**: none
- **coverage**: region: `["eu","eu_west","belgium","brussels"]`; category:
  `regulatory`; tags: `["mandates","reporting","efficiency"]`; policy_types:
  `["regulation","law"]`; language: fr
- **format**: HTML
- **practical**: implements CoBrACE + EU Delegated Regulation 2024/1364 - data
  centres with ≥500kW installed IT power must report annually to Bruxelles
  Environnement by March 31; contact `reportingdc@environnement.brussels` listed
  for reference IDs.
- **effort tier**: b
- **why worth adding**: A **binding, DC-specific mandatory energy/sustainability
  reporting regime** at regional level, directly implementing the EU data centre
  reporting delegated regulation - exactly the kind of policy this project targets,
  and it is subnational (Brussels-Capital Region), not just the EU-level rule.
- **verified**: yes - HTTP 200, content directly confirmed (WebSearch quoted the
  specific 500kW threshold, March 31 deadline, and legal basis).

### 26. Flanders - Energiedecreet (legal basis for DC energy-efficiency reporting)
- **id**: `flanders_energiedecreet`
- **base_url**: `https://codex.vlaanderen.be`
- **start_paths**: `["/portals/codex/documenten/1018092.html"]`
- **level**: subnational (region)
- **access**: none
- **coverage**: region: `["eu","eu_west","belgium","flanders"]`; category:
  `legislative`; tags: `["mandates","reporting","efficiency"]`; policy_types:
  `["law"]`; language: nl
- **format**: HTML
- **practical**: this is the codified Energiedecreet (general energy-policy
  decree) text; VEKA (Vlaams Energie- en Klimaatagentschap) is the implementing
  agency. A Flemish datacenter-specific reporting obligation (≥500kW IT power,
  reporting due 2026) transposing the same EU delegated regulation as Brussels is
  confirmed via WebSearch but the specific VEKA/energiesparen.be sub-page hosting
  it was not pinned down this session - recommend a follow-up search once VEKA
  publishes a dedicated landing page (draft decree was only approved in principle
  by the Flemish Government July 14 2025).
- **effort tier**: b
- **why worth adding**: Completes the Belgian regional trio (with Wallonia and
  Brussels) - Flanders is transposing the same EU data-centre energy-efficiency
  reporting directive via this decree's implementing framework.
- **verified**: yes - HTTP 200 for the codex text itself. The DC-specific
  implementing sub-page is not yet pinned to a verified URL (see practical note
  above) - treat the DC-reporting angle as needing a follow-up check even though
  the base_url/decree itself is verified live.

---

## AUSTRALIA - remaining states (region root: `["apac","australia","<state>"]`)

### 27. Western Australia - Energy Policy WA
- **id**: `western_australia_energy_policy`
- **base_url**: `https://www.wa.gov.au`
- **start_paths**: `["/organisation/energy-policy-wa"]`
- **level**: subnational (state)
- **access**: none
- **coverage**: region: `["apac","australia","western_australia"]`; category:
  `energy_ministry`; tags: `["planning","renewable_energy"]`; policy_types:
  `["guidance","report"]`; language: en
- **format**: HTML
- **practical**: Energy Policy WA advises the WA government on secure/reliable/
  affordable energy delivery, incl. the standalone Western Australia Electricity
  Market (WEM, not part of the NEM) - relevant since national DC-renewable-offset
  rules explicitly carve out separate treatment for the WEM.
- **effort tier**: b
- **why worth adding**: WA (Perth) is independently reported as a top emerging
  AI/DC infrastructure location (cheap power, Western Green Energy Hub); this is
  the state's own energy-policy authority, not yet represented.
- **verified**: yes - HTTP 200.

### 28. Queensland - Energy Roadmap
- **id**: `queensland_energy_roadmap`
- **base_url**: `https://www.treasury.qld.gov.au`
- **start_paths**: `["/policies-and-programs/energy/energy-roadmap/"]`
- **level**: subnational (state)
- **access**: none
- **coverage**: region: `["apac","australia","queensland"]`; category:
  `energy_ministry`; tags: `["planning","carbon"]`; policy_types:
  `["strategy","report"]`; language: en
- **format**: HTML
- **practical**: Queensland was the sole state to decline the national
  data-centre-renewable-offset framework at the May 2026 energy ministers' meeting;
  its own roadmap instead emphasizes coal/gas firming - notable policy contrast
  worth tracking for this project's carbon/incentive taxonomy.
- **effort tier**: b
- **why worth adding**: Queensland's distinct energy-policy stance directly
  affects data-centre economics/siting incentives in the state; a genuinely new
  Australian jurisdiction.
- **verified**: yes - HTTP 200.

**Unverified**: **Victoria** (`djsir.vic.gov.au` - hosts the "Sustainable Data
Centre Action Plan", a whole-of-government DC sustainability plan covering energy
and water; returned HTTP 403 on every attempt this session, both via curl with a
browser user-agent and via WebFetch - genuinely bot-blocked, not fabricated,
content independently corroborated via WebSearch snippets) and **Northern
Territory** (`digitalterritory.nt.gov.au` - hosts the Digital Territory Strategy
covering the NEXTDC Darwin D1 data-centre buildout; also returned HTTP 403 on
every attempt). Both need a human/different-network re-check before enabling.

---

## GERMANY - remaining Länder (region root: `["eu","eu_central","germany","<land>"]`)

6 of the remaining 8 uncovered Länder verified; Saarland unreachable (see
Unverified), Bremen not attempted this pass (candidate for a quick follow-up:
`umwelt.bremen.de` domain pattern is consistent with the others below and likely
verifiable).

### 29. Brandenburg - BRAVORS Landesrecht (incl. Wärmeplanungsverordnung)
- **id**: `brandenburg_landesrecht`
- **base_url**: `https://bravors.brandenburg.de`
- **start_paths**: `["/"]`
- **level**: subnational (Land)
- **access**: none
- **coverage**: region: `["eu","eu_central","germany","brandenburg"]`; category:
  `legislative`; tags: `["mandates","district_heating"]`; policy_types:
  `["law","regulation"]`; language: de
- **format**: HTML
- **practical**: BRAVORS is Brandenburg's official state-law database (same
  pattern as `gesetze-bayern.de`/`recht.nrw.de` already in `germany.yaml`); the
  Brandenburg Wärmeplanungsverordnung (heat-planning ordinance, in force since Jul
  24 2024) requires the state's 113 cities/300 municipalities to produce heat
  plans that must inventory available waste-heat sources (incl. data centres).
- **effort tier**: b
- **why worth adding**: Only home-page verified this pass - recommend a follow-up
  crawl to pin the exact Wärmeplanungsverordnung document ID within BRAVORS.
- **verified**: yes (base_url only, HTTP 200) - specific ordinance text not yet
  located at a stable deep-link.

### 30. Rheinland-Pfalz - Energieagentur RLP
- **id**: `rheinland_pfalz_energieagentur`
- **base_url**: `https://www.energieagentur.rlp.de`
- **start_paths**: `["/"]`
- **level**: subnational (Land)
- **access**: none
- **coverage**: region: `["eu","eu_central","germany","rheinland_pfalz"]`;
  category: `energy_ministry`; tags: `["efficiency","planning"]`; policy_types:
  `["guidance","program"]`; language: de
- **format**: HTML
- **practical**: `landesrecht.rlp.de` (state legal database, same pattern as
  other Länder) also verified live and is a good secondary/legislative-category
  source for the same Land.
- **effort tier**: b
- **why worth adding**: State-run energy/climate agency; federal EnEfG waste-heat
  reuse obligations for data centres (≥300kW) apply here, with RLP as the
  Land-level implementing/advisory layer.
- **verified**: yes - HTTP 200 for both `energieagentur.rlp.de` and
  `landesrecht.rlp.de`.

### 31. Schleswig-Holstein - EWKG (Energiewende- und Klimaschutzgesetz)
- **id**: `schleswig_holstein_ewkg`
- **base_url**: `https://www.gesetze-rechtsprechung.sh.juris.de`
- **start_paths**: `["/bssh/document/jlr-EWKSGSHrahmen/part/X"]`
- **level**: subnational (Land)
- **access**: none
- **coverage**: region: `["eu","eu_central","germany","schleswig_holstein"]`;
  category: `legislative`; tags: `["mandates","district_heating"]`; policy_types:
  `["law"]`; language: de
- **format**: HTML
- **practical**: EWKG requires buildings (pre-2009, on heating-system
  replacement) to cover ≥15% of annual heat demand via renewables/electricity/
  unavoidable waste heat; a concrete implementation example already exists
  (Stadtwerke Norderstedt district-heating network fed by a server-park's waste
  heat).
- **effort tier**: b
- **why worth adding**: Direct legal hook for data-centre waste-heat-to-district-
  heating requirements, with a real operating precedent in-state.
- **verified**: yes - HTTP 200 on the official Land legal-text server; the
  `schleswig-holstein.de` government energy/climate page also verified live as a
  secondary source.

### 32. Thüringen - Energieministerium (Umwelt/Klimaschutz)
- **id**: `thueringen_energieministerium`
- **base_url**: `https://umwelt.thueringen.de`
- **start_paths**: `["/aktuelles/anzeigen-medieninformationen/energieministerium-und-spitzenverband-der-stadtwerke-energiewende-vorantreiben"]`
- **level**: subnational (Land)
- **access**: none
- **coverage**: region: `["eu","eu_central","germany","thueringen"]`; category:
  `energy_ministry`; tags: `["district_heating","planning"]`; policy_types:
  `["strategy","report"]`; language: de
- **format**: HTML
- **practical**: ThürKlimaG (state climate law, since 2018) sets binding GHG
  targets and a near-climate-neutral building-stock goal by 2050; heat-network
  waste-heat share is separately tracked. `thega.de` (Thuringian Energy and
  GreenTech Agency) also verified live as a complementary practitioner-facing
  source.
- **effort tier**: b
- **why worth adding**: State ministry portal directly covers heat-transition
  (Wärmewende) policy and industrial waste-heat utilization in heat networks.
- **verified**: yes - HTTP 200 for both `umwelt.thueringen.de` and `thega.de`.

### 33. Sachsen-Anhalt - Kommunale Wärmeplanung / Energieministerium
- **id**: `sachsen_anhalt_waermeplanung`
- **base_url**: `https://mwu.sachsen-anhalt.de`
- **start_paths**: `["/energie/kommunale-waermeplanung"]`
- **level**: subnational (Land)
- **access**: none
- **coverage**: region: `["eu","eu_central","germany","sachsen_anhalt"]`;
  category: `energy_ministry`; tags: `["district_heating","planning"]`;
  policy_types: `["law","guidance"]`; language: de
- **format**: HTML
- **practical**: Ministry (MWU - Wissenschaft, Energie, Klimaschutz und Umwelt) is
  drafting a state municipal-heat-planning law; guidance already explicitly names
  data-centre waste heat alongside geothermal/solar-thermal as an eligible
  district-heating source, and funding programs support DH-network connections.
- **effort tier**: b
- **why worth adding**: Explicit, current state guidance naming data-centre waste
  heat as a district-heating input source.
- **verified**: yes - HTTP 200.

### 34. Mecklenburg-Vorpommern - Klimaschutzgesetz
- **id**: `mecklenburg_vorpommern_klimaschutzgesetz`
- **base_url**: `https://www.regierung-mv.de`
- **start_paths**: `["/Landesregierung/lm/Klima/Klimaschutz/klimaschutzgesetz/"]`
- **level**: subnational (Land)
- **access**: none
- **coverage**: region: `["eu","eu_central","germany","mecklenburg_vorpommern"]`;
  category: `legislative`; tags: `["mandates","district_heating"]`; policy_types:
  `["law"]`; language: de
- **format**: HTML
- **practical**: Climate Protection Act (climate-neutral state target 2040,
  state administration 2030); a companion Wärmeplanungsgesetz (heat-planning law,
  under the Interior Ministry) requires municipalities >100k pop. to plan by Jun
  2026, ≤100k by Jun 2028, and the energy ministry designates district-heating/
  hydrogen expansion zones.
- **effort tier**: b
- **why worth adding**: Only German coastal/northern Land not yet represented;
  heat-planning-law framework directly implicates waste-heat sourcing decisions.
- **verified**: yes - HTTP 200.

**Unverified**: **Saarland** (`saarland.de` domain, incl. the Energy Ministry's
"Wärmewende" page at `/mwide/DE/portale/energie/energiewende/waermewende` -
Saarland's Energy Efficiency Act implementation and heat-planning law content
confirmed via WebSearch, but the entire `saarland.de` domain returned HTTP 403 on
every path tried, including the bare homepage - looks like a site-wide bot block
rather than a dead link. Needs a human/different-network re-check.)

---

## CANADA - remaining (region root: `["north_america","canada","<province_territory>"]`)

Saskatchewan, New Brunswick, Nova Scotia, and Newfoundland & Labrador were already
proposed in wave2's `deep-subnational.yaml`. Remaining uncovered: PEI and the three
territories.

### 35. Prince Edward Island - IRAC (Island Regulatory and Appeals Commission)
- **id**: `pei_irac_energy`
- **base_url**: `https://irac.pe.ca`
- **start_paths**: `["/"]`
- **level**: subnational (province)
- **access**: none
- **coverage**: region: `["north_america","canada","prince_edward_island"]`;
  category: `regulatory`; tags: `["reporting","mandates"]`; policy_types:
  `["regulation","report"]`; language: en
- **format**: HTML/PDF
- **practical**: IRAC regulates PEI Energy Corporation and approves its
  Electricity Efficiency & Conservation Plan (2022-2025 plan targets 34.45 GWh net
  savings). PEI released a new Energy Strategy in October 2025 (per
  Efficiency Canada scorecard coverage) - a direct government URL for that
  specific strategy document was not pinned down this session; recommend a
  follow-up search on `princeedwardisland.ca` once located.
- **effort tier**: b
- **why worth adding**: PEI ranked #2 nationally in the 2024 Canadian Energy
  Efficiency Scorecard; IRAC is the regulator of record for its
  efficiency/conservation filings - a genuinely new Canadian jurisdiction.
- **verified**: yes - HTTP 200.

### 36. Northwest Territories - 2030 Energy Strategy
- **id**: `nwt_energy_strategy`
- **base_url**: `https://www.inf.gov.nt.ca`
- **start_paths**: `["/sites/inf/files/resources/gnwt_inf_7272_energy_strategy_web-eng.pdf"]`
- **level**: subnational (territory)
- **access**: none
- **coverage**: region: `["north_america","canada","northwest_territories"]`;
  category: `energy_ministry`; tags: `["planning","efficiency"]`; policy_types:
  `["strategy","report"]`; language: en
- **format**: PDF
- **practical**: GNWT Dept. of Infrastructure's "2030 Energy Strategy: A Path to
  More Affordable, Secure and Sustainable Energy"; territory also runs an Energy
  Efficiency Incentive Program, Energy Conservation Program, and Alternative
  Energy Technologies Program via the Arctic Energy Alliance (rebates up to
  $50,000 for business/non-profit/community-government efficiency projects).
- **effort tier**: b
- **why worth adding**: First Canadian territory represented in the registry.
- **verified**: yes - HTTP 200, full PDF downloads.

**Unverified**: **Yukon** (`yukon.ca` - "Find energy policies and reports" page;
territory has adopted Tier 1 of the 2020 National Building Code with a net-zero-
ready target by 2032 and a strong PACE financing program per Efficiency Canada's
scorecard - content confirmed via WebSearch, but `yukon.ca` returned HTTP 403 on
every attempt, including with a spoofed browser user-agent. Needs a human/
different-network re-check.)

---

## Summary of all 36 new distinct jurisdiction slugs (verified)

| # | Country | Jurisdiction | slug |
|---|---|---|---|
| 1 | India | Madhya Pradesh | `madhya_pradesh` |
| 2 | India | Andhra Pradesh | `andhra_pradesh` |
| 3 | India | Kerala | `kerala` |
| 4 | India | Punjab | `punjab` |
| 5 | India | Bihar | `bihar` |
| 6 | China | Gansu | `gansu` |
| 7 | China | Qinghai | `qinghai` |
| 8 | China | Guangdong | `guangdong` |
| 9 | China | Beijing | `beijing` |
| 10 | China | Shanghai | `shanghai` |
| 11 | China | Hebei | `hebei` |
| 12 | Japan | Hokkaido | `hokkaido` |
| 13 | Japan | Fukuoka | `fukuoka` |
| 14 | Japan | Kanagawa | `kanagawa` |
| 15 | Spain | Basque Country | `basque_country` |
| 16 | Spain | Castilla y León | `castilla_y_leon` |
| 17 | Spain | Valencia | `valencia` |
| 18 | Italy | Lazio | `lazio` |
| 19 | Italy | Piemonte | `piemonte` |
| 20 | Italy | Veneto | `veneto` |
| 21 | Italy | Emilia-Romagna | `emilia_romagna` |
| 22 | Switzerland | Ticino | `ticino` |
| 23 | Switzerland | Aargau | `aargau` |
| 24 | Belgium | Wallonia | `wallonia` |
| 25 | Belgium | Brussels-Capital | `brussels` |
| 26 | Belgium | Flanders | `flanders` |
| 27 | Australia | Western Australia | `western_australia` |
| 28 | Australia | Queensland | `queensland` |
| 29 | Germany | Brandenburg | `brandenburg` |
| 30 | Germany | Rheinland-Pfalz | `rheinland_pfalz` |
| 31 | Germany | Schleswig-Holstein | `schleswig_holstein` |
| 32 | Germany | Thüringen | `thueringen` |
| 33 | Germany | Sachsen-Anhalt | `sachsen_anhalt` |
| 34 | Germany | Mecklenburg-Vorpommern | `mecklenburg_vorpommern` |
| 35 | Canada | Prince Edward Island | `prince_edward_island` |
| 36 | Canada | Northwest Territories | `northwest_territories` |

**Unverified (6, real content, blocked/timed-out this session - not hallucinated):**
Sichuan (China, timeout), Victoria (Australia, HTTP 403), Northern Territory
(Australia, HTTP 403), Saarland (Germany, HTTP 403 site-wide), Yukon (Canada, HTTP
403), plus the Andhra Pradesh APEDB-hosted Data Center Policy 4.0 PDF specifically
(timeout; AP itself IS verified via the alternate `apit.ap.gov.in` domain above).
