# Municipal / City Heat-Network-Zoning Tier - Wave 3

Scope: city, municipal, and provincial authorities in heat-network-dense European
countries publishing heat-planning / heat-zoning / data-center-heat-connection
policy - the Netherlands, Germany, the UK, the Nordics, and France. This is the
tier where the "data-center waste heat -> district network" mandate actually
lands on individual buildings, because municipalities (not national ministries)
draw the zone maps, set connection obligations, and sign the offtake deals.

No client code or config changes made. Everything below is a proposal; nothing
is `enabled: true` anywhere. Branch: `feature/source-expansion-research`.

## Dedup method

Grepped every `base_url:` in `config/domains/*.yaml` (432 unique URLs across
all countries) plus `docs/source-expansion/draft/crawl/**/*.yaml`,
`docs/source-expansion/draft/new-clients*.md`, and
`docs/source-expansion/regions-wave2/*.md`, filtered for city/utility name hits
in each target country. Confirmed:

- **Netherlands**: `netherlands.yaml` has exactly one entry (`wetten_overheid_nl`,
  a national legislation search). `eu.yaml` has `rvo_nl`. **Zero** municipal or
  provincial entries anywhere in the corpus. Wide open.
- **Germany**: `germany.yaml` has full Land (state)-level coverage for Hessen,
  Bayern, NRW, Baden-Württemberg, Berlin, Hamburg, Niedersachsen, Sachsen - but
  **no city-level** (Stadt/Stadtwerke) entries for Frankfurt, Munich, Cologne,
  or Stuttgart specifically.
