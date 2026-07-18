# Standards Bodies — Source Expansion (Wave 2)

Branch: `feature/source-expansion-research`. Research only — no client code, nothing
enabled. Every candidate below is proposed with `enabled: false`.

## Scope and dedup performed

Read `docs/source-expansion/BRIEF.md`, `docs/source-expansion/draft/crawl/supranational.yaml`,
and `docs/source-expansion/draft/new-clients.md` before researching. Grepped every
`base_url:` in `docs/source-expansion/draft/crawl/*.yaml` (11 files) and every
`base_url:` already live in `config/domains/*.yaml` (29 files) for overlap.

Already covered — **not re-proposed**:
- `iea-4e.org`, `www.iso.org` (ISO/IEC 30134 catalog), `cencenelec.eu` (CG GDC group
  page), `euroheat.org`, `aseanenergy.org`, `c40knowledgehub.org`,
  `energy-community.org` — all in draft `supranational.yaml`.
- `www.energy.gov`, `www.energystar.gov`, `www.ferc.gov`, `www.eia.gov`,
  `www.whitehouse.gov`, `www.pjm.com` — all live in `config/domains/us/us_federal.yaml`.
- ASHRAE 90.4 is referenced today only as a **tag** (`ashrae_90_4`) inside
  `config/domains/us/oregon.yaml`'s notes — ASHRAE itself is not yet a crawled
  source anywhere. Net new.
- No existing entry anywhere in the repo for: NIST, eCFR/10 CFR, DIN, BSI, AFNOR,
  NEN, SIS, UNI, JIS/JISC, SAC/SAMR, BIS, The Green Grid, Uptime Institute,
  `standards.cencenelec.eu` (the CENELEC technical-committee database — a
  different domain from the `www.cencenelec.eu` marketing site wave 1 found),
  or `webstore.iec.ch` (a different domain from `www.iso.org`).

## How this wave differs from wave 1's supranational pass

Wave 1 found the general **CEN-CENELEC-ETSI Green Data Centres** coordination-group
landing page (`cencenelec.eu/areas-of-work/.../green-data-centres/`) and the ISO
**catalogue** page for one ISO/IEC 30134 part. This wave went one layer deeper: the
actual CENELEC technical-committee database (`standards.cencenelec.eu`, CLC/TC 215,
the committee that literally drafts EN 50600), the IEC's own commercial webstore
(distinct domain, distinct catalog UI from `iso.org`), and — the biggest find —
national standards bodies' own catalog pages for the same EN 50600 / ISO-IEC 30134
family, several of which surface content (scope text, technical-content summaries)
that ISO's own abstract page doesn't show.

---

## Verified candidates (ranked best-first)

### 1. China — National Standards Information Public Service Platform (SAMR/SAC)

- **name**: National Standards Information Public Service Platform (全国标准信息公共服务平台)
- **id**: `china_std_samr`
- **base_url**: `https://std.samr.gov.cn`
- **start_paths**: `/gb/search/gbDetailed?id=2E4DD4D8E2E84A4BE06397BE0A0AE354` (GB 40879
  revision project — mandatory data-center PUE limit standard); a keyword-search
  entry point would be better long-term but the search form is JS-driven — a
  crawler should be seeded with specific `id=` detail-page URLs discovered via
  periodic WebSearch/site-search rather than link-following from a static start
  page.
- **level**: national (China)
- **access**: none — free, no login required for the project/detail pages checked.
- **coverage**: `region: ["apac"]` (China has no dedicated VALID_REGIONS bucket,
  same treatment as the existing east-asia.yaml draft), `category: "standards"`,
  `tags: ["efficiency", "mandates", "reporting"]`, `policy_types: ["standard",
  "regulation"]`, `language: "zh"`
- **format**: HTML
- **practical**: government portal run by SAMR (State Administration for Market
  Regulation) / SAC (Standardization Administration of China); no robots.txt
  block observed on the pages fetched; no documented rate limit; likely
  requires_playwright for the search UI (not confirmed for detail pages, which
  rendered as plain server HTML).
- **effort tier**: (b) plain crawl domain — new file `config/domains/china.yaml`
  (per wave 1's east-asia.yaml draft header, China has zero prior coverage and
  needs this new file regardless of this standards-bodies pass).
