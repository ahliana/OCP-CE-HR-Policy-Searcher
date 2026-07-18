# Digital-Infrastructure / Telecom Ministry & National Data-Centre Strategy Sources

Researcher scope: national/regional digital-infrastructure, ICT, or industry ministries
and telecom/ICT regulators that publish DATA-CENTRE strategies, sustainability
roadmaps, or DC energy/efficiency policy — the class of source that hides in a
digital-ministry strategy PDF rather than an energy-ministry site.

## Dedup performed

Grepped `config/domains/*.yaml` (+ `config/domains/us/*.yaml`), all of
`docs/source-expansion/draft/crawl/**/*.yaml`, `docs/source-expansion/draft/new-clients*.md`,
and `docs/source-expansion/regions-wave2/*.md` for base_urls before proposing anything.

Already shipped / already drafted and explicitly SKIPPED as duplicates:
- `imda.gov.sg` (imda_sg, apac.yaml) — Singapore IMDA Green DC Roadmap, already covered.
- `meity.gov.in` (meity_in, india.yaml) — India's national digital ministry, already covered.
- `www.gov.ie`, `seai.ie`, `cru.ie`, `irishstatutebook.ie` (ireland.yaml) — existing Ireland
  entries; none of these is DETE's own domain (see #1 below, which is genuinely distinct).
- Malaysia SEDA / Energy Commission (Suruhanjaya Tenaga) — energy-ministry equivalents,
  drafted in `oceania-south-asia.yaml`/`.md`; distinct from the digital ministry (KKD)
  and MyDIGITAL Corp covered here.
- Indonesia ESDM (Energy Ministry) — drafted in `oceania-south-asia.yaml`/`.md`; distinct
  from Komdigi (digital ministry) covered here.
- Nigeria NERC (energy regulator) — drafted in `mena-africa.yaml`/`.md`; distinct from
  NITDA (digital ministry) covered here.
- Kenya EPRA (energy regulator, unverified draft in `mena-africa.md`) — distinct from
  Kenya's Ministry of ICT / ICT Authority covered here.
- Saudi Ministry of Energy + SEEC (saudi_arabia.yaml) — distinct from SDAIA (data/AI
  authority) covered here.
- UK DESNZ, Ofgem, and all existing `gov.uk` heat-network entries (uk.yaml) — same
  shared `gov.uk` base_url is reused throughout uk.yaml for distinct departments/paths;
  the DSIT entry below is a new department + new start_path, not a re-add of an
  existing entry.
- Japan METI (`meti.go.jp`, apac.yaml) — distinct ministry from MIC (`soumu.go.jp`)
  covered here.
- South Korea MOTIE (`motie.go.kr`, apac.yaml) + `law.go.kr` — distinct from MSIT
  covered here.
- EU EUR-Lex Data Centre Delegated Regulation 2024/1364, EED 2023/1791, JRC Code of
  Conduct (eu.yaml) — these are enacted-law sources. The CADA entry below is DG
  CONNECT's forthcoming-legislation/strategy page, a different base_url and a
  different stage of the policy lifecycle (not a duplicate).
- Australia NSW/SA state energy entries (australia.yaml) — no federal Australian
  entry exists yet; DTA is federal and digital, not energy.

No exact base_url duplicates were proposed below except the flagged UK DSIT case,
which is a new start_path on an already-present shared domain (explicitly called out).

---

## Verified candidates (ranked best-first)

### 1. Ireland — DETE Government Statement on the Role of Data Centres in Ireland's Enterprise Strategy
- **name**: "Ireland DETE - Government Statement on Data Centres in Enterprise Strategy"
- **id**: `dete_datacentres_ie`
- **base_url**: `https://enterprise.gov.ie`
- **start_paths**:
  - `/en/publications/government-statement-on-role-of-data-centres-in-enterprise-strategy.html`
  - `/en/publications/publication-files/government-statement-on-the-role-of-data-centres-in-irelands-enterprise-strategy.pdf`
- **level**: national
- **access**: none
- **coverage**: region: `["ireland","eu_west"]`; category: `digital_ministry`; tags:
  `["mandates","planning","renewable_energy","efficiency"]`; policy_types:
  `["strategy","guidance"]`; language: en
- **format**: HTML + PDF
- **practical**: no rate-limit info published; standard gov.ie-family site, low volume,
  update frequency irregular (last major statement July 2022, actively referenced in
  2026 "policy reset" coverage)
