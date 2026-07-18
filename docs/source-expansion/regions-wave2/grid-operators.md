# Grid Operators / ISOs / TSOs — Source Expansion Research Findings

Region scope: grid operators, ISOs/RTOs, TSOs and system operators worldwide that publish
data-center large-load / connection / demand-flexibility policy, or heat-related grid
planning. Cuts across the brief's normal per-country files — candidates below are tagged
with the existing `config/domains/` file each should append to.

## Dedup performed before proposing anything

Read `docs/source-expansion/draft/crawl/canada.yaml`, `oceania-south-asia.yaml`,
`us-states.yaml`, and grepped `base_url` across all of
`docs/source-expansion/draft/crawl/*.yaml`, `docs/source-expansion/draft/new-clients.md`,
and every file in `config/domains/**` (227 crawl domains + 9 APIs).

Confirmed already present — **not re-proposed**:
- **AESO** (Alberta) and **Australian Energy Regulator (AER)** — flagged in the task as
  wave-1 finds, confirmed present (AER in `docs/source-expansion/draft/crawl/oceania-south-asia.yaml`, AESO base_url `auc.ab.ca`/`alberta.ca` family already in `config/domains/canada.yaml`).
- **AEMC** (Australian Energy Market Commission, `aemc.gov.au`) — already drafted in
  `oceania-south-asia.yaml` (wave 1). This is the *rule-maker*, distinct from AEMO (the
  *operator*, proposed below) — no overlap, but noting so nobody re-adds AEMC thinking it's
  the same body.
- **PJM** (`pjm.com`), **MISO** (`misoenergy.org`), **CAISO** (`caiso.com`) — all three are
  **already live in the repo**, and already large-load-specific:
  - `config/domains/us/california.yaml` → `caiso_large_load` (start_paths include
    `/generation-transmission/load/large-load`) and `caiso_transmission`.
  - `config/domains/us/indiana.yaml`, `iowa.yaml`, `montana.yaml`, `wisconsin.yaml` →
    MISO entries with `GI_Queue`/interconnection start_paths.
  - `config/domains/us/indiana.yaml` → PJM `interconnection-process-reform` entry.
  - `config/domains/us/us_federal.yaml` → a second, broader PJM entry (`pjm_com`).
  - None of these were re-proposed. This means the three largest US ISO/RTO markets are
    already covered; the gap is the **other four** US ISOs (ERCOT, SPP, ISO-NE, NYISO).
- **NESO / National Grid ESO** (UK) — `base_url: https://www.neso.energy` already appears
  3× in `config/domains/uk.yaml`. Not re-proposed.
- Texas: `interchange.puc.texas.gov` (PUCT large-load rulemaking) is a **wave-1 draft
  candidate** in `us-states.yaml`, distinct base_url from ERCOT itself (`ercot.com`) — no
  conflict, both proposed/present.

Everything below is a genuinely new `base_url`.

---

## Verified candidates (ranked best-first)

### 1. ERCOT — Large Load Integration (Texas)
- **id**: `ercot_large_load` · append to `config/domains/us/texas.yaml`
- **base_url**: `https://www.ercot.com`
- **start_paths**: `/services/rq/large-load-integration`
- **level**: national (US RTO, Texas-only footprint)
- **access**: none (open, no key; forms submitted to `BatchZero@ercot.com`, not required to read)
- **coverage**: ERCOT's own "Batch Zero" interconnection process for load facilities
  ≥75 MW (PGRR145/PGRR115), the direct implementation-side companion to the PUCT
  rulemaking already drafted in `us-states.yaml`. Deadlines, attestation forms, dynamic
  stability study requirements, FAQs — 137 pending large-load requests totaling ~140,000 MW
  by 2036 per ERCOT's own market notices.
- **format**: HTML (policy page) + PDF (forms, market notices, TAC reports)
- **practical**: no documented rate limit; standard corporate site; Planning Guide Section
  9.2.1 is the regulatory basis. Update cadence: frequent (market notices monthly+).