- **why worth adding**: **Highest-value find of this wave.** This is not a
  paywalled catalog stub — the detail page for GB 40879 (数据中心能效限定值及能效等级,
  "Maximum allowable values of energy efficiency and energy efficiency grades for
  data centers") is FREE, FULL regulatory text: current limit values (PUE ≤ 1.5
  mandatory floor, Grade 2 ≤ 1.3, Grade 1 ≤ 1.2), the drafting committee (TC20,
  National Technical Committee for Energy Fundamentals and Management
  Standardization), and — critically — the exact policy gap driving the pending
  revision (China's 2024 four-ministry Data Center Green Low-Carbon Development
  Action Plan requires new large/hyperscale DCs to hit PUE ≤ 1.25 by end of 2025,
  ≤ 1.2 for national hub-node projects, which is stricter than the current GB
  40879 text — the page explains this gap verbatim). Also surfaces adjacent
  in-development standards: liquid-cooling cabinet specs, "green data center
  evaluation" (绿色数据中心评价), and an industry-standard PUE assessment/acceptance
  spec from MIIT. This is a mandatory (not voluntary) national standard directly
  analogous to what the brief is hunting for, in a free government database, in
  a jurisdiction none of the other waves cover in a standards-specific way.
  **verified: yes** — fetched the detail page directly; confirmed Chinese-language
  regulatory text, standard number, committee, and the PUE gap rationale.

### 2. CENELEC — CLC/TC 215 Technical Committee page (standards.cencenelec.eu)

- **name**: CENELEC Technical Committee CLC/TC 215 — Electrotechnical aspects of
  telecommunication equipment (drafts EN 50600)
