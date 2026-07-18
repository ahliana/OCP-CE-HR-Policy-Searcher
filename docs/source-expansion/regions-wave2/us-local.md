# US Local (County/Municipal) Source Expansion — Wave 2 Findings

Region scope: US **county and municipal** governments (and special-purpose local districts,
e.g. public utility districts) in major data-center markets — the tier below state energy
offices/PUCs and below the Virginia county pair (Loudoun, Prince William) already drafted in
wave 1. State-level and federal sources are out of scope here.

## Dedup note

Read `config/domains/us/*.yaml` (all 50 state files + `us_federal.yaml`) and
`docs/source-expansion/draft/crawl/us-states.yaml` before proposing anything below. Confirmed:
- No county/municipal `base_url` exists anywhere in `config/domains/` today (grepped every
  candidate jurisdiction name — zero hits except unrelated substring matches, e.g. "Fairfax" only
  appearing as a legislator's district in `virginia.yaml` bill sponsor metadata).
- `docs/source-expansion/draft/crawl/us-states.yaml` already carries **Loudoun County, VA**
  (`us_loudoun_county_va`, `loudoun.gov`) and **Prince William County, VA**
  (`us_prince_william_county_va`, `pwcva.gov`) as draft entries slated for
  `config/domains/us/virginia.yaml` — both skipped here, not re-proposed.
- All `base_url`s below are net-new.

## How to read "verified"

Each candidate was checked two ways: (1) a live WebFetch of the specific URL, and (2) at least
one independent news/legal-alert source corroborating the policy content. Several official
county/city sites (Culpeper, Fauquier, Fort Worth, Atlanta, Reno, Chicago, Elk Grove Village)
returned HTTP 403/404 to the automated fetch tool while still being indexed live by search
engines with matching titles — almost certainly bot/WAF blocking (CivicPlus/Cloudflare/Akamai),
not a dead page. Those are listed under **Unverified / needs-human-check** with the exact URL,
so a human with a real browser can confirm in seconds; do not silently upgrade them to verified.

---

## Verified candidates (ranked best-first)

### 1. Grant County Public Utility District No. 2 (Washington) — "Evolving Industry" Data Center Rate Schedule
- **name**: "Grant County PUD — Evolving Industry (Data Center) Rate Schedules"
- **id**: `us_grant_county_pud_wa` · new file `config/domains/us/washington.yaml` (append) or a
  locality subsection — Grant PUD is a special-purpose local government (public utility
  district), not the county itself, but is the operative "local government energy authority."
- **base_url**: `https://www.grantpud.org`
- **start_paths**: `/rates-fees`, `/templates/galaxy/images/images/Downloads/Rates/Evolving_Industry_Rate_17/Resolution_8940_-2.pdf`
- **level**: local (special-purpose district — county-created public utility district)
- **access**: none
- **coverage**: Rate Schedule 17 ("Evolving Industry," i.e., data centers/crypto/AI compute)
  restructures pricing effective April 2026: strips data centers of preferential low-cost
  hydropower access from Priest Rapids/Wanapum dams, creates a "core vs. non-core customer"
  cost-allocation policy, and layers demand charges as data centers reach 48% of Grant County's
  retail electric sales. region: `["us", "us_states", "washington"]`; category: `regulatory`;
  tags: `["mandates", "planning", "data_center_specific"]`; policy_types: `["regulation",
  "program"]`; language: `en`.
- **format**: HTML (rates landing page) + PDF (rate resolutions/schedules)
- **practical**: no documented rate limit; standard municipal-utility CMS. Rate schedule PDFs
  live under a versioned `/images/2026/2026-Rates/` and older `/images/images/Downloads/Rates/`
  path — expect path churn year to year; a crawl should target the `/rates-fees` index page and
  follow PDF links rather than hardcoding dated paths.
- **effort tier**: b (crawl domain)
- **why worth adding**: Quincy/Grant County WA is one of the single densest US data-center
  clusters (27+ buildings, Microsoft/Sabey/H5), and this is a real, numbered, dollar-figure local
  energy-rate policy singling out data centers — the most concrete "local government sets
  data-center energy terms" artifact found in this entire wave.
- **verified**: yes. Fetched `https://www.grantpud.org/rates-fees` live — confirmed official
  Grant County PUD page listing Rate Schedule 17 tiers (17-A/17-B) and linking current PDF rate
  resolutions. Corroborated by KilowattLogic and gcj.news coverage of the April 2026 restructure.

### 2. Linn County, Iowa — Data Center Zoning Ordinance (Unincorporated Linn County)
- **name**: "Linn County, Iowa — Data Centers in Unincorporated Linn County"
- **id**: `us_linn_county_ia`
- **base_url**: `https://www.linncountyiowa.gov`
- **start_paths**: `/1862/Data-Centers-in-Unincorporated-Linn-Coun`, `/DocumentCenter/View/27695/PA26-0001-Ordinance-PDF`
- **level**: local (county)
- **access**: none
- **coverage**: Adopted ordinance (approved ~Feb 18, 2026) creates zoning standards for data
  centers on unincorporated county land: setbacks, noise limits, traffic/road-impact review, and
  — for large projects — a mandatory water study (cooling method + efficiency measures),
  water-use agreement, and economic-development/community-benefit agreement. Secondary news
  coverage (Inside Climate News, Planetizen) additionally describes quarterly energy/on-site
  generation reporting to the Iowa Utilities Commission with sustainability metrics including
  waste-heat reuse — not independently confirmed on the county's own summary page, so treat that
  specific claim as needing the linked ordinance PDF for confirmation. region: `["us",
  "us_states", "iowa"]`; category: `regulatory`; tags: `["planning", "mandates",
  "data_center_specific"]`; policy_types: `["regulation"]`; language: `en`.
- **format**: HTML (summary page) + PDF (ordinance, staff report)
- **practical**: no documented rate limit; CivicPlus-style county CMS, standard.
- **effort tier**: b
- **why worth adding**: One of the most detailed county-level data-center ordinances found in
  the whole scan (cooling/water efficiency is directly adjacent to our PUE/heat-reuse taxonomy),
  and it is already forcing developer behavior — Google is reportedly trying to annex land into
  a neighboring city specifically to escape this ordinance.
- **verified**: yes. Fetched `https://www.linncountyiowa.gov/1862/Data-Centers-in-Unincorporated-Linn-Coun`
  live — confirmed official county page, last updated March 4, 2026, with working links to the
  ordinance PDF and staff report.

### 3. City of New Albany, Ohio — Data Centers (dedicated portal)
- **name**: "City of New Albany, Ohio — Data Centers"
- **id**: `us_new_albany_oh`
- **base_url**: `https://datacenters.newalbanyohio.org`
- **start_paths**: `/`
- **level**: local (municipal)
- **access**: none
- **coverage**: Dedicated city microsite covering the Technology Manufacturing District (TMD,
  Codified Ordinances §1154) and General Employment district (§1153) zoning that permits data
  centers in the 12,000-acre New Albany International Business Park (straddling Franklin/Licking
  counties). Documents architectural/design standards, mechanical-equipment screening, noise caps
  (tied to ambient residential traffic noise), water/wastewater and air-quality requirements.
  region: `["us", "us_states", "ohio"]`; category: `regulatory`; tags: `["planning", "mandates",
  "data_center_specific"]`; policy_types: `["regulation", "guidance"]`; language: `en`.
- **format**: HTML
- **practical**: no documented rate limit; small dedicated microsite, low page count, easy crawl.
- **effort tier**: b
- **why worth adding**: New Albany/Licking County is described in trade press as "the capital of
  Ohio's data center hub" (Meta, Google, Microsoft, Amazon, QTS, plus AEP's Intel-adjacent
  substation now feeding Meta) — this is the one city in the entire wave with a purpose-built,
  standalone government data-center policy site rather than a buried zoning-code page.
