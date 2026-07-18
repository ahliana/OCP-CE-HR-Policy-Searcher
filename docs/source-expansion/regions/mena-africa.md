# Source Expansion Research - Middle East + Africa

Branch: `feature/source-expansion-research`. Research only - no client code touched,
no domain added with `enabled: true`. All candidates below are draft additions.

## Dedup check performed

Read before researching: `config/domains/uae.yaml` (moei_ae, doe_abudhabi, dewa_dubai),
`config/domains/saudi_arabia.yaml` (moe_sa, seec_sa), `config/domains/south_africa.yaml`
(dmre_za, nersa_za), and `config/domains/api_sources.yaml` (9 structured API clients -
none regional to MENA/Africa). No `base_url` collisions found between those 7 existing
entries and any candidate below - all net-new.

## Regional coverage note on Egypt

Egypt is transcontinental (Africa + Middle East policy networks both claim it - it is
an RCREEE member and appears in Africa Energy Portal). Listed once below, tagged with
both `middle_east` and `africa` in `region`, to avoid a duplicate entry.

---

## Verified candidates (ranked best-first)

### 1. Israel - Ministry of Energy and Infrastructure (Policy Planning and Strategy Division)

- **name**: "Israel Ministry of Energy and Infrastructure - Policy Planning and Strategy Division"
- **proposed id**: `moe_il`
- **base_url**: `https://www.gov.il`
- **start_paths**: `/en/departments/units/planning_department`, `/en/departments/ministry-of-energy-and-infrastructure`
- **level**: national
- **access**: none (open, no key) - but see practical note below
- **coverage**: region: `["middle_east", "israel"]`; category: `energy_ministry`; tags:
  `["efficiency", "planning", "mandates"]`; policy_types: `["strategy", "regulation", "report"]`;
  language: `en` (Hebrew primary, English translation available)
- **format**: HTML, linked PDF reports (Regulatory Impact Assessment reports published
  on the Ministry's public-participation site)
- **practical**: `requires_playwright: true` recommended - a plain HTTP fetch (WebFetch
  tool, no browser) returned HTTP 403 on this domain twice; a real browser session
  loaded it cleanly, so this is very likely bot-detection on `gov.il`'s CDN, not a dead
  page. Update frequency: irregular, policy-driven. No robots.txt disallow found blocking
  this section.
- **effort tier**: b (plain crawl domain, needs Playwright)
- **why worth adding**: Israel's Ministry of Energy published an inter-ministerial
  interim policy specifically on data-center/server-farm energy demand (Feb 2026,
  covered by Israeli legal/policy press), including planning standards meant to "reduce
  energy consumption, minimize waste and maximize renewable energy use" for data
  centers - this is one of the most directly on-topic finds in the whole region.
- **verified**: yes. Loaded via browser; confirmed page title "Policy Planning and
  Strategy Division | Ministry of Energy and Infrastructure", content describes the
  division's regulatory-impact-assessment process and links to RIA reports.

### 2. RCREEE - Regional Center for Renewable Energy and Energy Efficiency (Arab states)

- **name**: "RCREEE - Regional Center for Renewable Energy and Energy Efficiency"
- **proposed id**: `rcreee_regional`
- **base_url**: `https://rcreee.org`
- **start_paths**: `/publications`, `/policies`
- **level**: supranational
- **access**: none
- **coverage**: region: `["middle_east", "africa"]` (17-member intergovernmental body:
  Algeria, Bahrain, Djibouti, Egypt, Iraq, Jordan, Kuwait, Lebanon, Libya, Mauritania,
  Morocco, Palestine, Somalia, Sudan, Syria, Tunisia, Yemen); category: `policy`; tags:
  `["efficiency", "research", "planning"]`; policy_types: `["report", "guidance"]`;
  language: `en` and `ar` (bilingual site, mixed per document)
- **format**: HTML publication index + linked PDFs
- **practical**: WordPress site, robots.txt only blocks `/wp-admin/` - no crawl
  restriction on publications. Sitemap at `/wp-sitemap.xml`. Update frequency: frequent
  (multiple publications per month).
- **effort tier**: b
- **why worth adding**: one source, 17 countries. Publications list (verified live)
  includes "Governance of Renewable Energy and Energy Efficiency Policies in Arab
  States," a regional workshop report on National Cooling Action Plans (NCAP - directly
  cooling/efficiency policy), and country-specific efficiency studies for Egypt. Best
  leverage-per-source find in the region.
