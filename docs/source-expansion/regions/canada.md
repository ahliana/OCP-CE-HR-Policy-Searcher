# Canada — Subnational + Federal Gaps

Scope: provincial/territorial energy & environment ministries, provincial utility
regulators, provincial legislature bill trackers, district energy authorities/municipal
programs, and federal bodies beyond Parliament (NRCan/CER). LEGISinfo (federal
Parliament, `source_type: legisinfo`) is already covered and not re-proposed.

Dedup check performed against `config/domains/canada.yaml` (13 existing entries,
base_urls: natural-resources.canada.ca, www.cer-rec.gc.ca, www.canada.ca,
oee.nrcan.gc.ca, www.ontario.ca, www.oeb.ca, www.ieso.ca, www2.gov.bc.ca,
cleanbc.gov.bc.ca, transitionenergetique.gouv.qc.ca, www.hydroquebec.com,
www.alberta.ca, www.auc.ab.ca) and `config/domains/api_sources.yaml` (legisinfo_api,
base_url www.parl.ca/legisinfo). All candidates below use a net-new `base_url`.

---

## Verified candidates (ranked best-first)

### 1. AESO — Large Load Projects (Data Centres)

- **name**: Alberta Electric System Operator — Large Load Projects (Data Centres)
- **id**: `aeso_large_load`
- **base_url**: `https://www.aeso.ca`
- **start_paths**: `/grid/connecting-to-the-grid/large-load-projects/`,
  `/grid/connecting-to-the-grid/process-updates/`
- **level**: subnational (Alberta) — grid operator / regulatory-adjacent
- **access**: none
- **coverage**: region `["north_america","canada","alberta"]`; category
  `grid_operator`; tags `["mandates","planning","efficiency"]`; policy_types
  `["guidance","regulation","report"]`; language `en`
- **format**: HTML (program pages) + PDF (guides, technical-characteristics docs,
  quarterly "Data Centre Update" reports)
- **practical**: robots.txt not fetchable by our tooling (404/blocked to bot fetch,
  but the page itself loads fine in a real browser — no evidence of a crawl
  restriction on `/grid/*`). No stated rate limit; use standard 2.0s. Updated
  frequently — new "Data Centre Update" PDFs posted every 1-3 months through 2025-2026.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: This is the single most directly on-point Canadian source
  found — AESO's live framework for connecting data centres to Alberta's grid
  (1,200 MW interim cap, Phase 2 large-load integration, the "Guide to AESO
  Connection Requirements for Transmission-Connected Data Centres" posted June
  2026) explicitly discusses data-centre load, technical requirements, and
  references waste-heat/self-generation considerations for large loads.
- **verified**: yes. Loaded `https://www.aeso.ca/grid/connecting-to-the-grid/large-load-projects/`
  in a real browser session — page titled "Large Load Projects » AESO", live
  content dated as recently as June 2026, with linked PDFs (connection
  requirements guide, technical/operating characteristics, quarterly updates).

---

### 2. BC Utilities Commission — Thermal Energy Systems

- **name**: British Columbia Utilities Commission — Thermal Energy Systems
- **id**: `bcuc_thermal`
- **base_url**: `https://www.bcuc.com`
- **start_paths**: `/WhatWeDo/ThermalEnergySystems`
- **level**: subnational (BC) — provincial utility regulator
- **access**: none
- **coverage**: region `["north_america","canada","british_columbia"]`; category
  `regulatory`; tags `["mandates","reporting"]`; policy_types
  `["regulation","guidance"]`; language `en`
- **format**: HTML + PDF (TES Guidelines, exemption orders, CPCN application forms)
- **practical**: robots.txt returned 403 to automated fetch, but the page itself
  rendered fully in-browser with no login wall — likely a bot-detection layer on
  root-level requests rather than a real access restriction on this path. No
  stated crawl rate; use standard 2.0s.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: BCUC directly regulates "Thermal Energy System" (TES)
  providers — BC's legal/regulatory term for district heating/cooling systems,
  the core adjacent-policy category the searcher targets. Publishes the TES
  Guidelines (five TES classes, filing/exemption requirements) and links to live
  proceedings (e.g., 2026 Creative Energy Sen̓áḵw rate order).
- **verified**: yes. Loaded via browser; page title "Thermal Energy Systems -
  BCUC", full text confirms TES regulatory framework, guidelines, and exemption
  orders are live and linked.

---

### 3. City of Vancouver — False Creek Neighbourhood Energy Utility

- **name**: City of Vancouver — False Creek Neighbourhood Energy Utility (NEU)
- **id**: `vancouver_neu`
- **base_url**: `https://vancouver.ca`
- **start_paths**: `/home-property-development/southeast-false-creek-neighbourhood-energy-utility.aspx`,
  `/home-property-development/how-the-utility-works.aspx`
