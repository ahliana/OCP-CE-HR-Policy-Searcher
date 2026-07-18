# Source Expansion - Wave 3: Water & Cooling Regulation

Angle: government bodies regulating **data-center water use and cooling** - water
rights/abstraction permitting, WUE reporting mandates, drought/water-stress
restrictions, and reclaimed/recycled cooling water policy. Adjacent to the core
waste-heat-reuse taxonomy but a distinct regulatory thread (water law, not energy law).

Dedup performed against: `config/domains/**/*.yaml` (292 existing `base_url` entries),
`docs/source-expansion/draft/crawl/**/*.yaml`, `docs/source-expansion/draft/new-clients*.md`,
`docs/source-expansion/regions-wave2/*.md`. Full method below each candidate.

---

## Verified candidates (ranked best-first)

### 1. Virginia DEQ - Water Withdrawal Permitting
- **name**: Virginia Department of Environmental Quality - Water Withdrawal
- **id**: `va_deq_water`
- **base_url**: `https://www.deq.virginia.gov`
- **start_paths**:
  - `/water/water-withdrawal`
  - `/water/water-quantity/water-supply-planning/water-withdrawal-reporting`
- **level**: subnational (state - Virginia)
- **access**: none (public HTML, no key)
- **coverage**: Ground Water Management Act of 1992 + Groundwater Withdrawal
  Regulations (permits required at 300,000+ gal/month in the two Groundwater
  Management Areas); Virginia Water Protection (VWP) Permit Program for surface
  water withdrawals (Article 2.2, State Water Control Law); the water-withdrawal
  reporting page is the DEQ side of 2026 HB589, which requires waterworks to
  report data-center water sales separately starting Jan 1, 2027.
  - region: `us`, `us_states`, `virginia` | category: `environmental_agency`
  - tags: `mandates`, `reporting`, `planning` | policy_types: `regulation`, `law`
  - language: `en`
- **format**: HTML
- **practical**: `www.deq.virginia.gov/robots.txt` redirects to the same host, no
  crawl block observed on `/water/*`; no visible rate-limit banner; DEQ updates
  regulatory guidance pages irregularly (not a frequent-publish site).
- **effort tier**: (b) plain crawl domain
- **why worth adding**: Virginia is the single largest US data-center market
  (Loudoun/Prince William "Data Center Alley") and just enacted the first
  state law forcing utility-level, per-sector water-use disclosure for data
  centers - directly in scope and not previously covered (only
  `energy.virginia.gov` and `lis.virginia.gov` exist in `virginia.yaml`).
- **verified**: yes - fetched via browser render (direct `curl`/WebFetch got
  HTTP 403, bot-protection on user-agent; a real browser tab loaded it cleanly).
  Confirmed live text: full description of GWMA groundwater permitting and VWP
  surface-water permitting, exactly on-topic.

### 2. Netherlands - Unie van Waterschappen: Datacenters position
- **name**: Dutch Water Authorities Association (Unie van Waterschappen) - Datacenters
- **id**: `nl_unie_waterschappen_dc`
- **base_url**: `https://unievanwaterschappen.nl`
- **start_paths**:
  - `/standpunten/datacenters/`
- **level**: national (umbrella body for the 21 regional waterschappen, the
  bodies with statutory water-quantity/quality authority in NL)
- **access**: none
- **coverage**: Explicit policy position that data centers' cooling-water
  discharge raises surface-water temperature and threatens Water Framework
  Directive ("Kaderrichtlijn Water") quality targets; calls for national +
  decentralized legal frameworks for data-center water/soil impact and early
  waterschap involvement in siting.
  - region: `eu`, `eu_west`, `netherlands` | category: `regulatory`
  - tags: `mandates`, `planning`, `water_quality` (new tag, or reuse `planning`)
  - policy_types: `guidance`, `report` | language: `nl`
- **format**: HTML
- **practical**: robots.txt uses a "Content-Signal" opt-in format, no outright
  disallow observed for this path; single static page, low crawl cost.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: This is the single clearest, most direct government-adjacent
  statement anywhere in this research tying data-center cooling water to a named
  EU directive and demanding regulation - a strong keyword-taxonomy match.
