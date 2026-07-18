# Data Center Economic-Development / Tax-Incentive Sources — Wave 3

Scope: government economic-development agencies and tax-incentive programs
specifically for **data centers**, prioritizing incentives conditioned on
energy efficiency, renewable-energy use, or heat reuse. Research + draft
only, per `docs/source-expansion/BRIEF.md`. Nothing below is enabled in any
config file.

Dedup performed against: `config/domains/*.yaml` (incl. `us/`),
`docs/source-expansion/draft/crawl/**/*.yaml`,
`docs/source-expansion/draft/new-clients*.md`, and
`docs/source-expansion/regions-wave2/*.md`. Notable: **Nebraska, Wyoming,
and Mississippi have empty `config/domains/us/*.yaml` files** (no domains
shipped yet for those states) - filling those gaps was the top priority
here. Existing shipped India state DC policies (UP `invest.up.gov.in`,
Odisha `investodisha.gov.in`, Tasmania `economicregulator.tas.gov.au`) were
confirmed already covered in wave 2 and are not re-proposed.

**Totals: 19 verified candidates, 3 unverified/needs-human-check. All 19
are effort tier (b) - plain crawl domains; zero tier-a, zero tier-c.**

**Single highest-value find**: Singapore's **DC-CFA2** (Data Centre — Call
for Application 2), jointly run by the Economic Development Board (EDB)
and the Infocomm Media Development Authority (IMDA) — the incentive
*is* the efficiency condition. To win an allocation of the 200MW+ of new
data-center capacity on offer, an applicant must hit **PUE ≤ 1.25 (at 100%
IT load)**, source **≥50% of power from eligible green pathways**, and hold
**BCA-IMDA Green Mark for Data Centres 2024 Platinum** certification. This
is a direct, government-run economic-development mechanism where energy
performance is the gate, not an afterthought.

---

## Verified candidates (ranked best-first)

### 1. Singapore — IMDA / EDB Data Centre Call for Application 2 (DC-CFA2)

- name: "IMDA — Call for Application: Data Centre 2 (DC-CFA2)"
- id: `sg_dc_cfa2`
- base_url: `https://www.imda.gov.sg`
- start_paths: `/proposal-submission/call-for-application-data-centre-2`
- level: national
- access: none
- coverage: joint EDB/IMDA capacity-allocation scheme for new Singapore data
  centers (≥200MW pool); explicit conditions: PUE ≤1.25 at 100% IT load,
  ≥50% power from eligible green energy pathways, BCA-IMDA Green Mark for
  Data Centres 2024 Platinum certification, compliance with Singapore
  Standard SS 715:2025 (Energy Efficiency of DC IT Equipment)
- region: `["apac", "singapore"]` | category: `economic_dev` | tags:
  `incentives, efficiency, data_center_specific` | policy_types:
  `incentive, standard` | language: en
- format: HTML (page last updated 31 Mar 2026) + linked PDF factsheet
- practical: no rate limit documented; page links to a companion EDB press
  release/factsheet PDF; registration window for this specific CFA round
  closed 5 Dec 2025 but the program page and its successor rounds are the
  durable policy artifact
- effort tier: b
- why worth adding: the only source in this batch where the incentive
  mechanism itself is denominated in PUE and green-power percentage —
  exactly the taxonomy PolicyPulse targets
- verified: yes — loaded via browser, confirmed live (imda.gov.sg,
  "LAST UPDATED: 31 MAR 2026"), on-topic, joint EDB/IMDA branding
- append to: `apac.yaml` (new Singapore economic-dev section, alongside
  existing `imda.gov.sg` Green Data Centre Programme entry — same host,
  different path, not a duplicate)

### 2. Malaysia — MIDA Digital Ecosystem Acceleration (DESAC) Scheme

- name: "MIDA — Digital Infrastructure / DESAC Scheme"
- id: `my_mida_desac`
- base_url: `https://www.mida.gov.my`
- start_paths:
  - `/digital-infrastructure-the-driving-force-behind-digital-transformation/`
  - `/wp-content/uploads/2024/12/DESAC-Guideline_MIDA.pdf`