- **verified**: yes. Fetched `https://datacenters.newalbanyohio.org/` live — confirmed official
  City of New Albany site (city seal, `newalbanyohio.org` links, ©2026 footer) with zoning,
  design-standard, and environmental content as described.

### 4. Storey County, Nevada — Tahoe-Reno Industrial Center Development Agreement
- **name**: "Storey County, Nevada — Tahoe-Reno Industrial Center (TRIC) Development Agreement"
- **id**: `us_storey_county_nv`
- **base_url**: `https://www.storeycounty.org`
- **start_paths**: `/647/Tahoe-Reno-Industrial-Center-Development`
- **level**: local (county)
- **access**: none
- **coverage**: Document repository (21 linked files) for the TRIC development agreement — I-2
  Heavy Industrial zoning ordinance (adopted 1999), infrastructure plans (water/sewer/drainage/
  rail/roadway), design guidelines, and CC&Rs governing the industrial park that hosts Switch,
  Google, and Microsoft data centers plus Tesla's Gigafactory. region: `["us", "us_states",
  "nevada"]`; category: `regulatory`; tags: `["planning", "incentives"]`; policy_types:
  `["regulation", "report"]`; language: `en`.
- **format**: HTML (index) + PDF (agreements, ordinance, infrastructure plans)
- **practical**: no documented rate limit; standard CivicPlus county site.
- **effort tier**: b
- **why worth adding**: TRIC is the largest industrial park in the US and third-largest in the
  world by land area, and its zoning + tax-abatement framework is the direct local-government
  counterpart to the state-level Nevada large-load/Clean Transition Tariff dockets already noted
  in `config/domains/us/nevada.yaml`.
- **verified**: yes. Fetched `https://www.storeycounty.org/647/Tahoe-Reno-Industrial-Center-Development`
  live — confirmed official Storey County page listing the development agreement, zoning
  ordinance, and infrastructure documents.