- **verified**: yes - fetched full page text directly. Confirmed live, exact
  quote captured (see coverage above), fully on-topic.

### 3. Netherlands - HHNK (Hoogheemraadschap Hollands Noorderkwartier): Datacenters Noord-Holland
- **name**: HHNK Regional Water Authority - Datacenters Noord-Holland
- **id**: `nl_hhnk_datacenters`
- **base_url**: `https://www.hhnk.nl`
- **start_paths**:
  - `/_flysystem/media/datacenters-2.pdf`
- **level**: subnational (regional water authority - Noord-Holland / Wieringermeer,
  the actual permitting authority for the Microsoft/Google Wieringermeer cluster)
- **access**: none
- **coverage**: Discharge-permit conditions HHNK imposes on the two active
  Wieringermeer data centers for cooling-water discharge to surface water
  (salt-content limits, no-chemicals condition, drought-priority ranking that
  places drinking water above cooling-water use). Confirmed via prior web
  search snippet quoting the same document; PDF itself downloaded successfully.
  - region: `eu`, `eu_west`, `netherlands` | category: `regulatory`
  - tags: `mandates`, `reporting` | policy_types: `guidance`, `report`
  - language: `nl`
- **format**: PDF
- **practical**: served from `hhnk.nl`'s `_flysystem` media host; 301-redirects
  at bare-domain level but the direct PDF path returned HTTP 200, 179KB file.
- **effort tier**: (b) plain crawl domain (single PDF; would sit under a small
  `hhnk_nl` domain entry with `max_pages` low)
- **why worth adding**: The single most concrete, facility-level cooling-water
  regulatory document found in this research - a real regional regulator's
  discharge-permit terms for named data centers, not a general statement.
- **verified**: yes - PDF fetched (200, downloaded, 179.2KB), title/metadata
  confirm Dutch-language document about "Datacenters Noord Holland"; full text
  extraction failed (PDF binary stream, needs OCR/PDF parser at crawl time -
  same as any other PDF source in this project), but resolution + on-topic
  identity is confirmed via the file itself and a corroborating search snippet
  quoting its content.

### 4. Ireland EPA - Water Abstraction Licensing/Registration
- **name**: Ireland Environmental Protection Agency - Water Abstraction
- **id**: `ie_epa_water_abstraction`
- **base_url**: `https://www.epa.ie`
- **start_paths**:
  - `/our-services/licensing/freshwater--marine/water-abstraction/`
  - `/our-services/licensing/waste-water/`
- **level**: national
- **access**: none
- **coverage**: Water Environment (Abstractions and Associated Impoundments)
  Act 2022 + 2024 Regulations (in force Aug 28, 2024), transposing the EU Water
  Framework Directive; registration/licensing required above 25 m3/day
  abstracted, applies to industrial users; also covers EPA wastewater discharge
  authorisation, the license data centers with on-site cooling-tower blowdown
  discharge would need.
  - region: `eu`, `eu_west`, `ireland` | category: `environmental_agency`
  - tags: `mandates`, `reporting` | policy_types: `law`, `regulation`
  - language: `en`
- **format**: HTML (register/licence search is a queryable HTML tool, not a
  documented API - tier-b, not tier-c)
- **practical**: no crawl block observed; EPA publishes a public abstraction
  register (searchable) alongside the regulatory text.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: `ireland.yaml` currently only covers SEAI (energy),
  gov.ie sustainability reporting, and CRU's electricity connection policy -
  no water regulator at all, despite Ireland's data-center water fight
  (South Dublin hosepipe-ban controversy) being one of the most visible in
  Europe. EPA is the correct body (not Uisce Éireann, which is the utility,
  not the regulator).
- **verified**: yes - fetched directly. Confirmed live text: exact statute
  names, in-force date, and 25 m3/day threshold, on-topic.

### 5. Singapore PUB - Mandatory Water Efficiency Management Practices
- **name**: PUB Singapore - Mandatory Water Efficiency Management Practices
- **id**: `sg_pub_water_efficiency`
- **base_url**: `https://www.pub.gov.sg`
- **start_paths**:
  - `/Public/WaterLoop/Water-Conservation/Mandatory-Water-Efficiency-Requirements`
  - `/-/media/Images/Feature/Content-Pages/Public/Singapore-Water-Loop/Water-Conversation/Mandatory-Water-Efficiency-Requirements/Guide-on-Water-Efficiency-Management-Practices.pdf`
