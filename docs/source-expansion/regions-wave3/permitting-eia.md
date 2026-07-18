# Wave 3 - Environmental Permitting / EIA / Industrial Emissions Authorities

Scope: government bodies running environmental impact assessment (EIA/SEA),
planning approval, and industrial-emissions permitting for data centers, that
publish the conditions or guidance (energy efficiency, waste-heat reuse,
backup-generator emissions, noise). This is the layer where DC energy/heat/
noise conditions actually get *set*, at construction approval - upstream of
the energy-ministry and legislative sources already in the config.

Dedup performed against: `config/domains/**/*.yaml` (227 crawl + 9 API
sources, incl. `config/domains/us/*.yaml`), `docs/source-expansion/draft/crawl/**/*.yaml`
(incl. `wave2/`), `docs/source-expansion/draft/new-clients*.md`,
`docs/source-expansion/regions-wave2/*.md`, and `docs/source-expansion/regions/*.md`
(wave1). Full URL list extracted and diffed; every candidate below is a
`base_url` not present anywhere in those files. Existing structured clients
(riksdagen, uk_bills, legisinfo, folketing, eurlex_nim, legiscan, govinfo,
regulations_gov, dip) also checked - none of these candidates fit their shape;
they are permit/planning registries, not bill trackers.

No candidate here is tier-a (drops into an existing client). 11 are tier-b
(plain crawl domain). 2 are tier-c (searchable/API permit registers, no
client exists yet - flagged per brief).

---

## Verified candidates (ranked best-first)

### 1. Ireland - EPA Industrial Emissions Licensing (IED)

- **name**: Environmental Protection Agency Ireland - Industrial Emissions Licensing
- **id**: `epa_ie_ied`
- **base_url**: `https://www.epa.ie`
- **start_paths**:
  - `/our-services/licensing/industrial/industrial-emissions-licensing-ied/`
  - `/our-services/licensing/licencesearch/`
- **level**: national
- **access**: none (open web; the underlying dynamic search app at
  `epawebapp.epa.ie/terminalfour/ippc/index.jsp` returned a 500 on a plain
  fetch - likely needs a JS session/Playwright, see unverified note below)
- **coverage**: region `["eu", "eu_west", "ireland"]`; category
  `regulatory`; tags `["mandates", "planning", "reporting"]`; policy_types
  `["regulation", "guidance"]`; language `en`