### 5. Fairfax County, Virginia — Data Centers Zoning Ordinance Amendment
- **name**: "Fairfax County, Virginia — Data Centers (Adopted Zoning Ordinance Amendment)"
- **id**: `us_fairfax_county_va`
- **base_url**: `https://www.fairfaxcounty.gov`
- **start_paths**: `/planning-development/data-centers`
- **level**: local (county)
- **access**: none
- **coverage**: Zoning ordinance amendment adopted Sept 10, 2024 (effective Sept 11, 2024).
  Requires a "future energy needs" assessment at special-exception application, proposed
  LEED-Silver/on-site-solar/off-site-renewable-investment energy standards, a 200-ft residential
  setback, fully-enclosed cooling/generator equipment, and a noise study. Links the adopted text,
  staff report, follow-on motions, and a Jan 2024 research report. region: `["us", "us_states",
  "virginia"]`; category: `regulatory`; tags: `["planning", "mandates", "efficiency",
  "data_center_specific"]`; policy_types: `["regulation", "report"]`; language: `en`.
- **format**: HTML (page) + PDF (adopted ordinance text, staff report, research report)
- **practical**: no documented rate limit; standard county CMS.
- **effort tier**: b
- **why worth adding**: Fairfax is the direct neighbor of Loudoun/Prince William (already in the
  wave-1 draft) in the densest data-center corridor in the world, and unlike most peer counties
  it explicitly proposes energy-efficiency (LEED/on-site renewables) conditions, not just
  noise/setback rules — closest fit to our efficiency/PUE taxonomy of the VA county tier.
- **verified**: yes. Fetched `https://www.fairfaxcounty.gov/planning-development/data-centers`
  live — confirmed official page with working links to the adopted ordinance PDF, staff report,
  and research report.

### 6. City of South Fulton, Georgia — Data Center Ordinance
- **name**: "City of South Fulton, Georgia — Data Center Ordinance / Town Hall"
- **id**: `us_south_fulton_ga`
- **base_url**: `https://www.cityofsouthfultonga.gov`
- **start_paths**: `/CivicAlerts.asp?AID=777`
- **level**: local (municipal)
- **access**: none
- **coverage**: City-enacted Data Center Ordinance: 100-150 ft residential buffers, equipment
  screening, noise/lighting controls, mandatory Special Use Permits, and risk-assessment review.
  region: `["us", "us_states", "georgia"]`; category: `regulatory`; tags: `["planning",
  "mandates", "data_center_specific"]`; policy_types: `["regulation"]`; language: `en`.