- **effort tier**: (b) plain crawl domain — new base_url, append to `ireland.yaml`
- **why worth adding**: Ireland's Department of Enterprise, Trade and Employment (not
  SEAI/CRU/gov.ie generic, which are already covered) is the ministry that actually sets
  DC siting and renewable-supply policy — including the widely-reported rule that new
  ≥1MVA data centres must source 80% of annual demand from new in-country renewables
  within 6 years of operation. This is the "twin transition" (digitalisation +
  decarbonisation) framing document.
- **verified**: yes — fetched `enterprise.gov.ie/en/publications/government-statement-on-role-of-data-centres-in-enterprise-strategy.html` directly; HTTP 200, confirmed DETE authorship, July 2022 publication date, on-topic content.

### 2. Nigeria — NITDA National Cloud Policy 2025 (supersedes 2019 Cloud Computing Policy)
- **name**: "NITDA - National Information Technology Development Agency"
- **id**: `nitda_ng`
- **base_url**: `https://nitda.gov.ng`
- **start_paths**:
  - `/wp-content/uploads/2025/10/National-Cloud-Policy-2025-Oct2-2025.pdf`
  - `/wp-content/uploads/2020/11/NCCPolicy_New1.pdf` (2019 predecessor, historical)
- **level**: national
- **access**: none
- **coverage**: region: `["africa","nigeria"]`; category: `digital_ministry`; tags:
  `["mandates","planning","incentives"]`; policy_types: `["policy","strategy","guidance"]`;
  language: en
- **format**: PDF
- **practical**: WordPress-hosted site, PDFs under `/wp-content/uploads/`; no published
  rate limits; update frequency ties to policy revision cycle (2019 → 2025 supersession)
- **effort tier**: (b) plain crawl domain — new `nigeria.yaml` file (NERC already
  drafted separately as the energy regulator)
- **why worth adding**: Nigeria's National Cloud Policy 2025 mandates that sovereign
  (Level 3/4) government data be hosted exclusively within Nigeria, and NITDA is
  actively building the "Nigeria Digital Triangle" — a national sovereign-cloud DC
  infrastructure strategy — making this the clearest African digital-ministry DC
  strategy found.
- **verified**: yes — fetched the 2025 policy PDF directly; resolved as a valid
  765.7KB PDF (HTTP 200 via curl), confirmed live by independent 2026 press coverage
  (NigeriaCommunicationsWeek, Technext24) describing the same document.

### 3. Kenya — Ministry of ICT / ICT Authority Data Centre Standard + Cloud Policy
- **name**: "Kenya Ministry of ICT and the Digital Economy - Policy Documents"
- **id**: `kenya_ict_dc`
- **base_url**: `https://ict.go.ke`
- **start_paths**:
  - `/policy-documents`
  - `/sites/default/files/2024-12/Kenya%20Cloud%20Policy%20-%202024.pdf`
- **secondary base_url**: `https://cms.icta.go.ke` (ICT Authority technical standards)
  - `/sites/default/files/2022-05/Data%20Centre%20Standard.pdf`
  - `/sites/default/files/2022-06/Cloud%20computing%20Standard.pdf`
- **level**: national
- **access**: none
- **coverage**: region: `["africa","kenya"]`; category: `digital_ministry`; tags:
  `["standards","mandates","reporting","efficiency"]`; policy_types:
  `["standard","policy"]`; language: en
- **format**: PDF, HTML index page
- **practical**: static Drupal-style file hosting, PDFs under `/sites/default/files/`;
  no published rate limits
- **effort tier**: (b) plain crawl domain — new `kenya.yaml` file (Kenya EPRA is a
  separate unverified energy-regulator draft in `mena-africa.md`)
- **why worth adding**: ICT Authority's Data Centre Standard applies compliance audits
  across all Ministries, Counties and Agencies — a binding national technical standard
  for government DC facilities — paired with the Ministry's 2024 Cloud Policy.
- **verified**: yes — `ict.go.ke/policy-documents` HTTP 200 (fetched, confirmed policy
  list includes "Kenya Cloud Policy - 2024"); `cms.icta.go.ke` Data Centre Standard PDF
  HTTP 200 (fetched as valid 460.5KB PDF; page-content OCR not available in this pass,
  but the document is confirmed live and the ICT Authority's `policy-documents` index
  independently lists it).

### 4. Japan — MIC (Ministry of Internal Affairs and Communications) Regional Data Centre Distribution Programme
- **name**: "Japan MIC - Digital Infrastructure Resilience / Regional Data Centre Distribution"
- **id**: `mic_datacenter_jp`
- **base_url**: `https://www.soumu.go.jp`
- **start_paths**:
  - `/menu_seisaku/ictseisaku/datacenter/index.html`
  - `/menu_seisaku/ictseisaku/digital_infrastructure/index.html`
