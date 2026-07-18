# US States/Local Source Expansion — Research Findings

Region scope: US subnational (state-level) + local/regional bodies. US federal legislation
(GovInfo), federal rulemaking (Regulations.gov), and state legislation (LegiScan) are already
covered and NOT re-proposed here.

## Dedup note - repo state is different than expected

The brief said "there is no US crawl file yet." That is not accurate: `config/domains/us/`
already contains **one file per state** (50 files + `us_federal.yaml`), and the well-populated
ones already cover exactly the categories this assignment asked for — state energy offices
(NYSERDA in `new_york.yaml`, California Energy Commission in `california.yaml`, Mass DOER in
`massachusetts.yaml`), PUCs (Arizona Corporation Commission, Illinois Commerce Commission, North
Carolina Utilities Commission, etc.), and even a Nashville Metro district energy system entry.
Several state files are non-empty stubs (comment-only, ~370 bytes: Alabama, Alaska, Arkansas,
Delaware, Hawaii, Idaho, Kansas, Kentucky, Louisiana, Maine, Mississippi, Missouri, Nebraska,
New Hampshire, New Mexico, North Dakota, Oklahoma, Rhode Island, South Dakota, Vermont, West
Virginia, Wyoming). All `base_url`s in the populated files were extracted and checked before any
candidate below was proposed (see full list pulled via grep across `config/domains/us/*.yaml`).

Every candidate below is a genuinely new `base_url` not present anywhere in `config/domains/us/`
or `config/domains/api_sources.yaml`. No new structured API client is proposed (tier c): every
state PUC docket system found is an HTML search interface, not a documented/public API, so all
candidates are tier b (plain crawl domains).

## Verified candidates (ranked best-first)

### 1. Virginia State Corporation Commission (SCC) — Case Information / Docket Search
- **id**: `va_scc` · append to `config/domains/us/virginia.yaml`
- **base_url**: `https://www.scc.virginia.gov` (case info hub redirects to `http://www.scc.virginia.gov/case-information/` — non-HTTPS canonical, worth flagging to the crawler config)
- **start_paths**: `/case-information/`, `/pages/Data-Centers` (SCC's own data-center initiatives fact sheet lives at `/media/sccvirginiagov-home/about-the-scc/fact-sheets/scc-data-center-initiatives-02-2026.pdf`)
- **level**: subnational (state regulatory commission)
- **access**: none (open docket search, no key)
- **coverage**: Virginia's PUC-equivalent. In Nov 2025 the SCC approved a new **GS-5 rate class** for customers ≥25 MW (nearly all of VA's ~450 data centers), effective Jan 1, 2027, with 14-year contracts and 85%/60% minimum demand charge floors. As of July 2026 the SCC is actively considering shifting more transmission cost allocation onto data centers in the Dominion biennial review. Directly complements the HB323/HB906/HB824 bill-tracking entries already in `virginia.yaml` — SCC is the body those bills direct to act.
- **format**: HTML (docket search + PDF orders/fact sheets)
- **practical**: no documented rate limit; standard state-government site; robots.txt not individually checked this pass — recommend crawler default (2-3s) and respecting robots.txt as usual. Update cadence: filings within 24-48 hrs per SCC's own case-info page.
- **effort tier**: b (crawl domain)
- **why worth adding**: Virginia is the single largest US data-center market and this repo already tracks three pending VA heat-reuse/load-flexibility bills that name the SCC as the implementing body — the SCC itself is not yet a source.
- **verified**: yes. Fetched `https://www.scc.virginia.gov/case-information/` (after 301 redirect) — live page describing the Docket Search portal, e-filing, rulemaking and public-comment process. Also fetched the SCC data-center fact-sheet PDF reference and multiple 2025-2026 news confirmations (Virginia Mercury, Utility Dive, Data Center Dynamics) of the GS-5 rate class and ongoing transmission-cost dockets.