- **format**: HTML
- **practical**: no documented rate limit; CivicPlus alert-page URL pattern (`AID=` query param)
  — likely to be superseded by newer alert IDs over time; recommend also crawling the city's main
  planning/zoning department page if a stable non-alert URL is found.
- **effort tier**: b
- **why worth adding**: South Fulton is a Fulton County-proper municipality with a genuinely
  adopted (not just proposed) data-center ordinance, filling the gap left by Fulton County itself
  (no dedicated ordinance page found — see Unverified list) and Atlanta (403-blocked).
- **verified**: yes. Fetched `https://www.cityofsouthfultonga.gov/CivicAlerts.asp?AID=777` live —
  confirmed official city page describing the ordinance and an active town hall/permitting
  pipeline.

### 7. Frederick County, Maryland — Data Centers Workgroup / Critical Digital Infrastructure Overlay
- **name**: "Frederick County, Maryland — Data Centers Workgroup"
- **id**: `us_frederick_county_md`
- **base_url**: `https://www.frederickcountymd.gov`
- **start_paths**: `/8544/Data-Centers-Workgroup`, `/CivicAlerts.aspx?AID=5845`
- **level**: local (county)
- **access**: none
- **coverage**: Documents the 2023-2024 Data Centers Workgroup (11 members) that produced a
  Critical Digital Infrastructure Overlay Zone limiting data centers to ~2,600 acres (0.6% of the
  county, concentrated around the Eastalco site), plus a July 2026 executive-order pause on new
  applications pending the state Data Center Impact Analysis, tied to Maryland's new PSC
  large-load customer registry (Utility RELIEF Act). region: `["us", "us_states", "maryland"]`;
  category: `regulatory`; tags: `["planning", "mandates", "data_center_specific"]`;
  policy_types: `["regulation", "report"]`; language: `en`.
- **format**: HTML
- **practical**: no documented rate limit; standard CivicPlus CMS; the `/9122/Data-Centers` path
  referenced in older press 404s — use `/8544/Data-Centers-Workgroup` and the CivicAlerts page
  instead.