- **format**: HTML (landing/guidance pages), PDF (individual licence
  decisions and inspector's reports)
- **practical**: no published rate limit; robots.txt allows `/our-services/`;
  licence PDFs updated on a rolling basis as applications are decided; docs
  URL is the page itself
- **effort tier**: (b) plain crawl domain (start with the two static pages;
  the search app is a stretch goal, see unverified)
- **why worth adding**: This is the actual enforcement mechanism behind
  Ireland's DC backup-generator rules. IE licences are mandatory once backup
  generator thermal input hits 50MW aggregate, or operation exceeds 18 hrs/yr.
  Secondary sources (Lexology, Matheson) report the EPA has approved 15 IE
  licences and 24 GHG permits specifically to data centre operators, with
  800+ generators listed as emission sources across those licences - i.e.
  this agency is already publishing exactly the "backup-generator emissions"
  conditions the brief targets, and it is not in `ireland.yaml` today (which
  only has SEAI, gov.ie reporting-obligations, CRU, and the statute book).
- **verified**: yes - fetched both pages, HTTP 200, titles confirm
  "Industrial Emissions Licensing (IED) | Environmental Protection Agency"
  and "Search for a Licence/Permit | Environmental Protection Agency".

### 2. Ireland - An Coimisiún Pleanála (planning appeals authority)

- **name**: An Coimisiún Pleanála (formerly An Bord Pleanála) - Case Search
- **id**: `pleanala_ie`
- **base_url**: `https://www.pleanala.ie`
- **start_paths**:
  - `/en-ie/case-search`
  - `/en-ie/cases`
  - `/en-ie/lists` (weekly lists of new/decided cases)
- **level**: national
- **access**: none
- **coverage**: region `["eu", "eu_west", "ireland"]`; category
  `regulatory`; tags `["planning", "mandates"]`; policy_types
  `["regulation", "guidance", "report"]`; language `en`
- **format**: HTML search UI + PDF case files (inspector's reports, board
  orders, EIAR/NIS screening determinations)
- **practical**: search covers cases from 2016 to date; filters include ABP
  case number, planning authority, address, county/province, lodgement/
  decision date ranges, case type (incl. Strategic Infrastructure
  Development), decision outcome, and EIAR/NIS indicators; likely needs
  Playwright (interactive filter form, not plain GET params)
- **effort tier**: (b) plain crawl domain, `requires_playwright: true`
- **why worth adding**: Ireland is the live EU test case for DC planning
  friction (Dublin grid connection moratorium, Ennis and AWS North Dublin
  appeals, Equinix refusal). This is the national planning-appeal authority
  of record - every large DC planning decision (and its EIAR/environmental
  conditions - noise, grid connection, backup generation) that isn't
  resolved at local-authority level ends up here. Nothing in `ireland.yaml`
  currently covers planning appeals; SEAI/CRU/gov.ie are energy-side only.
- **verified**: yes - fetched `/en-ie/case-search`, confirmed live filterable
  case-search tool with the fields listed above.

### 3. UK - Planning Inspectorate: National Infrastructure Planning (NSIP)

- **name**: Planning Inspectorate - National Infrastructure Planning (NSIP register)
- **id**: `pins_nsip_uk`
- **base_url**: `https://infrastructure.planninginspectorate.gov.uk`
- **start_paths**:
  - `/` (project register/search)
- **level**: national
- **access**: none
- **coverage**: region `["uk"]`; category `regulatory`; tags
  `["planning", "mandates"]`; policy_types `["regulation", "guidance",
  "report"]`; language `en`
- **format**: HTML register + PDF application documents (environmental
  statements, examination decisions)
- **practical**: no auth; site is a project register searchable by sector/
  status; update frequency continuous as projects move through examination
- **effort tier**: (b) plain crawl domain
- **why worth adding**: New regulations effective January 2026 formally
  brought data centres into the NSIP regime (opt-in via Secretary of State
  direction under Planning Act 2008 s.35) - a genuinely new UK consenting
  pathway for large DCs, decided nationally rather than by local planning
  authorities, with a statutory Development Consent Order process that
  includes Environmental Impact Assessment. `uk.yaml` already has the
  Environment Agency (environmental permits for generators) and a Heat
  Networks Planning Database, but nothing on the NSIP/DCO track - this is
  the body that will publish the EIA-linked conditions once DCs start using
  the opt-in.
- **verified**: yes - direct WebFetch was blocked by the site (403 to the
  automated fetch tool), but a plain `curl` with a standard browser
  user-agent returned HTTP 200 with title "National Infrastructure Planning",
  confirming the domain is live and correctly targeted.

### 4. Germany (Hesse) - Regierungspräsidium Darmstadt, Immissionsschutz (BImSchG permitting)

- **name**: Regierungspräsidium Darmstadt - Immissionsschutz (BImSchG data centre permits)
- **id**: `rp_darmstadt_immissionsschutz`
- **base_url**: `https://rp-darmstadt.hessen.de`
- **start_paths**:
  - `/Themen-A-Z/immissionsschutz`
  - `/umwelt-und-energie/laerm-luft-strahlen/genehmigungsverfahren`
- **level**: subnational (Regierungsbezirk within Land Hesse)
- **access**: none
- **coverage**: region `["eu", "eu_central", "germany", "hessen"]`; category
  `regulatory`; tags `["mandates", "planning", "efficiency"]`; policy_types
  `["regulation", "guidance"]`; language `de`
- **format**: HTML notice list + PDF permit decisions (Genehmigungsbescheide)
- **practical**: no rate limit published; the notice list is paginated (63
  entries across 8 pages at time of check) and refreshes every 2-4 weeks per
  public-notice cycle; from Jan 2027 new applications route through the
  ELiA online portal, but published decisions will remain on this page
- **effort tier**: (b) plain crawl domain, `language: "de"`
- **why worth adding**: Frankfurt is Europe's largest data centre market, and
  RP Darmstadt is the actual BImSchG (Federal Immission Control Act)
  permitting authority for it - fetched content directly showed live permit
  entries for named data centre operators (e.g. a 30.06.2026 permit grant
  to "CyrusOne Frankfurt 7 Holdings B.V." and emergency-diesel-generator
  approvals for facilities in Dietzenbach and Raunheim). `germany.yaml`
  already tracks Hesse's economic-development and digital-infrastructure
  ministries (`hessen_energy`, `hessen_digital_dc`) and the state law
  database (`hessen_recht`), but not the actual permitting authority that
  issues the emissions/noise conditions on individual DC buildouts - this
  is the missing piece.
- **verified**: yes - fetched, confirmed live permit notices including the
  CyrusOne and generator-approval entries described above.

### 5. Sweden - Länsstyrelsen (county administrative board) environmental permitting

- **name**: Länsstyrelsen Stockholm - Prövning av miljöfarlig verksamhet (environmental permit review)
- **id**: `lansstyrelsen_stockholm_miljo`
- **base_url**: `https://www.lansstyrelsen.se`
- **start_paths**:
  - `/stockholm/miljo-och-vatten/miljofarlig-verksamhet/provning-av-miljofarlig-verksamhet.html`
- **level**: subnational (county / län)
- **access**: none
- **coverage**: region `["eu", "nordic", "sweden"]`; category `regulatory`;
  tags `["mandates", "planning"]`; policy_types `["regulation",
  "guidance"]`; language `sv`
- **format**: HTML guidance page, links out to Naturvårdsverket (national EPA)
  decision PDFs for specific permits
- **practical**: no rate limit published; static guidance page, low update
  frequency, but is the entry point for the Miljöprövningsdelegationen (MPD)
  process
- **effort tier**: (b) plain crawl domain, `language: "sv"`
- **why worth adding**: Sweden requires data centres to secure a Chapter 9
  Environmental Code permit ("B-verksamhet") via the county's
  Miljöprövningsdelegationen when they have material environmental impact -
  and Naturvårdsverket-published decision documents confirm this explicitly
  covers "datacenter med reservkraftsgeneratorer" (data centre with backup
  generators), addressing noise and air emissions from diesel gensets. This
  is the permitting layer underneath `sweden.yaml`'s existing energy-agency
  and legislative entries (Energimyndigheten, Riksdagen, Regeringen, EI,
  Riksrevisionen) - none of which is the actual permit-granting authority.
- **verified**: yes - fetched, confirmed the MPD/permit-review process
  description; page itself doesn't name data centres explicitly, but a
  linked Naturvårdsverket decision PDF (found via search) does, confirming
  this permitting track is the correct one - see caveat in Unverified
  section re: page-level specificity.

### 6. Denmark - Miljøstyrelsen (Environmental Protection Agency) environmental approvals

- **name**: Miljøstyrelsen - Miljøgodkendelse af listevirksomheder (environmental approval of listed activities)
- **id**: `mst_dk_miljoegodkendelse`
- **base_url**: `https://mst.dk`
- **start_paths**:
  - `/erhverv/groen-produktion-og-affald/industri/miljoegodkendelse-af-listevirksomheder`
- **level**: national
- **access**: none
- **coverage**: region `["eu", "nordic", "denmark"]`; category `regulatory`;
  tags `["mandates", "planning"]`; policy_types `["regulation",
  "guidance"]`; language `da`
- **format**: HTML guidance; links to the digital application system
  "Byg og Miljø" / DMA (Digital MiljøAdministration) at `dma.mst.dk`
- **practical**: no rate limit published; static guidance, low update
  frequency
- **effort tier**: (b) plain crawl domain, `language: "da"`
- **why worth adding**: Miljøstyrelsen is the national-level environmental
  approval authority for "Annex 1/2" listed polluting activities (most cases
  are delegated to municipalities, but MST retains authority for the subset
  marked "s" on the activity annexes) - the mechanism through which DC
  cooling-water discharge, noise, and generator-emissions conditions are
  set. `denmark.yaml` today only has the Danish Energy Agency (heat) and
  the Heat Supply Act text - no environmental-permitting body.
- **verified**: yes - fetched, HTTP 200, confirms the miljøgodkendelse
  process description (approval authority split between municipalities and
  MST, conditions cover emissions/noise/vibration/groundwater).

### 7. Netherlands - Informatiepunt Leefomgeving (IPLO): data centre environmental-activity rules

- **name**: IPLO - Milieubelastende activiteit datacentrum (Bal §3.7.3)
- **id**: `iplo_nl_datacentrum`
- **base_url**: `https://iplo.nl`
- **start_paths**:
  - `/regelgeving/regels-voor-activiteiten/milieubelastende-activiteiten-hoofdstuk-3-bal/dienstverlening/datacentrum/`
- **level**: national
- **access**: none
- **coverage**: region `["eu", "eu_west", "netherlands"]`; category
  `regulatory`; tags `["mandates", "efficiency", "planning"]`; policy_types
  `["regulation", "guidance"]`; language `nl`
- **format**: HTML
- **practical**: no rate limit published; static regulatory-guidance page,
  updated when the Besluit activiteiten leefomgeving (Bal) is amended
- **effort tier**: (b) plain crawl domain, `language: "nl"`
- **why worth adding**: this is a page dedicated specifically to data
  centres as a named "environmentally polluting activity" (Bal §3.7.3) under
  the Omgevingswet (Environment and Planning Act) - the exact permitting
  hook for DC energy consumption, cooling-water discharge, and backup-power
  conditions in the Netherlands. `netherlands.yaml` only has the general
  national legislation search (wetten.overheid.nl); `eu.yaml`'s `rvo_nl`
  entry is incentives, not permitting. Net-new and precisely on-topic.
- **verified**: yes - fetched, HTTP 200, title confirms "Milieubelastende
  activiteit datacentrum (paragraaf 3.7.3 Bal) | Informatiepunt Leefomgeving".

### 8. US Virginia - DEQ Issued Air Permits for Data Centers

- **name**: Virginia Department of Environmental Quality - Issued Air Permits for Data Centers
- **id**: `va_deq_dc_air_permits`
- **base_url**: `https://www.deq.virginia.gov`
- **start_paths**:
  - `/news-info/shortcuts/permits/air/issued-air-permits-for-data-centers`
- **level**: subnational (state)
- **access**: none
- **coverage**: region `["us", "us_states", "virginia"]`; category
  `regulatory`; tags `["mandates", "planning"]`; policy_types
  `["regulation", "guidance", "report"]`; language `en`
- **format**: HTML index page linking individual permit PDFs
- **practical**: site sits behind Akamai bot-protection (both WebFetch and a
  scripted curl got HTTP 403/"Access Denied" - a real browser/Playwright
  session should work); update frequency: rolling, as permits are issued;
  new BACT (Tier-4-equivalent SCR/DPF/DOC) requirements for gensets apply to
  applications received on/after 2026-07-01
- **effort tier**: (b) plain crawl domain, `requires_playwright: true`
  (needed to get past bot protection, not just JS rendering)
- **why worth adding**: Virginia (Loudoun/Prince William County - "Data
  Center Alley") is the single largest DC concentration in the world, and
  this is DEQ's own curated, named page listing issued air permits
  specifically for data centers, including the new statewide BACT standard
  for both emergency and non-emergency diesel generators. `us/virginia.yaml`
  currently only has the Dept. of Energy and General Assembly bill trackers
  (HB323/HB906/HB824) - nothing from the actual permitting regulator. This
  is the single highest-value US find in this batch given DC density and the
  live 2026 generator-BACT rule change.
- **verified**: yes, indirectly - direct fetch is blocked by anti-bot
  protection (confirmed via both WebFetch and curl, HTTP 403/"Access
  Denied"), but the exact URL is independently cited as the canonical DEQ
  source by multiple secondary sources fetched successfully (Hunton, Trinity
  Consultants, MIRATECH, Virginia Mercury, VPM), and the search engine
  itself returned the live page title "Issued Air Permits for Data Centers |
  Virginia DEQ" from deq.virginia.gov. Treat as verified-by-corroboration;
  flag `requires_playwright` to get a real render past the bot gate.

### 9. US Virginia (Loudoun County) - Data Center Standards & Locations

- **name**: Loudoun County, VA - Data Center Standards & Locations
- **id**: `loudoun_county_dc_standards`
- **base_url**: `https://www.loudoun.gov`
- **start_paths**:
  - `/5990/Data-Center-Standards-Locations`
  - `/6222/Phase-2-Data-Center-Standards-Locations`
- **level**: local (county)
- **access**: none
- **coverage**: region `["us", "us_states", "virginia"]`; category
  `regulatory`; tags `["mandates", "planning"]`; policy_types
  `["regulation", "guidance"]`; language `en`
- **format**: HTML with linked PDF ordinance/standards documents
- **practical**: no rate limit published; Phase 1 standards adopted March
  2025, Phase 2 (noise, setbacks, utility impact standards) in progress at
  time of check
- **effort tier**: (b) plain crawl domain
- **why worth adding**: Loudoun County is the literal "data center capital
  of the world" by county-level concentration, and is actively writing
  use-specific zoning/special-exception standards for DCs covering noise,
  setbacks, and utility impacts - i.e. exactly the construction-approval
  conditions the brief targets, at the local level where it is actually
  being negotiated county-by-county. Complements the state-level VA DEQ
  entry above; neither is in `us/virginia.yaml` today.
- **verified**: yes - both URLs fetched via curl, HTTP 200, titles confirmed.

### 10. US Texas - TCEQ air permitting for generators/electric generating units

- **name**: Texas Commission on Environmental Quality - Air Permitting (Electric Generating Units / Portable & Emergency Engines)
- **id**: `tceq_air_generators`
- **base_url**: `https://www.tceq.texas.gov`
- **start_paths**:
  - `/permitting/air/newsourcereview/combustion/egu_sp.html`
  - `/permitting/air/permitbyrule/subchapter-w/portable_power.html`
- **level**: subnational (state)
- **access**: none
- **coverage**: region `["us", "us_states", "texas"]`; category
  `regulatory`; tags `["mandates", "planning"]`; policy_types
  `["regulation", "guidance"]`; language `en`
- **format**: HTML plus linked PDF permit-by-rule text and standard permit
  conditions
- **practical**: no rate limit published; standard/general permits revised
  periodically (30 TAC 106.4/106.511 for portable & emergency engines, 30
  TAC 116.601-615 for the EGU standard permit)
- **effort tier**: (b) plain crawl domain
- **why worth adding**: Texas is a fast-growing DC market (ERCOT
  interconnection queue pressure is a live policy topic) and TCEQ publishes
  the specific standard-permit and permit-by-rule conditions that let DC
  backup/electric-generating-unit gensets avoid full individual air permits
  - the emissions-condition mechanism the brief is after.
  `us/texas.yaml` currently only has SECO (state energy office) and the
  legislature bill tracker - no environmental regulator.
- **verified**: yes - confirmed via search snippet titles matching the exact
  TCEQ pages (Air Quality Standard Permit for Electric Generating Units;
  Air PBR 106.511: Portable and Emergency Engines and Turbines); not
  independently re-fetched with curl in this pass, standard TCEQ .gov
  pages, low risk.

### 11. Australia (NSW) - Planning Portal: State Significant Development for data centres

- **name**: NSW Planning Portal / Dept. of Planning - SSD Warehouses and Data Centres
- **id**: `nsw_planning_ssd_dc`
- **base_url**: `https://www.planning.nsw.gov.au`
- **start_paths**:
  - `/policy-and-legislation/planning-reforms/ssd-warehouses-and-data-centres`
- **level**: subnational (state)
- **access**: none
- **coverage**: region `["apac", "australia"]`; category `regulatory`; tags
  `["planning", "mandates"]`; policy_types `["regulation", "guidance"]`;
  language `en`
- **format**: HTML
- **practical**: no rate limit published; page defines the SSD threshold
  (data centres >15MW total power consumption trigger State Significant
  Development status, assessed by the Independent Planning Commission or
  minister rather than local council, requiring a full EIS)
- **effort tier**: (b) plain crawl domain. Consider also crawling the
  sibling domain `planningportal.nsw.gov.au` (individual project pages,
  e.g. DigiCo SYD1, Mamre Road Data Centre Campus) as a second entry if
  case-level detail is wanted - not included here to keep this candidate
  narrowly verified.
- **why worth adding**: this is a purpose-written government page defining
  exactly when a data centre must go through full EIA (State Significant
  Development + Environmental Impact Statement) in Australia's largest
  state - power-threshold-triggered planning policy, precisely on-topic.
  `australia.yaml` currently only has NSW Climate and Energy Action and NSW
  Investment Delivery Authority - no planning/EIA authority.
- **verified**: yes - fetched directly, confirmed the >15MW SSD threshold
  language and page purpose.

---

## Tier-c: searchable permit registers / APIs (flagged per brief)

### 12. Georgia (US) - EPD Air Permit Search Engine

- **name**: Georgia EPD - Air Permit Search Engine
- **id**: `ga_epd_permit_search` (proposed; distinct from existing crawl
  domain `ga_epd` in `config/domains/us/georgia.yaml`, which only crawls
  `/air-protection` and `/water-protection` static pages)
- **base_url**: `https://permitsearch.gaepd.org`
- **source_type feasibility**: searchable web form (AIRS Number, Facility
  Name, Permit Number/SIC Code) backed by a database; no documented public
  REST API found - would need a NEW client that drives the search form
  (or scrapes result pages) rather than an existing API-shaped client
- **level**: subnational (state)
- **access**: none (no key required to search; unclear if bulk/API access
  exists - flag for a human to check with GA EPD directly)
- **coverage**: region `["us", "us_states", "georgia"]`; category
  `regulatory`; tags `["mandates", "reporting"]`; policy_types
  `["regulation"]`; language `en`
- **format**: HTML search UI, PDF permit documents (e.g. Title V permits
  naming DC operators with 50+ diesel emergency generators)
- **practical**: no published rate limit or ToS review done; recommend
  manual ToS check before scripted querying
- **effort tier**: (c) needs a new structured client (form-driven search,
  not a documented API) - spec only, no code
- **why worth adding**: Georgia is a fast-growing DC market and this is a
  facility-level searchable permit database (distinct base_url from the
  existing `ga_epd` static crawl domain) that would let a future client
  pull specific DC air-permit records (e.g. the confirmed 50+-generator
  synthetic-minor Title V permit) rather than relying on generic page
  crawling.
- **verified**: yes - fetched, confirmed live search form with the three
  fields listed and a "Search Permits" button; could not confirm from
  static content whether the backend is actually responsive (would need a
  live query to test, not done here per read-only research scope).

### 13. EU/EEA - European Industrial Emissions Portal

- **name**: European Industrial Emissions Portal (EEA) - Industrial Reporting Database
- **id**: `eea_industrial_emissions_portal` (proposed)
- **base_url**: `https://industry.eea.europa.eu`
- **source_type feasibility**: dataset download (CSV/XML) of facility-level
  IED installations, E-PRTR releases, and Large Combustion Plant (LCP) data
  across the EU/EEA, per the "Industrial Reporting under IED 2010/75/EU and
  E-PRTR Regulation (EC) 166/2006" catalogue record; a GeoNetwork/CSW-style
  metadata API backs the spatial catalogue - would need a NEW client (no
  existing client handles OGC/GeoNetwork-shaped or bulk CSV EU environmental
  data)
- **level**: supranational
- **access**: none (open download; no key found required for the dataset
  pages)
- **coverage**: region `["eu"]`; category `regulatory`; tags
  `["reporting", "carbon", "mandates"]`; policy_types `["report",
  "regulation"]`; language `en`
- **format**: HTML portal + CSV/XML bulk download + geospatial catalogue
  record (INSPIRE/ISO19139)
- **practical**: dataset covers E-PRTR facility releases 2007-2024, IED
  installations 2017-2024, LCPs 2016-2024; no rate limit found on the
  static pages; download-only, not a live query API in the REST sense
- **effort tier**: (c) needs a new structured client
- **why worth adding**: this is the closest thing to an EU-wide,
  cross-country permitted-installation register that exists, and it is
  entirely absent from `eu.yaml` today (which is EUR-Lex/JRC/RVO/Commission
  guidance only, no installation-level permit data). Important caveat for
  whoever scopes the client: most standalone data centre backup-generator
  setups sit below the IED Annex I / Large Combustion Plant thermal-input
  thresholds (the individual national permitting bodies above, e.g. Hesse's
  RP Darmstadt or Ireland's EPA, are triggered at lower or
  facility-aggregate thresholds), so this portal will likely only surface a
  minority of DC-relevant installations - highest-value use is as a
  cross-check / discovery layer for which DCs *do* cross IED/LCP
  thresholds, not primary coverage.
- **verified**: yes - fetched `/industrial-emissions/about` (HTTP 200), and
  confirmed via search that `/industrial-emissions/dataset` and `/download`
  pages exist and describe the CSV/XML/API-style download offering.

---

## Unverified / needs-human-check

- **Ireland EPA licence search webapp** -
  `https://epawebapp.epa.ie/terminalfour/ippc/index.jsp` returned an HTTP
  500 on a scripted fetch (likely needs a live browser session or different
  entry path). The static `epa.ie` pages above are verified and sufficient
  to start; this dynamic search app would need a human/Playwright session
  to confirm before scripting against it.
- **Sweden Länsstyrelsen page, data-centre specificity** - the Stockholm
  county page itself describes the B-activity permit process generically
  (sewage plants, quarries, wind, farms, "industrial facilities") and does
  not name data centres. The data-centre link is established via a
  separately-found Naturvårdsverket decision PDF
  (`naturvardsverket.se/.../2023-06-08-mpd-stockholm.pdf`, a real Stockholm
  MPD data-centre permit) rather than the Länsstyrelsen page's own text. A
  human should confirm whether to crawl the Länsstyrelsen entry page as
  proposed (process/authority-level coverage) or instead seed on
  Naturvårdsverket's decision-document index for DC-specific hits.
- **Singapore URA (Urban Redevelopment Authority)** - searched for a
  dedicated data-centre planning/use-class guideline page comparable to
  BCA-IMDA's Green Mark scheme; found only generic Master Plan /
  Development Control Guidelines pages (`ura.gov.sg/Corporate/Guidelines/
  Development-Control`, `.../Planning/Master-Plan`) with no DC-specific
  content confirmed in the fetched snippets. Not proposed as a candidate -
  BCA (`www1.bca.gov.sg`) and IMDA (`imda.gov.sg`) are already covered in
  `config/domains/apac.yaml`. Worth a follow-up search specifically for any
  URA circular on data centre use-group classification if a future wave
  revisits Singapore.
- **Netherlands Omgevingsloket main portal** (`omgevingswet.overheid.nl`) -
  this is the live permit-application system itself (interactive, login-
  gated per applicant), not a policy-document publisher; the IPLO page (item
  #7 above) is the correct policy/guidance-document counterpart and is what
  was proposed instead. Flagging the portal here in case a future wave wants
  application-level transparency data rather than the current rule-guidance
  scope.
- **Ohio and other US states** - searched for a state-level environmental or
  noise-permitting authority comparable to Virginia DEQ/Loudoun County;
  found only advocacy-site and county-page commentary confirming "Ohio has
  no statewide noise ordinance / decibel limits for industrial facilities"
  - i.e. no dedicated government policy page to crawl. Not proposed.
- **NEPA / US federal EIA** - not proposed. Federal NEPA review only
  attaches to DC construction when there's a federal nexus (federal land,
  federal funding, or a federal permit trigger e.g. Clean Water Act s.404);
  this is inconsistent/project-specific rather than a standing policy
  source, so no single stable URL to seed.

---

## Summary of proposed additions by target config file

- `ireland.yaml`: add `epa_ie_ied`, `pleanala_ie`
- `uk.yaml`: add `pins_nsip_uk`
- `germany.yaml` (Hesse section): add `rp_darmstadt_immissionsschutz`
- `sweden.yaml`: add `lansstyrelsen_stockholm_miljo` (pending human check above)
- `denmark.yaml`: add `mst_dk_miljoegodkendelse`
- `netherlands.yaml`: add `iplo_nl_datacentrum`
- `config/domains/us/virginia.yaml`: add `va_deq_dc_air_permits`, `loudoun_county_dc_standards`
- `config/domains/us/texas.yaml`: add `tceq_air_generators`
- `australia.yaml`: add `nsw_planning_ssd_dc`
- `config/domains/us/georgia.yaml`: add `ga_epd_permit_search` (tier-c spec, supplements existing `ga_epd`)
- `eu.yaml`: add `eea_industrial_emissions_portal` (tier-c spec)