- **level**: local (municipal)
- **access**: none
- **coverage**: region `["north_america","canada","british_columbia"]`; category
  `district_heating`; tags `["efficiency","planning"]`; policy_types
  `["program","report"]`; language `en`
- **format**: HTML + PDF (council reports, connectivity guidelines)
- **practical**: robots.txt not fetchable by our tooling (empty/blocked response),
  but pages load fully in-browser. Update cadence: council reports roughly
  annual, news items as expansions occur (most recent Oct 2025 energy-centre
  expansion).
- **effort tier**: (b) plain crawl domain
- **why worth adding**: City-owned-and-operated district energy utility whose
  primary energy source (70%) is literal waste-heat recovery (sewage heat via
  heat pumps) — a textbook match for the "thermal energy reuse" / "grid heat"
  taxonomy terms, with a public policy history (Southeast False Creek official
  development plan mandating low-carbon heat).
- **verified**: yes. Loaded via browser; page title "False Creek Neighbourhood
  Energy Utility (NEU) | City of Vancouver", confirms city ownership, sewage
  heat recovery mechanics, and links to connection requirements/rate documents.

---

### 4. Markham District Energy

- **name**: Markham District Energy Inc.
- **id**: `markham_district_energy`
- **base_url**: `https://www.markhamdistrictenergy.com`
- **start_paths**: `/news-events/mde-news/`, `/who-benefits/community/`
- **level**: local (municipally-owned corporation, wholly owned by the City of
  Markham, Ontario)
- **access**: none
- **coverage**: region `["north_america","canada","ontario"]`; category
  `district_heating`; tags `["efficiency","planning"]`; policy_types
  `["program","report"]`; language `en`
- **format**: HTML + PDF (annual "Year in Review" reports 2014-2020+)
- **practical**: `robots.txt` fetched cleanly — disallows only `/wp-admin/`,
  crawl-delay 10s, sitemap at `/wp-sitemap.xml`. WordPress site, no
  Playwright needed.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: Explicitly named in scope as notable, and for good
  reason — MDE retrofitted an Equinix data centre to supply heat recovery into
  its municipal thermal network, and is currently building "the world's largest
  wastewater energy transfer" facility (breaking ground 2024, operational 2026).
  Directly documents a live data-centre-to-district-heating pathway.
- **verified**: yes. Fetched root URL — official MDE site with news/projects
  section, community benefits pages, and annual reports confirmed present.

---

### 5. City of Toronto — District Energy

- **name**: City of Toronto — District Energy
- **id**: `toronto_district_energy`
- **base_url**: `https://www.toronto.ca`
- **start_paths**:
  `/services-payments/water-environment/environmentally-friendly-city-initiatives/district-energy/`
- **level**: local (municipal)
- **access**: none
- **coverage**: region `["north_america","canada","ontario"]`; category
  `district_heating`; tags `["efficiency","planning"]`; policy_types
  `["strategy","program"]`; language `en`
- **format**: HTML
- **practical**: `robots.txt` fetched cleanly — blocks only legacy `/legdocs/`
  committee-agenda paths and `/wp-admin/`, not the environment/district-energy
  section. Sitemap at `/sitemap.xml`.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: Official city policy page tying district energy to
  TransformTO (Toronto's climate action plan) with an explicit 2050 target (30%
  of floor space on low-carbon thermal networks) and direct reference to
  Enwave's Deep Lake Water Cooling system serving data centres as anchor loads.
- **verified**: yes. Fetched via WebFetch — confirms TransformTO linkage,
  description of the four existing Toronto district energy systems, and mention
  of data centres among connected building types.

---

### 6. NRC — National Energy Code of Canada for Buildings (Codes Canada)

- **name**: National Research Council Canada — National Energy Code of Canada
  for Buildings
- **id**: `nrc_codes_canada`
- **base_url**: `https://nrc.canada.ca`
- **start_paths**:
  `/en/certifications-evaluations-standards/codes-canada/codes-canada-publications`
- **level**: national (but the Code is adopted/enforced provincially — bridges
  federal standards work into subnational building/energy regulation, the same
  pattern already used for `oee.nrcan.gc.ca`)
- **access**: none (free PDF via NRC Publications Archive; print copies are paid)
- **coverage**: region `["north_america","canada"]`; category `standards`; tags
  `["efficiency","mandates"]`; policy_types `["standard"]`; language `en`/`fr`