- **level**: national
- **access**: none
- **coverage**: Mandatory Water Efficiency Management Practices (MWEMP, since
  2015) - data centers and other large water users above 60,000 m3/year must
  submit annual water consumption, a Water Efficiency Management Plan, and
  install sub-meters; feeds Singapore's sectoral WUE benchmark (2.2 m3/MWh
  measured 2021, 2.0 m3/MWh target).
  - region: `apac`, `singapore` | category: `regulatory`
  - tags: `mandatory`, `reporting`, `wue`, `efficiency`
  - policy_types: `regulation`, `guidance` | language: `en`
- **format**: HTML + PDF guide
- **practical**: main site returns HTTP 200/robots empty (no disallow); the
  specific guide-page path 403'd to the automated fetch tool (likely WAF/UA
  filtering) but rendered fine in an interactive browser and the linked PDF
  itself returned HTTP 200 and downloaded cleanly (214.7KB, confirmed on-topic
  by content).
- **effort tier**: (b) plain crawl domain
- **why worth adding**: `apac.yaml` already has Singapore's IMDA (green DC /
  PUE) and BCA (Green Mark building code) but nothing from PUB - the actual
  water regulator, and the only body publishing a hard water-consumption
  threshold + mandatory reporting scheme naming data centers.
- **verified**: yes, via the linked PDF guide (200, downloaded, content
  confirms data centers, thresholds, and reporting obligations); the HTML
  landing page's existence and title were also confirmed live via browser
  render (page title "Mandatory Water Efficiency Requirements | PUB, Singapore's
  National Water Agency" loaded, though body text is client-rendered and did
  not extract cleanly - flag `requires_playwright: true`).

### 6. Arizona Department of Water Resources - Assured & Adequate Water Supply
- **name**: Arizona Department of Water Resources - Assured and Adequate Water Supply
- **id**: `az_water_resources`
- **base_url**: `https://www.azwater.gov`
- **start_paths**:
  - `/assured-and-adequate-water-supply`
  - `/laws-rules-policies`
- **level**: subnational (state; program is administered per Active Management
  Area - 7 AMAs statewide)
- **access**: none (public site; no data-center-specific portal)
- **coverage**: Assured Water Supply (AWS) program requires developers/users
  within an Active Management Area to demonstrate a 100-year water supply;
  Arizona's 2023 groundwater moratorium (new subdivisions outside Buckeye)
  does **not** apply to industrial users like data centers - the regulatory
  gap driving current Project Blue (Tucson) well-permit controversy that ADWR
  itself approved in 2026.
  - region: `us`, `us_states`, `arizona` | category: `regulatory`
  - tags: `planning`, `mandates` | policy_types: `regulation`, `guidance`
  - language: `en`
- **format**: HTML
- **practical**: **site is behind Cloudflare bot-challenge** - direct `curl`
  and the automated WebFetch tool both got a JS challenge page, not content.
  A real browser tab rendered it fully (confirmed live nav with links to
  `/aaws/aaws-overview`, `/ama/wmap`, and the `app.azwater.gov/ReportAnnualUsage`
  reporting tool). **Must set `requires_playwright: true`.**
- **effort tier**: (b) plain crawl domain (requires Playwright)
- **why worth adding**: `us/arizona.yaml` currently has only the Corporation
  Commission and legislature - no water authority, despite Arizona (Phoenix/
  Mesa/Tucson) being the #2 US water-stress data-center flashpoint after
  Virginia's reporting fight. ADWR is the only state body with statutory
  water-allocation authority relevant to DC siting.
- **verified**: yes, via interactive browser render (page loaded, real ADWR
  nav structure, AAWS/AMA/reporting links present); automated `curl`/WebFetch
  alone would have wrongly reported this as unreachable due to the Cloudflare
  challenge - noted so crawl config can allow for it.

### 7. Texas TCEQ - Water Rights Permitting
- **name**: Texas Commission on Environmental Quality - Water Rights
- **id**: `tx_tceq_water_rights`
- **base_url**: `https://www.tceq.texas.gov`
- **start_paths**:
  - `/permitting/water_rights/wr-permitting`
  - `/permitting/water_rights/wr-permitting/water-right-permits-annual-water-use-report`