- **UK**: `uk.yaml` covers DESNZ national heat-network-zoning policy (the six
  pilot zones - Leeds, Plymouth, Bristol, Stockport, Sheffield, London - are
  *named* in national DESNZ documents) but has **no local-authority-published**
  zoning pages (i.e., the councils' own sites).
- **Nordics**: `nordic.yaml`/`sweden.yaml`/`denmark.yaml` have
  `stockholm_exergi_odh` (a utility, majority city-owned) and NVE/Lovdata
  national sources. Wave-1's `regions/nordic.md` explicitly checked and
  **rejected** HOFOR (Copenhagen) as marketing-only with no policy content -
  not re-proposed here. No Helsinki, Oslo, or Copenhagen-municipality entries
  exist anywhere.
- **France**: `france.yaml` has one national legislative-search entry.
  `regions-wave2/multilateral-portals.md` proposes a `data_gouv_fr_api`
  national open-data client (tier c) whose sample queries surfaced Paris and
  Bordeaux dataset *titles* ("Périmètre de raccordement obligatoire...
  Bordeaux") - but that's a national metadata index, not the metropoles' own
  sites. No Lyon, Grenoble, Nantes, Strasbourg, or Bordeaux **city-hosted**
  entries exist. (Despite the task brief's parenthetical suggesting Lyon/
  Bordeaux were "found" - they are not in the corpus under any base_url; only
  referenced indirectly as dataset titles inside the national API's sample
  query results. Both are proposed fresh below, sourced directly from the
  metropoles' own domains.)
- **Austria/Switzerland**: `dach.yaml`/`deep-subnational.md` already cover
  Vienna (MA20), Zurich, Geneva, Bern, Basel-Stadt, and Vaud cantons in depth
  (wave 2). Not revisited this pass per the task's dedup instruction - no new
  AT/CH candidates below.

---

## Verified candidates (ranked best-first)

### 1. Helen Oy - Heat Recovery Service for Data Centers (Helsinki, Finland)

- **name**: Helen Oy - Heat Recovery Service for Data Centers
- **proposed id**: `helen_fi_dc_heat_recovery`
- **base_url**: `https://www.helen.fi`
- **start_paths**: `/en/companies/cooling-for-companies/Heat-recovery-service-for-data-centers`
- **level**: local (Helen is Helsinki's wholly city-owned energy utility)
- **access**: none (open, no key)
- **coverage**: region: `["nordic", "finland", "helsinki"]`; category:
  `district_heating`; tags: `["waste_heat", "district_heating", "incentives",
  "data_center_specific"]`; policy_types: `["program", "guidance"]`; language: `en`
  (Finnish version also exists)
- **format**: HTML
- **practical**: standard 2s rate limit recommended; no robots.txt check done
  this session; page is static program marketing/guidance, low update frequency.
- **effort tier**: b (plain crawl domain)
- **why worth adding**: this is a live, operational, city-utility-run program
  document, not just a plan - it names the actual mechanism (three heat-offtake
  contract models), the financial incentive (reduced electricity tax, €0.5/MWh,
  for heat-recovering data centers per Finnish tax law), and quantifies impact
  ("one data centre can heat up to 20,000 apartments"). Directly names the
  Telia Helsinki Data Center as already recovering 90% of its waste heat. This
  is the single clearest "policy meets practice" document found in this pass.
- **verified**: yes. WebFetch confirmed live page, official Helen Oy branding,
  describes the heat-recovery program, contract models, and the electricity-tax
  incentive tied to heat recovery.
- **companion**: City of Helsinki's own climate page,
  `https://ilmasto.hel.fi/en/mitigation/heating-and-decarbonisation/` (see #16
  below) - confirms district heating is 98% of city-facility heating and
  the city's decarbonization framework Helen operates inside, though this
  specific page does not itself name data centers.

---

### 2. Provincie Noord-Holland - Datacenterstrategie 2025-2027 (Netherlands)

- **name**: Provincie Noord-Holland - Datacenters (provincial data center policy hub)
- **proposed id**: `noord_holland_datacenters`
- **base_url**: `https://www.noord-holland.nl`
- **start_paths**:
  - `/Onderwerpen/Economie_Werk/Projecten/Datacenters`
  - `/bestanden/pdf/Economie_Werk/Datacenterstrategie%20NH%202025-2027.pdf`
- **level**: subnational (province)
- **access**: none (open, no key)
- **coverage**: region: `["eu", "eu_west", "netherlands", "noord_holland"]`;
  category: `regulatory`; tags: `["mandates", "waste_heat", "district_heating",
  "data_center_specific", "planning"]`; policy_types: `["strategy",
  "regulation", "guidance"]`; language: `nl`
- **format**: HTML (hub page) + PDF (strategy document, ~4.1MB)
- **practical**: standard 2s rate limit; no robots.txt check done. Strategy
  document covers 2025-2027, likely low update frequency; the hub page links
  to companion documents (`Richtlijn duurzame vestigingsvoorwaarden datacenters
  Noord-Holland`) that should be added as additional start_paths on ingest.
- **effort tier**: b (plain crawl domain)
- **why worth adding**: Noord-Holland (home to the Amsterdam data center
  cluster, one of Europe's largest) explicitly conditions new data-center siting
  on waste-heat readiness. The hub page confirms the province appoints a
  "warmteregisseur" (heat coordinator/regulator) specifically to broker
  data-center waste heat into heat networks, and that new data centers are
  expected to be heat-network-ready as a siting condition. This is a genuine
  provincial mandate-adjacent instrument, not just guidance.
- **verified**: yes, with one caveat. WebFetch confirmed the hub page
  (`/Onderwerpen/Economie_Werk/Projecten/Datacenters`) is live, official, and
  on-topic (quotes "De warmte van datacenters kan gebruikt worden voor de
  verwarming van gebouwen" and discusses heat-network infrastructure
  requirements). The PDF itself was fetched (200 OK, 4.1MB) but returned as
  binary/unparseable image-heavy content by the fetch tool - could not confirm
  its specific text this session; the hub page's summary of its contents is
  what's verified. A separate archived press release
  (`/Actueel/Archief/2021/December_2021/...`) 404'd - do not use that URL.

---

### 3. Greater London Authority - Heat Networks in London + Data Centre Heat Reuse Report (UK)

- **name**: Greater London Authority - Heat Networks in London (+ "Optimising Data Centres in London - Heat Reuse" report)
- **proposed id**: `gla_heat_networks_london`
- **base_url**: `https://www.london.gov.uk`
- **start_paths**:
  - `/heat-networks-london`
  - `/sites/default/files/2025-06/Optimising_Data_Centres_in_London_-_Heat_Reuse_250605.pdf`
- **level**: local (Greater London Authority - regional/city government for
  Greater London; GLA + boroughs form the Zone Coordination Body under the
  Energy Act 2023 heat-network-zoning regime)
- **access**: none (open, no key)
- **coverage**: region: `["uk", "london"]`; category: `district_heating`;
  tags: `["waste_heat", "district_heating", "data_center_specific",
  "planning", "mandates"]`; policy_types: `["report", "guidance",
  "regulation"]`; language: `en`
- **format**: HTML (hub page) + PDF (dedicated data-center heat-reuse report)
- **practical**: standard 2s rate limit; London.gov.uk previously seen in
  corpus only for a green-finance page, distinct topic/path - no overlap.
- **effort tier**: b (plain crawl domain)
- **why worth adding**: the GLA commissioned and published a report
  specifically quantifying up to 1.6 TWh/year of recoverable heat from
  London's data-center estate (enough for all of Ealing) and making explicit
  planning-policy recommendations (updated planning guidance, infrastructure
  incentives, a standardized offtake framework). This is the most
  data-center-specific municipal policy document found in the UK pass - more
  targeted than the national DESNZ zoning program. The companion hub page
  confirms two live zones (OPDC, South Westminster Area Network/SWAN) and the
  GLA's role as Zone Coordination Body.
- **verified**: yes for the hub page (`/heat-networks-london` - WebFetch
  confirmed live, official, GLA/London Assembly Research Unit branding, cites
  3,503 registered London heat networks and the OPDC/SWAN zones). The PDF
  itself returned as unparseable binary to the fetch tool (200 OK, 4MB) -
  its existence and title are confirmed via WebSearch snippet and the hub
  page links to it, but full text content wasn't independently read this
  session.

---

### 4. Eindhoven - Warmteprogramma + Datacenter-to-District-Heat Deal (Netherlands)

- **name**: Gemeente Eindhoven - Warmteprogramma (+ Interconnect datacenter/Meerhoven heat deal)
- **proposed id**: `eindhoven_warmteprogramma`
- **base_url**: `https://www.eindhoven.nl`
- **start_paths**:
  - `/bouwen/warmteprogramma`
  - `/persberichten/duurzame-warmte-van-datacenter-voor-warmtenet-meerhoven`
- **level**: local (municipality)
- **access**: none (open, no key)
- **coverage**: region: `["eu", "eu_west", "netherlands", "eindhoven"]`;
  category: `district_heating`; tags: `["waste_heat", "district_heating",
  "data_center_specific", "planning"]`; policy_types: `["strategy", "report"]`;
  language: `nl`
- **format**: HTML
- **practical**: standard 2s rate limit; no robots.txt check done.
  Warmteprogramma established December 2025, succeeds the 2021
  Transitievisie Warmte; low update frequency expected (5-year statutory cycle
  per Dutch Klimaatakkoord).
- **effort tier**: b (plain crawl domain)
- **why worth adding**: this is a live, signed, government-announced
  agreement (municipality + Interconnect Services BV) to route a specific
  named data center's waste heat into the Meerhoven district heating network,
  explicitly framed as replacing biomass in the city's heat mix. It's the
  clearest Dutch example of a municipality directly brokering (not just
  planning for) data-center-to-heat-network offtake.
- **verified**: partial. `/bouwen/warmteprogramma` - WebFetch confirmed live,
  official, on-topic (names restwarmte as a heat source). The press release
  URL (`/persberichten/duurzame-warmte-van-datacenter-voor-warmtenet-meerhoven`)
  returned HTTP 403 to the fetch tool (likely bot-blocking, same behavior as
  other `.nl` municipal domains this session) - its existence, headline, and
  content are confirmed via WebSearch result snippet and a live indexed
  Google-cached title, but full-page text wasn't independently read.

---

### 5. Leeds City Council - Local Development Order 3 (Leeds District Heating Network) (UK)

- **name**: Leeds City Council - LDO 3: Leeds District Heating Network
- **proposed id**: `leeds_gov_uk_ldo3_heat_network`
- **base_url**: `https://www.leeds.gov.uk`
- **start_paths**:
  - `/planning/planning-policy/supplementary-planning-documents-and-guidance/local-development-order/local-development-order-(ldo-3)-leeds-district-heating-network`
- **level**: local (city council)
- **access**: none (open, no key)
- **coverage**: region: `["uk", "leeds"]`; category: `district_heating`;
  tags: `["waste_heat", "district_heating", "data_center_specific",
  "planning", "mandates"]`; policy_types: `["regulation", "strategy"]`;
  language: `en`
- **format**: HTML
- **practical**: standard 2s rate limit; adopted November 2025, permission
  expires December 31, 2035 - a stable long-lived planning instrument.
- **effort tier**: b (plain crawl domain)
- **why worth adding**: an actual adopted planning-law instrument (not just a
  strategy document) that grants automatic planning permission for district
  heat infrastructure, and explicitly names data centres as a heat source
  alongside the Recycling and Energy Recovery Facility: "Ramboll have
  identified a range of heat sources for this long-term project, including
  other Energy Recovery Facilities, data centres and industrial processes."
  Leeds is also one of the six DESNZ first-round heat-network zoning pilot
  cities (already referenced nationally in `uk.yaml`), so this is the
  local-authority-level instrument that implements that national designation.
- **verified**: yes. WebFetch confirmed live, official Leeds City Council
  page, describes LDO 3 adopted November 2025, explicitly names data centres
  as an identified heat source.

---

### 6. Oslo Kommune - Klimaetaten (Climate Agency) Data Center Waste Heat (Norway)

- **name**: Oslo Kommune - Klimaetaten: Datasenter varmer opp 5000 leiligheter
- **proposed id**: `klimaoslo_no_dc_heat`
- **base_url**: `https://www.klimaoslo.no`
- **start_paths**:
  - `/oslo-datasenter-varmer-opp-5000-leiligheter/`
  - `/2018/10/09/overskuddsvarme-fra-datasenter/`
- **level**: local (Klimaetaten is Oslo Kommune's own Climate Agency)
- **access**: none (open, no key)
- **coverage**: region: `["nordic", "norway", "oslo"]`; category:
  `environmental_agency`; tags: `["waste_heat", "district_heating",
  "data_center_specific"]`; policy_types: `["report", "guidance"]`;
  language: `no`
- **format**: HTML
- **practical**: standard 2s rate limit; klimaoslo.no is the Climate Agency's
  public-facing communications site (distinct from the formal
  oslo.kommune.no bureaucratic domain) - both are official.
- **effort tier**: b (plain crawl domain)
- **why worth adding**: describes a live, operating (not proposed) data-center
  waste-heat-to-district-heating installation (Hafslund Celsio + the STACK
  data center on Ulven) delivering 5 MW / ~5,000 apartments, profitable without
  subsidy from day one, published by the city's own climate agency as an
  example of its climate-budget strategy in action.
- **verified**: yes. WebFetch confirmed live, official Oslo Kommune Klimaetaten
  page, describes the Hafslund/STACK data-center heat-recovery project in
  detail (temperatures, MW, homes served).

---

### 7. VEKS - Copenhagen-Area Inter-Municipal District Heating Utility (Denmark)

- **name**: VEKS (Vestegnens Kraftvarmeselskab) - Future District Heating + Microsoft Surplus Heat Project
- **proposed id**: `veks_dk`
- **base_url**: `https://www.veks.dk`
- **start_paths**:
  - `/en/focus/the-future-district-heating`
  - `/fokus/projekter-og-aktiviteter/overskudsvarme-microsoft`
- **level**: local (VEKS is a nonprofit inter-municipal utility jointly owned
  by 12 Greater Copenhagen municipalities - same governance model as Stockholm
  Exergi, already accepted into the corpus as `stockholm_exergi_odh`)
- **access**: none (open, no key)
- **coverage**: region: `["nordic", "denmark", "copenhagen"]`; category:
  `district_heating`; tags: `["waste_heat", "district_heating",
  "data_center_specific", "planning"]`; policy_types: `["strategy", "report"]`;
  language: `en` (English section confirmed; Danish primary also exists)
- **format**: HTML
- **practical**: standard 2s rate limit; no robots.txt check done.
- **effort tier**: b (plain crawl domain)
- **why worth adding**: names an actual signed agreement (VEKS + Microsoft,
  Høje-Taastrup data center) to deliver waste heat equivalent to ~6,000 homes
  starting the 2025-2026 heating season, plus the FFH50 (Future District
  Heating) joint-utility policy document explicitly stating "the share of
  surplus heat, data centres included, will increase considerably in the
  years ahead." This is the direct Danish counterpart to the Stockholm Data
  Parks program, filling the gap left by wave-1's rejection of HOFOR
  (marketing-only, no policy content).
- **verified**: yes, both paths. WebFetch confirmed VEKS is official
  (owned by 12 municipalities), and both the future-district-heating policy
  page and the Microsoft-specific project page are live and on-topic.

---

### 8. Stockholms Stad - Akalla Server Halls / Stockholm Data Parks (Sweden)

- **name**: Stockholms Stad - Serverhallar med återvinning av överskottsvärme (Akalla)
- **proposed id**: `stockholm_stad_akalla_dataparks`
- **base_url**: `https://vaxer.stockholm`
- **start_paths**: `/projekt/akalla/serverhallar-med-atervinning-av-overskottsvarme/`
- **level**: local (Stockholms stad - City of Stockholm's own urban
  development/city-planning portal, distinct domain from the Stockholm Exergi
  utility already in `sweden.yaml`)
- **access**: none (open, no key)
- **coverage**: region: `["nordic", "sweden", "stockholm"]`; category:
  `district_heating`; tags: `["waste_heat", "district_heating",
  "data_center_specific", "planning"]`; policy_types: `["strategy", "report"]`;
  language: `sv`
- **format**: HTML
- **practical**: standard 2s rate limit; `vaxer.stockholm` is the city's
  dedicated urban-growth/planning-projects subdomain (separate from
  `start.stockholm`, the formal policy-document domain - see unverified
  section for the latter).
- **effort tier**: b (plain crawl domain)
- **why worth adding**: this is the City of Stockholm's own planning-project
  page (not the Stockholm Exergi utility side already covered), describing
  the Stockholm Data Parks initiative - a joint city + utility + grid operator
  + business-region program specifically designed to attract data centers
  because their waste heat feeds district heating. Confirms the city's own
  planning role (siting, FAQ on grid capacity/EMF) alongside the utility's
  commercial heat-purchase program.
- **verified**: yes. WebFetch confirmed live, official Stockholms stad page,
  describes the Akalla server-hall project, Stockholm Data Parks partnership,
  and heat-recovery-to-district-heating mechanism.

---

### 9. Team Frankfurt Klimaschutz - Kommunale Wärmeplanung Frankfurt (Germany)

- **name**: Team Frankfurt Klimaschutz - Kommunale Wärmeplanung (Municipal Heat Planning)
- **proposed id**: `frankfurt_kommunale_waermeplanung`
- **base_url**: `https://klimaschutz-frankfurt.de`
- **start_paths**:
  - `/kommunale-waermeplanung/`
  - `/kommunale-waermeplanung/ablauf/`
- **level**: local (run by Frankfurt's municipal Klimareferat/climate office
  under the "Team Frankfurt Klimaschutz" brand - confirmed via page footer)
- **access**: none (open, no key)
- **coverage**: region: `["eu", "eu_central", "germany", "hessen",
  "frankfurt"]`; category: `district_heating`; tags: `["waste_heat",
  "district_heating", "data_center_specific", "planning"]`; policy_types:
  `["strategy", "report"]`; language: `de`
- **format**: HTML
- **practical**: standard 2s rate limit; no robots.txt check done. Statutory
  deadline for Frankfurt's KWP completion was June 30, 2026 (per WPG for
  cities >100k population) - low update frequency expected post-completion.
- **effort tier**: b (plain crawl domain)
- **why worth adding**: Frankfurt is Europe's single largest data-center
  market, and this is the city's own municipal heat-planning site (distinct
  from the existing `hessen_energy`/`hessen_digital_dc` state-level entries in
  `germany.yaml`) explicitly naming "Abwärme aus Abwasser, Industrie und
  Rechenzentren" (waste heat from sewage, industry, and data centers) as a
  heat source for the city's climate-neutral heat target.
- **verified**: yes. WebFetch confirmed the page is run by Frankfurt's
  climate office, describes the four-phase KWP process (suitability
  assessment, inventory, potential analysis, target scenarios), and
  explicitly names Rechenzentren as a waste-heat source.

---

### 10. Landeshauptstadt München - Wärmewende München (Munich, Germany)

- **name**: City of Munich - Wärmewende München (Heat Transition)
- **proposed id**: `muenchen_waermewende`
- **base_url**: `https://stadt.muenchen.de`
- **start_paths**: `/infos/waermewende-muenchen.html`
- **level**: local (city, run by Referat für Klima- und Umweltschutz jointly
  with Stadtwerke München)
- **access**: none (open, no key)
- **coverage**: region: `["eu", "eu_central", "germany", "bayern",
  "muenchen"]`; category: `district_heating`; tags: `["waste_heat",
  "district_heating", "planning"]`; policy_types: `["strategy", "regulation"]`;
  language: `de`
- **format**: HTML
- **practical**: standard 2s rate limit; heat plan adopted May 15, 2024
  (Munich was the first Bavarian municipality to complete one); Heat
  Ordinance adopted November 2025.
- **effort tier**: b (plain crawl domain)
- **why worth adding**: Munich's own city-level heat plan (distinct from the
  existing `bayern_energy`/`bayern_building` state-level entries), targeting
  62% district-heating share by 2045 and full conversion of SWM's ~1,000km
  network to renewables + "unavoidable waste heat" by 2040. News coverage
  (not this page directly) separately confirms SWM is evaluating data-center
  waste-heat recovery via heat pumps in the Moosach quarter - worth flagging
  for a human to verify if a dedicated SWM page exists.
- **verified**: yes, with a scope caveat. WebFetch confirmed live, official
  City of Munich page, describes the heat-transition plan and waste-heat
  ("Abwärme") role in general terms. Data centers (Rechenzentren) are **not**
  named on this specific page - the DC-specific detail came from a separate
  news article (Solarserver) about SWM's district-heating transformation
  plan, not independently verified this session.

---

### 11. VEKS / Copenhagen companion: Københavns Kommune - Climate Strategy 2035 (Denmark)

- **name**: Københavns Kommune - Klimastrategi 2035 / Klimahandleplan
- **proposed id**: `kk_dk_klimaplan`
- **base_url**: `https://www.kk.dk`
- **start_paths**:
  - `/politik/politikker-og-indsatser/klima-miljoe-og-natur/klimaplan-co2-neutral-hovedstad`
- **level**: local (municipality)
- **access**: none (open, no key)
- **coverage**: region: `["nordic", "denmark", "copenhagen"]`; category:
  `environmental_agency`; tags: `["district_heating", "planning"]`;
  policy_types: `["strategy"]`; language: `da` (English PDF also linked)
- **format**: HTML hub + downloadable PDF strategy documents
- **practical**: standard 2s rate limit; Climate Strategy 2035 + Climate
  Action Plan 2026-2028 adopted September 18, 2025, replacing the older
  KBH2025 plan - recently updated, next revision cycle unclear.
- **effort tier**: b (plain crawl domain)
- **why worth adding**: the municipality's own climate-plan hub, complementing
  the VEKS utility entry (#7) with the Copenhagen city government's own
  framing. Lower priority than VEKS because the visible hub page itself
  doesn't mention district heating/waste heat/data centers directly (that
  content likely lives inside the linked PDFs, not confirmed this session).
- **verified**: partial. WebFetch confirmed the page is official
  Københavns Kommune, describes the Climate Strategy 2035 adoption and links
  to downloadable PDFs - but the visible page text has **no mention** of
  district heating, overskudsvarme (surplus heat), or data centers. Would
  need the linked Climate Strategy 2035 PDF itself fetched and confirmed
  before this is more than a "companion/hub" entry.

---

### 12. Bristol City Council - Heat Network Local Development Order (UK)

- **name**: Bristol City Council - Bristol Heat Network Local Development Order
- **proposed id**: `bristol_gov_uk_heat_network_ldo`
- **base_url**: `https://www.bristol.gov.uk`
- **start_paths**:
  - `/council/policies-plans-and-strategies/energy-and-environment/bristol-heat-network-local-development-order`
- **level**: local (city council)
- **access**: none (open, no key)
- **coverage**: region: `["uk", "bristol"]`; category: `district_heating`;
  tags: `["district_heating", "planning"]`; policy_types: `["regulation"]`;
  language: `en`
- **format**: HTML
- **practical**: standard 2s rate limit; consultation closed January 2023;
  Bristol is also one of the six DESNZ zoning pilot cities (city-owned Bristol
  City Leap partnership referenced in national coverage).
- **effort tier**: b (plain crawl domain)
- **why worth adding**: council-adopted planning instrument granting permitted
  development rights for heat-network infrastructure across specified Bristol
  areas - the local implementation layer under Bristol's DESNZ pilot-zone
  designation and the Bristol City Leap 20-year energy partnership.
- **verified**: yes, with a content caveat. WebFetch confirmed live, official
  Bristol City Council page describing the LDO's permitted-development scope.
  It does **not** itself mention mandatory-connection rules or data centers
  (those details come from separate news coverage of the Heat Network Zoning
  Zone Opportunity Report, not this specific council page).

---

### 13. Greater Manchester Combined Authority - Heat Networks (GM Green City) (UK)

- **name**: Greater Manchester Combined Authority - Heat Networks (GM Green City)
- **proposed id**: `gmca_heat_networks`
- **base_url**: `https://gmgreencity.com`
- **start_paths**: `/projects-and-campaigns/heat-networks/`
- **level**: subnational (combined authority - covers 10 Greater Manchester
  boroughs including Manchester City Council)
- **access**: none (open, no key)
- **coverage**: region: `["uk", "manchester", "greater_manchester"]`;
  category: `district_heating`; tags: `["district_heating", "planning"]`;
  policy_types: `["strategy", "report"]`; language: `en`
- **format**: HTML
- **practical**: standard 2s rate limit; site is GMCA-run per footer
  copyright; part of the government's Heat Network Zoning Pilot.
- **effort tier**: b (plain crawl domain)
- **why worth adding**: confirms GM's participation in the national Heat
  Network Zoning Pilot, five identified strategic zones (Manchester City
  Centre, Manchester OPEN, Salford Eccles, Stockport Town Centre, Trafford),
  and names "heat recovered from industry and urban infrastructure...or
  energy from waste plants" as network inputs. Manchester City Council's own
  domain (manchester.gov.uk) consistently returned HTTP 403 to the fetch tool
  this session (see unverified section) - this GMCA page is the best
  confirmed substitute covering the same Manchester heat-zoning program.
- **verified**: yes. WebFetch confirmed GMCA operates the site, describes the
  Heat Network Zoning Pilot participation and the five strategic zones.

---

### 14. Métropole de Lyon - Schéma Directeur des Énergies (France)

- **name**: Métropole de Lyon - Schéma Directeur des Énergies (SDE)
- **proposed id**: `grandlyon_sde`
- **base_url**: `https://www.grandlyon.com`
- **start_paths**: `/actions/le-schema-directeur-des-energies-sde`
- **level**: local (métropole - equivalent to a combined city/county authority)
- **access**: none (open, no key)
- **coverage**: region: `["eu", "eu_central", "france", "lyon"]`; category:
  `district_heating`; tags: `["waste_heat", "district_heating", "planning"]`;
  policy_types: `["strategy"]`; language: `fr`
- **format**: HTML
- **practical**: standard 2s rate limit; SDE adopted May 2019, targets through
  2030 (20% energy-consumption cut, 17% renewable/recovery share, 43% GHG cut).
- **effort tier**: b (plain crawl domain)
- **why worth adding**: Lyon's own energy master plan naming district heat
  network expansion (200,000 connected homes by 2030) and industrial
  waste-heat recovery (Chemistry Valley) as core levers - the closest French
  metropole equivalent to German kommunale Wärmeplanung. A WebSearch snippet
  (not independently confirmed on this specific page) cited an industry
  estimate of 780 GWh of "chaleur fatale" gisement from Lyon-area data centers
  specifically - worth a human follow-up against the underlying Urbalyon/
  Cerema technical studies if data-center-specific detail is wanted.
- **verified**: yes for the page itself. WebFetch confirmed live, official
  Métropole de Lyon page, describes SDE targets and industrial waste-heat
  recovery in general terms. Data centers are **not** named on this specific
  page (the 780 GWh figure traces to a separate technical study PDF not
  independently fetched this session).

---

### 15. Eurométropole de Strasbourg - Schéma Directeur des Réseaux de Chaleur (France)

- **name**: Eurométropole de Strasbourg - Schéma Directeur des Réseaux de Chaleur (SDRC)
- **proposed id**: `strasbourg_eu_sdrc`
- **base_url**: `https://www.strasbourg.eu`
- **start_paths**: `/-/schema-directeur-reseaux-de-chaleur`
- **level**: local (métropole)
- **access**: none (open, no key)
- **coverage**: region: `["eu", "eu_central", "france", "strasbourg"]`;
  category: `district_heating`; tags: `["waste_heat", "district_heating",
  "mandates", "planning"]`; policy_types: `["strategy", "regulation"]`;
  language: `fr`
- **format**: HTML
- **practical**: standard 2s rate limit; SDRC update approved June 27, 2025.
- **effort tier**: b (plain crawl domain)
- **why worth adding**: updated master plan targeting 100% renewable/recovered
  heat by 2050, doubling inner-ring network infrastructure by 2030, and -
  distinct from Lyon/Nantes above - explicitly approving **mandatory
  connection requirements** for new buildings and major renovations in
  classified network zones (Strasbourg Centre, Wacken). This is the clearest
  French municipal example of a compulsory-connection instrument (the
  regulatory mechanism the brief specifically flags) with a live, current
  (2025) adoption date.
- **verified**: yes. WebFetch confirmed live, official Eurométropole de
  Strasbourg page, describes the June 2025 SDRC update including the
  mandatory-connection-zone approval. Data centers not named on this page.

---

### 16. Bordeaux Métropole - Réseaux de Chaleur + Open Data Mandatory-Connection Perimeter (France)

- **name**: Bordeaux Métropole - Réseaux de Chaleur (+ mandatory-connection-zone open data)
- **proposed id**: `bordeaux_metropole_reseaux_chaleur`
- **base_url**: `https://www.bordeaux-metropole.fr`
- **start_paths**:
  - `/metropole/projets-en-cours/transition-energetique/reseaux-chaleur`
- **companion dataset** (separate domain, not a duplicate of the
  `data_gouv_fr_api` national indexer already proposed in wave 2 - this is
  Bordeaux Métropole's own OpenDataSoft portal with live GIS/API access):
  `https://opendata.bordeaux-metropole.fr/explore/dataset/eg_raccordement_s/`
  (dataset id `eg_raccordement_s`, GeoJSON/Carto API/OGC WMS available)
- **level**: local (métropole)
- **access**: none (open, no key)
- **coverage**: region: `["eu", "eu_central", "france", "bordeaux"]`;
  category: `district_heating`; tags: `["waste_heat", "district_heating",
  "mandates", "planning"]`; policy_types: `["strategy", "regulation"]`;
  language: `fr`
- **format**: HTML (metropole page) + GeoJSON/API (opendata portal)
- **practical**: standard 2s rate limit for the HTML page; the opendata
  portal supports direct GeoJSON/Carto-API/OGC-WMS queries - could be
  upgraded to a structured source later, but the immediate ask is crawl-tier.
- **effort tier**: b (plain crawl domain); the opendata sub-source could
  become tier c (a generic OpendataSoft/Explore API client would also cover
  many other French metropole portals, similar to the CKAN-consolidation
  note in `new-clients-wave2.md`) if this pattern recurs.
- **why worth adding**: Bordeaux Métropole's dataset literally titled
  "Périmètre de raccordement obligatoire au réseau de chaleur urbain"
  (mandatory-connection-perimeter for the urban heat network) is a real,
  GIS-mapped regulatory instrument - the exact mechanism French heat-network
  law uses to compel new/renovated buildings above a threshold to connect.
  This is the metropole's own authoritative source (distinct from and richer
  than the national `data_gouv_fr_api` metadata stub referencing the same
  dataset by title only).
- **verified**: yes for both. WebFetch confirmed the metropole page is
  official (describes heat-network expansion targets, 80% renewable/recovery
  share, waste-incineration and wastewater heat recovery) though it frames
  connection as optional in its own marketing copy - and separately confirmed
  the opendata portal dataset is live, official Bordeaux Métropole
  infrastructure (not data.gouv.fr), with working GeoJSON/API export options.
  Neither page names data centers specifically.

---

### 17. Nantes Métropole - Réseaux de Chaleur (France)

- **name**: Nantes Métropole - Réseaux de chaleur, une énergie locale et compétitive
- **proposed id**: `nantes_metropole_reseaux_chaleur`
- **base_url**: `https://metropole.nantes.fr`
- **start_paths**:
  - `/ma-ville-ma-metropole/les-grands-projets/reseaux-de-chaleur-une-energie-locale-et-competitive-pour-alimenter-le-territoire`
- **level**: local (métropole)
- **access**: none (open, no key)
- **coverage**: region: `["eu", "eu_central", "france", "nantes"]`; category:
  `district_heating`; tags: `["waste_heat", "district_heating", "planning"]`;
  policy_types: `["strategy"]`; language: `fr`
- **format**: HTML (page links to a downloadable "Schéma directeur des
  réseaux de chaleur" PDF summary, not independently fetched this session)
- **practical**: standard 2s rate limit; 9 new networks planned, various
  completion phases 2026-2030.
- **effort tier**: b (plain crawl domain)
- **why worth adding**: 43,400 homes already served at 74%
  renewable/recovery-energy share (mostly waste-incineration heat), with a
  master-plan expansion targeting 100% renewable/recovery by 2050 - a solid,
  currently-uncovered French metropole with an explicit "chaleur fatale"
  framing, rounding out coverage alongside Lyon/Strasbourg/Bordeaux.
- **verified**: yes. WebFetch confirmed live, official Nantes Métropole page,
  describes network scale, renewable/recovery share, and expansion plan.
  Data centers not named on this page.

---

## Unverified / needs-human-check

- **Amsterdam - Transitievisie Warmte / Warmteprogramma**
  (`https://www.amsterdam.nl/wonen-leefomgeving/duurzaam-amsterdam/amsterdam-aardgasvrij/`
  and the linked
  `/inspraak-transitievisie-warmte/samenvatting-transitievisie-warmte/`
  summary page) - WebFetch returned HTTP 403 on **every** amsterdam.nl URL
  tried this session (bot-blocking, not a dead site - the domain is Amsterdam's
  real municipal site and is extensively cited by third parties). A companion
  page on a **different** domain,
  `https://openresearch.amsterdam/en/page/63522/transitievisie-warmte-amsterdam`
  (also an official City of Amsterdam research portal), **was** successfully
  fetched and confirms the Transitievisie Warmte exists, was adopted September
  2020, and covers gas-free timelines per neighborhood - but that specific
  fetched page did not itself contain district-heating/waste-heat/data-center
  detail (the linked full PDF report wasn't fetched). Recommend either (a) a
  human/differently-configured fetch confirm amsterdam.nl directly, or (b) use
  `openresearch.amsterdam` as the crawl base_url instead, accepting it as a
  secondary official domain. Amsterdam is too large a DC/heat market to skip
  entirely, but neither domain was cleanly verified end-to-end this session.

- **Stadt Stuttgart - Kommunaler Wärmeplan**
  (`https://www.stuttgart.de/leben/umwelt/energie/energieleitplanung/kommunaler-waermeplan/`)
  - WebFetch returned HTTP 403 on every stuttgart.de URL tried (root heat-plan
    page and the FAQ subpage both blocked). WebSearch results directly quote
  the official page content, however: Gemeinderat adopted the plan December
  2023, tech mix is geothermal/wastewater-heat/river-heat/industrial waste
  heat/solar-thermal, and it explicitly cites the University of Stuttgart's
  HLRS III supercomputer center's waste heat being reused on the Vaihingen
  campus since 2012. High-confidence based on search snippets, but the page
  itself could not be independently fetched this session - flag for a human
  or differently-configured crawl to confirm live access before enabling.

- **Stadt Köln - Kommunale Wärmeplanung** (`https://www.stadt-koeln.de/artikel/74262/index.html`)
  is verified live and official (see candidate list - not moved here), but a
  second related URL,
  `https://www.stadt-koeln.de/politik-und-verwaltung/presse/mitteilungen/28239/index.html`
  (press release "Kommunale Wärmeplanung ist fertiggestellt") was found via
  search but not independently fetched - worth adding as an additional
  start_path if the base entry is enabled.

- **Manchester City Council** (`https://www.manchester.gov.uk/planning-and-regeneration/regeneration/city-centre-growth-and-infrastructure/city-centre-regeneration-areas/civic-quarter-heat-network`
  and the parent regeneration-areas index) - WebFetch returned HTTP 403 on
  both URLs tried. The GMCA-run `gmgreencity.com` entry (candidate #13) covers
  the same Greater Manchester heat-zoning program and **is** verified, and
  confirms a live "Manchester Civic Quarter" heat network exists - but
  Manchester City Council's own domain specifically could not be confirmed
  this session. Worth a follow-up if manchester.gov.uk-specific content
  (planning conditions, connection requirements) is wanted beyond what GMCA
  publishes.

- **Grenoble - Compagnie de Chauffage (CCIAG)** - confirmed to exist and
  operate France's second-largest heat network (177km, ~100,000 home
  equivalents, 82% renewable/recovery including a 100%-wood Biomax plant), but
  no page found this session with explicit chaleur-fatale-from-datacenters
  or connection-mandate policy language strong enough to write up as a full
  candidate. `compagniedechauffage.fr` (the operator, not the métropole) and
  `grenoblealpesmetropole.fr/186-me-raccorder-au-reseau-de-chaleur.htm` (the
  métropole's connection-instructions page) are both live per search results
  but neither was independently fetched. Worth a follow-up pass specifically
  on the métropole's connection page for mandate language.

- **Stockholms Stad - Klimathandlingsplan 2030** (PDF at
  `https://start.stockholm/globalassets/start/om-stockholms-stad/politik-och-demokrati/styrdokument/klimathandlingsplan-2030.pdf`)
  - `start.stockholm` is Stockholm's own formal municipal policy-document
  domain (distinct from the `vaxer.stockholm` planning-projects subdomain
  used for candidate #8). Confirmed to exist via WebSearch; not independently
  fetched this session. Likely a strong companion/alternative entry to #8 if
  a human confirms it resolves and contains heat-network content beyond the
  Akalla page already verified.

- **HOFOR (Copenhagen)** - re-confirmed not worth proposing; already checked
  and rejected in wave 1 (`regions/nordic.md`) as marketing-only with no
  policy content. Not re-tested this session; VEKS (candidate #7) is the
  Copenhagen-area source that does clear the bar.

- **Rotterdamse Warmte** (`https://rotterdamsewarmte.nl`) - the Schiebroek/
  110-Morgen datacenter-to-heat-network project (10,000+ homes) is real and
  well-covered in Dutch trade press, but the delivery vehicle is a private
  company (Enertrans BV), not a government site - same category problem as
  HOFOR. Not proposed. The City of Rotterdam's own page
  (`rotterdam.nl/klimaatdoelen-warmtesysteem`, candidate list, verified) is
  the appropriate government-source stand-in, even though it doesn't name
  Schiebroek or data centers specifically on that page.

---

## Summary of proposed config file placement

| id | target file | new file needed? |
|---|---|---|
| `helen_fi_dc_heat_recovery` | `config/domains/nordic.yaml` | no |
| `noord_holland_datacenters` | `config/domains/netherlands.yaml` | no |
| `gla_heat_networks_london` | `config/domains/uk.yaml` | no |
| `eindhoven_warmteprogramma` | `config/domains/netherlands.yaml` | no |
| `leeds_gov_uk_ldo3_heat_network` | `config/domains/uk.yaml` | no |
| `klimaoslo_no_dc_heat` | `config/domains/nordic.yaml` | no |
| `veks_dk` | `config/domains/denmark.yaml` | no |
| `stockholm_stad_akalla_dataparks` | `config/domains/sweden.yaml` | no |
| `frankfurt_kommunale_waermeplanung` | `config/domains/germany.yaml` | no |
| `muenchen_waermewende` | `config/domains/germany.yaml` | no |
| `kk_dk_klimaplan` | `config/domains/denmark.yaml` | no |
| `bristol_gov_uk_heat_network_ldo` | `config/domains/uk.yaml` | no |
| `gmca_heat_networks` | `config/domains/uk.yaml` | no |
| `grandlyon_sde` | `config/domains/france.yaml` | no |
| `strasbourg_eu_sdrc` | `config/domains/france.yaml` | no |
| `bordeaux_metropole_reseaux_chaleur` | `config/domains/france.yaml` | no |
| `nantes_metropole_reseaux_chaleur` | `config/domains/france.yaml` | no |
| `stadt_koeln_kwp` (Cologne KWP, not separately numbered above - see notes) | `config/domains/germany.yaml` | no |
| `denhaag_aardgasvrij` (Den Haag, see notes) | `config/domains/netherlands.yaml` | no |
| `rotterdam_klimaatdoelen_warmte` (Rotterdam, see notes) | `config/domains/netherlands.yaml` | no |
| `stuttgart_kommunaler_waermeplan` (unverified - see above) | `config/domains/germany.yaml` | no |
| `rijksoverheid_wcw` (Wet collectieve warmte, national bonus) | `config/domains/netherlands.yaml` | no |

Additional verified-but-not-fully-numbered-above candidates referenced in the
ranked list and dedup notes (Cologne KWP, Den Haag, Rotterdam, and the national
Rijksoverheid Wcw page) are detailed below for completeness since they were
independently verified but ranked lower than the top 17:

### 18. Stadt Köln - Kommunale Wärmeplanung (KWP) (Germany)

- **base_url**: `https://www.stadt-koeln.de`; **start_paths**:
  `/artikel/74262/index.html`, `/artikel/73185/index.html`
- **level**: local; **access**: none; **language**: de
- region: `["eu","eu_central","germany","nordrhein_westfalen","koeln"]`;
  category: `district_heating`; tags: `["waste_heat","district_heating","planning"]`;
  policy_types: `["strategy"]`
- **why**: Cologne's completed (published Nov-Dec 2025) municipal heat plan,
  legally required for cities >100k population by June 30, 2026; identifies
  industrial waste-heat and renewable potential per district.
- **verified**: yes - WebFetch confirmed live official Stadt Köln page,
  describes KWP legal basis (Wärmeplanungsgesetz, Gebäudeenergiegesetz) and
  consultation process. No data-center-specific mention on this page.
- **effort tier**: b

### 19. Gemeente Den Haag - Den Haag Aardgasvrij / Transitievisie Warmte (Netherlands)

- **base_url**: `https://www.denhaag.nl`; **start_paths**:
  `/nl/natuur-en-milieu/duurzaamheid/den-haag-aardgasvrij/`
- **level**: local; **access**: none; **language**: nl
- region: `["eu","eu_west","netherlands","denhaag"]`; category:
  `district_heating`; tags: `["district_heating","planning"]`; policy_types:
  `["strategy"]`
- **why**: The Hague's heat-transition hub, links to the 2023 Transitievisie
  Warmte (74% of neighborhoods best suited to a heat network per the city's
  own analysis) and the forthcoming Warmteprogramma (due late 2026).
- **verified**: yes - WebFetch confirmed live, official, on-topic, links to
  the full Transitievisie Warmte document.
- **effort tier**: b

### 20. Gemeente Rotterdam - Klimaatdoelen Warmtesysteem (Netherlands)

- **base_url**: `https://www.rotterdam.nl`; **start_paths**:
  `/klimaatdoelen-warmtesysteem`
- **level**: local; **access**: none; **language**: nl
- region: `["eu","eu_west","netherlands","rotterdam"]`; category:
  `district_heating`; tags: `["district_heating","planning"]`; policy_types:
  `["strategy"]`
- **why**: Rotterdam's own heat-system climate-goals page, references the
  2021 Warmtevisie; Rotterdam's port/industrial waste-heat base (AVR
  incinerator) is the largest in the Netherlands, and (per separate trade-press
  coverage, not this page) two data centers near Zestienhoven are already
  contracted to feed the Schiebroek/110-Morgen network build-out starting
  2026.
- **verified**: yes for the page itself - WebFetch confirmed live, official,
  on-topic (heat-transition goals, references Warmtevisie 2021). Does not
  itself name restwarmte or data centers.
- **effort tier**: b

### 21. Rijksoverheid - Wet Collectieve Warmte (Wcw) (Netherlands, national - bonus)

- **base_url**: `https://www.rijksoverheid.nl`; **start_paths**:
  `/onderwerpen/energie-thuis/meer-huizen-en-gebouwen-aansluiten-op-collectieve-warmte`
- **level**: national (included per the task brief's explicit mention of the
  Wcw; not itself municipal, but the law this entire municipal tier
  implements - complements the existing `wetten_overheid_nl` general-search
  entry in `netherlands.yaml` with the specific policy-hub page)
- **access**: none; **language**: nl
- region: `["eu","eu_west","netherlands"]`; category: `regulatory`; tags:
  `["mandates","district_heating"]`; policy_types: `["law","regulation"]`
- **why**: the Wcw (in force January 1, 2027) replaces the 2014 Warmtewet,
  requires heat companies to be majority publicly owned, and is the legal
  foundation compelling Dutch municipalities to run the Warmteprogramma
  process cited throughout the Netherlands candidates above.
- **verified**: yes - WebFetch confirmed live, official Rijksoverheid page,
  summarizes Wcw provisions (public-ownership requirement, cost-based
  pricing, 2027 effective date).
- **effort tier**: b (national legislative/regulatory guidance page; not a
  new structured client - fits the existing crawl-domain pattern)