- **format**: HTML (landing pages) + PDF (full code text, ~348 pages per edition)
- **practical**: robots.txt returned 404 to automated fetch (canada.ca-family
  sites vary by subdomain); page itself loads without a login wall.
  Publication cadence: every 5 years (2011, 2015, 2017, 2020, 2025 editions all
  listed).
  Note: `nrc.canada.ca` is a distinct base_url from the already-configured
  `natural-resources.canada.ca` and `oee.nrcan.gc.ca` — not a duplicate.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: The National Energy Code of Canada for Buildings is the
  baseline efficiency standard that every province references or adopts
  (directly relevant to Manitoba's and Nova Scotia's Tier-based code adoption
  noted below) — a `standard`-type policy_type source we're currently missing
  for Canada.
- **verified**: yes. Fetched via WebFetch — confirms live NRC page for the 2025
  edition with ISBN/catalogue metadata and free-PDF access via NRC Publications
  Archive.

---

### 7. Régie de l'énergie (Quebec energy regulator)

- **name**: Régie de l'énergie — Gouvernement du Québec
- **id**: `regie_energie_qc`
- **base_url**: `https://www.regie-energie.qc.ca`
- **start_paths**: `/fr`, `/fr/nouvelles/communiques`
- **level**: subnational (Quebec) — provincial utility regulator
- **access**: none
- **coverage**: region `["north_america","canada","quebec"]`; category
  `regulatory`; tags `["mandates","reporting","incentives"]`; policy_types
  `["regulation","report"]`; language `fr`
- **format**: HTML + PDF (decisions/"dossiers", numbered e.g. D-2022-061,
  R-4333-2026)
- **practical**: robots.txt not fetchable by our tooling (empty response), but
  the root page rendered fully via WebFetch. Decisions published on an ongoing
  basis (multiple per month across all dossiers).
- **effort tier**: (b) plain crawl domain
- **why worth adding**: Quebec's counterpart to Ontario Energy Board / BCUC —
  regulates Hydro-Québec and Énergir rates and has active dossiers on building
  heating decarbonization support (e.g., D-2022-061 approving a GHG-reduction
  rate mechanism for dual-energy heating, and 2025 rulings on renewable-gas
  connection mandates). Fills the Quebec-regulator gap; existing `quebec_energy`
  and `hydroquebec_ee` entries only cover the ministry/utility side, not the
  regulator.
- **verified**: yes. Fetched root URL — confirms decisions, dossiers (electricity/
  gas/petroleum), laws/regulations, and directives sections are live; a
  building-heat-decarbonization decision was independently confirmed via search
  (quebec.ca news release on D-2022-061).

---

### 8. Données Québec — Assemblée nationale du Québec, "Projets de loi" open dataset

- **name**: Données Québec — Projets de loi (Assemblée nationale du Québec)
- **id**: `donneesquebec_bills` (proposed; needs new client — see effort tier)
- **base_url**: `https://www.donneesquebec.ca`
- **source_type feasibility**: the portal runs on CKAN, which exposes a standard
  REST API (`/api/3/action/package_show?id=projets-de-loi`, etc.) — does not
  match any of the 9 existing clients (riksdagen, uk_bills, legisinfo, folketing,
  eurlex_nim, legiscan, govinfo, regulations_gov, dip). A generic CKAN client
  would also unlock other Données Québec datasets.
- **level**: subnational (Quebec) — legislature bill tracker with genuine open
  data (net-new; LEGISinfo is federal-only)
- **access**: none
- **coverage**: region `["north_america","canada","quebec"]`; category
  `legislative`; tags `["mandates"]`; policy_types `["legislation"]`; language `fr`
- **format**: CSV via the dataset page today; JSON available through the CKAN API
- **practical**: robots.txt not retrievable via our tooling; dataset metadata
  states "Fréquence de mise à jour: Temps réel" (real-time updates), last
  modified 2026-06-16 at time of check. License: CC-BY-NC 4.0 (attribution,
  non-commercial) — flag for legal review since it's more restrictive than the
  fully-open sources already in `api_sources.yaml`. Contact:
  donneesouvertes@assnat.qc.ca.
- **effort tier**: (c) needs a new structured client (generic CKAN action-API
  client); a plain crawl of the dataset page (tier b, CSV download only) is a
  viable fallback if a CKAN client isn't prioritized.
- **why worth adding**: Only genuinely open-data provincial bill tracker found
  in this pass — covers current + previous legislature, all sessions, in a
  structured, licensed, real-time-updated format. Directly answers the brief's
  call for "provincial legislature bill trackers with open data / APIs."
- **verified**: yes. Loaded dataset page via browser — confirms CSV resource,
  update frequency, license, and organization (Assemblée nationale du Québec).

---

### 9. Legislative Assembly of Ontario — All Bills

- **name**: Legislative Assembly of Ontario — Bills
- **id**: `ola_bills`
- **base_url**: `https://www.ola.org`
- **start_paths**: `/en/legislative-business/bills/all`,
  `/en/legislative-business/bills/current`