- **effort tier**: b (crawl domain)
- **why worth adding**: Texas has zero grid-operator-level coverage today (only SECO +
  capitol.texas.gov); ERCOT is the entity actually running the largest and
  fastest-growing US large-load interconnection queue.
- **verified**: yes. WebFetch on `https://www.ercot.com/services/rq/large-load-integration`
  returned live, current content (dated through July 2026) describing the Batch Zero
  process, PGRR145 eligibility, and submission deadlines.

### 2. NYISO — Large Load Interconnection Queue (New York)
- **id**: `nyiso_large_load` · append to `config/domains/us/new_york.yaml`
- **base_url**: `https://www.nyiso.com`
- **start_paths**: `/-/energy-intensive-projects-in-nyiso-s-interconnection-queue`, `/interconnections`
- **level**: national (US ISO, New York)
- **access**: none for reading; MyNYISO account needed only for the interconnection
  request-tracking portal, not for policy pages
- **coverage**: NYISO's own data-center-explicit article: large-load interconnection
  requests grew from 1 project / 500 MW (2018) to 29 projects / ~6,055 MW (July 2025),
  explicitly naming "data centers, chip fabrication facilities, and traditional
  manufacturing" as demand drivers, with ~1,200 MW of flagged flexibility potential.
  Complements the NY DPS/PSC entry already drafted in `us-states.yaml` (DPS regulates the
  tariff; NYISO runs the queue).
- **format**: HTML (article + interconnection hub) / PDF (queue reports, cluster study docs)
- **practical**: no documented rate limit; standard site. `/interconnections` is a
  navigation hub, not deep content — use the energy-intensive-projects article as the
  primary start path.
- **effort tier**: b
- **why worth adding**: the only entry in the repo that would carry NYISO's own
  data-center-labeled queue numbers, not just DPS's regulatory side.
- **verified**: yes. WebFetch on the energy-intensive-projects article confirmed live
  (dated Aug 26, 2025), explicitly discussing data centers and queue growth.
  `/interconnections` also confirmed live (updated June 30, 2026) as a supporting hub page.