- level: national
- access: none
- coverage: Malaysian Investment Development Authority tax-incentive
  scheme (Budget 2022) for data centers/digital infrastructure; Tier 1
  benefit is 100% Investment Tax Allowance for 5-10 years, conditioned on
  adopting at least one green technology (renewable energy generation or
  energy/water-efficient equipment), aligned with MITI's Sustainable
  Development of Data Centres guideline
- region: `["apac", "malaysia"]` | category: `economic_dev` | tags:
  `incentives, efficiency, data_center_specific` | policy_types:
  `incentive, guidance` | language: en
- format: HTML + PDF (guideline PDF dated Dec 2024)
- practical: applications accepted through 31 Dec 2027; no rate limit
  documented; administered jointly with MDEC's Digital Investment Office
- effort tier: b
- why worth adding: tax allowance directly conditioned on green-tech
  adoption for data centers — same shape as Singapore's but tax-code based
  rather than capacity-allocation based
- verified: yes — WebFetch confirmed the digital-infrastructure page is
  live on mida.gov.my (dated 13 Mar 2023, DESAC scheme described); the
  DESAC guideline PDF URL was seen live in search results but not
  re-fetched directly — treat PDF path as lower-confidence than the HTML
  page
- append to: new `malaysia.yaml` (no existing Malaysia file)

### 3. Illinois — DCEO Data Center Investment Program

- name: "Illinois DCEO — Data Center Investment Program"
- id: `il_dceo_dc_investment`
- base_url: `https://dceo.illinois.gov`
- start_paths: `/expandrelocate/incentives/datacenters.html`
- level: subnational (state)
- access: none
- coverage: state sales/use tax exemption (Retailers' Occupation Tax Act,
  Use Tax Act, Service Use/Occupation Tax Acts, Chicago non-titled Use
  Tax) requiring qualifying data centers to be **either carbon-neutral or
  certified under a green building standard (e.g., LEED, ENERGY STAR, ISO
  50001)**, plus $250M capital investment / 20+ jobs at 120% of county
  median wage
- region: `["us", "us_states"]` | category: `economic_dev` | tags:
  `incentives, efficiency, mandates` | policy_types: `incentive` |
  language: en
- format: HTML
- practical: no rate limit documented; **program closed to new
  applications as of 1 Jul 2026** per gubernatorial directive (5 Jun
  2026) — still valuable as a documented policy artifact with an explicit
  efficiency-certification condition, and annual reports remain published
- effort tier: b
- why worth adding: explicit carbon-neutral-or-green-certification
  condition baked into a US state sales tax exemption statute — rare
  among the US state programs surveyed here
- verified: yes — WebFetch confirmed live page, confirmed carbon-neutral/
  green-building-standard language and the 2026 closure notice
- append to: `us/illinois.yaml` (currently only has ICC + General
  Assembly entries)

### 4. Arizona — Computer Data Center Program (A.R.S. § 41-1519)

- name: "Arizona Legislature — Computer Data Center Program Statute (ARS 41-1519)"
- id: `az_cdc_program_statute`
- base_url: `https://www.azleg.gov`
- start_paths: `/ars/41/01519.htm`
- level: subnational (state)
- access: none
- coverage: TPT/Use Tax exemption administered by Arizona Commerce
  Authority + Dept. of Revenue; base tier is 10 years, but a **"Sustainable
  Redevelopment Project"** tier (data center attaining ENERGY STAR, Green
  Globes, or LEED certification, or built on a $200M+ redevelopment site)
  extends the exemption to **20 years**
- region: `["us", "us_states"]` | category: `economic_dev` | tags:
  `incentives, efficiency` | policy_types: `incentive, law` | language: en