- **id**: `cenelec_clc_tc215`
- **base_url**: `https://standards.cencenelec.eu`
- **start_paths**:
  - `/dyn/www/f?p=305:7:0:25:::FSP_ORG_ID,FSP_LANG_ID:1258297` (committee overview
    — scope, secretariat, chair's country)
  - a "Published Standards" tab is linked from that page (URL is a dynamic Oracle
    APEX session parameter, not a stable path — note for the crawler dev: this
    site uses session-scoped URLs, treat as `requires_playwright: true` and crawl
    from the stable overview URL above rather than hardcoding the Published
    Standards link).
- **level**: supranational (EU — CEN/CENELEC/ETSI joint recognition)
- **access**: none
- **coverage**: `region: ["eu"]`, `category: "standards"`, `tags: ["efficiency",
  "research"]`, `policy_types: ["standard", "guidance"]`, `language: "en"` (also
  FR/DE toggles present)
- **format**: HTML
- **practical**: no robots.txt blocker observed; static-feeling Oracle APEX
  rendering (page text extracted cleanly without JS); no documented rate limit.
- **effort tier**: (b) plain crawl domain — **append to `config/domains/eu.yaml`**,
  same file wave 1 recommended for the general CG GDC page (this is a companion
  entry, not a duplicate — different domain, different content: this is the
  actual drafting-committee record, not the public-facing coordination-group
  marketing page).
- **why worth adding**: this is the literal official committee record for the
  body that writes EN 50600 (scope text explicitly says: "to review international
  standardization results of ISO/IEC JTC 1 as far as ... Energy Efficient Data
  Centres are concerned"). Confirms Germany's DKE holds the secretariat. Distinct
  from wave 1's `cencenelec.eu` marketing-site group page (different domain,
  `standards.cencenelec.eu` vs `www.cencenelec.eu`) — this is the standards
  database, that was the news/coordination-group page. Recent committee output
  found via search: CLC/TS 50600-5-1 (second edition, 2023/2024), a data-center
  "maturity model" for environmental sustainability explicitly framed as
  supporting the EU Green Deal — five maturity levels with requirements/practices
  across infrastructure and IT equipment. **verified: yes** — fetched the
  committee overview page directly; confirmed scope text, secretariat (DKE/
  Germany), and the "Published Standards" navigation tab exists.

### 3. ASHRAE — Standards and Guidelines portal

- **name**: ASHRAE Standards and Guidelines (TC 9.9 datacom / Standard 90.4 / 127)
- **id**: `ashrae_standards`
- **base_url**: `https://www.ashrae.org`
- **start_paths**:
  - `/technical-resources/standards-and-guidelines`
  - `/technical-resources/bookstore/datacom-series`
  - `/technical-resources/standards-and-guidelines/standards-addenda/standard-90-4-2022`
- **level**: national (US-headquartered) but its standards are cited
  extra-jurisdictionally — e.g. `config/domains/us/oregon.yaml` already
  references ASHRAE 90.4 by tag today, and 90.4/127 translations exist in
  Korean/Spanish per the bookstore page. Recommend `region: ["us",
  "supranational"]`, same dual-tag convention wave 1 used for the Energy
  Community entry.
- **access**: **mixed** — free with registration for a read-only preview
  ("Preview ASHRAE Standards and Guidelines... Free read-only access... after
  completing and agreeing to the registration terms"); addenda for
  continuous-maintenance standards (90.4 is one) are free PDF downloads with no
  login; the purchasable full PDF/print copies are paywalled (`auth_type` would
  be `form` if the free-preview login flow is ever wired up — not needed for a
  crawl of the free addenda/pages).
- **coverage**: `category: "standards"`, `tags: ["efficiency", "mandates"]`,
  `policy_types: ["standard", "guidance"]`, `language: "en"`
- **format**: HTML (addenda are PDF, free)
- **practical**: no robots.txt blocker observed; standard site navigation; no
  documented rate limit; `requires_playwright` likely needed for the standards-
  addenda listing (not confirmed either way this pass — treat as a build-time
  check).
- **effort tier**: (b) plain crawl domain — **new file** needed
  (`config/domains/standards_bodies.yaml` recommended — see note at bottom of
  this doc — or fold into wave 1's still-uncommitted `config/domains/
  supranational.yaml` plan).
- **why worth adding**: ASHRAE Standard 90.4 (Energy Standard for Data Centers)
  and Standard 127 (data-center/ITE air-conditioning test method) are the two
  standards the brief names by number, and they underpin US state energy-code
  adoption (already cited in this repo's own Oregon entry). Free addenda +
  registration-gated preview beats a pure paywall — worth indexing the free
  layer even though the full standard text is commercial. **verified: yes** —
  fetched the standards-and-guidelines page directly (confirmed free-preview
  registration model, free addenda for continuous-maintenance standards) and the
  datacom-series bookstore page (confirmed Standard 90.4-2025 and Standard
  127-2020 both listed, free white papers/Handbook excerpts vs. paywalled full
  standards/Datacom Encyclopedia).

### 4. IEC Webstore — ISO/IEC 30134 series (distinct from the ISO catalog)

- **name**: IEC Webstore — ISO/IEC 30134 Data Centre KPI series
- **id**: `iec_webstore_30134`
- **base_url**: `https://webstore.iec.ch`
- **start_paths**:
  - `/en/publication/111538` (30134-2:2026, PUE — current edition)
  - `/en/publication/70719` (30134-6:2021, ERF)
- **level**: supranational / global
- **access**: none for the catalog/abstract page; full text paywalled (CHF
  159 for 30134-2, confirmed on-page).
- **coverage**: `region: ["supranational", "global"]`, `category: "standards"`,
  `tags: ["efficiency"]`, `policy_types: ["standard"]`, `language: "en"`,
  `max_depth: 1` (same reasoning as wave 1's ISO entry — do not attempt to
  crawl past the abstract/catalog layer).
- **format**: HTML (catalog), PDF (paywalled)
- **practical**: individual publication IDs are stable, numeric, and
  non-sequential (not derivable from the standard number) — a maintainer will
  need to re-search webstore.iec.ch periodically as new parts/editions publish
  rather than guess URLs. Search/browse pages on this domain returned 403/404 to
  automated fetch this pass — direct publication-ID URLs worked fine.
- **effort tier**: (b) plain crawl domain — same new file as the ASHRAE/global
  entries above.
- **why worth adding**: the brief explicitly asked to add IEC-specific pages if
  distinct from wave 1's ISO catalog find, and this is: a different organization
  domain (IEC's own commercial webstore vs. `iso.org`), with its own free
  abstract text ("This international standard specifies PUE as a KPI... 35-page
  technical document") and its own pricing/edition metadata (webstore shows the
  2026 edition already; iso.org's page wave 1 checked was the older -6/ERF part).
  Coverage is **metadata/abstract only** — full standard text is paywalled, same
  caveat as wave 1's ISO entry. **verified: yes** — fetched both publication
  pages directly; confirmed titles, prices, free-abstract text, and (for 30134-2)
  the 2026 edition update notes.

### 5. US — eCFR Title 10, Part 431 (Energy Efficiency Program for Commercial/Industrial Equipment)

- **name**: Electronic Code of Federal Regulations — 10 CFR Part 431
- **id**: `ecfr_10_cfr_431`
- **base_url**: `https://www.ecfr.gov`
- **start_paths**: `/current/title-10/chapter-II/subchapter-D/part-431`
- **level**: national (US federal)
- **access**: none
- **coverage**: `region: ["us"]`, `category: "regulatory"`, `tags: ["mandates",
  "efficiency"]`, `policy_types: ["regulation", "law"]`, `language: "en"`
- **format**: HTML (full regulation text rendered in-page)
- **practical**: **WebFetch (this agent's plain-HTTP tool) was redirected to a
  bot-check page (`unblock.federalregister.gov`) on a direct fetch** — a real
  browser session loaded it fine (confirmed via the Browser tool), so this site
  needs `requires_playwright: true` or a proper browser-like user agent, not a
  bare HTTP client. No documented rate limit; this is the canonical, continuously
  updated (checked "up to date as of 7/16/2026") federal regulation text.
- **effort tier**: (b) plain crawl domain, distinct `base_url` from the existing
  `energy_gov` entry (`www.energy.gov`) — **append to `config/domains/us/
  us_federal.yaml`**, new entry (not a duplicate of DOE's own site).
- **why worth adding**: 10 CFR Part 431 is the actual binding regulatory text
  (DOE's EPCA-derived commercial/industrial equipment energy-conservation
  program) that the brief calls out by name — distinct from DOE's own policy/
  guidance pages (`energy.gov`, already in the repo) which describe the program
  but aren't the regulation itself. Covers the appliance/equipment standards
  process that could extend to data-center-adjacent equipment categories
  (UPS, air-conditioning/cooling equipment already regulated here in part).
  **verified: yes** — via the Browser tool, confirmed live, full regulatory
  text rendered (Part 431 "General Provisions," definitions, authority citation
  to 42 U.S.C. 6291-6317).

### 6. US — DOE Better Buildings Data Center Accelerator / Solution Center

- **name**: Better Buildings & Better Plants Initiative — Data Centers Sector
- **id**: `betterbuildings_datacenters`
- **base_url**: `https://betterbuildingssolutioncenter.energy.gov`
- **start_paths**:
  - `/sectors/data-centers`
  - `/data-center-toolkit`
  - `/accelerators/data-centers`
- **level**: national (US federal, DOE program)
- **access**: none
- **coverage**: `region: ["us"]`, `category: "energy_ministry"`, `tags: [
  "efficiency", "incentives", "research"]`, `policy_types: ["guidance",
  "report"]`, `language: "en"`
- **format**: HTML, PDF (toolkits/fact sheets)
- **practical**: no robots.txt blocker observed; no documented rate limit.
- **effort tier**: (b) plain crawl domain, **distinct base_url from the existing
  `energy_gov` entry** (that entry crawls `www.energy.gov`; this is a separate
  DOE-run subdomain/site) — append to `config/domains/us/us_federal.yaml` as a
  new entry, not a duplicate.
- **why worth adding**: this is DOE's dedicated data-center energy-efficiency
  program site — richer, more data-center-specific content than the existing
  `energy_gov` entry's two `/eere/` start paths (which point at general
  buildings/FEMP pages). Confirmed real program results (36% average
  infrastructure-energy improvement across ~partners, $3.9M annual savings),
  a "Data Center Accelerator Toolkit," and named case studies (Sabey Data
  Centers, NREL, LBNL/NERSC). **verified: yes** — fetched `/sectors/data-centers`
  directly via the Browser tool; confirmed live with substantial on-topic
  content (the `/data-centers` short-URL redirects to a 404, use the paths
  above).

### 7. India — BIS Standards Portal (new voluntary data-center CER standard)

- **name**: Bureau of Indian Standards — Standards Portal
- **id**: `bis_standards_india`
- **base_url**: `https://standards.bis.gov.in`
- **start_paths**: `/` (homepage has a "Know Your Standards" search entry point;
  no stable deep-link to the specific new standard was found this pass — see
  practical note)
- **level**: national (India)
- **access**: none for search/browse.
- **coverage**: `region: ["apac"]` (India also has its own `india.yaml` file —
  recommend appending there, consistent with existing repo convention, rather
  than the broader apac bucket), `category: "standards"`, `tags: ["efficiency"]`,
  `policy_types: ["standard"]`, `language: "en"`
- **format**: HTML
- **practical**: homepage confirmed live and has a working "Search" feature;
  the specific new standard was reported in trade press (dated Feb 25, 2026)
  as a BIS-notified Indian Standard defining a Cooling Efficiency Ratio (CER)
  methodology "derived from international ISO/IEC frameworks" for data centers
  — **the exact IS standard number/URL was not independently found on
  standards.bis.gov.in this pass** (trade-press coverage only) — flag for a
  follow-up search-portal query once building the crawler.
- **effort tier**: (b) plain crawl domain — append to `config/domains/india.yaml`.
- **why worth adding**: India just (Feb 2026) issued its first data-center-
  specific national standard (voluntary; a QCO would be needed to make it
  mandatory) — genuinely new-jurisdiction coverage the brief is hunting for,
  and a live regulatory trend (voluntary-first, same pattern the article notes
  BIS used for cloud computing and "ethical AI" alongside it). **verified:
  partial** — portal homepage confirmed live via Browser tool (title, search
  functionality); the specific CER-standard detail page not independently
  located this session — treat the exact IS-standard entry as
  needs-human-check even though the portal itself is verified.

### 8. Netherlands — NEN EN 50600 directory page

- **name**: NEN — De Europese norm voor datacenters EN 50600
- **id**: `nen_en_50600`
- **base_url**: `https://www.nen.nl`
- **start_paths**: `/ict/datacenters/en-50600`
- **level**: national (Netherlands)
- **access**: none for the directory page; individual standards purchase-gated
  (same paywall pattern as every other national body below).
- **coverage**: `region: ["eu"]` (Netherlands doesn't have its own
  `netherlands.yaml` region tag beyond `eu` in the existing convention — check
  against `config/domains/netherlands.yaml`'s existing entry's region value
  before finalizing), `category: "standards"`, `tags: ["efficiency"]`,
  `policy_types: ["standard"]`, `language: "nl"`
- **format**: HTML
- **effort tier**: (b) — append to `config/domains/netherlands.yaml`.
- **why worth adding**: free directory page lists the full current EN 50600
  part structure (parts 1, 2.1-2.5, 3.1, 4.1-4.5 including Renewable Energy
  Factor and Energy Reuse Factor, plus three free-standing technical-report
  guidance documents) better than most other national bodies' pages — a good
  single-page index of "what parts exist" even though it's metadata only.
  **verified: yes** — fetched directly; confirmed free directory content,
  full part listing, "standards documents are paywalled" confirmed by the
  page's own purchase links.

### 9. Sweden — SIS catalog (SS-EN 50600 series)

- **name**: SIS (Swedish Institute for Standards) — SS-EN 50600 series
- **id**: `sis_en_50600`
- **base_url**: `https://www.sis.se`
- **start_paths**: `/en/produkter/information-technology-office-machines/general/ssen506001/`
- **level**: national (Sweden)
- **access**: none for catalog page; standard purchase-gated (645 SEK confirmed
  for SS-EN 50600-1, which is itself withdrawn/superseded — flag that the
  specific ID checked is stale, a live search would need to find the current
  edition's product page).
- **coverage**: `region: ["nordic"]` (existing `config/domains/sweden.yaml`
  convention), `category: "standards"`, `tags: ["efficiency"]`,
  `policy_types: ["standard"]`, `language: "en"` (site has EN/SV toggle)
- **format**: HTML
- **effort tier**: (b) — append to `config/domains/sweden.yaml`.
- **why worth adding**: same EN 50600 series, Sweden-specific storefront/
  catalog — no unique content beyond confirming Swedish availability, lowest
  marginal value of the national-body entries in this list, included for
  completeness since the brief named SIS explicitly. **verified: yes** —
  fetched directly; confirmed title, price, withdrawn/superseded status, no
  free abstract on this particular (stale) product page.

### 10. UK — BSI Knowledge (current BS EN 50600-4-6, free abstract)

- **name**: BSI Knowledge — BS EN 50600-4-6:2020 (Energy Reuse Factor)
- **id**: `bsi_en_50600_4_6`
- **base_url**: `https://knowledge.bsigroup.com`
- **start_paths**:
  `/products/information-technology-data-centre-facilities-and-infrastructures-energy-reuse-factor`
- **level**: national (UK)
- **access**: none for the product/abstract page; full standard purchase-gated
  (price not shown on the page fetched — check at build time).
- **coverage**: `region: ["uk"]`, `category: "standards"`, `tags: [
  "efficiency"]`, `policy_types: ["standard"]`, `language: "en"`
- **format**: HTML
- **effort tier**: (b) — append to `config/domains/uk.yaml`.
- **why worth adding**: unlike the SIS/Sweden and older BSI product pages
  checked this pass (several EN 50600 parts on BSI Knowledge are marked
  **withdrawn**), this specific page confirmed **Current** status with a real
  free abstract describing ERF's purpose and audience (installers,
  manufacturers, designers, facility managers, network operators) — better
  free-content depth than most other national-body pages found. **verified:
  yes** — fetched directly; confirmed "Current," Aug 2020 publication date,
  free descriptive abstract present.

### 11. France — AFNOR Éditions boutique (NF EN 50600 series)

- **name**: AFNOR Éditions — NF EN 50600 series
- **id**: `afnor_en_50600`
- **base_url**: `https://www.boutique.afnor.org`
- **start_paths**: homepage confirmed live; specific part URLs (e.g.
  `/en-gb/standard/nf-en-5060021/...`) found via search but not independently
  re-fetched this pass — **treat individual part URLs as needs-human-check**,
  the boutique homepage itself is verified.
- **level**: national (France)
- **access**: none for catalog; standards purchase-gated.
- **coverage**: `region: ["eu"]` (check `config/domains/france.yaml`'s existing
  region convention), `category: "standards"`, `tags: ["efficiency"]`,
  `policy_types: ["standard"]`, `language: "fr"`
- **format**: HTML
- **effort tier**: (b) — append to `config/domains/france.yaml`.
- **why worth adding**: same EN 50600 series, France-specific storefront;
  named by the brief. **verified: partial** — fetched the AFNOR Éditions
  homepage directly (confirmed live, real standards listing, French standards
  publisher); an attempted direct fetch of one specific NF EN 50600-4-6 part
  URL returned the homepage instead (the URL from search results appears to
  need the numeric product-ID suffix AFNOR uses, not just the slug) — do not
  hardcode a specific part URL without re-confirming it resolves.

### 12. Germany — DIN Media catalog (DIN EN 50600 series)

- **name**: DIN Media — DIN EN 50600 series
- **id**: `din_en_50600`
- **base_url**: `https://www.dinmedia.de`
- **start_paths**: `/en/standard/din-en-50600-4-6/327766295`
- **level**: national (Germany)
- **access**: none for catalog page; standard purchase-gated (93.27 EUR
  confirmed for DIN EN 50600-4-6:2020-11).
- **coverage**: `region: ["eu"]` (check against `config/domains/germany.yaml`'s
  existing region convention — that file already has 23 base_urls, likely uses
  a Germany-specific tag), `category: "standards"`, `tags: ["efficiency"]`,
  `policy_types: ["standard"]`, `language: "de"`
- **format**: HTML
- **practical**: `www.din.de` (the DIN organization's own site) does **not**
  host the actual standard catalog — that's on the separate `dinmedia.de`
  storefront domain; don't confuse the two when building this entry.
- **effort tier**: (b) — append to `config/domains/germany.yaml`.
- **why worth adding**: DIN is the committee holder for CLC/TC 215 (confirmed
  in candidate #2 above — DKE is DIN's electrotechnical arm), making Germany's
  own catalog page for the series a natural companion entry. **verified: yes**
  — fetched directly; confirmed current status, price, page count, and a
  "Relationship to other standards" cross-reference section linking to other
  EN 50600-4-x parts.

---

## Verified — industry bodies (flagged per brief's judgment-call note)

These are **not government/IGO policy sources** by the brief's own definition,
but they originate the exact KPIs (PUE/ERE/ERF/WUE/CUE) that every government
source above cites by name, and one of them (JDCC) is tied directly into a
national government's regulatory reporting regime. Including per the brief's
explicit instruction to flag these as a judgment call rather than silently
drop them.

### 13. The Green Grid

- **id**: `the_green_grid`
- **base_url**: `https://thegreengrid.org` (note: `www.thegreengrid.org` redirects
  to the bare domain — use the apex domain as `base_url`)
- **start_paths**: `/resources` (the older `/en/resources/library-and-tools`
  path from wave-1-era conventions 404s — site was restructured; `/resources`
  is the current live page)
- **access**: none
- **coverage**: `region: ["supranational", "global"]`, `category: "standards"`,
  `tags: ["efficiency", "research"]`, `policy_types: ["guidance", "report"]`,
  `language: "en"`
- **why flagged industry, not dropped**: this is the organization that
  originated PUE (2007), ERE, ERF, WUE, CUE, and DCeP — the metrics ISO/IEC
  30134, EN 50600-4-x, and multiple national mandates (China's GB 40879 above
  explicitly cites TGG/Green Grid as PUE's originator) all formalize. Recent
  activity confirmed live: a new "Water Usage Impact" metric published Oct
  2025, and a public statement (June 2025) backing US EPA ENERGY STAR — active
  government-advocacy engagement with US EPA, EU Lot 9, China's CNIS, and
  India's TEC named on the current homepage. **verified: yes** — fetched
  homepage and `/resources` directly via Browser tool; both live, on-topic.

### 14. Uptime Institute

- **id**: `uptime_institute`
- **base_url**: `https://uptimeinstitute.com`
- **start_paths**: `/publications`
- **access**: none for the publications index (individual reports may gate
  behind an email/registration wall — not confirmed either way this pass).
- **coverage**: `region: ["supranational", "global"]`, `category: "standards"`,
  `tags: ["efficiency", "research"]`, `policy_types: ["guidance", "report"]`,
  `language: "en"`
- **why flagged industry, not dropped**: publishes the "Tier Standard"
  (Topology / Operational Sustainability) referenced across data-center
  regulatory and industry discourse worldwide, plus a dedicated "Heat Reuse: A
  Management Primer" report directly on this project's exact subject matter
  (found via search: covers ~60 documented European heat-recovery projects and
  explicitly discusses the EU EED recast's 1 MW waste-heat-recovery mandate).
  **verified: partial** — `/publications` confirmed live via WebFetch (listed
  Tier Standard titles); the specific heat-reuse primer URL
  (`uptimeinstitute.com/resources/research-and-reports/heat-reuse-a-management-
  primer`) was found via search but not independently re-fetched this pass —
  treat that specific URL as needs-human-check even though the domain/section
  is verified live.

### 15. Japan — JDCC (Japan Data Center Council) PUE Guideline

- **id**: `jdcc_pue_guideline`
- **base_url**: `https://www.jdcc.or.jp`
- **start_paths**: `/pue_guide/`
- **access**: none
- **coverage**: `region: ["apac", "japan"]`, `category: "standards"`,
  `tags: ["efficiency", "mandates"]`, `policy_types: ["guidance"]`,
  `language: "ja"`
- **why flagged industry, not dropped**: unlike Green Grid/Uptime, JDCC's PUE
  guideline is tied directly to a live Japanese government mandate — Japan's
  revised Energy Conservation Law (effective April 2023) requires qualifying
  data-center operators to report PUE, with a policy goal that the top 15% of
  domestic operators reach PUE ≤ 1.4 by 2030, and a hard PUE ≤ 1.3 requirement
  for data centers commencing operation in 2029 or later. JDCC's guideline is
  the industry-side benchmark implementation Japanese operators use to comply.
  Appending to `config/domains/apac.yaml` (Japan already has entries there).
  **verified: yes** — fetched `/pue_guide/` directly via Browser tool; page
  live and on-topic (PUE guideline / benchmark system content confirmed).

---

## Unverified / needs-human-check

- **Italy — UNI (`store.uni.com`)**: homepage confirmed live via Browser tool,
  but the site is JS-heavy (the accessibility tree returned effectively empty
  on first read) and a specific catalog page for EN 50600 or its international
  successor ISO/IEC TS 22237 could not be located/confirmed this pass. Trade
  press (ICT Security Magazine, DNV, Euris Technology — all Italian
  certification-industry sites, not UNI itself) states Italy's data-center
  standard track has moved from EN 50600 toward the joint ISO/IEC TS 22237
  successor — if built, search `store.uni.com` at build time for "22237" and
  "50600" directly with a real browser session rather than reusing search-engine
  cached URLs.
- **Japan — JIS/JISC dedicated data-center standard**: no JIS-numbered standard
  specific to data-center energy efficiency or PUE was found this session
  (only the JDCC industry guideline above, and Japan's Energy Conservation Law
  itself, which is a national-government not standards-body source and likely
  already/better covered by existing `apac.yaml`/`japan`-tagged entries — not
  independently confirmed against the existing file in this pass). JSA Group
  Webdesk (`webdesk.jsa.or.jp`) is a general standards storefront, not
  data-center-specific — do not add without finding an actual on-topic JIS
  standard number first.
- **NIST**: no dedicated NIST data-center energy-efficiency standard or policy
  page was confirmed. `nist.gov/energy-efficiency` is live but is a general
  buildings/residential-energy portal, not data-center-specific (fetched and
  confirmed via Browser tool — content is about home HVAC/insulation, not data
  centers). A single NIST-affiliated conference paper ("Energy Efficiency
  Scaling for 2 Decades (EES2) Roadmap for Computing," 2024, IEEE HPEC) exists
  in NIST's publications database, but it is one academic paper citation, not
  a policy/standard artifact worth a crawl domain — do not add as a source.
- **ETSI's own standard-numbered deliverables**: `www.etsi.org/standards-search`
  is a live, general ETSI standards search portal (confirmed via Browser tool),
  but EN 50600 is a **CENELEC**-numbered standard, not an ETSI-numbered one —
  ETSI's role is the joint CEN-CENELEC-ETSI agreement referenced in CLC/TC 215's
  own scope text (candidate #2 above), not a separate EN-50600-adjacent
  ETSI-specific standard catalog. No distinct, on-topic ETSI-numbered standard
  was found to justify its own entry beyond what's already captured by the
  CLC/TC 215 entry — flagging as checked-but-not-worth-adding rather than a
  genuine gap.
- **BIS India exact standard number/URL** (see candidate #7 above) — portal
  verified live, specific new CER standard's detail page not located.
- **Uptime Institute's specific heat-reuse-primer URL** (see candidate #14
  above) — section verified live, specific report URL not re-fetched.
- **AFNOR specific NF EN 50600 part URLs** (see candidate #11 above) — boutique
  homepage verified live, specific part URLs from search results not
  independently re-confirmed to resolve as given.

---

## File-placement summary (for whoever turns this into real config/domains/*.yaml)

- **New file needed**: `config/domains/china.yaml` (candidate #1 — also already
  flagged as needed by wave 1's east-asia.yaml draft, independent of this pass).
- **New file needed**: something for the global/supranational standards bodies
  with no national home — candidates #3 (ASHRAE), #4 (IEC Webstore), #13 (Green
  Grid), #14 (Uptime Institute). Wave 1 already flagged the same gap (its
  `iea_4e_edna_datacentres`, `iso_iec_30134_datacentre_kpi`, etc. need a new
  `config/domains/supranational.yaml`) — recommend merging these four into that
  same planned file rather than creating a second new file, OR splitting a
  dedicated `config/domains/standards_bodies.yaml` if the project prefers
  standards bodies kept separate from policy/coordination bodies. Either way,
  this also revives wave 1's flagged need to add `"supranational"` and
  `"global"` to `VALID_REGIONS` in `src/core/config.py`.
- **Append to existing eu.yaml**: candidate #2 (CENELEC CLC/TC 215).
- **Append to existing us/us_federal.yaml**: candidates #5 (eCFR Part 431) and
  #6 (DOE Better Buildings Data Centers).
- **Append to existing india.yaml**: candidate #7 (BIS).
- **Append to existing netherlands.yaml**: candidate #8 (NEN).
- **Append to existing sweden.yaml**: candidate #9 (SIS).
- **Append to existing uk.yaml**: candidate #10 (BSI).
- **Append to existing france.yaml**: candidate #11 (AFNOR, needs-human-check
  on exact part URL).
- **Append to existing germany.yaml**: candidate #12 (DIN).
- **Append to existing apac.yaml**: candidate #15 (JDCC, Japan).