- **effort tier**: b
- **why worth adding**: Maryland is emerging as a second major East Coast battleground (Prince
  George's, Frederick, Washington County all active in 2026); Frederick has the most fully
  documented workgroup-to-ordinance pipeline of the three, and ties directly to the new state PSC
  large-load registry — a genuine local/state policy linkage.
- **verified**: yes. Fetched both URLs live — confirmed official Frederick County pages (both
  under `frederickcountymd.gov`) describing the workgroup mandate and the July 2026 pause.

### 8. Maricopa County, Arizona — Modernized Zoning Ordinance (Data Center Definitions)
- **name**: "Maricopa County, Arizona — Adopted (Modernized) Zoning Ordinance"
- **id**: `us_maricopa_county_az`
- **base_url**: `https://www.maricopa.gov`
- **start_paths**: `/2753/Adopted-Regulations`, `/CivicAlerts.aspx?AID=3541`
- **level**: local (county)
- **access**: none
- **coverage**: Board of Supervisors adopted a modernized zoning ordinance (Dec 10, 2025) that,
  for the first time, formally defines "Data Center" as a land use and restricts it to IND-2
  (general industrial) and IND-3 (heavy industrial) districts; land not so zoned must go through
  full rezoning. region: `["us", "us_states", "arizona"]`; category: `regulatory`; tags:
  `["planning", "mandates", "data_center_specific"]`; policy_types: `["regulation"]`;
  language: `en`.
- **format**: HTML (page) + PDF (full zoning ordinance, agenda packets)
- **practical**: no documented rate limit; standard county CMS.
- **effort tier**: b
- **why worth adding**: Maricopa County (Phoenix metro) is one of the top-3 US data-center
  markets and this is the county's first-ever formal data-center zoning definition — a clean,
  recent, directly on-topic land-use policy.
- **verified**: yes. Fetched both URLs live — confirmed official Maricopa County pages; the news
  flash explicitly states the ordinance "clarifies and expands definitions, including for...
  Data Centers."

### 9. City of Chandler, Arizona — Data Center Zoning Ordinance No. 5033
- **name**: "City of Chandler, Arizona — Data Center Ordinance (No. 5033)"
- **id**: `us_chandler_az`
- **base_url**: `https://www.chandleraz.gov`
- **start_paths**: `/news-center/chandlers-data-center-ordinance-now-effect`, `/sites/default/files/departments/development-services/PLH22-0053-Ordinance-No-5033-Data-Center.pdf`
- **level**: local (municipal)
- **access**: none
- **coverage**: Ordinance 5033 (effective Jan 5, 2023) restricts data centers to
  Planned-Area-Development (PAD) zones only, and mandates pre-construction and five-years-of
  annual noise studies, resident notification protocols, and backup-generator
  maintenance/testing limits. region: `["us", "us_states", "arizona"]`; category: `regulatory`;
  tags: `["planning", "mandates", "data_center_specific"]`; policy_types: `["regulation"]`;
  language: `en`.
- **format**: HTML (news page) + PDF (adopted ordinance text)
- **practical**: no documented rate limit; standard municipal CMS; the ordinance PDF is hosted
  directly on `chandleraz.gov` (not a third-party mirror).
- **effort tier**: b
- **why worth adding**: One of the earliest (Jan 2023) and most specific city-level data-center
  noise/generator ordinances in the country, hosted with the actual ordinance PDF on the city's
  own domain — a clean, fully self-contained source.
- **verified**: yes. Fetched the news-center page live — confirmed official City of Chandler page
  (city seal, department contact info) describing Ordinance 5033's provisions in detail.

### 10. Prince George's County, Maryland — Qualified Data Center Task Force (Legislative Branch)
- **name**: "Prince George's County, Maryland — Qualified Data Center Task Force"
- **id**: `us_prince_georges_county_md`
- **base_url**: `https://pgccouncil.us`
- **start_paths**: `/1051/Qualified-Data-Center-Task-Force`
- **level**: local (county — legislative/council branch domain, distinct from `princegeorgescountymd.gov`)
- **access**: none
- **coverage**: Council Resolution CR-16-2025 established a 19-member task force (county
  government, utilities, labor, business, environmental-justice, academic reps) to study energy
  demand/ratepayer impact, air/water/woodland environmental effects, and quality-of-life impacts
  of "Qualified Data Center" siting; final report issued Nov 2025 with rezoning recommendations.
  Page links the final report and the founding council resolution as PDFs. region: `["us",
  "us_states", "maryland"]`; category: `regulatory`; tags: `["planning", "research"]`;
  policy_types: `["report", "regulation"]`; language: `en`.
- **format**: HTML (page) + PDF (final report, resolution)
- **practical**: no documented rate limit; note the domain is `pgccouncil.us`, NOT
  `princegeorgescountymd.gov` — the county executive branch's own site returned a 403 to the
  fetch tool on the guessed URL and no working replacement was found this pass (see Unverified).
- **effort tier**: b
- **why worth adding**: Prince George's passed a full two-year moratorium on new data-center
  development in 2026 after this task force's report — among the strongest local-government
  responses found in the entire wave, and the underlying study explicitly scopes energy-demand
  and environmental impact.
- **verified**: yes. Fetched `https://pgccouncil.us/1051/Qualified-Data-Center-Task-Force` live —
  confirmed official Prince George's County Council page with working links to the final report
  and resolution PDFs.

### 11. Morrow County, Oregon — Zoning Ordinance (Industrial Districts Used for Data-Center Rezoning)
- **name**: "Morrow County, Oregon — Zoning Ordinance"
- **id**: `us_morrow_county_or`
- **base_url**: `https://www.morrowcountyor.gov`
- **start_paths**: `/planning/page/zoning-ordinance`, `/ordinances/morrow-county-zoning-ordinance`
- **level**: local (county)
- **access**: none
- **coverage**: The 2017 Morrow County Zoning Ordinance (10 articles) is the instrument the county
  has repeatedly used to rezone agricultural land to industrial for AWS/Amazon and other
  hyperscale campuses (e.g., the Percheron project, ag-to-industrial rezone near Boardman); the
  ordinance's "Space Age Industrial," "General Industrial," and "Port Industrial" zones are the
  operative districts. No data-center-specific chapter exists yet — this is the general
  zoning-amendment mechanism, lower specificity than entries #1-10 above. region: `["us",
  "us_states", "oregon"]`; category: `regulatory`; tags: `["planning"]`; policy_types:
  `["regulation"]`; language: `en`.
- **format**: HTML
- **practical**: no documented rate limit; standard county CMS.
- **effort tier**: b
- **why worth adding**: Morrow/Umatilla counties are Oregon's single largest data-center
  corridor (AWS Boardman/Hermiston, Sabey Umatilla), and every rezoning fight there runs through
  this ordinance — worth tracking even without a dedicated DC chapter, to catch future
  amendments.
- **verified**: yes. Fetched `https://www.morrowcountyor.gov/planning/page/zoning-ordinance` live
  — confirmed official Morrow County page hosting the full zoning ordinance text online.