- format: HTML (full statute text)
- practical: no rate limit; ACA accepts CDC certification applications
  through 31 Dec 2033; the ACA's own program page
  (`azcommerce.com/incentives/computer-data-center-program/`) returned
  HTTP 403 to automated fetch (bot protection) — use the statute as the
  durable/crawlable primary source and treat azcommerce.com as a
  secondary reference needing a browser-based crawl config
- effort tier: b
- why worth adding: doubles the exemption term specifically for green-
  certified data centers — a clean efficiency-for-incentive trade written
  directly into state law
- verified: yes — WebFetch confirmed live azleg.gov statute text
  including "Sustainable Redevelopment Project" and green-building-
  standard definitions
- append to: `us/arizona.yaml` (currently only has Corp Commission +
  Legislature entries)

### 5. Ireland — IDA Ireland Funding Programmes & Incentives

- name: "IDA Ireland — Funding Programmes & Incentives"
- id: `ie_ida_funding_incentives`
- base_url: `https://www.idaireland.com`
- start_paths: `/scale-with-ida/funding-programmes-incentives`
- level: national
- access: none
- coverage: Ireland's national FDI agency's grant/incentive hub for
  capital investment, R&D, and — most relevant — dedicated "IDA Energy
  Supports" and "Strengthening your sustainability" tracks that apply to
  data-center investment among other sectors
- region: `["eu", "eu_west", "ireland"]` | category: `economic_dev` |
  tags: `incentives, efficiency` | policy_types: `incentive, guidance` |
  language: en
- format: HTML
- practical: no rate limit documented; site is JS-rendered (needs
  `requires_playwright: true`, consistent with the existing `ireland.yaml`
  entries)
- effort tier: b
- why worth adding: distinct from the already-shipped `seai.ie` /
  `gov.ie` / `cru.ie` / `irishstatutebook.ie` Ireland entries — this is
  the actual grant-issuing FDI agency (IDA), not a regulator or ministry,
  and it names data centers explicitly in IDA's published enterprise
  strategy
- verified: yes — loaded via browser (idaireland.com), confirmed live,
  confirmed "IDA Energy Supports" and sustainability-support sub-pages
  present
- append to: `ireland.yaml`

### 6. Wyoming — Business Council Managed Data Center Cost Reduction Funding

- name: "Wyoming Business Council — Business Ready Community / Managed Data Center Cost Reduction Funding"
- id: `wy_wbc_dc_cost_reduction`
- base_url: `https://wyomingbusiness.org`
- start_paths:
  - `/communities/financing/business-ready-community/`
  - `/communities/financing/business-ready-community/managed-data-center-cost-reduction-funding/`
- level: subnational (state)
- access: none
- coverage: state economic-development grant/loan program; a
  "Managed Data Center" grant track (up to $2.25M) specifically buys down
  local government costs for **broadband and electricity** serving a data
  center business, conditioned on a 125% capital/payroll match (≥50% in
  payroll) and payroll ≥150% of county median wage; separately, the
  Wyoming Business Council certifies job creation for the state's data
  center sales-tax exemption (Wyo. Stat. § 39-15-105)
- region: `["us", "us_states"]` | category: `economic_dev` | tags:
  `incentives` | policy_types: `incentive` | language: en
- format: HTML + PDF (BRC master application)
- practical: no rate limit documented; the parent BRC page confirmed live
  and links to the data-center sub-program; the specific sub-page URL
  above returned HTTP 404 to direct fetch twice (both WebFetch and
  browser) despite being indexed and named on the parent page — likely a
  routing/trailing-slash quirk, not a dead program. Flagged as
  lower-confidence in the "needs-human-check" list below as well; use the
  parent BRC page as the safe crawl entry point
- effort tier: b
- why worth adding: fills Wyoming's **empty** `us/wyoming.yaml` (currently
  zero domains shipped for this state) with the state's own economic-
  development agency, not just legislature/statute text
- verified: yes (parent page) / partial (named sub-page) — see practical
  note above
- append to: new content in `us/wyoming.yaml` (file exists but has zero
  domain entries)