- **level**: national
- **access**: none
- **coverage**: region: `["apac","japan"]`; category: `digital_ministry`; tags:
  `["incentives","planning","efficiency"]`; policy_types: `["program","guidance","report"]`;
  language: ja
- **format**: HTML, linked PDFs
- **practical**: standard soumu.go.jp gov site; no API; Japanese-language only;
  update frequency tied to annual budget/subsidy rounds (¥130bn+ Digital Infrastructure
  Development Fund, "Digital Infrastructure Development Plan 2030" issued June 2025)
- **effort tier**: (b) plain crawl domain — new entry, distinct ministry from the
  already-covered METI (`meti.go.jp`) entry in `apac.yaml`
- **why worth adding**: MIC runs the subsidy programme moving DC siting out of
  Tokyo/Osaka into depopulating regions — a genuinely distinct national DC-siting/
  energy-resilience strategy from a telecom regulator, not an energy ministry.
- **verified**: yes — fetched both pages directly; confirmed MIC authorship, subsidy
  amounts (¥1-2bn per project, ¥130bn+ fund total), and regional-siting policy intent.

### 5. Malaysia — Ministry of Digital (KKD) + MyDIGITAL Corporation
- **name**: "Malaysia Ministry of Digital (KKD)" / "MyDIGITAL - Malaysia Digital 2030"
- **id**: `kkd_my` / `mydigital_my`
- **base_url**: `https://www.digital.gov.my` / `https://www.mydigital.gov.my`
- **start_paths**:
  - `/en-GB/profil-kementerian` (KKD ministry profile)
  - `/` and `/budget-2026-accelerating-malaysias-digital-transformation-for-all/` (MyDIGITAL)
- **level**: national
- **access**: none
- **coverage**: region: `["apac","malaysia"]`; category: `digital_ministry`; tags:
  `["planning","incentives"]`; policy_types: `["strategy","report"]`; language: en
- **format**: HTML, linked PDFs (e.g. NIMP 2030 Digital & ICT sectoral plan)
- **practical**: standard gov.my sites; no rate-limit info published
- **effort tier**: (b) plain crawl domain — new `malaysia.yaml` file (SEDA/Energy
  Commission are the separate energy-ministry equivalents already drafted)
- **why worth adding**: KKD is the ministry overseeing Malaysia's DC sector (alongside
  MCMC as regulator); MyDIGITAL's blueprint names cloud/data-centre investment as a
  named "catalytic project" with a stated sustainability framing for DC growth. Content
  is strategy-level rather than a standalone PUE mandate, so rank this below entries
  with binding standards.
- **verified**: yes — both fetched; `digital.gov.my/en-GB/profil-kementerian` and
  `mydigital.gov.my` both HTTP 200 and content-confirmed on-topic. MCMC's own
  `/en/legal/acts` page was checked and found too generic (no DC-specific technical
  standard visible) — dropped from this list, see Unverified section.

### 6. Indonesia — Komdigi (Ministry of Communication and Digital Affairs) — PP 71/2019
- **name**: "Komdigi JDIH - Legal Database (PP 71/2019 Electronic Systems & Data Centres)"
- **id**: `komdigi_id`
- **base_url**: `https://jdih.komdigi.go.id`
- **start_paths**:
  - `/produk_hukum/view/id/695/t/peraturan+pemerintah+nomor+71+tahun+2019`
  - `/produk_hukum` (search/index)
- **level**: national
- **access**: none
- **coverage**: region: `["apac","indonesia"]`; category: `digital_ministry`; tags:
  `["mandates","planning"]`; policy_types: `["law","regulation"]`; language: id
- **format**: HTML (full statute text)
- **practical**: JDIH legal-repository CMS; Indonesian-language only; no API
- **effort tier**: (b) plain crawl domain — new `indonesia.yaml` file (ESDM energy
  ministry already drafted separately, distinct focus)
- **why worth adding**: PP 71/2019 is Indonesia's foundational data-centre/data-
  localization regulation — sets the strategic/high/low data-classification scheme that
  determines which data centres must be sited domestically. This is the digital
  ministry's own legal-instrument portal, not a secondary summary site.
- **verified**: yes — fetched directly; confirmed the page hosts the full PP 71/2019
  text and that `jdih.komdigi.go.id` is Komdigi's official legal-documentation site
  (HTTP 200).