---

## Unverified / needs-human-check

All of these have real, on-topic policy content confirmed via search-engine snippets and/or
independent news/legal-alert coverage, and the URL below is the exact page search results point
to on the jurisdiction's own domain — but the automated fetch tool got HTTP 403 or 404 (bot/WAF
blocking is the likely cause; several of these sites are known to run Cloudflare/Akamai bot
protection). Do not add to `config/domains/` until a human confirms with a real browser.

- **Culpeper County, VA** — `https://web.culpepercounty.gov/planning/page/ch-5-economic-development`
  (Technology Zones / Culpeper Tech Zone, 690-acre by-right data-center area). 403 on fetch;
  content independently confirmed via Google-cached search snippets of the same URL and
  Data Center Frontier coverage.
- **Fauquier County, VA** — county's own site (`fauquiercounty.gov`) 403'd on every path tried;
  the Dec 14, 2023 Data Center Development Policy itself is only confirmed hosted at a
  third-party mirror (`pecva.org/wp-content/uploads/fauquier-data-center-policy-december-14-2023.pdf`),
  which is NOT an acceptable `base_url` per the brief (not the government's own site). Needs a
  human to find the policy's actual location on `fauquiercounty.gov` (likely under Community
  Development or BoardDocs).
- **City of Fort Worth, TX** — `https://www.fortworthtexas.gov/departments/city-manager/datacenters`
  (dedicated page per its exact search-result title "Data Centers – Welcome to the City of Fort
  Worth"; city considering 250-ft residential setbacks and closed-loop cooling mandates as of
  July 2026). 403 on fetch.
- **City of Atlanta, GA** — `https://citycouncil.atlantaga.gov/Home/Components/News/News/3928/`
  (Ordinance 25-O-1063, special-use permits citywide, water/energy disclosure requirements,
  Beltline/MARTA-adjacent bans). 403 on fetch; also available at the city's Legistar instance,
  `https://atlantacityga.iqm2.com/Citizens/Detail_LegiFile.aspx?ID=37303`.
- **City of Chicago, IL** — `https://www.chicago.gov/city/en/depts/env/supp_info/sustainable-data-centers.html`
  (Sustainable Data Centers Working Group, interdepartmental energy/environmental-impact study,
  recommendations report delivered July 2026). 403 on fetch; exact title/URL confirmed via
  search.
- **City of Reno, NV** — data-center land-use/CUP standards under Title 18 of the Reno Land
  Development Code; the specific zoning-code and April 2026 council-news URLs both 404'd for the
  fetch tool. Base domain would be `https://www.reno.gov`; a human should locate the current
  Title 18 data-center text-amendment page via the city's own site search.
- **Village of Elk Grove Village, IL** — `https://www.elkgrove.org/government/community-development/codes-standards`
  (I-1/I-2 industrial rezonings for the Stream DC and other data-center campuses). 403 on fetch.
- **City of Hillsboro, OR** — `https://www.hillsboro-oregon.gov/community/data-centers` (exact
  title match "Data Centers in Hillsboro | City of Hillsboro, OR" in search; city council
  evaluating a new data-center use category/definition and utility-impact review standards in
  2026). 403 on fetch.