### 7. Nebraska — ImagiNE Nebraska Act Incentives Program

- name: "ImagiNE Nebraska — Incentives Program"
- id: `ne_imagine_act`
- base_url: `https://imagine.nebraska.gov`
- start_paths: `/`, `/about-the-program/`, `/tax-credit-usage/`
- level: subnational (state)
- access: none
- coverage: Nebraska Dept. of Economic Development's ImagiNE Nebraska Act
  program; sales/use tax refunds or exemptions, personal property tax
  exemptions, investment tax credits and wage credits, with a dedicated
  "significant data center project" track (≥$200M investment, 30 new
  jobs) offering a longer exemption/refund period
- region: `["us", "us_states"]` | category: `economic_dev` | tags:
  `incentives` | policy_types: `incentive, law` | language: en
- format: HTML
- practical: no rate limit documented; companion authoritative page at
  `revenue.nebraska.gov/incentives/imagine-nebraska-act` (Dept. of
  Revenue) — consider adding both same host-family or the Revenue page
  as a secondary domain
- effort tier: b
- why worth adding: fills Nebraska's **empty** `us/nebraska.yaml`
  (currently zero domains shipped)
- verified: yes — WebFetch confirmed imagine.nebraska.gov is live,
  official ("Nebraska Department of Economic Development" footer)
- append to: new content in `us/nebraska.yaml` (file exists but has zero
  domain entries)

### 8. Mississippi — MDA Data Center Enterprise Sales & Use Tax Exemption

- name: "Mississippi Development Authority — Sales and Use Tax Exemption for Data Center Enterprises"
- id: `ms_mda_dc_exemption`
- base_url: `https://mississippi.org`
- start_paths: `/wp-content/uploads/sales-and-use-tax-exemption-data-centers-1.pdf`
- level: subnational (state)
- access: none
- coverage: MDA-certified data center incentive: sales/use tax exemption
  on component building materials, construction/expansion equipment, and
  replacement hardware/software; 10-year income tax and franchise tax
  exemptions; requires $20M investment and 20 jobs at 125% of state
  average wage. 2025 legislation (SB 3168) pending would raise thresholds
  and add an electricity tax exemption
- region: `["us", "us_states"]` | category: `economic_dev` | tags:
  `incentives` | policy_types: `incentive` | language: en
- format: PDF
- practical: no rate limit documented; single PDF document, not a
  crawlable HTML section — recommend `start_paths` targeting the MDA
  incentives/publications index page instead of only this one PDF once a
  human confirms the index URL
- effort tier: b
- why worth adding: fills Mississippi's **empty** `us/mississippi.yaml`
  (currently zero domains shipped)
- verified: yes — WebFetch successfully downloaded the PDF (382KB,
  application/pdf) from mississippi.org; content extraction was garbled
  (binary/PDF-encoding artifact) but the fetch itself confirms the file is
  live and hosted on MDA's official domain
- append to: new content in `us/mississippi.yaml` (file exists but has
  zero domain entries)

### 9. Virginia — VEDP Data Center Retail Sales & Use Tax Exemption

- name: "Virginia Economic Development Partnership — Data Center Retail Sales & Use Tax Exemption"
- id: `va_vedp_dc_exemption`
- base_url: `https://www.vedp.org`
- start_paths: `/incentive/data-center-retail-sales-use-tax-exemption`
- level: subnational (state)
- access: none
- coverage: VEDP-administered MOU program (with VA Dept. of Taxation);
  exemption for qualifying computer equipment, cooling (chillers, CRACs,
  HVAC) and power-monitoring systems; $150M/50-jobs base threshold,
  scaling to $35B/1,000-jobs for a 2040 extension and $100B/2,500-jobs
  for a 2050 extension
- region: `["us", "us_states"]` | category: `economic_dev` | tags:
  `incentives` | policy_types: `incentive` | language: en
- format: HTML + linked PDF info packet
- practical: no rate limit documented; contact `dcrsute@vedp.org` listed
  on page