### 7. EU — Cloud and AI Development Act (CADA), DG CONNECT
- **name**: "European Commission Digital Strategy - Cloud and AI Development Act"
- **id**: `eu_cada`
- **base_url**: `https://digital-strategy.ec.europa.eu`
- **start_paths**: `/en/policies/cloud-and-ai-development-act`
- **level**: supranational
- **access**: none
- **coverage**: region: `["eu"]`; category: `digital_ministry`; tags:
  `["planning","efficiency","incentives"]`; policy_types: `["strategy","directive"]`
  (forthcoming legislation); language: en (+ all EU languages via site selector)
- **format**: HTML
- **practical**: standard EC digital-strategy CMS; no rate limits published
- **effort tier**: (b) plain crawl domain — new entry in `eu.yaml`, distinct base_url
  from existing EUR-Lex/JRC/E3P entries (which cover enacted law, not this forthcoming
  initiative)
- **why worth adding**: CADA explicitly targets tripling EU data-centre capacity while
  "improving access to key resources such as energy, land, water and financing" and
  deploying "sustainable cloud and data centre infrastructure" — this is DG CONNECT
  (the EU's digital ministry equivalent) setting DC sustainability/capacity policy,
  complementing rather than duplicating the already-covered EED/Delegated Regulation
  enacted-law entries.
- **verified**: yes — fetched directly, HTTP 200, content confirms DC-capacity and
  sustainability framing as described.

### 8. Saudi Arabia — SDAIA (Saudi Data & AI Authority)
- **name**: "SDAIA - National Strategy for Data & AI / Government Cloud"
- **id**: `sdaia_sa`
- **base_url**: `https://sdaia.gov.sa`
- **start_paths**:
  - `/en/SDAIA/SdaiaStrategies/Pages/NationalStrategyForDataAndAI.aspx`
  - `/en/Services/Pages/Deem.aspx` (government cloud "Deem")
- **level**: national
- **access**: none
- **coverage**: region: `["mena","saudi_arabia"]`; category: `digital_ministry`; tags:
  `["planning","mandates"]`; policy_types: `["strategy","policy"]`; language: en/ar
- **format**: HTML, linked PDFs
- **practical**: standard .aspx-based gov site; one specific sub-path
  (`/en/SDAIA/about/Pages/RegulationsAndPolicies.aspx`) returned a WAF/access-denied
  block during verification — avoid that path, use the two start_paths above instead
- **effort tier**: (b) plain crawl domain — new entry in `saudi_arabia.yaml`, distinct
  from the already-covered Ministry of Energy / SEEC entries
- **why worth adding**: SDAIA is Saudi Arabia's national data/AI/cloud authority
  (distinct from the energy ministry) and sets data-sovereignty and government-cloud
  hosting requirements that shape where national data centres may be sited.
- **verified**: yes for the two start_paths listed (HTTP 200, content confirmed);
  **no** for `RegulationsAndPolicies.aspx` (blocked) — do not use that path.

### 9. UK — DSIT Data Centres Critical National Infrastructure Policy
- **name**: "UK DSIT - Data Centres as Critical National Infrastructure"
- **id**: `dsit_datacentres_uk`
- **base_url**: `https://www.gov.uk` (⚠ already present many times in `uk.yaml` for
  other departments/paths — this is a NEW start_path under the same shared domain, not
  a duplicate entry; append to the existing `uk.yaml` domains list rather than
  re-adding `gov.uk` as a fresh top-level entry)
- **start_paths**:
  - `/government/publications/cyber-security-and-resilience-network-and-information-systems-bill-factsheets/data-centres`
  - `/government/news/data-centres-to-be-given-massive-boost-and-protections-from-cyber-criminals-and-it-blackouts`
- **level**: national
- **access**: none
- **coverage**: region: `["uk"]`; category: `digital_ministry`; tags:
  `["mandates","planning"]`; policy_types: `["regulation","guidance"]`; language: en
- **format**: HTML
- **practical**: standard gov.uk publication pages; DSIT is preparing a new National
  Policy Statement for data centres under the Planning Act 2008 (Section 35 NSIP regime)
- **effort tier**: (b) plain crawl domain — append new start_paths to existing
  `uk.yaml` gov.uk block
- **why worth adding**: This is the Department for Science, Innovation and Technology
  (not DESNZ, which is already covered) designating data centres as Critical National
  Infrastructure (Sept 2024) and, per the June 2026 policy paper, bringing ≥1MW-load DCs
  under NIS Regulations with Ofcom as operational regulator — a distinct
  digital-ministry policy track from the existing heat-network/DESNZ content in
  `uk.yaml`.
- **verified**: yes — fetched the June 30, 2026 policy paper directly; HTTP 200,
  content confirmed (1MW threshold, Ofcom regulator role, NIS Regulations designation).

---

## Lower-confidence / needs-human-check (partial verification)

### 10. Australia — DTA Hosting Certification Framework
- **name**: "Australia DTA - Hosting Certification Framework"
- **id**: `dta_hcf_au`
- **base_url**: `https://www.dta.gov.au` (also relevant: `https://www.hostingcertification.gov.au`, `https://architecture.digital.gov.au`)
- **start_paths**: `/articles/new-data-centre-panel`; `hostingcertification.gov.au` root
- **level**: national
- **access**: none
- **coverage**: region: `["australia"]`; category: `digital_ministry`; tags:
  `["mandates","reporting","efficiency"]`; policy_types: `["standard","guidance"]`
- **format**: HTML
- **effort tier**: (b) plain crawl domain — new entry (Australia currently only has
  NSW/SA state energy entries, no federal digital-agency entry)
- **why worth adding**: DTA's Hosting Certification Framework has mandatory
  sustainability reporting for government-facing DC providers — environmental ratings,
  power consumption, renewable-energy percentage — a binding federal requirement, if
  confirmed.
- **verified**: PARTIAL. `curl` (no redirect-follow) confirmed all three `.gov.au`
  hostnames are live and return valid HTTP 301 redirects to their `www.` counterparts,
  but every attempt to fetch the actual page content (`www.dta.gov.au`,
  `www.hostingcertification.gov.au`, `architecture.digital.gov.au`) timed out from
  this environment — the sites appear to be real but slow/network-constrained to
  reach here. Content claims above are corroborated by independent secondary sources
  (DataCenterDynamics, Lexology, Holding Redlich, NextDC blog) describing the same
  framework and its sustainability-reporting requirement in detail, but no primary-source
  page was directly rendered. **Recommend browser-based human verification before
  enabling.**

---

## Unverified / dropped

- **UAE — TDRA (Telecommunications and Digital Government Regulatory Authority)**,
  `https://tdra.gov.ae/en/About/sustainability` — page resolves (HTTP 200, fetched) but
  content is general corporate-sustainability marketing copy (LEED-certified TDRA
  offices, FedNet virtualization) rather than a DC sector policy/standard document. No
  dedicated UAE national DC strategy PDF was located from TDRA in this pass. Not
  proposed as a candidate; flag for a follow-up search specifically for a UAE Cabinet
  or Ministry of AI data-centre/cloud policy document if one exists.
- **Malaysia — MCMC `/en/legal/acts`** — fetched, HTTP 200, but the legislation index
  is generic (spectrum, technical-standards regulations) with no DC-specific content
  visible without opening each linked act. Dropped in favor of KKD/MyDIGITAL above;
  worth a follow-up if the "Communications and Multimedia (Technical Standards)
  Regulations 2000" text itself turns out to address DC facilities.
- **Thailand — MDES (Ministry of Digital Economy and Society)**, `https://www.mdes.go.th/`
  — site resolves (HTTP 200) and is confirmed as the correct ministry, but no dedicated
  national data-centre strategy document was located in Thai or English in this pass.
  Needs a native-Thai-language follow-up search of MDES/DEPA publications before
  proposing a specific start_path.
- **South Korea — MSIT decentralization-from-Seoul DC policy** — the ministry itself
  (`msit.go.kr`) is verified live (HTTP 200) and its "Digital Strategy of Korea" page
  is on-topic for national digital/cloud strategy generally, but is not included as a
  standalone verified candidate above because the content found (semiconductor/NPU/
  supercomputer strategy) is only loosely DC-specific. The specific, often-cited
  "national policy to decentralize data centres away from Seoul following the 2022
  Pangyo fire" is corroborated only by an academic journal article (KoreaScience) and
  industry press (Cushman & Wakefield, w.media) — no primary MSIT policy document
  implementing this was located. Worth a dedicated Korean-language follow-up search
  of MSIT's Korean-language site (not just `/eng/`) before proposing a start_path.

---

## Summary

- **Region**: Digital-infrastructure / telecom ministries and national data-centre
  strategies (cross-regional).
- **Verified candidates**: 9 (all tier-b plain crawl domains; no tier-a/tier-c —
  none of these fit an existing structured API client or need a new one).
- **Tier split**: 0 tier-a, 9 tier-b, 0 tier-c (verified); 1 additional tier-b
  partially-verified (Australia DTA); 3 dropped/unverified.
- **Highest-value find**: Ireland DETE's Government Statement on the Role of Data
  Centres in Ireland's Enterprise Strategy (`enterprise.gov.ie`) — the actual ministry
  document behind Ireland's binding 80%-new-renewables DC rule, previously missed
  because the existing Ireland coverage (SEAI/CRU/gov.ie/Irish Statute Book) never
  reached DETE's own domain.
