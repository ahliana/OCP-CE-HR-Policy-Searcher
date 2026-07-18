# Wave 4: Data-Center Noise / Land-Use / Zoning — Research Findings

Region scope: US local/subnational, Europe (Netherlands, Germany, Ireland, Nordic), and APAC
(Singapore, Japan, Australia) government sources for data-center **noise ordinances**,
**zoning/land-use rules**, and **siting standards** — the dimension driving most current
community opposition to data centers, and increasingly bundling energy-efficiency, waste-heat,
and cooling-equipment conditions directly into the zoning text.

## Dedup performed

Grepped `base_url` across `config/domains/**/*.yaml` and `docs/source-expansion/draft/crawl/**/*.yaml`
before researching. Confirmed already covered (skipped): Loudoun County VA (`loudoun.gov`),
Prince William County VA archived advisory group (`pwcva.gov` advisory-group path), Fairfax
County VA, Maricopa County AZ, City of Chandler AZ (Ordinance 5033), New Albany OH, Storey
County NV, Grant County PUD WA, Linn County IA, City of South Fulton GA, Frederick County MD,
Prince George's County MD, Morrow County OR (all wave-2 `us-local.yaml`); Noord-Holland,
Eindhoven, Den Haag, Rotterdam, Rijksoverheid (NL); London GLA, Leeds, Bristol, Greater
Manchester (UK — all district-heating documents, not zoning); Helsinki/Helen, Oslo, VEKS,
Stockholm, Copenhagen (Nordic — all district-heating/climate-strategy, not zoning); Frankfurt
`klimaschutz-frankfurt.de`, Munich, Cologne (DE — all municipal heat-planning, not zoning) (all
wave-3 `municipal-heat-zoning.yaml`). Every candidate below is a genuinely new `base_url`, or —
in three US Virginia cases sharing a county's root domain (Prince William, Loudoun-adjacent) —
a distinct document type/path not previously proposed.

## Verified candidates (ranked best-first)

### 1. Aurora, IL — "Gold Standard" Data Center & Warehouse Regulations
- **id**: `us_il_aurora` · new file `config/domains/us/illinois.yaml` (append; existing file
  only has ICC + ilga.gov)
- **base_url**: `https://www.aurora-il.org` (confirm exact host — agent verified via
  `aurora.il.us`; both resolve to the City of Aurora)
- **start_paths**: `/Property-Business/Zoning-and-Planning/New-Data-Center-and-Warehouse-Regulations`
- **level**: local (city)
- **access**: none
- **coverage**: Adopted March 25, 2026 via four ordinances (O26-021 through O26-024) after a
  180-day moratorium. All new data centers become conditional use requiring public hearing +
  Council approval. Bundles noise/vibration performance standards, energy limits (modular
  nuclear prohibited), water-use limits (evaporative cooling prohibited), an on-site renewable
  requirement (25% of peak load) or battery storage (50% of peak load / 15 min), and annual
  energy/water/noise reporting plus continuous vibration monitoring.
- **format**: HTML (hub page) + linked PDFs (ordinance text, FAQ, task-force presentations)
- **language**: en
- **practical**: no documented rate limit; standard CivicPlus-style municipal site. WebFetch
  returned 403 on this domain; browser-tool fetch succeeded cleanly.
- **effort tier**: b
- **why worth adding**: the single most comprehensive quantified bundled (noise + zoning +
  energy + water) data-center ordinance found in this entire wave, adopted 2026.