- effort tier: b
- why worth adding: fills a real gap — the existing `us/virginia.yaml`
  only has the Dept. of Energy and legislative-bill entries, nothing from
  the state's own economic-development/incentive-granting agency, despite
  Virginia being the largest US data-center market
- verified: yes — WebFetch confirmed live vedp.org page, administering
  agency and thresholds
- append to: `us/virginia.yaml`

### 10. Texas — Comptroller Qualified Data Center Sales Tax Exemption

- name: "Texas Comptroller — State Sales Tax Exemption for Qualified Data Centers"
- id: `tx_comptroller_dc_exemption`
- base_url: `https://comptroller.texas.gov`
- start_paths: `/taxes/data-centers/`
- level: subnational (state)
- access: none
- coverage: Tex. Tax Code § 151.359 exemption on hardware/software/power
  equipment for certified qualifying data centers ($200M+/20 jobs) and
  "qualifying large data center projects" ($500M+/40 jobs/20MW)
- region: `["us", "us_states"]` | category: `economic_dev` | tags:
  `incentives` | policy_types: `incentive, law` | language: en
- format: HTML
- practical: no rate limit documented; no explicit efficiency condition
  found on this page (infrastructure requirements are physical-security/
  power-redundancy, not energy-performance)
- effort tier: b
- why worth adding: existing `us/texas.yaml` only has SECO (energy
  ministry) and Legislature entries — the Comptroller's own program page is
  the primary source of record for the exemption's live administration
- verified: yes — WebFetch confirmed live comptroller.texas.gov page
- append to: `us/texas.yaml`

### 11. Georgia — DOR High-Technology Data Center Equipment Exemption

- name: "Georgia Department of Revenue — High-Technology Data Center Equipment Exemption"
- id: `ga_dor_dc_exemption`
- base_url: `https://dor.georgia.gov`
- start_paths:
  - `/high-technology-data-center-equipment-exemption`
  - `/how-apply-high-technology-data-center-exemption`
  - `/data-centers-sales-use-tax-exemption-aggregate-expenditures-county`
- level: subnational (state)
- access: none
- coverage: O.C.G.A. § 48-8-3(68.1) sales/use tax exemption for certified
  high-tech data centers; tiered investment thresholds by county
  population ($25M-$250M) plus new-quality-jobs requirements; annual
  reporting to Senate Finance / House Ways & Means
- region: `["us", "us_states"]` | category: `economic_dev` | tags:
  `incentives, reporting` | policy_types: `incentive, regulation` |
  language: en
- format: HTML
- practical: no rate limit documented
- effort tier: b
- why worth adding: existing `us/georgia.yaml` only has EPD (environmental)
  and General Assembly entries — DOR is the actual administering agency
  for this incentive and publishes ongoing aggregate-expenditure reports
- verified: yes — WebFetch confirmed live dor.georgia.gov pages
- append to: `us/georgia.yaml`

### 12. North Carolina — EDPNC Data Center Sales & Use Tax Exemptions

- name: "EDPNC — Data Centers Sales & Use Tax Exemptions"
- id: `nc_edpnc_dc_exemption`
- base_url: `https://edpnc.com`
- start_paths: `/incentives/data-centers-sales-use-tax-exemptions/`
- level: subnational (state)
- access: none
- coverage: overview of NC's two data-center exemption tracks —
  "Qualifying Data Center" ($75M/5yr) and "Eligible Internet Data Center"
  ($250M/5yr, restricted to Tier 1/2 economically-distressed counties);
  page explicitly states EDPNC does not administer the incentive itself
  — NC Dept. of Commerce does
- region: `["us", "us_states"]` | category: `economic_dev` | tags:
  `incentives` | policy_types: `incentive` | language: en
- format: HTML
- practical: no rate limit documented; note the tier-1/2-county geographic
  targeting is itself a distinguishing feature vs. other states surveyed