- **level**: subnational (Ontario) — legislature bill tracker
- **access**: none
- **coverage**: region `["north_america","canada","ontario"]`; category
  `legislative`; tags `["mandates"]`; policy_types `["legislation"]`; language `en`/`fr`
- **format**: HTML (no API/export found — see caveat below)
- **practical**: robots.txt fetched cleanly (Drupal site) — blocks admin/auth
  paths and Parliament-42 committee report pages, but not `/legislative-business/bills/*`.
  Crawl-delay not specified.
- **effort tier**: (b) plain crawl domain — **not** an open-data/API source
  despite the brief's preference; the "Data resources" page has moved/broken
  and no RSS/API was found on the bills pages themselves during this pass.
  Included anyway since it's Ontario's only bill tracker and the largest
  data-centre-market province currently has no legislative-bills coverage in
  `canada.yaml`.
- **why worth adding**: Fills the Ontario provincial-legislation gap (current
  `ontario_energy`/`oeb_ca`/`ieso_ca` entries are all executive-branch, not
  legislative) — bills like energy/climate acts would surface here before
  reaching regulation stage.
- **verified**: yes. Loaded via WebFetch — confirms "All bills" page listing
  sessions from the 36th Parliament (1995) to the current 44th, live and
  publicly accessible.

---

### 10. Manitoba — Energy Efficiency / Green Building Policy

- **name**: Government of Manitoba — Energy Efficiency (Environment, Climate and
  Parks)
- **id**: `manitoba_energy`
- **base_url**: `https://www.gov.mb.ca`
- **start_paths**: `/sd/environment_and_biodiversity/energy/green_bldg.html`,
  `/sd/environment_and_biodiversity/energy/incentives.html`
- **level**: subnational (Manitoba) — provincial ministry (first Manitoba entry
  in `canada.yaml`)
- **access**: none
- **coverage**: region `["north_america","canada","manitoba"]`; category
  `energy_ministry`; tags `["efficiency","incentives"]`; policy_types
  `["regulation","program"]`; language `en`
- **format**: HTML
- **practical**: robots.txt fetched cleanly — blocks unrelated department
  sub-pages (labour, expense reports, etc.), not the energy section.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: Rounds out provincial coverage per the brief's "etc." —
  documents the Energy Savings Act (retrofit financing), a Green Building Policy
  requiring LEED Silver on government-funded projects, and North America's
  highest gas-furnace-efficiency standard (92%), plus Manitoba Hydro industrial
  waste-heat/bioenergy incentive programs referenced from this page.
- **verified**: yes. Fetched via WebFetch — confirms live Manitoba government
  page with the programs described above.

---

## Unverified / needs-human-check

- **Nova Scotia Department of Energy** (`https://novascotia.ca` → redirects to
  `energy.novascotia.ca`) — the department root page loaded fine in-browser
  (confirms legislation/programs/news sections exist), but the specific
  efficiency-and-conservation sub-page
  (`energy.novascotia.ca/energy-efficiency/efficiency-and-conservation`)
  returned **"Access denied"** to both WebFetch and the browser session —
  likely bot-detection (Cloudflare or similar) on that subdomain rather than a
  real 404. Needs a human (or Playwright with a real browser fingerprint) to
  confirm the efficiency content is reachable before proposing start_paths.
  Nova Scotia's own content is also thinner on data-centre/waste-heat specifics
  than the verified candidates above (general energy-department scope, plus a
  2024-announced move to Tier 3 national building energy code by 2027-2029).

- **NRCan CanmetENERGY — district energy & waste-heat-source-mapping research**
  (`https://natural-resources.canada.ca/science-data/science-research/research-centres/cost-effective-large-scale-district-energy-thermal-storage-systems-flexible-resilient-energy-efficient-communities-0`) —
  verified live and highly on-topic (explicitly targets "heat rejected from
  building cooling and refrigeration systems in facilities such as data
  centers" for a 2023-2028 district-energy mapping project), **but** its
  `base_url` (`natural-resources.canada.ca`) is already used by the existing
  `nrcan_ca` domain entry in `canada.yaml`. Recommend appending this path to
  `nrcan_ca.start_paths` rather than creating a new domain entry — flagging
  here instead of listing as a duplicate candidate.

---

## Summary of what's net-new vs. recommended edits

- 9 new crawl-domain candidates (tier b) + 1 tier-c API candidate, all distinct
  `base_url`s from the 13 existing Canada entries and the 1 existing Canada API
  entry (legisinfo_api).
- 1 recommended edit to an existing entry (`nrcan_ca` — add a CanmetENERGY
  start_path), not counted as a new source.
- 1 flagged-but-unverified ministry (Nova Scotia) pending a bot-detection
  workaround.