### 2. Georgia Public Service Commission — Data Center / Large-Load Rulemaking
- **id**: `ga_psc` · append to `config/domains/us/georgia.yaml`
- **base_url**: `https://psc.ga.gov`
- **start_paths**: `/` (homepage carries the "Information on Data Centers" section), `/site/downloads/datacenterfactsheet.pdf`
- **level**: subnational (state regulatory commission)
- **access**: none (docket search via "FACTS Docket Search," no key; login only needed to subscribe to docket-update alerts)
- **coverage**: Georgia's PUC. Docket #44280 / Documents #222325 & #221165 established a **100 MW peak-demand threshold** (effective Feb 1, 2025) requiring large-load (data-center) customers to accept non-standard terms and pay upstream generation/transmission/distribution costs; July 2025 order froze Georgia Power base rates through 2028 and mandates quarterly large-load tracking reports. `georgia.yaml` already notes SB 34 (cost-allocation law) but has no PSC entry — this is the regulator that implements it.
- **format**: HTML (homepage + docket search) / PDF (fact sheet, orders)
- **practical**: no documented API; standard state site; robots.txt not individually checked. Advanced Search / FACTS Docket Search available; docket updates trackable via free registration (not required to read).
- **effort tier**: b
- **why worth adding**: Georgia is a top-5 and fast-growing US data-center market with an active, on-topic large-load tariff regime not yet represented in the repo.
- **verified**: yes. Fetched `https://psc.ga.gov/` directly — homepage confirmed to carry a dedicated data-center section referencing Docket #44280 and the 2028 rate freeze, plus a downloadable data-center fact sheet and working docket-search navigation.

### 3. Texas PUC Interchange — Large Load Interconnection Rulemaking (Project 58481)
- **id**: `tx_puc_interchange` · append to `config/domains/us/texas.yaml`
- **base_url**: `https://interchange.puc.texas.gov`
- **start_paths**: `/Search/Filings?ControlNumber=58481` (the SB6 large-load rulemaking project — 203 filings as of this check)
- **level**: subnational (state regulatory commission)
- **access**: none (public filing search, no key; note: the plain `puc.texas.gov` marketing site has been rebuilt and old deep links 404 — the Interchange filing system is a separate, stable subdomain)
- **coverage**: Implements Texas SB6 (2025), which directs PUCT to set interconnection standards for large loads (≥75 MW) in ERCOT. Proposed rule 16 TAC §25.194 (March 2026) sets $100k-$300k study fees, $50k/MW financial security, and "Intermediate Agreement" site-control requirements. Comment deadline in this project was April 17, 2026 — an active, on-topic rulemaking docket with filings from the Data Center Coalition, EdgeConneX, NRG, Oncor, CenterPoint, etc.
- **format**: HTML (dynamic docket search results table, one row per filing) with linked PDFs
- **practical**: query-string driven (`?ControlNumber=`); a crawler would need to target specific control numbers (58481 verified; ERCOT/PUCT numbers new load rules would need periodic re-discovery). No documented rate limit; recommend conservative rate limiting since it's a dynamic ASP.NET search app. Old `puc.texas.gov` static pages 404 post-redesign — do not use as base_url.
- **effort tier**: b
- **why worth adding**: Texas is the fastest-growing US data-center/large-load market; this is the live regulatory record of the exact large-load interconnection rule everyone in the sector is reacting to, and Texas has zero PUC-level coverage in the repo today (only SECO + capitol.texas.gov).
- **verified**: yes. Live-navigated to `https://interchange.puc.texas.gov/Search/Filings?ControlNumber=58481` — page rendered "Filings for 58481 / Case Style RULEMAKING TO IMPLEMENT LARGE LOAD INTERCONNECTION STANDARDS UNDER PURA 37.0561 / 203 filing(s)" with a real, dated filing table. (Note: WebFetch returned HTTP 402 on this URL — verification was done via the browser tool instead, which rendered it correctly; the 402 appears to be a WebFetch-side artifact, not a site problem.)