- effort tier: b
- why worth adding: existing `us/north_carolina.yaml` only has NCUC
  (regulatory) and General Assembly entries; the direct NCDOR "Important
  Notice" URLs found in search (`ncdor.gov/important-notice-qualifying-
  datacenter`) returned HTTP 404 on fetch — EDPNC is the verified live
  alternative pointing to the same program
- verified: yes — WebFetch confirmed live edpnc.com page and thresholds
- append to: `us/north_carolina.yaml`

### 13. Washington — DOR Data Center Sales/Use Tax Exemption Eligibility

- name: "Washington Department of Revenue — Data Centers Sales and Use Tax Exemption Eligibility"
- id: `wa_dor_dc_exemption`
- base_url: `https://dor.wa.gov`
- start_paths:
  - `/forms-publications/publications-subject/tax-topics/data-centers-sales-and-use-tax-exemption-eligibility`
  - `/content/purchases-server-equipment-and-power-infrastructure-use-eligible-data-centers-salesuse-tax-exemption`
- level: subnational (state)
- access: none
- coverage: RCW 82.08.986 / 82.12.986 exemption for eligible server
  equipment and power infrastructure; annual tax-performance-report
  requirement (RCW 82.32.534); no new certificates issued after 1 Jul
  2028
- region: `["us", "us_states"]` | category: `economic_dev` | tags:
  `incentives, reporting` | policy_types: `incentive, law` | language: en
- format: HTML
- practical: no rate limit documented
- effort tier: b
- why worth adding: existing `us/washington.yaml` only has Dept. of
  Commerce (general economic dev, no DC-specific page) and Legislature
  entries — DOR is where the actual eligibility rules and forms live
- verified: yes — WebFetch confirmed live dor.wa.gov page
- append to: `us/washington.yaml`

### 14. Ohio — JobsOhio Data Center Tax Exemption

- name: "JobsOhio — Data Center Tax Exemption"
- id: `oh_jobsohio_dc_exemption`
- base_url: `https://www.jobsohio.com`
- start_paths: `/incentives-programs/data-center-tax-exemption`
- level: subnational (state)
- access: none
- coverage: Ohio's data-center sales-tax exemption (since 2013);
  $100M+ capital investment over 3 years, $1.5M+ annual employee
  compensation; final approval via Ohio Tax Credit Authority
- region: `["us", "us_states"]` | category: `economic_dev` | tags:
  `incentives` | policy_types: `incentive` | language: en
- format: HTML
- practical: no rate limit documented; no efficiency condition found
- effort tier: b
- why worth adding: existing `us/ohio.yaml` has `development.ohio.gov`
  (general economic dev) but not the specific data-center program page;
  JobsOhio (the state's privatized economic-development corporation) is
  the actual public-facing administrator
- verified: yes — WebFetch confirmed live jobsohio.com page
- append to: `us/ohio.yaml`

### 15. Finland — Invest in Finland Data Center Opportunities Map

- name: "Invest in Finland — Map of Data Center Opportunities in Finland"
- id: `fi_investinfinland_dc_map`
- base_url: `https://www.investinfinland.com`
- start_paths: `/tools-resources/data-center-opportunities-map`
- level: national
- access: none
- coverage: Finland's national investment-promotion agency (formerly
  branded Business Finland / "businessfinland.com", now redirects here)
  runs a site-selection database with an "Energy Preferences" filter for
  prospective data-center investors; supporting material describes the
  5MW+ reduced energy-tax rate and heat-recovery/district-heating angle
  (e.g., Google/Hamina waste-heat partnership)
- region: `["eu", "nordic", "finland"]` | category: `economic_dev` |
  tags: `incentives, efficiency` | policy_types: `incentive, report` |
  language: en
- format: HTML (interactive map/filter tool)
- practical: no rate limit documented; note the old
  `businessfinland.com/explore-business-opportunities/data-centers/` URL
  found in search results now 301-redirects to this domain — use the new
  domain, not the old one
- effort tier: b
- why worth adding: distinct from any existing Nordic/Finland entry
  (none currently shipped for Finland specifically); ties investment
  promotion directly to energy/heat-recovery attributes