- **verified**: yes. Browser-fetched directly (WebFetch 403'd, browser tool rendered the page).
  Confirmed page title, ordinance numbers, and the adoption narrative described above.

### 2. Haarlemmermeer (Netherlands) — Datacenterbeleid & Omgevingsplan
- **id**: `nl_haarlemmermeer_datacenters` · new entry, `config/domains/netherlands.yaml`
- **base_url**: `https://www.haarlemmermeergemeente.nl` (legal text mirrored at
  `https://lokaleregelgeving.overheid.nl/CVDR646404`)
- **start_paths**: `/omgevingsplan`, `/informeer-online/meer-grip-op-vestiging-datacenters`
- **level**: local (municipality)
- **access**: none
- **coverage**: Designates four data-center concentration areas (Polanenpark, Corneliahoeve,
  Schiphol-Rijk, Schiphol Trade Park) with hard MVA capacity caps (100/100/350/200), prohibits
  data centers outside those zones, mandates **PUE < 1.2** and the LEAP framework for 20-40%
  energy reduction, requires either a district-heating waste-heat connection or reserved space
  for future waste-heat delivery, and requires facilities over 80 MVA to build their own 150kV
  substation. Municipal cap of 750 MVA through 2030. This is the strongest single
  energy/PUE/heat-reuse bundle found in the whole Europe pass.
- **format**: HTML (CVDR legal text) + PDF (council decision documents)
- **language**: nl
- **practical**: no rate-limit info published; standard Dutch municipal site; policy under
  active revision (5th concentration area being added).
- **effort tier**: b
- **why worth adding**: Haarlemmermeer (Amsterdam Science Park / Schiphol area) is the largest
  data-center siting fight in the Netherlands and was not previously covered.
- **verified**: yes. Fetched CVDR646404 directly; quoted PUE<1.2 requirement, MVA caps, and
  waste-heat conditions verbatim from the live legal text.

### 3. Fort Worth, TX — Data Centers policy hub
- **id**: `us_tx_fort_worth` · append to `config/domains/us/texas.yaml`
- **base_url**: `https://www.fortworthtexas.gov`
- **start_paths**: `/departments/city-manager/datacenters`
- **level**: local (city)
- **access**: none
- **coverage**: Active rulemaking (Fort Worth's first data-center-specific ordinance proposal).
  Draft requires industrial zoning only, 250 ft residential setback, 50 ft landscape buffer,
  rooftop cooling equipment behind an acoustic barrier 1-1.5x equipment height, and bans
  cryptocurrency mining. Links directly to the Zoning Ordinance, Industrial Districts chapter,
  and city Noise Ordinance. Zoning Commission denied the draft 7-4 (~July 8, 2026); sent back to
  Council for an Aug. 4 work session / Aug. 11 final vote.
- **format**: HTML with linked PDFs (Council slides, FAQ)
- **language**: en
- **practical**: no rate limits documented; WebFetch 403'd, browser tool succeeded. Actively
  updated "Key Dates" timeline — good re-crawl candidate.
- **effort tier**: b
- **why worth adding**: only major DFW-metro city with a dedicated live regulatory hub bundling
  zoning + noise + water + economic-development threads.
- **verified**: yes. Browser-fetched; confirmed page title and full timeline/proposed-regulation
  links.

### 4. Prince William County, VA — CURRENT Data Center Opportunity Zone Overlay District (DCOZOD)
- **id**: `us_va_pwc_dcozod` · append to `config/domains/us/virginia.yaml` (distinct path from
  the already-covered archived advisory-group entry)
- **base_url**: `https://www.pwcva.gov`
- **start_paths**: `/department/planning-office/dpa2026-00006-data-center-opportunity-zone-overlay-district-dcozod`
- **level**: local (county)
- **access**: none
- **coverage**: Live Zoning Text Amendment (initiated March 3, 2026; re-initiated under
  Resolution 26-374, June 9, 2026) to shrink/redefine the Data Center Opportunity Zone Overlay
  District boundaries. Outside the Overlay, data centers in B-1, O(L)/O(H)/O(M)/O(F), M-1, M-2
  now require a Special Use Permit. Underlying codified Zoning Ordinance §32-509 sets a
  1.0-FAR bonus for in-district data centers. Planning Commission hearing scheduled July 15,
  2026. Distinct current/live document from the archived advisory-group page already in the
  repo (which only covers the disbanded 2023-2025 process).
- **format**: HTML (status page) + Municode ordinance text
  (`library.municode.com/va/prince_william_county` — CH32ZO_ARTVOVDI_PT509DACEOPZOOVDI)
- **language**: en
- **practical**: no rate limits documented; fetched cleanly, no WAF on this specific path.
- **effort tier**: b
- **why worth adding**: captures PWC's live, evolving overlay-district zoning text plus the
  codified ordinance section, not just the historical advisory-group record already tracked.
- **verified**: yes. WebFetch succeeded directly; confirmed as a current planning-initiative
  page (not archival) with the ZTA timeline and district list described above.

### 5. DeKalb County, GA — Data Center Text Amendment (Engage DeKalb)
- **id**: `us_ga_dekalb` · new entry, `config/domains/us/georgia.yaml`
- **base_url**: `https://engagedekalb.dekalbcountyga.gov`
- **start_paths**: `/data-center-text-amendment`
- **level**: local (county)
- **access**: none
- **coverage**: Board of Commissioners denied the draft Text Amendment June 23, 2026, but a
  data-center moratorium remains in force (extended through ~March 2027). The denied draft
  (kept as the working framework for redrafts) defines five size tiers, a 500 ft minimum
  setback from residential zones (750 ft from parks/trails), 20 ft landscaped buffers with 8 ft
  walls for large tiers, required closed-loop cooling, and noise assessments measured at both
  A-weighted and C-weighted frequencies — directly bundling cooling/energy conditions into the
  siting standard.
- **format**: HTML
- **language**: en
- **practical**: no rate limits documented; fetched cleanly, no WAF encountered.
- **effort tier**: b
- **why worth adding**: most detailed, quantified GA county-level draft standard found, distinct
  jurisdiction from the already-covered City of South Fulton, with an active moratorium keeping
  the topic live.
- **verified**: yes. WebFetch succeeded directly; standards list and contact confirmed on the
  live page.

### 6. Chesapeake, VA — Data Center Ordinance and Policy
- **id**: `us_va_chesapeake` · new entry, `config/domains/us/virginia.yaml` (locality section)
- **base_url**: `https://www.cityofchesapeake.net`
- **start_paths**: `/3783/Data-Center-Ordinance-and-Policy`
- **level**: local (city)
- **access**: none
- **coverage**: Council adopted an Initiating Resolution Jan 13, 2026; draft ordinance
  PLN-TXT-2026-001 / policy PLN-TXT-2026-002 would convert data centers from by-right to
  conditional-use in industrial districts and the Fentress Airfield Overlay District. Planning
  Commission voted 9-0 to recommend approval July 9, 2026. Reported (secondary-sourced) 500 ft
  structure setback / 100 ft property-line setback from residential.
- **format**: HTML with linked draft-ordinance PDFs
- **language**: en
- **practical**: no rate limits documented; official page fetched cleanly. Some linked news
  mirrors (wavy.com) 403'd — use the .gov page itself.
- **effort tier**: b
- **why worth adding**: only Hampton Roads/Peninsula jurisdiction with a fully live, official
  city-hosted docket page moving toward adoption in 2026.
- **verified**: yes. WebFetch succeeded directly; resolution dates, docket numbers, and
  zoning-district list confirmed from live page text.

### 7. Fauquier County, VA — Zoning Ordinance (PCID data-center provisions + noise standards)
- **id**: `us_va_fauquier` · new entry, `config/domains/us/virginia.yaml` (locality section)
- **base_url**: `https://www.fauquiercounty.gov`
- **start_paths**: `/government/departments-a-g/community-development/codes-ordinances/zoning-ordinance`
- **level**: local (county)
- **access**: none
- **coverage**: Live ordinance (amended through April 9, 2026). Data centers restricted to
  Business Park (BP) and Planned Commercial Industrial Development (PCID) districts (Article 4,
  Part 6). A 2024 zoning text amendment requires special-exception approval for any data-center
  building/assemblage over 50,000 sq ft in the PCID (Vint Hill), reviewed against
  "height, setback, noise, design and community compatibility." Ordinance separately contains
  Article 9, Part 7 (Noise Standards) and Part 8 (Earthborn Vibration Standards), applicable
  countywide including to data centers.
- **format**: HTML (ordinance hub, links to full PDF chapters)
- **language**: en
- **practical**: WebFetch returned 403 (WAF-like block); browser tool succeeded. Periodic
  amendment updates — good re-crawl candidate.
- **effort tier**: b
- **why worth adding**: live ordinance text for one of Virginia's most-cited "strictest"
  data-center zoning regimes, with dedicated noise/vibration performance-standard articles.
- **verified**: yes. Browser-fetched (WebFetch blocked with 403); Article/Part table of
  contents confirmed live.

### 8. Stafford County, VA — Data Center Applications / Regulations
- **id**: `us_va_stafford` · new entry, `config/domains/us/virginia.yaml` (locality section)
- **base_url**: `https://www.staffordcountyva.gov`
- **start_paths**: `/government/departments_p-z/planning_and_zoning/data_centers/index.php`
- **level**: local (county)
- **access**: none
- **coverage**: Ordinance O23-24 (Oct. 2023) added data-center definitions/regulations to County
  Code §§28-25, 28-35, 28-39 (original: 100 ft setback within Urban Service Areas / 200 ft
  outside, 50 ft vegetated buffer). Ordinance O25-29 / O25-29(R) (Oct-Dec 2025) tightened this:
  residential setback raised 100→500 ft, vegetative buffer 50→200 ft, with grandfathering for
  five named projects. Also covers noise mitigation, security fencing, tree preservation.
- **format**: HTML
- **language**: en
- **practical**: fetched cleanly, no blocking, no documented rate limits.
- **effort tier**: b
- **why worth adding**: concrete, dated, numeric setback/buffer escalation with named
  grandfathered projects.
- **verified**: yes. WebFetch succeeded directly; ordinance numbers and setback figures
  confirmed from live page content.

### 9. Henrico County, VA — Data Center Design Guidelines / Technology Boulevard Overlay
- **id**: `us_va_henrico` · new entry, `config/domains/us/virginia.yaml` (locality section)
- **base_url**: `https://henrico.gov`
- **start_paths**: `/public-data/data-center-design-guidelines/`
- **level**: local (county)
- **access**: none
- **coverage**: June 10, 2025: Board of Supervisors adopted the "Data Center Comprehensive Plan
  Amendment" as an appendix to the Vision 2026 Comprehensive Plan, governing new data-center
  development countywide. A pending "Technology Boulevard Special Focus Area" overlay
  (~3,100 acres around White Oak Technology Park) would be the only area where data centers can
  be built without a provisional-use permit/public hearing; Planning Commission recommended
  approval May 15, 2025.
- **format**: HTML landing page + linked PDF (full Comprehensive Plan Amendment text)
- **language**: en
- **practical**: fetched cleanly via browser, no WAF issue, no documented rate limits.
- **effort tier**: b
- **why worth adding**: confirms an adopted (not just proposed) comprehensive-plan-level policy
  plus tracks the pending White Oak overlay — a Richmond-metro locality not yet covered.
- **verified**: yes. Browser-fetched; page confirmed with adoption date and content described
  above.

### 10. Culpeper County, VA — Planning & Zoning / Culpeper Technology Zone
- **id**: `us_va_culpeper` · new entry, `config/domains/us/virginia.yaml` (locality section)
- **base_url**: `https://web.culpepercounty.gov`
- **start_paths**: `/planning`
- **level**: local (county)
- **access**: none
- **coverage**: Hosts the "03.2025 Updated Culpeper Technology Zone.pdf" plus the current Zoning
  and Subdivision Ordinances. The Culpeper Tech Zone (CTZ) is a 690-acre by-right data-center
  district (Zoning Ordinance §7.1A-2-2.5, Light Industrial permitted use) capping individual
  developments at 300 MW with required own substations. A Planning Commission-advanced
  amendment would add a conditional-use-permit requirement outside the by-right tech zone.
- **format**: HTML hub page + linked PDFs
- **language**: en
- **practical**: WebFetch 403'd; browser tool succeeded; no documented rate limits.
- **effort tier**: b
- **why worth adding**: a notably different regulatory model (permissive by-right zone vs.
  restrictive overlay) worth contrasting with Loudoun/Prince William.
- **verified**: yes. Browser-fetched; confirmed live with the tech-zone PDF and Zoning
  Ordinance links.

### 11. Montgomery County, MD — ZTA 26-01 data-center zoning
- **id**: `us_md_montgomery` · new entry, `config/domains/us/maryland.yaml` (Frederick County is
  a different, already-covered MD county)
- **base_url**: `https://www.montgomerycountymd.gov`
- **start_paths**: `/mcgportalapps/Press_Detail.aspx?Item_ID=48105`,
  `/news/montgomery-county-executive-marc-elrich-signs-executive-order-temporarily-pause-data-center-permitting`
- **level**: local (county)
- **access**: none
- **coverage**: ZTA 26-01 (introduced Jan 20, 2026) would restrict data centers to industrial
  zones only (currently permitted countywide as "communications facilities"). Bundled
  provisions: 500 ft setback on sites abutting residential zoning, proof of noise-ordinance
  compliance, vegetative screening/lighting requirements, Tier-4-EPA-compliant low-emission
  diesel backup generators, environmentally-sensitive-area protections. County Executive Elrich
  separately signed a six-month moratorium on new data-center permit processing.
- **format**: HTML (press release + news/EO page)
- **language**: en
- **practical**: fetched cleanly, no documented rate limits.
- **effort tier**: b
- **why worth adding**: live legislative process bundling noise-ordinance compliance and a
  generator-emissions condition directly into zoning siting standards.
- **verified**: yes. WebFetch succeeded directly; ZTA number and setback/generator figures
  confirmed from live press-release text.

### 12. Inzai City, Chiba Prefecture (Japan) — District Plans (地区計画) data-center restriction
- **id**: `japan_inzai_district_plans` · new entry, `config/domains/apac.yaml` (or a new
  `japan.yaml` if the repo splits APAC by country elsewhere)
- **base_url**: `https://www.city.inzai.lg.jp`
- **start_paths**: `/0000000440.html` (district-plan index, 38 plans city-wide),
  `/0000019530.html` (2025 public-comment page on new station-area data-center rules)
- **level**: subnational (municipal, Chiba Prefecture)
- **access**: none
- **coverage**: The 武西学園台商業・業務施設地区地区計画 (Takenishi Gakuendai district plan) and its
  Operating Standards (rev. May 2024) explicitly list
  「事務所（データセンターの用に供するものに限る。）」— "offices limited to data center use" — as a
  prohibited building type in the Public Benefit Facility District (Category-2 Residential
  zoning), near Chiba New Town Chuo Station, a major DC-cluster station. Also specifies minimum
  site area (400m²), wall setbacks (5m/2m/1m by frontage), building-color/design standards, and
  hedge/fence height limits (2m max). This is the concrete municipal mechanism behind Inzai's
  2025 city-council move to restrict new data-center construction near stations.
- **format**: HTML (index) + PDF (individual plan documents)
- **language**: ja
- **practical**: municipal static site, no blocking observed, low request volume; district
  plans amended a few times a year — monthly re-crawl of the index is sufficient.
- **effort tier**: b
- **why worth adding**: a rare primary government document naming data centers as a specific
  restricted land-use category tied to a residential zone — exactly the DC-zoning angle this
  wave targets, and currently live (city considering city-wide expansion).
- **verified**: yes. Fetched both PDFs directly and read the Japanese text (not just the URL);
  confirmed the data-center clause and all numeric standards above. Also fetched
  `0000019530.html` directly, confirming the 2025 public-comment process.

### 13. Singapore — URA Development Control Handbook, B1 Allowable Uses (Data Centres)
- **id**: `singapore_ura_b1_data_centres` · new entry, `config/domains/apac.yaml`
- **base_url**: `https://www.ura.gov.sg`
- **start_paths**: `/guidelines/development-control/development-control-handbooks/non-residential/b1/allowable-uses/`,
  `/Corporate/Guidelines/Development-Control`
- **level**: national
- **access**: none
- **coverage**: Data centres/data farms are classified as an industrial "e-business" use
  permitted within the 60% predominant-use quantum in Business Park, B1, and B2 zoned
  developments. Data centres require prior planning permission with technical-agency
  consultation (NEA, PUB, SCDF, LTA) before URA approves the use — case-by-case siting review,
  not automatic like other e-business uses. Page also gives URA's operative definition of
  "data centre."
- **format**: HTML
- **language**: en
- **practical**: static gazetted-guideline pages, no blocking observed; content tied to Master
  Plan review cycles (~5 years) with occasional circular updates — quarterly re-check
  sufficient.
- **effort tier**: b
- **why worth adding**: the URA zoning-authority angle (which zones permit DCs and the extra
  approval hurdle they face), distinct from IMDA's national DC moratorium/sustainability policy.
- **verified**: yes. Fetched directly; confirmed the B1/B2 allowable-use table entry, the
  prior-planning-permission requirement, and the technical-agency consultation language.

### 14. Frankfurt am Main (Germany) — Steuerung von Rechenzentren (data-center zoning concept)
- **id**: `de_frankfurt_rechenzentrenkonzept` · new entry, `config/domains/germany.yaml`
  (distinct document type from the already-covered `klimaschutz-frankfurt.de` heat-planning
  entry)
- **base_url**: `https://www.stadtplanungsamt-frankfurt.de`
- **start_paths**: `/steuerung_von_rechenzentren_22137.html`
- **level**: local (municipality)
- **access**: none
- **coverage**: City council-adopted (June 9, 2022) Data Center Concept classifying industrial
  areas into suitable/restricted/exclusion zones for independent data centers (suitable:
  Sossenheim, Rödelheim, Griesheim, Gallus, Ostend, Fechenheim, Seckbach). States that binding
  land-use plans (Bebauungspläne) will progressively implement these zones. Commits to a
  citywide waste-heat (Abwärme) feasibility study for DC heat reuse and future
  urban-quality/climate/resource-consumption guidelines. No parcel-specific Bebauungsplan
  number is published yet (see Unverified section).
- **format**: HTML
- **language**: de
- **practical**: fetched cleanly, no documented rate limits.
- **effort tier**: b
- **why worth adding**: the genuine site-steering/zoning document requested for Germany —
  distinct in both domain and document type from Frankfurt's existing municipal heat-planning
  entry.
- **verified**: yes. Fetched directly; zone classifications and binding-plan-implementation
  language quoted from the live page.

### 15. Fingal County Development Plan — Chapter 13 Land Use Zoning (Ireland)
- **id**: `ie_fingal_cdp_ch13_zoning` · new entry, `config/domains/ireland.yaml`
- **base_url**: `https://consult.fingal.ie`
- **start_paths**: `/en/consultation/draft-fingal-county-development-plan-2023-2029/chapter/chapter-13-land-use-zoning`
- **level**: local (county)
- **access**: none
- **coverage**: Data centres are explicitly listed as "Not Permitted" in the High Technology
  (HT) zoning matrix, as well as in Local Centre, General Employment, and High Amenity zones —
  despite HT lands historically hosting established data centres. Documents Ireland's
  zoning-level exclusion approach, a useful counterpoint to South Dublin's conditional-permit
  approach (see Unverified section).
- **format**: HTML
- **language**: en
- **practical**: fetched cleanly, no documented rate limits.
- **effort tier**: b
- **why worth adding**: concrete documentary evidence of a zoning-level data-center prohibition
  in one of Ireland's most DC-dense counties.
- **verified**: yes. Fetched directly; confirmed "Data Centre" listed under "Not Permitted" in
  the HT-zone use matrix.

### 16. Varde Kommune (Denmark) — Microsoft data-center lokalplan process
- **id**: `dk_varde_datacenterprojekter` · new entry, `config/domains/nordic.yaml` or a new
  `denmark.yaml`
- **base_url**: `https://www.vardekommune.dk`
- **start_paths**: `/borger/bolig-og-byggeri/datacenterprojekter/microsoft-ansoegninger-til-datacentre-2/`
- **level**: local (municipality)
- **access**: none
- **coverage**: Council decision (June 24, 2026) to initiate lokalplan + kommuneplantillæg work
  for two Microsoft data-center sites (Tinghøj and Lunde). Siting criteria explicitly listed:
  grid access/energy capacity, security/risk profile, fiber connectivity, zoned-land
  sufficiency, skilled-labour access. Links application-update PDFs and a Code of Conduct
  document.
- **format**: HTML + PDF (application docs, hearing responses)
- **language**: da
- **practical**: fetched cleanly, no documented rate limits.
- **effort tier**: b
- **why worth adding**: Denmark had zero zoning/lokalplan entries in existing coverage; a live,
  actively-updated planning process for two hyperscale sites.
- **verified**: yes. Fetched directly; siting-criteria language quoted from the live page.

### 17. Kouvola (Finland) — Lossitie asemakaava (atNorth data-center site)
- **id**: `fi_kouvola_lossitie_asemakaava` · new entry, `config/domains/nordic.yaml`
- **base_url**: `https://www.kouvola.fi`
- **start_paths**: `/asuminen-ja-ymparisto/kaavoitus-ja-kaupunkisuunnittelu/ajankohtaiset-asemakaavat/lossitie/`
- **level**: local (municipality)
- **access**: none
- **coverage**: Site-specific detailed zoning plan (asemakaava 35/003) for ~35.3 ha in
  Ummeljoki/Myllykoski, rezoning land to industrial/storage/business use for atNorth's FIN04A
  data-center campus (legally valid since March 9, 2026). Includes a riparian buffer
  requirement along the Kymijoki river. Linked kaavaselostus (plan description) and
  cultural-landscape assessment. Noise/PUE/waste-heat specifics were not visible on the summary
  page itself — flagged for a follow-up read of the linked PDF.
- **format**: HTML (landing page) + PDF (kaavaselostus, kaavakartta — not machine-readable via
  WebFetch this pass)
- **language**: fi
- **practical**: fetched cleanly, no documented rate limits.
- **effort tier**: b
- **why worth adding**: a genuine site-specific municipal asemakaava for a named hyperscale DC
  campus — a distinct document type from the Nordic district-heating entries already covered.
- **verified**: yes, for existence/process/siting (landing page fetched directly). The linked
  kaavaselostus PDF did not render readable text — noise/energy specifics inside it are
  unconfirmed; recommend a human/OCR follow-up before treating those as sourced.

## Unverified / needs-human-check

- **Coweta County, GA data-center ordinance + June 2026 moratorium** — well corroborated by news
  (Times-Herald, GPB, AJC: light-industrial-vs-industrial-only siting, noise, buffers, on-site
  power generation, community-meeting requirements), but `coweta.ga.us/government/government/planning-development-ordinances`
  and `/departments/community-development/community-planning` both 404'd live (root domain
  loads fine). Needs a human to find the reorganized correct path, or use the Municode mirror
  `library.municode.com/ga/coweta_county`.
- **James City County, VA — Ordinance 31A-364** (data centers limited to industrial districts,
  setbacks/design standards/size limits/buffers/water-energy review, adopted ~Sept 9, 2025) —
  the county PDF downloaded (81KB, real file) but is an image-scanned PDF with no extractable
  text; standards above are secondary-sourced (WHRO, WyDaily) only. Recommend OCR or the
  Municode-hosted version (`library.municode.com/va/james_city_county`).
- **York County, VA — ZT-200-24** (data-center definition, noise limits reported as
  55 dBA/65 dBC, setbacks/buffers, energy/water letters-of-service) — the official DocumentCenter
  PDF downloaded (627KB, real file) but is image-scanned, not text-extractable; figures are
  secondary-sourced (Williamsburg Independent) only. Note: `yorkcounty.gov/185/Zoning` itself
  does not mention data centers — content lives only in DocumentCenter PDFs.
- **Tucson, AZ — "Data Center Code Update" Planning Commission memo** (Sept 17, 2025) — WebFetch
  403'd; browser tool triggered a forced-download prompt then an unrelated redirect anomaly.
  Could not confirm content; needs a manual download-and-read pass.
- **Elk Grove Village, IL — Chapter 10 (Noise Control)** applying IL Pollution Control Board
  Title 35 Subtitle H sound-emission standards to I-1/I-2 industrial districts where the
  village's ~20 existing + 19 pipeline data centers sit (per Daily Herald reporting) — the
  amlegal.com code host is "Under Revision" and redirects to `elkgrove.org` document IDs not
  yet fetched to confirm chapter text.
- **Not yet enacted / no ordinance exists (do not add as sources, tracked for future waves)**:
  Plano TX and Richardson TX (no DC zoning category or ordinance yet), Virginia Beach VA (DCs
  fall under generic warehousing use, only a CUP recommendation under consideration), Santa
  Clara CA and San Jose CA (project-level denials/guideline directives only, no enacted
  ordinance), DuPage County IL and Franklin Park IL (general zoning only, nothing
  data-center-specific found).
- **Chandler, AZ noise ordinance** — confirmed there is no separate noise-specific ordinance;
  the noise-mitigation regime (no increase over pre-construction baseline, mandatory
  third-party acoustic study, resident meetings) is written directly into the already-covered
  Ordinance No. 5033. Not a new candidate.
- **South Dublin County Development Plan — Policy EDE7** (steers data centres outside the M50,
  requires demonstrated energy efficiency and maximised on-site renewables "to ensure as far as
  possible 100% powered by renewable energy"; the council's 2022 attempted outright ban was
  overridden by a Ministerial Direction) — EDE7 text corroborated verbatim across multiple
  independent search snippets, but WebFetch could not render the actual Chapter 9 PDF, and the
  precise adopted-plan URL (vs. the draft-plan mirror at `consult.sdublincoco.ie`) was not
  confirmed. Recommend a human open the PDF directly before adding — likely the single
  highest-value Ireland candidate once confirmed, given South Dublin's central role in Ireland's
  DC moratorium fight.
- **Amsterdam paraplubestemmingsplan Datacenters + Vestigingsbeleid 2020-2030** — city-wide
  umbrella zoning plan (≥2000 m² floor area / ≥5 MVA connection triggers coverage), restricting
  new/expanded DCs to five clusters, capping growth at 670 MVA total, mandating annual renewable
  procurement and decoupled waste-heat reuse for home heating. The official gemeente Amsterdam
  page and the adopted-plan PDF title page were confirmed live, but the PDF body would not
  OCR through WebFetch — a human/PDF-parser pass would let this be promoted to fully verified.
- **Espoo (Finland) — Suosaari/Laajalahti data-center zoning amendment** (Equinix-owned parcel,
  asemakaava replacing a 1974 office building with 38,000 m² of DC building rights, city-council
  consideration from Oct 15, 2025) — existence, parcel, and operator details were corroborated
  via search-result synthesis, not a direct fetch of `espoo.fi`. Needs a human to open the
  project page and kaavaselostus directly.
- **Rollag kommune (Norway) — Numedal Næringspark detaljreguleringsplan** (plan ID 2026/001,
  referencing "utilization of excess heat and collaboration with energy-related actors") — the
  municipal notice page returned only header/title content via WebFetch, no body text; existence
  corroborated via a Laagendalsposten news article. Needs a human to pull the actual planprogram
  PDF.
- **Frankfurt parcel-level Bebauungsplan** — the Rechenzentrenkonzept (verified candidate #14
  above) is a citywide steering concept, not a named-parcel Bebauungsplan as originally sought.
  No adopted or draft B-Plan tied to a specific Frankfurt DC campus (e.g. FRA15/FRA17/MWH01) was
  found — those pages are developer marketing content, not municipal planning documents. A human
  should search Frankfurt's Bebauungsplan register directly by district (Fechenheim, Seckbach).
- **Singapore — BCA/IMDA Green Mark for Data Centres (GMDC:2024)** — scheme's existence, name,
  and joint BCA-IMDA administration corroborated by three independent sources (IMDA's own scheme
  page, SGBC's announcement, BCA's Green Mark hub), but the actual criteria PDF
  (`bca.gov.sg/.../20241008_gmdc2024_ver1.pdf`) 404'd on every attempt, including the
  `?sfvrsn=` variant. A reported PUE ceiling of ≤2.2 (measured at 25/50/75/100% IT load) is
  **not independently confirmed** — do not cite that figure until a human finds the live PDF
  (possibly via the `go.gov.sg/gmdc-nov24-es` short link).
- **NSW, Australia — Mamre Road Precinct Development Control Plan 2021** — confirmed to exist
  and to be actively applied to a live State Significant Development application (1.2 GW / 52 ha
  data-centre campus at 706-752 Mamre Rd), but every fetch of the DCP document itself returned
  only navigation shells, not text. Unclear whether it contains bespoke data-center clauses or
  only generic IN1 industrial-zone controls that happen to apply. A human should open the PDF
  via `planningportal.nsw.gov.au/MamreRd-DCP` to confirm before adding.
- **UK Western Crescent local plans** (Slough, Hillingdon, Hounslow, Spelthorne) — all four
  boroughs are actively grappling with data-center policy in their Local Plans (Slough's June
  2026 appeal decision explicitly weighs data-center locational need under the NPPF; Hounslow's
  Local Plan Review, adoption expected 2026, references "the draft Local Plan approach to data
  centres"), but no specific, citable policy number/text was retrievable for any of the four —
  Hillingdon's "Policy DMCI 7" lead turned out to be about Community Infrastructure Levy, not
  data centers. Needs a human to open each adopted/emerging Local Plan PDF directly.
- **Dublin City Development Plan 2022-2028** — no data-centre-specific zoning/siting policy
  (distinct from national grid-constraint commentary) was located; unclear whether Dublin City
  Council has an EDE7-style policy at all.
- **Victoria, Australia — state-level data-center planning provisions** — no dedicated Victorian
  Planning Provision, Practice Note, or Advisory Note found despite direct searches of
  `planning.vic.gov.au` and `vpa.vic.gov.au`. What exists instead is individual Ministerial
  permits for specific projects (e.g. NEXTDC M3 at Tottenham) under the Development Facilitation
  Program, and a "Planning for Data Centres" guidance note published by the Planning Institute
  of Australia — an industry body, not government, so out of scope. Not recommended as a source
  this wave; a productive follow-up would be per-council Precinct Structure Plans (Wyndham,
  Hume, Melton) for the Truganina/Derrimut/Tottenham employment precincts.
- **Osaka Prefecture, Japan — Digital Infrastructure strategy page** — fetched directly; it is a
  strategy/coordination page for the Osaka Digital Infrastructure Council, mentioning future
  "review of requirements for data-center cluster candidate sites" but containing no actual
  zoning designations, district names, or numeric standards. Wrong document type (strategy, not
  ordinance) — no qualifying Osaka/Kansai candidate found this wave.
- **Zeewolde (NL) bestemmingsplan "Trekkersveld IV"** — explicitly dead: the Raad van State
  annulled this zoning plan in September 2023 after Meta withdrew in 2022. Noted only so it
  isn't mistakenly re-proposed in a future wave.

## Summary of what was NOT found

No structured/API source was found anywhere in this wave — noise ordinances, zoning
ordinances, and land-use/development plans are universally published as HTML hub pages with
linked PDF ordinance/plan text, not as queryable APIs. Every verified candidate is tier b (plain
crawl domain); zero tier-a (no existing structured client fits ordinance/zoning content) and
zero tier-c (no API worth a new client) this wave.