- **Douglas County, GA** — moratorium (90 days, extended) on data-center zoning applications is
  well-documented in press, but no live page was found on the county's own domain
  (`douglascountyga.gov`); the resolution PDF is only confirmed hosted at a third-party mirror
  (`wwals.net`). Needs a human to locate the resolution on the county's own site (likely under
  Board of Commissioners agendas/BoardDocs).
- **Fulton County, GA (proper, not South Fulton)** — a "Data Center Review Committee" is
  referenced in local news/social coverage, but no dedicated ordinance page was found on
  `fultoncountyga.gov`; only the general Planning/Zoning/Permitting ordinances index page
  (`fultoncountyga.gov/inside-fulton-county/fulton-county-departments/public-works/planning-zoning-and-permitting/permits-and-plan-review/ordinances-and-regulations`)
  was confirmed, which is not data-center-specific enough to propose on its own.
- **Iron County, UT** — `https://ironcountyut.gov/files/planning/data-center-solar-moratorium.pdf`
  (Ordinance 2026-13, 180-day data-center/solar moratorium). The PDF fetched successfully (not a
  404) but its content could not be text-extracted by the fetch tool — needs a human to confirm
  the ordinance text directly.
- **City of Mesa, AZ** — `https://mesa.legistar.com/View.ashx?M=F&ID=14286289&GUID=01EC687C-17BD-42D8-883A-50E276C8F1FB`
  (Data Center & PAD Text Amendments, June 11, 2025 — noise study, utility-confirmation-letter,
  and future-energy-needs-assessment requirements for data-center applications). PDF fetched
  successfully but binary/unreadable to the fetch tool; content corroborated only by the
  Legistar item title and a Tucson planning-commission memo referencing Mesa's amendment.
- **City of Quincy, WA** — Ordinance 22-570 (fetched via a Washington State OFM ordinance-archive
  mirror, not the city's own site) could not be confirmed as data-center-specific; Quincy's own
  municipal-code host is `codepublishing.com/WA/Quincy/` — a human should search that host
  directly for data-center zoning text before proposing a `base_url`.
- **Box Elder County, UT** and **Cache County, UT** — both passed 180-day data-center
  moratoriums in 2026 (widely reported, tied to the Stratos Project fight), but no direct fetch
  of either county's own site was attempted this pass; likely candidates for a follow-up check.
- **San Antonio, TX** — City Council is actively drafting zoning amendments (1,000-ft buffer from
  residential/parks) as of March 2026, but no ordinance has been adopted yet and no dedicated
  city page was found — revisit once (if) the ordinance passes.

## Explicitly checked, no source found (do not re-check next wave without a new signal)

- **Goodyear, AZ** — no data-center-specific overlay found (only a generic Transit-Oriented
  Development Overlay and Freeway Development Overlay).
- **City of Dallas, TX** — no dedicated data-center zoning ordinance found; data centers fall
  under existing generic industrial-use zoning.
- **Abilene, TX** — no dedicated ordinance found despite major OpenAI/Stargate construction
  nearby; existing nuisance/noise ordinances apply generically.
- **Cook County, IL** — only a generic property-tax-incentive program (Class 6b/8, assessed-value
  abatement) that is not data-center-specific; not proposed.
- **Umatilla County, OR** — no county-specific zoning/energy page found; Umatilla Electric
  Cooperative (private, not a government body) is the relevant energy actor, and the only
  government hit was the state ODOE's Umatilla-Morrow siting-coordination page (state-level, out
  of scope for this local-tier pass).
- **East Wenatchee, WA** — no data-center provisions found in Title 17 of its municipal code.
- **Des Moines, West Des Moines, Council Bluffs, Altoona, IA** — heavy hyperscale presence
  (Microsoft, Meta, Google) but no dedicated government data-center policy page found for any of
  the four; zoning actions exist only as one-off council-meeting approvals, not standing
  ordinances or pages.
- **Omaha and Papillion, NE** — no data-center-specific zoning ordinance or page found; general
  zoning chapters exist but are not data-center-specific.

---

## Summary of new client needs

None. Every verified and unverified candidate above is a plain crawl domain (tier b — HTML pages
with linked PDFs). No new structured API client (tier c) is needed for this region.