- **level**: subnational (state)
- **access**: none
- **coverage**: Surface-water rights permitting (applications, change-of-ownership,
  drought contingency plans, watermaster programs) and the annual Water Use
  Report (WUR) system; TCEQ also administers reclaimed-water agreements
  allowing non-potable water for industrial cooling. Texas legislators are
  currently pressing TCEQ over data centers not disclosing water use.
  - region: `us`, `us_states`, `texas` | category: `regulatory`
  - tags: `reporting`, `mandates`, `planning` | policy_types: `regulation`
  - language: `en`
- **format**: HTML
- **practical**: `robots.txt` returned empty (no disallow rules); page is
  server-rendered, no JS required.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: `us/texas.yaml` only has the State Energy Conservation
  Office and the legislature - no water regulator, despite Texas being a top-3
  US data-center hub with an active drought/water-rights permitting fight.
- **verified**: yes - fetched directly, confirmed on-topic (surface water
  rights, drought contingency, annual water-use reporting).

### 8. California DWR - Water Use Efficiency (Land & Water Use)
- **name**: California Department of Water Resources - Water Use Efficiency
- **id**: `ca_dwr_water_use`
- **base_url**: `https://water.ca.gov`
- **start_paths**:
  - `/Programs/Water-Use-And-Efficiency/Land-And-Water-Use`
  - `/wateruseefficiency/`
- **level**: subnational (state)
- **access**: none
- **coverage**: General land/water-use survey and CII (commercial/industrial/
  institutional) data program. Currently does **not** mention data centers by
  name, but DWR is the statutorily designated agency (under pending AB 2469 /
  AB 2619) required to publish a data-center water-use definition and annual
  consumption estimate by June 30, 2028, ahead of the State Water Resources
  Control Board's mandatory CII classification for data centers by Dec 31, 2029.
  - region: `us`, `us_states`, `california` | category: `regulatory`
  - tags: `planning`, `research` | policy_types: `report`, `guidance`
  - language: `en`
- **format**: HTML
- **practical**: HTTP 200, no crawl block encountered.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: forward-looking placeholder for the 2028/2029 CA
  data-center water mandate - not yet publishing DC-specific content, so
  ranked lower than the others, but `california.yaml` has zero water-agency
  coverage today (only CEC/CPUC/CARB/CAISO energy-side bodies) and this is
  the correct body to seed now so the crawler picks up the mandated report
  when it lands.
- **verified**: yes (page live, on-topic for CII/water-use-efficiency
  generally) - explicitly **not yet** verified to mention data centers; see
  caveat above. Recommend re-check in 2028.

### 9. California State Water Resources Control Board - Water Rights Diversion & Use Rulemaking
- **name**: California SWRCB - Water Measurement and Reporting Regulations Rulemaking
- **id**: `ca_swrcb_water_rulemaking`
- **base_url**: `https://www.waterboards.ca.gov`
- **start_paths**:
  - `/waterrights/water_issues/programs/diversion_use/rulemaking.html`
  - `/conservation/water-use-explorer/`
- **level**: subnational (state)
- **access**: none
- **coverage**: Water rights diversion/use measurement & reporting rulemaking
  docket (the SWRCB side of the same AB 2469/AB 2619 data-center water package
  described above - SWRCB must adopt a CII water-use classification for data
  centers, separate from other CII users, by Dec 31, 2029); Water Use Explorer
  tool covers CII classification generally under AB 1668/SB 606 (no DC mention
  yet).
  - region: `us`, `us_states`, `california` | category: `regulatory`
  - tags: `planning`, `reporting` | policy_types: `regulation`, `report`
  - language: `en`