- **verified**: yes. Loaded live; publications page lists 40+ PDF titles including the
  NCAP and governance-of-efficiency-policy reports named above.

### 3. Turkey - EPDK / EMRA (Energy Market Regulatory Authority)

- **name**: "Turkey Energy Market Regulatory Authority (EPDK/EMRA)"
- **proposed id**: `epdk_tr`
- **base_url**: `https://www.epdk.gov.tr`
- **start_paths**: `/Home/En`
- **level**: national
- **access**: none
- **coverage**: region: `["middle_east", "turkey"]`; category: `regulatory`; tags:
  `["mandates", "efficiency"]`; policy_types: `["law", "regulation"]`; language: `en`/`tr`
- **format**: HTML, linked PDF laws/regulations
- **practical**: no robots.txt disallow found on public paths. Site groups content by
  energy sector (Electricity, Natural Gas, Petroleum, LPG, Energy Transition), each with
  its own Laws/Regulations subsection - crawler will need `allowed_path_patterns` tuned
  to the Electricity and Energy Transition sections to avoid petroleum/LPG noise.
- **effort tier**: b
- **why worth adding**: national electricity regulator with a dedicated "Energy
  Transition" legislation section; Turkey has an EU-aligned building energy efficiency
  framework the regulator co-administers.
- **verified**: yes. Loaded live via WebFetch; confirmed English homepage with
  "LAWS"/"REGULATIONS" subsections under Electricity and Energy Transition.

### 4. Nigeria - NERC (Nigerian Electricity Regulatory Commission)

- **name**: "Nigerian Electricity Regulatory Commission (NERC)"
- **proposed id**: `nerc_ng`
- **base_url**: `https://nerc.gov.ng`
- **start_paths**: `/regulations`, `/codes`, `/orders`
- **level**: national
- **access**: none
- **coverage**: region: `["africa", "nigeria"]`; category: `regulatory`; tags:
  `["mandates", "reporting"]`; policy_types: `["regulation", "standard"]`; language: `en`
- **format**: HTML, linked PDF regulatory instruments
- **practical**: robots.txt is stock WordPress (`Disallow: /wp-admin/` only), sitemap at
  `/sitemap.xml`. Update frequency: regular (quarterly/annual reports plus ad hoc orders).
- **effort tier**: b
- **why worth adding**: NERC regulates under the Electricity Act 2023 and maintains a
  dedicated "Regulatory Instruments" hub with Regulations, Codes, Orders, and
  Standards/Guidelines subsections - Nigeria is Africa's largest power market and a
  growing data-center hub (Lagos).
- **verified**: yes. Loaded live via WebFetch; confirmed "Regulatory Instruments"
  navigation with Regulations/Codes/Orders/Standards & Guidelines subsections.

### 5. Egypt - EgyptERA (Egyptian Electric Utility and Consumer Protection Regulatory Agency)

- **name**: "EgyptERA - Egyptian Electric Utility and Consumer Protection Regulatory Agency"
- **proposed id**: `egyptera_eg`
- **base_url**: `https://www.egyptera.org`
- **start_paths**: `/en/`
- **level**: national
- **access**: none
- **coverage**: region: `["middle_east", "africa", "egypt"]`; category: `regulatory`;
  tags: `["mandates", "efficiency", "reporting"]`; policy_types: `["law", "regulation",
  "report"]`; language: `en`/`ar`