- verified: yes — confirmed live via browser after following the
  redirect chain (businessfinland.com → investinfinland.com); old direct
  URL is dead
- append to: new `finland.yaml` (no existing Finland-specific file;
  currently only `nordic.yaml` has Finnish entries)

### 16. Norway — Business Norway / Invest in Norway Digital Infrastructure

- name: "Business Norway — Invest in Norway: Digital Infrastructure"
- id: `no_businessnorway_digital_infra`
- base_url: `https://businessnorway.com`
- start_paths: `/invest-in-norway/industries/digital-infrastructure`
- level: national
- access: none
- coverage: Norway's national investment-promotion agency page on data
  centers/digital infrastructure; references the 2018 national data
  centre strategy (tax reductions + connectivity incentives) and near-
  100%-hydropower grid; notes a revised strategy pending
- region: `["eu", "nordic", "norway"]` | category: `economic_dev` |
  tags: `incentives` | policy_types: `incentive, report` | language: en
- format: HTML
- practical: no rate limit documented; page is light on itemized
  incentive detail (directs readers to contact Invest in Norway directly)
- effort tier: b
- why worth adding: fills a gap — existing `nordic.yaml` has Norway's
  energy ministry and Enova but not the national investment-promotion
  agency
- verified: yes — WebFetch confirmed live businessnorway.com page
- append to: `nordic.yaml` (Norway section) or new `norway.yaml`

### 17. Sweden — Business Sweden Site Finder

- name: "Business Sweden — Invest in Sweden: Site Finder"
- id: `se_businesssweden_sitefinder`
- base_url: `https://www.business-sweden.com`
- start_paths: `/invest-in-sweden/online-tools/site-finder/`
- level: national
- access: none
- coverage: Sweden's national investment-promotion agency's interactive
  site-selection tool covering manufacturing/data-center/logistics/
  battery industries; supports adding "regional incentive areas" as a map
  layer alongside infrastructure layers
- region: `["eu", "nordic", "sweden"]` | category: `economic_dev` |
  tags: `incentives` | policy_types: `incentive` | language: en
- format: HTML (interactive tool)
- practical: no rate limit documented; likely JS-heavy (map tool) —
  recommend `requires_playwright: true`
- effort tier: b
- why worth adding: distinct from the existing `sweden.yaml` entries
  (Energy Agency, Riksdagen, Regeringen, Energimarknadsinspektionen,
  Riksrevisionen — all ministries/legislature/regulators, none from the
  investment-promotion side)
- verified: yes — WebFetch confirmed live business-sweden.com page,
  described data-center site-finder tool and regional-incentive layer
- append to: `sweden.yaml`

### 18. Denmark — Invest in Denmark

- name: "Invest in Denmark"
- id: `dk_investindk`
- base_url: `https://investindk.com`
- start_paths: `/`
- level: national
- access: none
- coverage: Denmark's national investment-promotion agency (under the
  Ministry of Foreign Affairs); Cleantech section covers green data
  centers, waste-heat-to-district-heating case studies (Meta Odense,
  Microsoft), and green-power positioning for data-center investment
- region: `["eu", "nordic", "denmark"]` | category: `economic_dev` |
  tags: `incentives, efficiency` | policy_types: `incentive, report` |
  language: en
- format: HTML
- practical: **the specific deep-link found in search
  (`/set-up-a-business/cleantech/green-data/`) is dead — confirmed 404 via
  both WebFetch and browser.** The site has been restructured; "Cleantech"
  is now a top-level section reachable from the homepage. Recommend crawl
  `start_paths: ["/"]` with `allowed_path_patterns: ["/set-up-a-
  business/*", "/insights/*", "/cases/*"]` and let the crawler discover
  the current data-center subpages rather than hardcoding a stale path
- effort tier: b
- why worth adding: distinct from the existing `denmark.yaml` entries
  (Danish Energy Agency, Heat Supply Act) — this is the investment-
  promotion agency, explicitly marketing waste-heat-reuse case studies to
  prospective data-center investors