- **format**: HTML
- **practical**: `robots.txt` disallows `/images/`, `/css/`, `/dev/`,
  `/javascript/` only - `/waterrights/*` and `/conservation/*` are crawlable.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: pairs with DWR (#8) as the other half of California's
  forward data-center water mandate; SWRCB is the body that will actually
  publish the binding CII classification.
- **verified**: yes (both pages live, fetched directly); rulemaking docket
  page confirmed to exist via search but not deep-fetched for this specific
  page - the Water Use Explorer sub-page **was** directly fetched and confirmed
  on-topic for CII/AB 1668 (no DC mention yet, same caveat as #8).

---

## Unverified / needs-human-check

- **Spain - Confederación Hidrográfica del Ebro** (`https://www.chebro.es/en/`)
  - River-basin authority governing water concessions for the Aragón data-center
    cluster (Amazon/Microsoft, ~€47B committed investment, water demand cited
    at 750,000+ m3/year regionally). Site resolves (HTTP 200) and the authority
    is clearly the correct regulator for this region's water concessions, but
    I could not find or confirm a specific page/document on the CHEbro site
    itself addressing data-center water concessions - only third-party news
    coverage (Público, AraInfo) discussing the issue politically. Do not add
    without a human finding the actual concession/permitting page or a named
    CHEbro policy document on data-center water use.

- **Ireland - Uisce Éireann (Irish Water) Developer Services**
  (`https://www.water.ie/connections/developer-services`)
  - Uisce Éireann's own PR describes a "Pre-Connection Enquiry" process
    specifically conditioning data-center connections on on-site water storage
    and reuse, but the live page I fetched (`/connections/developer-services`)
    only covers general housing/developer connections with no data-center
    content visible. The right underlying document is likely their "Water
    Services Policy Statement 2024-2030" PDF
    (`https://www.water.ie/sites/default/files/2025-05/water-services-policy-statement-2024-2030.pdf`,
    not yet content-checked for DC-specific language) or a dedicated statement
    page not surfaced by search. Flag for a human to locate the primary
    document before adding; base_url `cru.ie` (the economic regulator that
    approves Uisce Éireann's connection policy) is **already covered** in
    `ireland.yaml` (`cru_ie_dc`), so only the utility side would be net-new.

- **England - GOV.UK abstraction-licence guidance page** - **not a new
  candidate, dedup note only**. `config/domains/uk.yaml` already has an
  `uk_environment_agency` entry on `base_url: https://www.gov.uk` with
  `water_abstraction` already tagged, but its `start_paths` do not include the
  specific abstraction-licensing guidance page
  (`/guidance/manage-your-water-abstraction-or-impoundment-licences-online`).
  Recommend a human add this one path to the existing entry rather than create
  a duplicate domain (same base_url is an automatic skip per dedup rule).

- **EU Water Framework Directive / DC water reporting** - **not a new
  candidate, dedup note only**. The EU's data-center WUE/PUE/ERF/REF annual
  reporting database (Delegated Regulation EU/2024/1364, the exact page found
  at `energy.ec.europa.eu/.../energy-performance-data-centres_en`) is **already
  fully covered** by the existing `ec_energy_datacentres` entry in `eu.yaml`
  (same base_url, same exact start_path already present). No action needed.

- **Netherlands - Rijkswaterstaat water permits**
  (`https://www.rijkswaterstaat.nl/water/wetten-regels-en-vergunningen/vergunningen-rijkswateren`)
  - Confirmed live (fetched directly) and it is the correct national-waters
    permitting authority (Waterwet permits for discharge/withdrawal to
    Rijkswateren), but the fetched page is a generic permitting-process
    overview with no industrial-cooling-water or data-center-specific text.
    Weaker than the Unie van Waterschappen / HHNK entries above; include only
    if a human wants blanket NL national-waters permitting coverage rather
    than the two DC-specific NL sources already verified.

---

## Summary of dedup findings (for reviewer)

- `epd.georgia.gov` (Georgia EPD, includes `/water-protection`) is **already
  covered** in `us/georgia.yaml` - checked before proposing a Georgia water
  candidate, correctly skipped.
- `waterrights.utah.gov` and `www.cpuc.ca.gov` already exist in `config/domains/`
  under non-water categories; neither overlaps with the candidates above.
- No existing crawl domain or draft file anywhere referenced `deq.virginia.gov`,
  `azwater.gov`/`water.az.gov`, `tceq.texas.gov`, `water.ca.gov`,
  `waterboards.ca.gov`, `epa.ie`, `unievanwaterschappen.nl`, `hhnk.nl`,
  `rijkswaterstaat.nl`, or `pub.gov.sg` - all confirmed net-new base_urls.