- **format**: HTML, linked PDFs (laws/decisions, annual reports, "awareness
  publications" aimed at energy conservation)
- **practical**: established under Electricity Law 87/2015, which specifically tasks
  EgyptERA with overseeing electricity-use efficiency via annual demand-management and
  efficiency plans - directly in our taxonomy. Update frequency: frequent (news/decision
  postings dated within the last few months at verification time).
- **effort tier**: b
- **why worth adding**: the regulator with the actual statutory efficiency mandate
  (Egypt's National Energy Efficiency Action Plan II sits under this framework), not
  just the renewables-focused NREA (see below, added as a secondary, weaker candidate).
- **verified**: yes. Loaded live; homepage confirmed sections "LAWS AND DECISIONS,"
  "CIRCULARS," "AWARENESS PUBLICATIONS," "EGYPTERA ANNUAL REPORT."

### 6. Ghana - Energy Commission (Energy Efficiency Standards & Labelling)

- **name**: "Ghana Energy Commission - Energy Efficiency Regulations"
- **proposed id**: `energycom_gh`
- **base_url**: `https://www.energycom.gov.gh`
- **start_paths**: `/newsite/index.php/regulation/energy-efficiency-ie`
- **level**: national
- **access**: none
- **coverage**: region: `["africa", "ghana"]`; category: `regulatory`; tags:
  `["mandates", "efficiency", "standards"]`; policy_types: `["regulation", "standard"]`;
  language: `en`
- **format**: HTML index + linked PDF Legislative Instruments (LIs)
- **practical**: robots.txt stock (blocks `/wp-admin/` only). Nineteen laws under the
  Energy Commission Act 1997 (Act 541); 2022 batch (LI 2442-2461) covers computers,
  set-top boxes, air conditioners, industrial fans, distribution transformers.
- **effort tier**: b
- **why worth adding**: explicit minimum-energy-performance-standard regulations for
  "computers" and industrial cooling/electrical equipment - closer to IT-equipment
  efficiency mandates than most national efficiency-standard regimes we've captured so
  far.
- **verified**: yes. Loaded live via WebFetch; confirmed full LI list (2442-2461) plus
  "Energy Efficiency Guidelines for Regulated Appliances" download.

### 7. Kuwait - Ministry of Electricity, Water and Renewable Energy (MEW)

- **name**: "Kuwait Ministry of Electricity, Water and Renewable Energy (MEW)"
- **proposed id**: `mew_kw`
- **base_url**: `https://www.mew.gov.kw`
- **start_paths**: `/en/`
- **level**: national
- **access**: none
- **coverage**: region: `["middle_east", "kuwait"]`; category: `energy_ministry`; tags:
  `["efficiency", "planning"]`; policy_types: `["guidance", "strategy"]`; language: `en`/`ar`
- **format**: HTML, linked PDF ("Guide to Rationalizing Electricity and Water
  Consumption")
- **practical**: `robots.txt` returned 404 on `www.mew.gov.kw/robots.txt` (no
  restrictions file present at all - unusual but not blocking). Site has "Access
  Rights" / "Corporate Governance" sections with law/guide references. Kuwait targets
  30% renewable electricity by 2030, which will show up in future strategy documents
  here.
- **effort tier**: b
- **why worth adding**: only national energy ministry for Kuwait; weaker on
  data-center-specific content today, but it is the correct authority to watch as Kuwait's
  renewable/efficiency strategy documents get published.
- **verified**: yes. Loaded live via WebFetch; confirmed official MEW site with
  About/Media Center/Services/Access Rights/Vacancies navigation and a consumption-
  rationalization guide.

### 8. Morocco - AMEE (Agence Marocaine pour l'Efficacité Énergétique)

- **name**: "AMEE - Moroccan Agency for Energy Efficiency"
- **proposed id**: `amee_ma`
- **base_url**: `https://www.amee.ma`
- **start_paths**: `/` (site's `/en/moroccan-agency-for-energy-efficiency` path 404'd at
  verification time - use the French-language homepage as the crawl root instead)
- **level**: national
- **access**: none
- **coverage**: region: `["africa", "morocco"]`; category: `energy_ministry`; tags:
  `["efficiency", "planning"]`; policy_types: `["strategy", "regulation", "guidance"]`;
  language: `fr` (primary; limited English)
- **format**: HTML, linked PDF (RTCM - Règlement Thermique de Construction au Maroc /
  Thermal Building Regulation)
- **practical**: created 2016 from the former ADEREE; under the Ministry of Energy
  Transition. Update frequency: frequent (news posts from June 2026 at verification
  time). No robots.txt check completed - recommend a conservative
  `rate_limit_seconds: 3.0` given the small agency site.
- **effort tier**: b
- **why worth adding**: national efficiency agency covering buildings, industry,
  transport, and public lighting - the Thermal Building Regulation (RTCM) is the
  closest Moroccan analogue to an efficiency mandate that would eventually touch data
  centers.
- **verified**: yes, with a caveat. `https://www.amee.ma/en/moroccan-agency-for-energy-
  efficiency` (from search results) 404'd ("Page non trouvée") when loaded live; the
  bare domain `https://amee.ma` / `https://www.amee.ma` resolves fine and is clearly the
  real AMEE site (confirmed via page text: "Agence Marocaine pour l'Efficacité
  Énergétique (AMEE)", sector pages for Industrie/Transport/Agriculture/Bâtiment).
  Use the domain root as `start_paths`, not the specific URL that appeared in search.

### 9. Turkey - Ministry of Energy and Natural Resources

- **name**: "Turkey Ministry of Energy and Natural Resources"
- **proposed id**: `enerji_tr`
- **base_url**: `https://www.enerji.gov.tr`
- **start_paths**: `/en-US/Pages/Energy-Efficiency`
- **level**: national
- **access**: none
- **coverage**: region: `["middle_east", "turkey"]`; category: `energy_ministry`; tags:
  `["efficiency", "strategy"]`; policy_types: `["strategy", "regulation"]`; language: `en`/`tr`
- **format**: HTML
- **practical**: site was intermittently unreachable during verification (timeouts on
  three of four attempts) - possibly geo-fencing or rate-limiting against automated
  clients rather than being down, since one browser load succeeded with the correct
  page title. Recommend `requires_playwright: true` and a generous `rate_limit_seconds`
  (4-5s) if this is added.
- **effort tier**: b
- **why worth adding**: complements EPDK (#3) with the ministry-level strategy side
  (EPDK is the regulator; this is the policy-setting ministry) - together they cover
  Turkey's EU-aligned building energy efficiency framework.
- **verified**: partial. The bare domain `https://enerji.gov.tr` (no `www.`) loaded once
  via browser with title "T.C. Enerji ve Tabii Kaynaklar Bakanlığı" (confirming it is
  the real ministry), but the specific `/en-US/Pages/Energy-Efficiency` subpath could not
  be independently reloaded in this session (repeated timeouts) - it matches a live
  search-result title ("...Ministry of Energy and Natural Resources - Energy
  Efficiency"), so the page almost certainly exists, but flag for a human re-check
  before enabling.

### 10. AFREC - African Energy Commission (African Union)

- **name**: "AFREC - African Energy Commission"
- **proposed id**: `afrec_au`
- **base_url**: `https://au-afrec.org`
- **start_paths**: `/energy-efficiency-programme`, `/policy-briefs`
- **level**: supranational
- **access**: none
- **coverage**: region: `["africa"]`; category: `policy`; tags: `["efficiency",
  "research", "planning"]`; policy_types: `["report", "guidance", "strategy"]`;
  language: `en`/`fr`
- **format**: HTML, linked PDF
- **practical**: continental specialized energy agency of the African Union; also
  reachable at `afrec.au.int` (older domain, redirects/mirrors content - use
  `au-afrec.org` as canonical, it's the one that loaded cleanly). Publishes the African
  Energy Efficiency Strategy (AfEES) and hosted the first continental energy-efficiency
  conference in Dec 2025.
- **effort tier**: b
- **why worth adding**: continent-wide efficiency strategy body, parallel to RCREEE for
  the Arab states but pan-African - covers Kenya/Nigeria/Ghana/Morocco (and everyone
  else) at a strategy level even where the national regulator's own site is thin.
- **verified**: yes. Loaded live via WebFetch; confirmed "M&E Handbook on Energy
  Efficiency Policy Instruments," "MEPS Development, Implementation and Adoption"
  training material, and a dedicated Policy Briefs section.

### 11. Egypt - NREA (New and Renewable Energy Authority)

- **name**: "Egypt New and Renewable Energy Authority (NREA)"
- **proposed id**: `nrea_eg`
- **base_url**: `https://nrea.gov.eg`
- **start_paths**: `/test/en/Home`
- **level**: national
- **access**: none
- **coverage**: region: `["middle_east", "africa", "egypt"]`; category: `energy_ministry`;
  tags: `["strategy", "planning"]`; policy_types: `["strategy", "standard"]`; language: `en`/`ar`
- **format**: HTML
- **practical**: site runs under a `/test/` path prefix even in production (unusual but
  consistently live); no robots.txt check completed.
- **effort tier**: b
- **why worth adding**: weakest candidate in this batch - NREA is almost entirely
  renewable-generation-focused (wind/solar project execution, 30%-by-2030 target), with
  little visible waste-heat/data-center/efficiency-mandate content. Included for
  completeness since it's Egypt's other national energy authority alongside EgyptERA
  (#5, the stronger pick); consider skipping if source-count budget is tight.
- **verified**: yes. Loaded live via browser; confirmed official NREA homepage.

### 12. Oman - APSR (Authority for Public Services Regulation)

- **name**: "Oman Authority for Public Services Regulation (APSR)"
- **proposed id**: `apsr_om`
- **base_url**: `https://apsr.om`
- **start_paths**: `/en/renewableenergy` (per search results; not independently
  re-verified this session, see caveat)
- **level**: national
- **access**: none
- **coverage**: region: `["middle_east", "oman"]`; category: `regulatory`; tags:
  `["mandates", "efficiency"]`; policy_types: `["regulation", "standard"]`; language: `en`/`ar`
- **format**: HTML (JS-rendered SPA - see practical note)
- **practical**: the domain returns HTTP 200 and a valid page title ("APSR"), but the
  page body renders empty in a non-JS-executing fetch and stayed empty even after a
  short wait in a real browser session - this is very likely a heavy client-side app
  (React/Angular) that needs longer render time or specific routing. Mark
  `requires_playwright: true` with an increased load-wait if added.
- **effort tier**: b, possibly c if the content is served via an internal API the
  Playwright crawler can't trigger without additional wait/scroll logic
- **why worth adding**: sole national regulator for electricity (and five other public
  services) in Oman; per search results, is working on mandatory energy-efficiency
  specifications for major appliances - directly on-topic once the crawler can actually
  render the page.
- **verified**: partial. Domain resolves (not dead, not blocked), title confirms it's
  APSR, but no policy content could be independently read this session. Recommend a
  human check with a JS-capable browser and longer wait before enabling.

---

## Unverified / needs-human-check

These could not be reached from this session's network at all (DNS failure or
connection refused, repeated across both the WebFetch tool and a real browser tab) despite
strong secondary evidence - live PDFs hosted on the domain turning up directly in web
search, and citation from third-party regulator directories (ERRA, IEA). Given the
brief's instruction not to list unverified/hallucinated endpoints as verified, these are
called out separately. A human on a different network should confirm these load before
any config is written.

### Qatar - Kahramaa (Qatar General Electricity & Water Corporation) - District Cooling

- **proposed id**: `kahramaa_qa`
- **base_url**: `https://www.km.qa`
- **candidate start_paths**: `/DistrictCooling/Pages/WhatIsDistrictCooling.aspx`,
  `/CustomerService/ServiceRegulations/DISTRICT%20COOLING%20Design%20and%20Water%20Managementcode%202016.pdf`
- **level**: national
- **access**: none (no key apparent)
- **coverage**: region: `["middle_east", "qatar"]`; category: `district_heating`; tags:
  `["district_heating", "efficiency", "mandates"]`; policy_types: `["regulation",
  "standard", "law"]`; language: `en`/`ar`
- **why it would be high-value if confirmed**: this is the single best district-cooling
  regulatory find in the region - Qatar's Council of Ministers Law No. 19 (2024)
  formally hands Kahramaa authority to license and regulate district cooling
  (mandatory building connection in designated zones, 15-year licenses), and Kahramaa's
  District Cooling Department already publishes a "Design and Water Management Code
  2016" PDF directly on this domain. District cooling is adjacent to waste-heat reuse
  and is explicitly called out in the brief as significant in the Gulf.
- **connection attempts**: WebFetch (twice) -> `ECONNREFUSED 80.76.166.133:443`; a real
  browser tab -> "navigation to km.qa was denied or failed" (both root and the specific
  path). Search-engine snippets independently show the PDF path and page titles are
  real and current (2026 news coverage of new district-cooling decisions).

### Bahrain - Sustainable Energy Authority (SEA)

- **proposed id**: `sea_bh`
- **base_url**: `https://www.sea.gov.bh`
- **candidate start_paths**: `/` (National Energy Efficiency Action Plan, green building
  code, MEPS pages - exact paths not confirmed)
- **level**: national
- **access**: none
- **coverage**: region: `["middle_east", "bahrain"]`; category: `energy_ministry`; tags:
  `["efficiency", "standards", "mandates"]`; policy_types: `["strategy", "standard",
  "regulation"]`; language: `en`/`ar`
- **why it would be high-value if confirmed**: Bahrain hit its 6% NEEAP efficiency
  target six years early and has a Ministerial Order (70/2015) setting MEPS/labeling for
  AC units, plus a green-building-code initiative under NEEAP - all squarely in our
  taxonomy.
- **connection attempts**: WebFetch (twice) -> `getaddrinfo ENOTFOUND www.sea.gov.bh`; a
  real browser tab -> "navigation to sea.gov.bh was denied or failed" on both
  `https://www.sea.gov.bh` and `https://sea.gov.bh`. DNS-level failure specifically,
  which is different from the Qatar/Kenya connection-refused pattern - possibly this
  specific sandbox's resolver doesn't have `.bh` government-zone records cached, or the
  domain is genuinely down. IEA and ESMAP profile pages cite `sea.gov.bh` as the
  authority's real domain.

### Kenya - EPRA (Energy and Petroleum Regulatory Authority)

- **proposed id**: `epra_ke`
- **base_url**: `https://www.epra.go.ke`
- **candidate start_paths**: `/energy-efficiency`, `/regulations`
- **level**: national
- **access**: none
- **coverage**: region: `["africa", "kenya"]`; category: `regulatory`; tags:
  `["mandates", "efficiency", "reporting"]`; policy_types: `["regulation"]`; language: `en`
- **why it would be high-value if confirmed**: the Energy Act 2019 gives EPRA an
  explicit efficiency mandate; the Energy (Energy Management) Regulations 2025
  (gazetted Feb 2025, replacing the 2012 regulations) require energy audits and
  conservation measures for facilities above a 180,000 kWh consumption threshold - large
  data centers would likely fall inside that threshold. A five-star appliance labeling
  scheme also exists under a separate 2016 regulation.
- **connection attempts**: WebFetch (three times, two different paths) -> consistently
  `ECONNREFUSED 212.22.165.242:443`; a real browser tab -> "navigation to epra.go.ke was
  denied or failed" (retried twice). Search results directly surfaced live PDF reports
  hosted on `epra.go.ke` (e.g., a September 2025 statistics report), so the domain is
  almost certainly live outside this sandbox.

---

## Summary of what to append where

- New file recommended: `config/domains/israel.yaml`, `qatar.yaml` (once verified),
  `kuwait.yaml`, `bahrain.yaml` (once verified), `oman.yaml`, `turkey.yaml`, `egypt.yaml`,
  `kenya.yaml` (once verified), `nigeria.yaml`, `morocco.yaml`, `ghana.yaml` - each
  region is a distinct country not yet represented, so none of these fit cleanly into
  the three existing MENA/Africa files (`uae.yaml`, `saudi_arabia.yaml`,
  `south_africa.yaml`), which are already single-country files by convention in this repo.
- `rcreee_regional` and `afrec_au` are cross-country - propose a new
  `config/domains/mena_africa_regional.yaml` for supranational bodies, mirroring how
  `eu.yaml` holds EU-level (as opposed to member-state) sources.