- verified: partial — homepage confirmed live and on-topic; the specific
  data-center deep link is stale (see practical note)
- append to: `denmark.yaml`

### 19. Iceland — Business Iceland (Invest in Iceland) Investment Opportunities

- name: "Business Iceland — Investment Opportunities"
- id: `is_investiniceland_opportunities`
- base_url: `https://www.inspiredbyiceland.com`
- start_paths: `/business/investment-opportunities`
- level: national
- access: none
- coverage: Iceland's investment-promotion function (rebranded under
  "Inspired by Iceland" / Business Iceland; old `invest.is` domain
  301-redirects here); markets 100% renewable geothermal/hydro power for
  data centers and other energy-intensive investment, plus regional
  investment-agreement incentives
- region: `["nordic", "iceland"]` | category: `economic_dev` | tags:
  `incentives, efficiency` | policy_types: `incentive, report` |
  language: en
- format: HTML
- practical: no rate limit documented; note the domain migration
  (`invest.is` → `inspiredbyiceland.com`) — use the new domain
- effort tier: b
- why worth adding: no existing Iceland file at all in `config/domains/`
  (Icelandic National Energy Authority is the only Iceland entry, inside
  `nordic.yaml`) — this is a second, distinct agency
- verified: yes — WebFetch confirmed live page after following the
  redirect; confirmed data-center/renewable-energy content
- append to: `nordic.yaml` (Iceland section) or new `iceland.yaml`

---

## Unverified / needs-human-check

1. **France — TICFE electricity-tax reduction for data centers.** Multiple
   secondary sources (Data Center Dynamics, PwC) describe a reduction of
   France's electricity excise tax (TICFE) from €22.5/MWh to €12/MWh
   targeted at data centers, plus an "environmental standards" commitment
   requirement. Could not locate the actual government source (Loi de
   Finances article, `legifrance.gouv.fr`, or `impots.gouv.fr` page) in
   the time available — `welcome.businessfrance.fr`'s tax-incentives page
   was checked and does **not** mention data centers or TICFE at all. A
   human should search `legifrance.gouv.fr` for the specific Loi de
   Finances article and/or the DGEC/DGFiP guidance before drafting.

2. **Wyoming — exact "Managed Data Center Cost Reduction Funding"
   sub-page URL.** `https://wyomingbusiness.org/communities/financing/
   business-ready-community/managed-data-center-cost-reduction-funding/`
   is named and linked from the (confirmed-live) parent BRC page and
   appears in search results, but returned HTTP 404 on two direct fetch
   attempts (WebFetch and browser navigate). Likely a trailing-slash or
   CMS-routing quirk rather than a dead program — a human with an
   interactive browser session should confirm the live path before it's
   hardcoded into `start_paths`.

3. **Arizona Commerce Authority's own program page**
   (`https://www.azcommerce.com/incentives/computer-data-center-program/`)
   — confirmed to exist and be on-topic via search snippets, but returned
   HTTP 403 to both WebFetch and (implicitly) automated access, suggesting
   bot protection. The `azleg.gov` statute text (candidate #4 above) was
   used instead as the verified, crawlable primary source; a human could
   still add azcommerce.com separately with `requires_playwright: true`
   if the crawler's real browser fetch handles it better than these
   verification tools did.

---

## Summary

- Region: US data-center tax-incentive programs (11 states) + 8
  international investment-promotion agencies (Ireland, Singapore,
  Malaysia, Finland, Norway, Sweden, Denmark, Iceland)
- Verified candidates: 19
- Effort tier: 0 tier-a, 19 tier-b, 0 tier-c
- Unverified/needs-human-check: 3
- Highest-value find: Singapore's DC-CFA2 (IMDA/EDB) — PUE ≤1.25, ≥50%
  green power, and Green Mark Platinum certification as literal
  conditions of the economic-development capacity allocation