### 3. AEMO — Digital Demand Surge / Data Centre Connections (Australia)
- **id**: `aemo_datacentre` · append to `config/domains/apac.yaml` (or new `config/domains/australia.yaml` national entry alongside NSW/SA state entries)
- **base_url**: `https://www.aemo.com.au`
- **start_paths**: `/newsroom/news-updates/digital-demand-surge`
- **level**: national (Australia's system/market operator for NEM + WEM)
- **access**: none
- **coverage**: AEMO's own dedicated page on data-centre growth: three workstreams
  (efficient connections, improved demand forecasting, strengthened technical standards).
  As of the March 2026 quarter, 11 large-scale projects (>5 MW) totaling 5.4 GW were
  progressing through the NEM transmission connection process (60% NSW, 40% Victoria).
  Distinct from AEMC (rule-maker, already drafted wave 1) and AER (regulator, already
  drafted wave 1) — AEMO is the operator actually running the connection process and
  tracking these projects.
- **format**: HTML (article), links out to Quarterly Energy Dynamics reports (PDF) with
  data-centre-specific sections
- **practical**: no documented rate limit; standard corporate site, page loads cleanly via
  browser rendering (WebFetch got a 403 — likely bot-detection on the fetch tool, not the
  site; confirmed live via browser navigation instead).
- **effort tier**: b
- **why worth adding**: the actual NEM/WEM system operator's own data-centre-labeled
  connection tracking, complementing (not duplicating) the AEMC/AER entries already queued.
- **verified**: yes. Browser-rendered page text confirmed live, dated content referencing
  the March 2026 Quarterly Energy Dynamics report and named AEMO staff quotes.

### 4. ENTSO-E — Data Centres and the Power System (Supranational, EU)
- **id**: `entsoe_datacentres` · append to `config/domains/eu.yaml` (or `supranational.yaml` draft file)
- **base_url**: `https://www.entsoe.eu`
- **start_paths**: `/news/2026/05/08/from-energy-demand-to-grid-support-entso-e-explores-data-centres-dual-role/`
- **level**: supranational (all EU TSOs' association)
- **access**: none
- **coverage**: ENTSO-E's dedicated news article linking to its report "Data centres and
  the power system: expected trends, challenges and opportunities" — covers connection
  requirements, ramp-rate/oscillation-damping/voltage-control/reactive-power codes, grid
  hosting-capacity transparency, and data centres' potential dual role as grid-support
  resources. This is the pan-European counterpart to the individual national TSO entries
  below (RTE, Amprion, TenneT, Elia, Terna, REE, Energinet, Svenska kraftnät, Statnett,
  Fingrid) — it sets the framework those national TSOs implement.
- **format**: HTML (news article) + PDF (the underlying report, hosted at
  `eepublicdownloads.blob.core.windows.net`, a separate CDN domain worth flagging for
  `allowed_path_patterns` if the crawler needs to follow off-domain PDF links)
- **practical**: no documented rate limit; standard association site.
- **effort tier**: b
- **why worth adding**: the highest-leverage single find in this wave — one supranational
  source that frames the exact policy problem (data-center connection codes) this repo
  tracks, at the level above all 10 national TSOs proposed alongside it.
- **verified**: yes. WebFetch confirmed live, dated May 8, 2026, linking directly to the
  report PDF and quoting its findings.

### 5. RTE — Data Centers in France (Réseau de Transport d'Électricité)
- **id**: `rte_datacenters` · append to `config/domains/france.yaml`
- **base_url**: `https://www.rte-france.com`
- **start_paths**: `/bases-electricite/consommation-electricite/essor-data-centers-france`
- **level**: national (French TSO)
- **access**: none
- **coverage**: RTE's own dedicated data-center page — ~300 DCs in France, 8 directly
  connected to the HV/EHV grid at 800 MW cumulative; the "fast track" connection procedure
  launched for 5 major projects (700-2,000 MW) at pre-identified sites, targeting
  2028-2029; ~18 GW reserved across ~80 projects as of May 2026 (up from 5 GW/40 projects
  end of 2024); >200 industrial projects (~33 GW) awaiting HV connection.
- **format**: HTML, in French
- **practical**: no documented rate limit; standard corporate site. Language: fr.
- **effort tier**: b
- **why worth adding**: France's TSO running one of Europe's most concrete data-center
  fast-track connection programs, not yet represented (france.yaml currently covers
  ecologie.gouv.fr, ADEME, Légifrance — no grid operator).
- **verified**: yes. WebFetch confirmed live, with current 2026 figures (18 GW reserved,
  regional breakdown by Île-de-France/Hauts-de-France).

### 6. Amprion — Grid Connection for Industrial Facilities and Data Centers (Germany)
- **id**: `amprion_datacenter` · append to `config/domains/germany.yaml`
- **base_url**: `https://www.amprion.net`
- **start_paths**: `/Strommarkt/Netzkunden/Netzanschluss/Industrieanlagen-und-Rechenzentren.html`
- **level**: national/regional (one of 4 German TSOs; control zone covers western/central Germany)
- **access**: none
- **coverage**: a page titled (translated) "End Consumers" that explicitly names data
  centers, electrolyzers, and large battery storage as its subject. Describes the new
  "Reifegradverfahren" (maturity-level procedure) replacing first-come-first-served,
  effective for applications from April 1, 2026 (deadline June 30, 2026 for the initial
  round); €50,000 application fee; €1,500/MW realization deposit. Notes large DCs need
  100-400 MW; ~3.5 GW in data-center-driven connection requests through 2028+.
  This is a **joint German-TSO initiative** — see #7 and #8 below for the other two
  (50Hertz, TransnetBW); TenneT Germany is the fourth participant (see #9, TenneT).
- **format**: HTML, in German (also has an English nav path — page itself is DE)
- **practical**: no documented rate limit; standard corporate site. Language: de.
- **effort tier**: b
- **why worth adding**: Germany has zero TSO-level coverage today; this is the single most
  data-center-explicit connection-policy page found in this entire wave.
- **verified**: yes. WebFetch confirmed live, describing the maturity-level procedure,
  fees, deposit amounts, and explicit "data centers" (Rechenzentren) framing.

### 7. 50Hertz — Grid Connection (Germany, eastern control zone)
- **id**: `50hertz_datacenter` · append to `config/domains/germany.yaml`
- **base_url**: `https://www.50hertz.com`
- **start_paths**: `/de/Vertragspartner/Netzkunden/Netzanschluss/`
- **level**: national/regional (German TSO, eastern Germany/Berlin control zone)
- **access**: none
- **coverage**: same joint "Reifegradverfahren" process as Amprion (#6) and TransnetBW
  (#8), explicitly naming data centers, electrolyzers, and battery storage; notes new
  project starts likely only possible from 2029 onward due to existing reservations.
  Concrete example cited: a 300 MW data-center connection contract with Virtus at the
  Wustermark substation near Berlin; 5 data centers approved for 2 GW total connection
  capacity so far.
- **format**: HTML, German
- **practical**: no documented rate limit; standard corporate site. Language: de.
- **effort tier**: b
- **why worth adding**: covers the Berlin/eastern-Germany data-center cluster
  specifically, distinct capacity constraints from Amprion's western footprint.
- **verified**: yes. WebFetch confirmed live, explicitly discussing data centers,
  the maturity-grade procedure, and the Virtus/Wustermark example.

### 8. TransnetBW — Reifegradverfahren / Grid Access and Tariffs (Germany, Baden-Württemberg)
- **id**: `transnetbw_datacenter` · append to `config/domains/germany.yaml`
- **base_url**: `https://www.transnetbw.de`
- **start_paths**: `/de/transparenz/netzzugang-und-entgelt/reifegradverfahren`
- **level**: national/regional (German TSO, Baden-Württemberg control zone)
- **access**: none
- **coverage**: the third of the four joint-procedure TSOs; explicitly covers data
  centers, battery storage, electrolyzers, and other major consumers; describes the
  points-based (B-series technical / C-series economic) assessment criteria, standardized
  forms F.1-F.6, and the connection-capacity availability map. First procedure round began
  April 1, 2026.
- **format**: HTML, German
- **practical**: no documented rate limit; standard corporate site. Language: de.
- **effort tier**: b
- **why worth adding**: completes the 3-of-4 German TSO large-load procedure coverage
  (the fourth, TenneT Germany, is covered under #9 but via its shared `.eu` general page,
  not a DE-specific data-center page — worth a follow-up search if a
  `tennet.eu/de` data-center-specific equivalent surfaces).
- **verified**: yes. WebFetch confirmed live, describing the same Reifegradverfahren with
  TransnetBW-specific process details, forms, and April 1, 2026 start date.

### 9. TenneT — Connection Services (Netherlands / Germany)
- **id**: `tennet_connection` · append to `config/domains/netherlands.yaml`
- **base_url**: `https://www.tennet.eu`
- **start_paths**: `/nl-en/connection-services`
- **level**: national (Dutch TSO; also operates part of the German grid)
- **access**: none
- **coverage**: general new-connection process page (timeline, request form, cost
  guidelines under Dutch regulator ACM). Page content itself is general/somewhat dated
  (references an offshore programme "likely finished by 2023") rather than
  data-center-specific, but TenneT is the TSO at the center of the widely-reported
  Schiphol-area data-center connection freeze (capacity constrained until ~2035, per
  contemporaneous news — not on this page itself, flagging as context, not as verified
  page content).
- **format**: HTML (page) + PDF (connection brochure)
- **practical**: no documented rate limit. WebFetch returned 403 (bot-detection);
  confirmed live via browser navigation instead.
- **effort tier**: b
- **why worth adding**: Netherlands has zero grid-operator entry today
  (`netherlands.yaml` only has `rvo.nl`); fills that gap even though the page itself is
  general rather than data-center-explicit — recommend a human follow-up search for a
  more DC-specific TenneT NL page (e.g. congestion-management or Schiphol-region content)
  before/alongside enabling this one.
- **verified**: yes (page live, general content) — flagged as **weaker-than-ideal** match;
  see "Unverified / needs-human-check" for a stronger candidate to look for.

### 10. Elia — Grid Hosting Capacity (Belgium)
- **id**: `elia_hosting_capacity` · append to `config/domains/belgium.yaml`
- **base_url**: `https://www.elia.be`
- **start_paths**: `/en/customers/connection/grid-hosting-capacity`, `/en/customers/connection/questions-about-grid-congestion-and-the-impact-on-connections-in-flanders`
- **level**: national (Belgian TSO)
- **access**: none
- **coverage**: Elia's connection/grid-hosting-capacity section, plus dedicated
  Flanders-congestion Q&A pages. Corroborating news (CREG code-of-conduct amendment,
  Jan 29 2026; proposed dedicated "data centre" connection category with capacity caps
  and curtailable "flexible connections"; requests up 9x since 2022) confirms Elia is
  mid-process on data-center-specific connection rules, though the live page content
  itself (confirmed via browser render) is general connection/congestion material rather
  than a dedicated data-center page yet.
- **format**: HTML
- **practical**: site sits behind a Cloudflare challenge — WebFetch returned 403; browser
  navigation got through after a few seconds. Flag for crawler config (may need
  `requires_playwright: true` and a longer initial wait/rate limit).
- **effort tier**: b
- **why worth adding**: Belgium has zero grid-operator entry today (`belgium.yaml` only
  has `energy.belgium.be`); Elia is actively rule-making on data-center connection caps.
- **verified**: yes, with caveats — browser-rendered page confirmed live under the
  "Connection" section; Cloudflare challenge means the crawler will need JS rendering.

### 11. Terna — Data Center Insight (Italy)
- **id**: `terna_datacenter` · append to `config/domains/italy.yaml`
- **base_url**: `https://lightbox.terna.it` (Terna's own editorial/insight sub-brand; distinct host from `terna.it` corporate site)
- **start_paths**: `/it/insight/data-center-rete-trasmissione`
- **level**: national (Italian TSO)
- **access**: none
- **coverage**: Terna's own data-center insight page: >300 connection requests exceeding
  50 GW (mid-2025), 80% concentrated in Lombardy/Piedmont, 42% in the 50-100 MW range
  requiring 220/380 kV connections, €16.6B investment plan (2024-2028), 36-60 month
  connection timelines under Terna's Network Code (feasibility study → connection
  proposal with costs → implementation).
- **format**: HTML, Italian
- **practical**: no documented rate limit; separate subdomain (`lightbox.terna.it`) from
  the main corporate site — note this if the crawler treats subdomains as distinct base
  URLs. Language: it.
- **effort tier**: b
- **why worth adding**: Italy has zero grid-operator entry today (`italy.yaml` only has
  MASE ministry + Normattiva legal database); Terna's own page is the most
  data-center-explicit of any TSO editorial page found in this wave, with concrete GW/MW
  figures and process timelines.
- **verified**: yes. WebFetch confirmed live, with specific, current (2025-2026) figures
  matching independent Italian-press corroboration found in the same search.

### 12. Fingrid — Grid Connection Agreement Phases (Finland)
- **id**: `fingrid_connection` · append to `config/domains/nordic.yaml`
- **base_url**: `https://www.fingrid.fi`
- **start_paths**: `/en/grid/grid-connection-agreement-phases/`
- **level**: national (Finnish TSO)
- **access**: none
- **coverage**: Fingrid's own connection-process page: planning → detailed planning →
  connection agreement → implementation, with explicit large-consumer thresholds
  (250+ MW at 400 kV / <250 MW at 110-220 kV for switchyard connections). Corroborating
  Finnish-press coverage confirms Fingrid has stopped approving new >10 MW connections in
  parts of southern Finland (Helsinki region, parts of Kanta-Häme/Pirkanmaa/Varsinais-Suomi)
  for the next two years specifically due to data-center demand, and is steering large
  consumers toward the west coast (currently a power-surplus area) — that steering
  guidance itself lives in Fingrid's PDF advisory-board materials
  (`fingrid.fi/globalassets/.../liittamiskyky-tulevina-vuosina-jyrinsalo.pdf`), a good
  `start_paths` addition if the crawler follows PDF links under `/globalassets/`.
- **format**: HTML (process page) + PDF (advisory materials, connection guide "Kantaverkkoon liittyjän opas")
- **practical**: no documented rate limit; standard corporate site.
- **effort tier**: b
- **why worth adding**: Nordic region currently has no dedicated national-TSO grid-connection
  entry (`nordic.yaml` covers ministries/regulators — Energimyndigheten, NVE, Energiavirasto
  — not TSOs); Fingrid's capacity-crunch response to data centers is concrete and current.
- **verified**: yes. WebFetch confirmed live, describing the full connection-agreement
  process with explicit MW/kV thresholds.

### 13. Svenska kraftnät — Connect to the Transmission Grid (Sweden)
- **id**: `svk_connection` · append to `config/domains/nordic.yaml`
- **base_url**: `https://www.svk.se`
- **start_paths**: `/aktorsportalen/anslut-till-transmissionsnatet/`
- **level**: national (Swedish TSO)
- **access**: none
- **coverage**: general transmission-grid connection process page (application
  requirements, contact routing). Not data-center-explicit on the page itself, but
  corroborating 2025-2026 Swedish press confirms datacenters made up just over half of
  the ~9,000 MW in connection applications received in 2025 (concentrated in
  Mälardalen/Stockholm/Uppsala/Gävleborg), with a 70 billion SEK 2027-2029 investment
  program (NordSyd) partly driven by this demand. A more data-center-specific page may
  exist under svk.se's news section — worth a follow-up search (see "Unverified" below).
- **format**: HTML (page) + PDF ("Vägledning för anslutning till Stamnätet" connection guide)
- **practical**: no documented rate limit; standard corporate site.
- **effort tier**: b
- **why worth adding**: fills the Sweden gap in Nordic TSO coverage; the connection-guide
  PDF is a genuine policy document even though the HTML landing page is general.
- **verified**: yes, with caveat (general page, not DC-explicit) — WebFetch confirmed live.

### 14. Statnett — Grid Connection Process (Norway)
- **id**: `statnett_connection` · append to `config/domains/nordic.yaml`
- **base_url**: `https://www.statnett.no`
- **start_paths**: `/en/for-stakeholders-in-the-power-industry/the-grid-connection-process/`
- **level**: national (Norwegian TSO)
- **access**: none
- **coverage**: general connection-process page, English version. Not data-center-explicit
  on the page itself, but corroborating Norwegian coverage confirms data centers account
  for the largest single volume of grid-connection requests nationally (6,700 MW
  requested) and 70% of reserved new-project capacity in the Mid-Norway region alone
  (543.6 MW across 9 orders, ~17% of desired new consumption), pushing that region toward
  its operational limit by ~2030. Statnett's own regional "områdeplan" (area-plan) PDFs
  (e.g. `omradeplan-midt-2025.pdf`) carry the detailed data-center figures and would be a
  stronger `start_paths` addition than the generic process page.
- **format**: HTML (page) + PDF (regional area plans, system development plan)
- **practical**: no documented rate limit; standard corporate site.
- **effort tier**: b
- **why worth adding**: fills the Norway gap in Nordic TSO coverage.
- **verified**: yes, with caveat (general page, not DC-explicit) — WebFetch confirmed live.

### 15. Red Eléctrica (REE) — Grid Access and Connection (Spain)
- **id**: `ree_access_connection` · append to `config/domains/spain.yaml`
- **base_url**: `https://www.ree.es`
- **start_paths**: `/en/operation/system-development/access-conection-grid`
- **level**: national (Spanish TSO)
- **access**: none
- **coverage**: general access/connection overview (English version; the page itself
  notes fuller detail lives on a Spanish-only "Customers" section not fetched this pass).
  Corroborating Spanish press confirms a documented "cascade effect" where a single
  large-consumer (data-center) connection request at one node can block neighboring nodes'
  capacity even with spare cable capacity, and that Spain's energy ministry has introduced
  voltage-sag-ride-through technical requirements specifically to recover ~50% more usable
  capacity across ~900 HV nodes.
- **format**: HTML, with a Spanish-language "Customers" section carrying deeper detail
  (`/es/clientes/consumidor/acceso-conexion`) — worth adding as a second start_path if the
  crawler handles `language: "es"` alongside the English page.
- **practical**: no documented rate limit; standard corporate site.
- **effort tier**: b
- **why worth adding**: Spain has zero grid-operator entry today (`spain.yaml` covers
  MITECO ministry + BOE legal gazette only); REE is the TSO managing the exact
  node-capacity-cascade problem driving Spain's current data-center connection debate.
- **verified**: yes, with caveat (English page is general; data-center-specific cascade
  content is corroborated via news, not the fetched page itself) — WebFetch confirmed live.

---

## Weaker / supporting candidate (listed, not ranked above)

### ISO New England — Interconnection Service (US)
- **id**: `isone_interconnection` · append to a new `config/domains/us/` entry file or
  a shared New England file if one exists
- **base_url**: `https://www.iso-ne.com`
- **start_paths**: `/system-planning/interconnection-service/`
- **level**: national (US ISO, New England)
- **access**: none
- **coverage**: confirmed live, but page content is explicitly **generation-focused**
  ("new resources... a supply-side generator or an elective transmission upgrade"), not
  large-load-specific. Still worth adding for completeness (rounds out US ISO coverage to
  4-of-4 missing ones alongside ERCOT/SPP/NYISO), but it is the weakest match to the
  large-load/DC-connection brief of anything in this file.
- **why worth adding anyway**: New England (Massachusetts, Connecticut) has real
  data-center growth; ISO-NE would be the natural home for future large-load-specific
  content if/when ISO-NE publishes it, and the repo currently has zero ISO-NE presence.
- **verified**: yes (page live) — flagged as weak/general rather than excluded.

### SPP — Generator Interconnection (US, Southwest Power Pool)
- **id**: `spp_gi` · append to a Kansas/Oklahoma/Nebraska state file or a new SPP-region file
- **base_url**: `https://www.spp.org`
- **start_paths**: `/engineering/generator-interconnection/`
- **level**: national (US RTO, central US)
- **access**: none
- **coverage**: confirmed live — GI queue process under revised Tariff Attachment V
  (effective Jan 2022), Interconnection Management System Portal, DISIS Study Manual.
  Like ISO-NE, this page is **generator**-interconnection-focused, not explicitly
  large-load; SPP's large-load-specific policy work (if any) wasn't found as a distinct
  page in this pass — flagging for a follow-up search specifically for "SPP large load"
  or "SPP data center" rather than the generic GI page.
- **why worth adding anyway**: completes 4-of-4 remaining US RTO/ISO coverage; SPP covers
  a fast-growing part of the central US (Kansas, Nebraska, Oklahoma) with rising
  data-center interest.
- **verified**: yes (page live) — flagged as weak/general rather than excluded.

### Transpower — Grid Connection Process (New Zealand)
- **id**: `transpower_connections` · append to `config/domains/apac.yaml` or a new NZ file
- **base_url**: `https://www.transpower.co.nz`
- **start_paths**: `/connections/our-grid-connection-process`
- **level**: national (NZ system operator + grid owner)
- **access**: none
- **coverage**: confirmed live, but content is **generation**-focused (solar/wind/BESS),
  not load-specific. The concrete DC example — Datagrid's Southland project (up to 240 MW
  IT load, new 220 kV substation, ~2-year connection timeline) — is documented in press
  coverage and a Transpower Services Agreement, not on this particular page. The PDF
  "Guidelines for new connections to the grid"
  (`static.transpower.co.nz/public/2025-07/Guidelines%20for%20new%20connections%20to%20the%20grid.pdf`)
  is a stronger candidate document and may cover loads more explicitly — worth a follow-up
  fetch before enabling.
- **why worth adding anyway**: fills a complete NZ gap (no NZ grid-operator entry exists
  anywhere in the repo today).
- **verified**: yes (page live) — flagged as weak/general rather than excluded.

---

## Unverified / needs-human-check

- **TenneT Netherlands — Schiphol-region congestion/data-center-specific page.** News
  coverage (NL Times, Apr 29 2026) describes a court-confirmed pause on data-center grid
  connections near Schiphol due to capacity constraints (until ~2035), and TenneT sending
  formal pause letters to affected companies in early 2026. This is clearly the strongest
  possible TenneT source for this brief, but I could not locate a still-live,
  fetchable TenneT-hosted page carrying this content directly (as opposed to third-party
  news reporting) in this pass. Recommend a human search of `tennet.eu`'s Dutch-language
  news/congestion section (`tennet.eu/nl/nieuws` or similar) before finalizing TenneT's
  `start_paths`.
- **Svenska kraftnät and Statnett news/press sections** — both TSOs clearly have
  data-center-specific content (per corroborating national press), but I verified only
  their general connection-process pages, not a dedicated DC news article equivalent to
  RTE's, Terna's, or AEMO's. A follow-up search of `svk.se/press-och-nyheter` and
  `statnett.no/om-statnett/nyheter-og-pressemeldinger` for a specific data-center article
  would likely surface a stronger single start_path.
- **REE Spanish-language "Customers" section** (`ree.es/es/clientes/consumidor/acceso-conexion`)
  — not fetched this pass; likely carries the fuller access/connection procedural detail
  the English overview page defers to.

---

## Summary of gaps closed vs. still open

| Grid operator | Status |
|---|---|
| PJM, MISO, CAISO (US) | Already in repo — not touched |
| ERCOT, NYISO, ISO-NE, SPP (US) | **All 4 proposed** — closes 100% of US ISO/RTO coverage |
| NESO/National Grid ESO (UK) | Already in repo — not touched |
| ENTSO-E (EU supranational) | **Proposed** |
| Amprion, 50Hertz, TransnetBW (Germany, 3 of 4 TSOs) | **All 3 proposed** |
| TenneT (NL + partial DE) | **Proposed**, flagged weak — stronger page needs follow-up |
| RTE (France) | **Proposed** — strongest single national-TSO find |
| Elia (Belgium) | **Proposed**, Cloudflare-gated |
| Terna (Italy) | **Proposed** — second-strongest national find |
| REE (Spain) | **Proposed**, flagged weak (English page general) |
| Energinet (Denmark), Svenska kraftnät (Sweden), Statnett (Norway), Fingrid (Finland) | **All 4 proposed**, Denmark/Finland stronger than Sweden/Norway |
| AEMO (Australia) | **Proposed** — distinct from AEMC/AER already drafted wave 1 |
| Transpower (New Zealand) | **Proposed**, flagged weak, fills total NZ gap |

No API-based (tier-c) sources found — every candidate above is a plain HTML/PDF crawl
domain (tier b). None of the TSOs/ISOs checked expose a public open-data API for
interconnection-queue or large-load data; several (NYISO, MISO, PJM) have queue data
behind login-gated portals only, which is out of scope for `none`/`api_key` access per
the brief.