### 4. New York Department of Public Service / PSC — Large Load Interconnection Reform
- **id**: `ny_dps` · append to `config/domains/us/new_york.yaml`
- **base_url**: `https://dps.ny.gov`
- **start_paths**: `/`, document search via `https://documents.dps.ny.gov/public/Common/ViewDoc.aspx` (query-parameter driven, DocRefId per document)
- **level**: subnational (state regulatory commission)
- **access**: none for public documents; "DMM Login" (Document and Matter Management) exists for filers, not required to read
- **coverage**: In Feb 2026 NY PSC opened the "Proceeding on the Motion of the Commission to Address Interconnection Reforms for Large Loads" (Gov. Hochul's Energize NY initiative) — reviewing planning/interconnection, cost allocation, and tariff structure for large loads (11.9 GW in the NYISO queue as of Feb 2026). Technical conference due by Dec 31, 2026; white paper due Feb 12, 2027. `new_york.yaml` currently only has NYSERDA and the state senate — PSC/DPS itself, the body that will set the actual tariff rules, is missing.
- **format**: HTML (site + case search) / PDF (orders, comments)
- **practical**: no documented rate limit; standard NY state site. The `documents.dps.ny.gov` viewer serves PDFs behind a DocRefId GUID param — not browsable without a search step first (via File Search on the main site).
- **effort tier**: b
- **why worth adding**: New York is actively legislating and regulating data-center load growth in 2026 (including a widely reported statewide construction pause), and none of that PSC/DPS activity is currently tracked.
- **verified**: yes. Fetched `https://dps.ny.gov/` — confirmed live, with "File Search" and case-search navigation, and confirmed (via search results) the live Feb 2026 order text at `documents.dps.ny.gov` (direct PDF binary fetch wasn't text-extractable by the fetch tool, but the order's existence and content were corroborated by multiple independent 2026 news sources — Governor's press release, Utility Dive, Columbia Climate Law Blog).

### 5. Oregon Public Utility Commission — Large Customer / Data Center Tariffs
- **id**: `or_puc_large_load` · append to `config/domains/us/oregon.yaml`
- **base_url**: `https://www.oregon.gov/puc` (path-qualified; note this shares the `oregon.gov` root domain with the existing `or_building_codes` entry, which uses bare `https://www.oregon.gov` as its base_url — flagging per the repo's own established pattern of multiple entries sharing one root domain with different paths, e.g. `energy.ca.gov` appears 6× in `california.yaml`)
- **start_paths**: `/puc/utilities/pages/large-load.aspx`
- **level**: subnational (state regulatory commission)
- **access**: none
- **coverage**: Implements Oregon's 2025 POWER Act (HB 3546). Docket **UM 2377** (approved May 7, 2026) created **Schedule 96** for Portland General Electric data centers >20 MW: 100% distribution-upgrade cost recovery, 90% minimum demand charges, 10-30 year escalating contract terms, 1¢/kWh surcharge on >100 MW projects funding low-income energy-burden programs. Related dockets: **UE 433** (Pacific Power), **UE 463**, **UE 424**, **UM 2024**.
- **format**: HTML (policy page linking dockets) / PDF (orders at `apps.puc.state.or.us/orders/`)
- **practical**: no documented rate limit; standard state site. Order PDFs live on a separate `apps.puc.state.or.us` subdomain — worth a follow-up `allowed_path_patterns` note if that subdomain needs separate handling.
- **effort tier**: b
- **why worth adding**: `oregon.yaml` already has the OR Dept. of Energy data-center program and the 2025 building energy code, but not the PUC — the body that just created a first-in-nation dedicated waste-heat-adjacent large-load rate schedule.
- **verified**: yes. Fetched `https://www.oregon.gov/puc/utilities/pages/large-load.aspx` directly — live page confirmed discussing UE 424, UE 430, UM 2024 and general large-customer tariff policy (page content reflects an active, currently-maintained OPUC page; UM 2377/Schedule 96 specifics were corroborated via Utility Dive and Oregon PUC's own May 2026 press release/order PDF found in search).

### 6. Missouri Public Service Commission — Large Load / Data Center Rate Cases
- **id**: `mo_psc` · replaces the stub `config/domains/us/missouri.yaml`
- **base_url**: `https://psc.mo.gov`
- **start_paths**: `/Electric`, `/`  (Orders/Notices, Proposed Rules, and EFIS docket-file access are linked from the homepage)
- **level**: subnational (state regulatory commission)
- **access**: none for reading; "Access EFIS" (Electronic Filing Information System) for docket files, no key required
- **coverage**: Under Missouri SB4, PSC approved (Nov 24, 2025, effective Dec 4) a large-load rate plan for Ameren Missouri covering any new facility ≥75 MW peak demand at 115kV+, with 12-year minimum contracts, 2-year collateral, and an "exit fee" for early termination. Filers included Amazon Data Services, Google, Sierra Club, and Missouri Office of Public Counsel.
- **format**: HTML (homepage, orders/notices) / PDF (orders) / EFIS docket search
- **practical**: no documented rate limit; standard state site. Individual press-release deep link tried during verification (`.../pr-26-40`) 404'd — use the Orders/Notices and Press Releases index pages as start paths rather than guessing dated slugs.
- **effort tier**: b
- **why worth adding**: fills an entirely empty state stub with a state that just ran a live, contested, on-topic large-load data-center rate case.
- **verified**: yes. Live-navigated to `https://psc.mo.gov` — confirmed live homepage with working "Orders/Notices," "PSC Rules/Statutes," "Proposed Rules," and "Access EFIS" navigation. The specific Ameren large-load order was corroborated via psc.mo.gov's own press-release title (indexed in search) plus St. Louis Public Radio, KSDK, and Warren County Record coverage, though the specific dated press-release URL guessed during this check 404'd (flagged above).

### 7. Missouri Department of Natural Resources — Division of Energy
- **id**: `mo_energy_division` · append alongside `mo_psc` in `config/domains/us/missouri.yaml`
- **base_url**: `https://dnr.mo.gov`
- **start_paths**: `/about-us/division-energy`
- **level**: subnational (state energy office)
- **access**: none
- **coverage**: Missouri's state energy office — efficiency/weatherization, renewable-energy demonstration grants, green building registry, and the state's forthcoming (Sept 2026) comprehensive energy plan under Gov. Kehoe. General energy-policy office, not data-center-specific, but the natural home for any future MO data-center efficiency rulemaking.
- **format**: HTML
- **practical**: no documented rate limit; standard state site.
- **effort tier**: b
- **why worth adding**: completes Missouri coverage alongside the PSC entry above (energy-ministry + regulatory pairing, matching the pattern used for other states in this repo).
- **verified**: yes. Fetched `https://dnr.mo.gov/about-us/division-energy` directly — live page confirmed with efficiency, renewable-energy, weatherization, and green-building program content.

### 8. Loudoun County, Virginia — Data Center Standards & Locations (local government)
- **id**: `us_loudoun_county_va` · append to `config/domains/us/virginia.yaml` (locality section)
- **base_url**: `https://www.loudoun.gov`
- **start_paths**: `/5990/Data-Center-Standards-Locations`, `/6222/Phase-2-Data-Center-Standards-Locations`
- **level**: local (county government)
- **access**: none
- **coverage**: Loudoun is the self-described "Data Center Capital of the World." March 2025 zoning ordinance amendment eliminated by-right data-center development (special-exception review now required). The Phase 2 page explicitly scopes review of "energy opportunities" and on-site power generation/storage; a companion county brief (linked from this hub) recommends **waste-heat recapture (district energy) to heat nearby buildings** as a specific option under consideration.
- **format**: HTML (project hub pages) / PDF (board reports, briefs)
- **practical**: no documented rate limit; municipal CivicPlus-style site; robots.txt not individually checked.
- **effort tier**: b
- **why worth adding**: this is the single most concrete "local government considering data-center waste-heat reuse" source found in this pass — directly on-topic for the project's core subject, at the locality with the largest data-center concentration in the US.
- **verified**: yes. Fetched both URLs directly. `/5990/...` confirmed live, describing the by-right elimination and Phase 2 scope. `/6222/...` confirmed live and explicitly mentions "energy opportunities" and on-site generation/storage review (does not use the words "waste heat" on that specific page, but the waste-heat-recapture recommendation appears in the linked county brief document surfaced in search — flagged as a slightly weaker link below).

### 9. Prince William County, Virginia — Data Center Ordinance Advisory Group (local government, archived)
- **id**: `us_prince_william_county_va` · append to `config/domains/us/virginia.yaml` (locality section)
- **base_url**: `https://www.pwcva.gov`
- **start_paths**: `/department/planning-office/data-center-ordinance-advisory-group`
- **level**: local (county government)
- **access**: none
- **coverage**: Documents the 2023-2025 Data Center Ordinance Advisory Group process: Ordinance 23-07 (noise ordinance amendment), Resolution 23-111 (Design & Construction Standards Manual / Zoning Ordinance amendment for data-center impacts), meeting notes and consultant assessments. The page states the group has been disbanded and content is being folded into a new consolidated "Data Centers" page — so this is archival but still contains real, citable ordinance text and dates.
- **format**: HTML (hub page) / PDF (meeting notes, ordinance text, consultant reports linked from `/assets/...`)
- **practical**: the county relaunched its website in 2026 — the old URL from the brief's original research (`/department/zoning-administration/impacts-of-data-center-uses`) now 404s; use the URL above instead. No documented rate limit.
- **effort tier**: b
- **why worth adding**: second-largest Virginia data-center locality, with its own multi-year ordinance/zoning process distinct from Loudoun's; note it's explicitly archival, lower priority than #8.
- **verified**: yes, with a caveat. Live-navigated to `https://www.pwcva.gov/department/planning-office/data-center-ordinance-advisory-group` — page confirmed live and on-topic. The URL originally found in search (`/department/zoning-administration/impacts-of-data-center-uses`) 404'd after the county's 2026 site relaunch; do not use that one.

### 10. Nebraska Department of Water, Energy and Environment (DWEE) — state energy office
- **id**: `ne_dwee` · replaces the stub `config/domains/us/nebraska.yaml`
- **base_url**: `https://dwee.nebraska.gov`
- **start_paths**: `/`, `/taxonomy/term/74` (public information / news)
- **level**: subnational (state energy office, merged with the former environmental agency in 2019)
- **access**: none
- **coverage**: General state energy office — efficiency loan programs (Dollar & Energy Saving Loans), weatherization assistance, the ONE RED decarbonization/emissions program, and an annual State Energy Report. No data-center-specific content found as of this check, despite Nebraska's growing hyperscale presence (Meta, Google, Facebook facilities near Omaha) — flagged as a general-coverage fill rather than a high-signal find.
- **format**: HTML
- **practical**: no documented rate limit; standard state site.
- **effort tier**: b
- **why worth adding**: lowest-priority candidate in this list, included only to replace an entirely empty stub file with real content; revisit once/if Nebraska produces data-center-specific policy.
- **verified**: yes. Fetched `https://dwee.nebraska.gov/` directly — live homepage confirmed with the program content described above; no data-center-specific material found on this pass.

## Unverified / needs-human-check

- **Illinois "POWER Act"** (data-center water/energy/heat-reuse-plan requirements) — reported by Circle of Blue and Capitol News Illinois as having **failed to pass** in the 2026 session. Not proposed as a source because there is no enacted law or standing docket to point at yet; worth re-checking next session. If/when it's reintroduced, `illinois.yaml` already has ICC and the state legislature (ilga.gov) covered, so a bill-specific entry (same pattern as `virginia.yaml`'s HB323/HB906/HB824) would be the natural addition.
- **Washington UTC dedicated large-load rulemaking** — as of this check, the UTC's rulemakings index (`https://www.utc.wa.gov/documents-and-proceedings/rulemakings`, verified live) does not yet list a formally docketed data-center/large-load rulemaking; the process was still in a multi-month technical-workshop/comment phase (per Governor Ferguson's 2025 Data Center Workgroup and SB 5982's clean-energy-reporting directive). Recommend adding `wa_utc` (`base_url: https://www.utc.wa.gov`, `start_paths: ["/documents-and-proceedings/rulemakings"]`) now as a tier-b watch source even though no docket number exists yet, since the commission's own page confirms this rulemaking is actively coming — but treat it as lower-confidence than #1-9 above since there's no specific docket to point at today.
- **NY DPS specific order PDF** (`documents.dps.ny.gov/.../DocRefId={B040539C-...}`) — the PDF binary could not be text-extracted by the fetch tool during this check; its existence and substance were corroborated only via secondary news sources (Governor's press release, Utility Dive, Columbia Climate Law Blog), not by directly reading the primary document. The parent site (`dps.ny.gov`) itself was independently verified live.
- **Minnesota HF4888 / 2025 data-center heat-reuse & environmental law** — real and verified (Minnesota House "New Laws" page, effective June 15, 2025; requires large-scale data centers to certify green-building standards within 3 years and pays into an efficiency/weatherization fund). Not proposed as a new source because `minnesota.yaml` already has `mn_puc` (mn.gov/puc), `mn_commerce` (mn.gov/commerce/energy), and `mn_legislature` (revisor.mn.gov/bills) covering this structurally. Flagging as an opportunity for a bill-specific entry in the same style as Virginia's HB323/HB906/HB824, if the team wants law-level (not just domain-level) granularity for this one.

## Summary of what was NOT found

No new **structured/API** source was found at the US subnational level — every state PUC docket
system checked (Texas Interchange, NY DMM, Georgia FACTS, Missouri EFIS) is a web search UI, not
a documented public API. No dedicated government-run **district energy authority** distinct from
what's already in the repo (Nashville's district energy system in `tennessee.yaml`) was found;
private district-steam operators (Vicinity Energy in Boston/Philadelphia/Baltimore, etc.) were
excluded as out of scope per the brief (not government policy sources).
