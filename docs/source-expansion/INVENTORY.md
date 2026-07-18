# Source Expansion Inventory

Consolidated ranked inventory of every candidate surfaced by the 11
region-research agents (`docs/source-expansion/regions/*.md`). Transcription
and organization only — no new sources invented, nothing enabled. Every
crawl-domain candidate is drafted at
`docs/source-expansion/draft/crawl/<region>.yaml` with `enabled: false`;
every tier-c (new client needed) candidate is specced at
`docs/source-expansion/draft/new-clients.md`.

## Schema note (read before using the drafts)

`config/domains/_template.yaml`'s comment block lists a small illustrative
set of `region`/`category`/`tags`/`policy_types` values. The **actual**
validation enums live in `src/core/config.py` (`VALID_REGIONS`,
`VALID_CATEGORIES`, `VALID_TAGS`, `VALID_POLICY_TYPES`) and are far larger —
they already include `canada`, `south_africa`, `uae`, individual German
Länder, Swiss cantons, Indian/Australian states, `legislation` as a
category, `waste_heat`/`district_heating`/`pue_limits` as tags, etc. An
unrecognized region value only produces a config-loader **warning**, never a
hard failure (`src/core/config.py` ~line 629). The drafts below map every
region-file value to the richer `src/core/config.py` enum first, and only
fall back to a genuinely "closest allowed" substitution (noted inline) for
the handful of values that fit neither list — e.g. "supranational"/"global"
(used by IEA 4E EDNA, C40, ISO/IEC 30134, OECD SDMX), which aren't in either
enum today and are flagged as a recommended small addition rather than
force-mapped into "eu" or "apac".

## Totals

| Metric | Count |
|---|---|
| **Total verified candidates (unique, deduped)** | **154** |
| Tier a (drops into existing client) | 0 |
| Tier b (plain crawl domain) | 138 |
| Tier c (needs a new structured client) | 16 |
| Duplicates merged | 1 — data.europa.eu Search API, independently proposed in both `eu-uncovered.md` and `supranational.md`, merged into one entry (`data_europa_eu_search_api`) |
| Unverified / needs-human-check items (appendix) | 45 |

### By region file

| Region file | Verified (unique contribution) | Tier b | Tier c |
|---|---|---|---|
| us-states.md | 10 | 10 | 0 |
| canada.md | 10 | 9 | 1 |
| nordic.md | 7 | 5 | 2 |
| dach.md | 22 | 22 | 0 |
| eu-uncovered.md | 27 | 23 | 4 |
| uk-ireland.md | 6 | 4 | 2 |
| east-asia.md | 15 | 11 | 4 |
| oceania-south-asia.md | 21 | 20 | 1 |
| mena-africa.md | 12 | 12 | 0 |
| latam.md | 16 | 15 | 1 |
| supranational.md | 8 (1 more, `data_europa_eu_search_api`, counted under eu-uncovered.md as the merge target) | 7 | 1 |
| **Total** | **154** | **138** | **16** |

---

## Master table — Tier c (new structured client needed), ranked best-first

Full technical spec + draft `api_sources.yaml` entries for every row:
`docs/source-expansion/draft/new-clients.md`.

| # | Name | id | Level | Access | Region file | Why |
|---|---|---|---|---|---|---|
| 1 | Houses of the Oireachtas Open Data API | `oireachtas_api` | national | none | uk-ireland.md | Verified end-to-end incl. a working keyword query against the Heat (Networks and Miscellaneous Provisions) Bill 2024 — Ireland's only legislative API of any kind |
| 2 | European Parliament Open Data API v2 | `europarl_opendata_api` | supranational | none | eu-uncovered.md | Only pan-EU source exposing the legislative process itself (amendments, committee reports, votes), not just final law text |
| 3 | LeyChile / BCN Legislative Web Service | `leychile_api` | national | none | latam.md | Only genuine open-data legislative API found across all 6 LatAm countries in scope |
| 4 | New Zealand Legislation API | `nz_legislation_api` | national | api_key (email request) | oceania-south-asia.md | Real, documented gov JSON API for NZ Acts/Bills/regs — zero prior NZ legislative coverage |
| 5 | data.europa.eu Search API | `data_europa_eu_search_api` | supranational | none | eu-uncovered.md (cross-listed in supranational.md — merged) | One integration surfaces energy/waste-heat datasets from every EU member state's open-data catalog |
| 6 | Scottish Parliament Open Data API | `scottish_parliament_api` | subnational (Scotland) | none | uk-ireland.md | Live JSON bill/event API; Scotland has the UK's most advanced heat-network legislation |
| 7 | e-Gov Law Search API v2 (Japan) | `egov_law_api` | national | none | east-asia.md | Keyless documented API trading a Playwright-scraped search UI for the same EE law corpus |
| 8 | Storting Open Data API (Norway) | `stortinget_api` | national | none | nordic.md | Completes structured-API coverage for the Nordic "big three" parliaments |
| 9 | Eduskunta Avoin Data API (Finland) | `eduskunta_api` | national | none | nordic.md | Confirmed live JSON tables; completes all 3 largest Nordic parliaments with an API |
| 10 | Donnees Quebec — Projets de loi | `donneesquebec_bills` | subnational (Quebec) | none | canada.md | Only genuinely open-data provincial bill tracker found; CKAN, real-time updates (CC-BY-NC license — flag for legal review) |
| 11 | Verkhovna Rada Open Data Portal (Ukraine) | `rada_opendata_ua` | national | none | eu-uncovered.md | Would track Ukraine's district-heating reform bill through the bill-registration dataset |
| 12 | data.gov.cy Open Data Portal | `data_gov_cy_energy` | national | none | eu-uncovered.md | Government catalog grouped by ministry — pulls Cyprus energy datasets without a bespoke scraper |
| 13 | Open Law API (South Korea) | `open_law_kr_api` | national | api_key | east-asia.md | 191-API documented XML service over the same statutory corpus as the existing `law_kr` crawl entry |
| 14 | Open National Assembly Information OpenAPI (South Korea) | `open_assembly_kr_api` | national | api_key | east-asia.md | Pre-enactment bill tracking to complement the enacted-law crawl |
| 15 | OECD SDMX Statistics API | `oecd_sdmx_api` | supranational/global | none | supranational.md | Keyless global stats gateway; hold until the PINE dataflow ID is confirmed reachable |
| 16 | Singapore Open Data Portal | `data_gov_sg` | national | none (unconfirmed) | east-asia.md | Lowest-confidence entry — no relevant dataset confirmed yet, contingent |

---

## Master table — Tier b (plain crawl domain), grouped by region file, ranked best-first within each

Full YAML for every row (exact `_template.yaml` schema, `enabled: false`):
`docs/source-expansion/draft/crawl/<region>.yaml`.

### us-states.md — 10

| # | Name | id | Level | Access | Why |
|---|---|---|---|---|---|
| 1 | Virginia SCC — Case Information / Docket Search | `va_scc` | subnational | none | GS-5 large-load rate class implementing body for VA's ~450 data centers |
| 2 | Georgia PSC — Data Center / Large-Load Rulemaking | `ga_psc` | subnational | none | 100MW large-load threshold + 2028 rate freeze, Docket #44280 |
| 3 | Texas PUC Interchange — Large Load Interconnection (Project 58481) | `tx_puc_interchange` | subnational | none | Live SB6 large-load interconnection rulemaking docket, 203+ filings |
| 4 | New York DPS/PSC — Large Load Interconnection Reform | `ny_dps` | subnational | none | Feb 2026 proceeding, 11.9GW in NYISO queue |
| 5 | Oregon PUC — Large Customer / Data Center Tariffs | `or_puc_large_load` | subnational | none | First-in-nation dedicated waste-heat-adjacent large-load Schedule 96 |
| 6 | Missouri PSC — Large Load / Data Center Rate Cases | `mo_psc` | subnational | none | Live, contested Ameren Missouri large-load rate case |
| 7 | Missouri DNR — Division of Energy | `mo_energy_division` | subnational | none | Replaces an empty stub with MO's general energy office |
| 8 | Loudoun County, VA — Data Center Standards & Locations | `us_loudoun_county_va` | local | none | Most concrete local-govt DC waste-heat-reuse consideration found in the US |
| 9 | Prince William County, VA — Data Center Ordinance Advisory Group | `us_prince_william_county_va` | local | none | Second-largest VA DC locality's ordinance/zoning history (archival) |
| 10 | Nebraska DWEE | `ne_dwee` | subnational | none | Replaces an empty stub; no DC-specific content found yet |

### canada.md — 9

| # | Name | id | Level | Access | Why |
|---|---|---|---|---|---|
| 1 | AESO — Large Load Projects (Data Centres) | `aeso_large_load` | subnational (Alberta) | none | Live grid-connection framework for DCs, discusses waste-heat/self-gen |
| 2 | BC Utilities Commission — Thermal Energy Systems | `bcuc_thermal` | subnational (BC) | none | Regulates BC's legal term for district heating/cooling systems |
| 3 | City of Vancouver — False Creek NEU | `vancouver_neu` | local | none | City-owned DH utility, 70% literal sewage waste-heat recovery |
| 4 | Markham District Energy Inc. | `markham_district_energy` | local | none | Retrofitted an Equinix DC for heat recovery into a municipal network |
| 5 | City of Toronto — District Energy | `toronto_district_energy` | local | none | Ties DH to TransformTO climate plan, mentions DCs as anchor loads |
| 6 | NRC — National Energy Code of Canada for Buildings | `nrc_codes_canada` | national | none | Baseline efficiency standard every province references/adopts |
| 7 | Regie de l'energie (Quebec) | `regie_energie_qc` | subnational (Quebec) | none | Quebec's DH/utility regulator, active heat-decarbonization dossiers |
| 8 | Legislative Assembly of Ontario — Bills | `ola_bills` | subnational (Ontario) | none | Fills Ontario's legislative-bill gap, Canada's largest DC-market province |
| 9 | Government of Manitoba — Energy Efficiency | `manitoba_energy` | subnational (Manitoba) | none | First Manitoba entry; industrial waste-heat/bioenergy incentives |

### nordic.md — 5

| # | Name | id | Level | Access | Why |
|---|---|---|---|---|---|
| 1 | NVE Guide to the Waste Heat CBA Regulation (Norway) | `nve_overskuddsvarme_guide` | national | none | Regulator's own operational guidance for the exact DC waste-heat mandate already tracked |
| 2 | Island.is Regulations Database (Iceland) | `island_is_reglugerdir` | national | none | Closes Iceland's national legislation-database gap |
| 3 | Stockholm Exergi — Open District Heating | `stockholm_exergi_odh` | subnational/local | none | Operational mechanism for 30+ Stockholm DCs to sell waste heat into DH |
| 4 | Finnish Energy (Energiateollisuus) | `energiateollisuus_fi` | national | none | Trade body for DH utilities receiving DC waste heat, takes legislative positions |
| 5 | Veitur — District Heating Network (Iceland) | `veitur_is` | subnational/local | none | Dominant Icelandic DH operator, thin on policy content |

### dach.md — 22

| # | Name | id | Level | Access | Why |
|---|---|---|---|---|---|
| 1 | Geneve — Loi sur l'energie (LEn) | `ge_len_energie` | subnational (canton) | none | Explicitly names DC "serveurs informatiques" heat in mandatory recovery law |
| 2 | Basel-Stadt — Energiegesetz (EnG) | `bs_energiegesetz` | subnational (canton) | none | Large-consumer waste-heat + heat-planning duty naming "Rechenzentren" |
| 3 | Vaud — Legislation sur l'energie (LVLEne) | `vd_energie_legislation` | subnational (canton) | none | Large-consumer + territorial energy planning, same MuKEn threshold |
| 4 | Bern — WEU Energie | `be_weu_energie` | subnational (canton) | none | Cantonal energy directorate, municipal plans account for DC waste-heat |
| 5 | Rheinland-Pfalz — MWTEK | `rlp_energy` | subnational (Land) | none | State law implementing federal municipal heat-planning duty |
| 6 | Landesrecht Rheinland-Pfalz | `rlp_recht` | subnational (Land) | none | Consolidated state law database |
| 7 | Brandenburg — MWEKE | `brandenburg_energy` | subnational (Land) | none | State heat-planning ordinance, Potsdam heat-plan deadline 2026 |
| 8 | BRAVORS (Brandenburg) | `brandenburg_recht` | subnational (Land) | none | State law/regulation search |
| 9 | Sachsen-Anhalt — MWU | `sachsen_anhalt_energy` | subnational (Land) | none | Cabinet-approved municipal heat-planning implementation, concrete deadlines |
| 10 | Landesrecht Sachsen-Anhalt | `sachsen_anhalt_recht` | subnational (Land) | none | Consolidated state law database |
| 11 | Schleswig-Holstein — MEKUN | `schleswig_holstein_energy` | subnational (Land) | none | State climate law mandates heat planning for 1,104 municipalities |
| 12 | Gesetze-Rechtsprechung Schleswig-Holstein | `schleswig_holstein_recht` | subnational (Land) | none | 1,400+ consolidated state laws |
| 13 | Saarland — Warmewende (MWIDE) | `saarland_energy` | subnational (Land) | none | Dedicated Warmewende advisory office + state study |
| 14 | Buergerservice Saarland | `saarland_recht` | subnational (Land) | none | Only Saarland state-law source |
| 15 | Mecklenburg-Vorpommern — Energy Ministry | `mv_energy` | subnational (Land) | none | Rural/low-density heat-network policy posture, useful contrast |
| 16 | Landesrecht Mecklenburg-Vorpommern | `mv_recht` | subnational (Land) | none | Consolidated state law database |
| 17 | Bremen — Warmewende | `bremen_energy` | subnational (Land) | none | City-state heat-planning draft, heat plan due Jun 2026 |
| 18 | Bremische Vorschriften | `bremen_recht` | subnational (Land) | none | 600+ consolidated laws, transparency-portal platform |
| 19 | ThEGA — Kommunale Waermeplanung (Thueringen) | `thueringen_thega` | subnational (Land) | none | Runs the state waste-heat cadastre for third-party reuse registration |
| 20 | Landesrecht Thueringen | `thueringen_recht` | subnational (Land) | none | Completes German 16/16 Laender law-database coverage |
| 21 | Klima- und Energiefonds (Austria) | `at_klimafonds` | national | none | National incentive fund, direct grants for low-temp waste heat |
| 22 | Wien — Energieplanung (MA 20) | `at_wien_ma20` | subnational (Vienna) | none | Austria's primary DC market, produces the Wiener Warmeplan 2040 |

### eu-uncovered.md — 23

| # | Name | id | Level | Access | Why |
|---|---|---|---|---|---|
| 1 | Ministry of Physical Planning — Energy Efficiency (Croatia) | `mpgi_hr_energy_efficiency` | national | none | Lists Croatia's EE Act, Building Act, EPBD transposition |
| 2 | Croatian Energy Regulatory Agency (HERA) | `hera_hr` | national | none | Direct authority for DH tariff/pricing decisions |
| 3 | Ministry of Economy (Croatia) | `mingo_gov_hr` | national | none | Primary energy ministry — partial verification only |
| 4 | Portal Energetika (Slovenia) | `energetika_portal_si` | national | none | Ministry-run energy hub, building renovation grants |
| 5 | Energy Directorate (Slovenia) | `gov_si_energy_directorate` | national | none | Ministry unit implementing EE/RES incentive programs |
| 6 | Agencija za energijo (Slovenia) | `agen_rs_si` | national | none | Heat-network regulator entry for Slovenia |
| 7 | ARSO Environmental Indicators — DH efficiency (Slovenia) | `arso_kazalci_district_heating` | national | none | Rare structured ground-truth waste-heat-share data |
| 8 | SEDA/SEEA (Bulgaria) | `seea_government_bg` | national | none | Administers national efficiency-obligation scheme |
| 9 | EWRC/KEVR (Bulgaria) | `dker_bg` | national | none | Heat-network/tariff regulator |
| 10 | Ministry of Energy (Bulgaria) | `me_government_bg` | national | none | Primary national ministry of record |
| 11 | Public Utilities Commission — DH (Latvia) | `sprk_gov_lv` | national | none | Detailed DH regulation scope, concrete thresholds |
| 12 | Ministry of Climate and Energy (Latvia) | `em_gov_lv` | national | none | Tasked with promoting waste-heat recovery per NECP |
| 13 | Energy Agency of Serbia (AERS) | `aers_rs` | national | none | Laws + Secondary Legislation sections |
| 14 | Ministry of Mining and Energy (Serbia) | `mre_gov_rs` | national | none | Origin of the Law on EE and Rational Use of Energy |
| 15 | NEURC (Ukraine) | `nerc_gov_ua` | national | none | Heat-sector regulator, dedicated Heat section |
| 16 | Ministry of Energy (Ukraine) | `mev_gov_ua` | national | none | Active EE regulatory-acts publisher |
| 17 | Energy Service Ministry (Cyprus) | `energy_gov_cy` | national | none | National EE policy authority |
| 18 | Energy and Water Agency (Malta) | `energywateragency_gov_mt` | national | none | EED Art.11 audit-obligation authority; Malta has no DH networks |
| 19 | REWS (Malta) | `rews_org_mt` | national | none | Completes ministry+regulator pair for Malta |
| 20 | Ministry of Economy (Slovakia) | `economy_gov_sk` | national | none | Responsible for the EE action plan + DH-relevant CHP tenders |
| 21 | URSO — DH (Slovakia) | `urso_gov_sk` | national | none | Only heat-network regulator entry for Slovakia (Slovak-only docs) |
| 22 | VERT (Lithuania) | `vert_lt` | national | none | DH/price regulator; blocked 403 to automated fetch |
| 23 | Ministry of Energy (Lithuania) | `enmin_lrv_lt` | national | none | Content not directly inspected (403) — identity well-corroborated |

### uk-ireland.md — 4

| # | Name | id | Level | Access | Why |
|---|---|---|---|---|---|
| 1 | DCEE — District Heating policy hub (Ireland) | `ie_dcee_district_heating` | national | none | Lead ministry for Heat Networks Bill 2024 + EUR5m DH fund |
| 2 | South Dublin County Council — Tallaght DH Scheme | `sdcc_ie_district_heating` | local | none | Ireland's first DC-waste-heat DH network, 10MW from an Amazon DC |
| 3 | National Infrastructure Commission for Wales (NICW) | `wales_nicw` | subnational | none | Wales Infrastructure Assessment — DH deployment barriers |
| 4 | Utility Regulator (Northern Ireland) | `uregni_general` | subnational | none | NI's Ofgem counterpart, proposed heat-network oversight role |

### east-asia.md — 11

| # | Name | id | Level | Access | Why |
|---|---|---|---|---|---|
| 1 | Tokyo Bureau of Urban Development — DC Guideline | `tokyo_toshiseibi_dc` | local | none | Single highest-value East Asia find: DC waste-heat community reuse funding FY2026 |
| 2 | Beijing Municipal Government — DC Policy | `beijing_gov_dc` | local | none | Most detailed municipal PUE-linked pricing/incentive regime found |
| 3 | Shanghai Municipal Government — DC Policy | `shanghai_gov_dc` | local | none | Numbered municipal regulation with hard PUE thresholds + phase-out |
| 4 | MIIT — Data Center Policy (China) | `miit_cn` | national | none | Named ministry, flagship national 3-Year DC Action Plan |
| 5 | China gov.cn — DC & Energy Notices | `govcn_dc` | national | none | More resilient full-text mirror of MIIT's national policy notice |
| 6 | Hong Kong — Data Centre Facilitation Portal | `datacentre_hk` | national (SAR) | none | Government's own aggregator index of every HK DC energy scheme |
| 7 | EMSD — Energy Management (Hong Kong) | `emsd_hk` | national (SAR) | none | Named regulator, mandatory energy-audit ordinance |
| 8 | Tokyo Bureau of Environment — Cap-and-Trade | `tokyo_kankyo_capandtrade` | local | none | World's first urban cap-and-trade; covers large DCs by threshold |
| 9 | Korea Energy Agency (KEA) | `kea_kr` | national | none | Implementing agency underneath MOTIE's policy |
| 10 | Energy Administration MOEA (Taiwan) | `moeaea_tw` | national | none | Foundational national source — Taiwan had zero prior coverage |
| 11 | Laws & Regulations Database (Taiwan) | `law_moj_tw` | national | none | Bilingual statutory text companion to MOEAEA |

### oceania-south-asia.md — 20

| # | Name | id | Level | Access | Why |
|---|---|---|---|---|---|
| 1 | Australian Energy Regulator (AER) | `aer_au` | national | none | Dedicated Data Centre Connections guidance — most DC-specific reg doc region-wide |
| 2 | Australian Energy Market Commission (AEMC) | `aemc_au` | national | none | Active draft rule on DC grid-connection technical standards |
| 3 | Energy Policy WA | `energy_policy_wa` | subnational | none | WA's state energy-policy body, Pilbara Energy Transition Plan |
| 4 | Queensland Treasury — Energy | `qld_treasury_energy` | subnational | none | Largest AU state not yet covered, Energy Roadmap |
| 5 | Victoria — DEECA Energy | `vic_energy` | subnational | none | Mandatory efficiency scheme; Melbourne is a major AU DC market |
| 6 | EECA (New Zealand) | `eeca_nz` | national | none | Dedicated efficiency-mandate body, Regional Heat Demand Database |
| 7 | MBIE — Energy and Natural Resources (NZ) | `mbie_energy_nz` | national | none | NZ's primary energy-ministry function |
| 8 | Rajasthan Electricity Regulatory Commission | `rerc_in` | subnational | none | New source TYPE for India: first State Electricity Regulatory Commission |
| 9 | Rajasthan Renewable Energy Corp (RRECL) | `rrecl_in` | subnational | none | Nodal agency for India's #1 solar-park state; thin JS content |
| 10 | Haryana Renewable Energy Dev Agency (HAREDA) | `hareda_in` | subnational | none | Renewable-energy nodal agency + EC Act implementer |
| 11 | West Bengal Renewable Energy Dev Agency (WBREDA) | `wbreda_in` | subnational | none | Fills an East-India gap; nodal agency since 1993 |
| 12 | Gujarat Energy Development Agency (GEDA) | `geda_in` | subnational | none | India's #1 renewable-capacity state's SNA/SDA; unreachable this pass |
| 13 | Central Electricity Regulatory Commission (CERC) | `cerc_in` | national | none | National tariff/regulatory body complementing the planning body |
| 14 | India Code | `india_code` | national | none | Authoritative full-text repository of Indian Acts; 403-blocked |
| 15 | PRS Legislative Research | `prs_india` | national | none | Standard India bill-tracking citation — NOT government (judgment call) |
| 16 | Philippines Department of Energy | `doe_ph` | national | none | Actively drafting a DC energization policy — most on-topic PH find |
| 17 | SEDA (Malaysia) | `seda_my` | national | none | Statutory renewable/efficiency authority, FiT + NEM |
| 18 | Energy Commission / Suruhanjaya Tenaga (Malaysia) | `st_my` | national | none | National electricity/gas regulator, complements SEDA |
| 19 | Ministry of Energy and Mineral Resources (Indonesia) | `esdm_id` | national | none | Dedicated EBTKE conservation directorate |
| 20 | Ministry of Industry and Trade (Vietnam) | `moit_vn` | national | none | Energy-labeling program + pricing decrees |

### mena-africa.md — 12

| # | Name | id | Level | Access | Why |
|---|---|---|---|---|---|
| 1 | Israel Ministry of Energy and Infrastructure | `moe_il` | national | none | Inter-ministerial interim DC/server-farm energy-demand policy |
| 2 | RCREEE (17 Arab states) | `rcreee_regional` | supranational | none | One source, 17 countries; NCAP cooling-policy workshop report |
| 3 | Turkey EPDK/EMRA | `epdk_tr` | national | none | National electricity regulator, dedicated Energy Transition section |
| 4 | Nigerian Electricity Regulatory Commission (NERC) | `nerc_ng` | national | none | Africa's largest power market, dedicated Regulatory Instruments hub |
| 5 | EgyptERA | `egyptera_eg` | national | none | Regulator with the actual statutory efficiency mandate |
| 6 | Ghana Energy Commission — EE Regulations | `energycom_gh` | national | none | Explicit MEPS regulations naming "computers" as regulated equipment |
| 7 | Kuwait Ministry of Electricity, Water and Renewable Energy | `mew_kw` | national | none | Only national energy ministry for Kuwait; weak DC content today |
| 8 | AMEE (Morocco) | `amee_ma` | national | none | National EE agency, Thermal Building Regulation (RTCM) |
| 9 | Turkey Ministry of Energy and Natural Resources | `enerji_tr` | national | none | Ministry strategy side complementing EPDK; intermittent access |
| 10 | AFREC (African Union) | `afrec_au` | supranational | none | Continent-wide EE strategy body |
| 11 | Egypt NREA | `nrea_eg` | national | none | Weakest candidate — renewable-generation-focused only |
| 12 | Oman APSR | `apsr_om` | national | none | Sole electricity regulator; JS-shell content not yet readable |

### latam.md — 15

| # | Name | id | Level | Access | Why |
|---|---|---|---|---|---|
| 1 | Ministerio de Energia (Chile) | `energia_cl` | national | none | Primary national policy body, largest LatAm DC market under construction |
| 2 | CNE (Chile) | `cne_cl` | national | none | Electricity/hydrocarbon regulator, discusses DC grid demand growth |
| 3 | SEC (Chile) | `sec_cl` | national | none | Binding technical-standards layer under CNE/ministry policy |
| 4 | Ministerio de Minas y Energia (Colombia) | `minenergia_co` | national | none | National ministry, FENOGE/FNCER incentive funds |
| 5 | UPME (Colombia) | `upme_co` | national | none | PROURE program — analogue to Brazil's PROCEL |
| 6 | CREG (Colombia) | `creg_co` | national | none | Electricity/gas regulator, binding-rule layer |
| 7 | Secretaria de Energia (Argentina) | `energia_ar` | national | none | National energy ministry, efficiency subsecretariat |
| 8 | ENRE (Argentina) | `enre_ar` | national | none | National electricity regulator |
| 9 | MINEM (Peru) | `minem_pe` | national | none | National ministry, growing Lima-area DC market |
| 10 | OSINERGMIN (Peru) | `osinergmin_pe` | national | none | Electricity/energy/mining regulator |
| 11 | MIEM (Uruguay) | `miem_uy` | national | none | EE certificate program, 100%-renewable-grid DC pitch market |
| 12 | URSEA (Uruguay) | `ursea_uy` | national | none | Energy-services regulator |
| 13 | ARESEP (Costa Rica) | `aresep_cr` | national | none | Electricity regulator, near-100%-renewable grid angle |
| 14 | SUIN-Juriscol (Colombia) | `suin_juriscol_co` | national | none | Authoritative full-text Colombian legislation search |
| 15 | InfoLEG (Argentina) | `infoleg_ar` | national | none | National legislative/documentary database |

### supranational.md — 7

| # | Name | id | Level | Access | Why |
|---|---|---|---|---|---|
| 1 | IEA 4E EDNA — Data Centre Energy Efficiency | `iea_4e_edna_datacentres` | supranational | none | IEA's own dedicated DC energy-efficiency policy workstream |
| 2 | CEN-CENELEC-ETSI Green Data Centres Group | `cencenelec_green_datacentres` | supranational | none | The actual joint-ESO body behind EN 50600 |
| 3 | Euroheat & Power — Knowledge Hub | `euroheat_power_knowledge_hub` | supranational | none | Best aggregator of DC-waste-heat-to-DH case studies found |
| 4 | Energy Community Secretariat — Acquis | `energy_community_acquis` | supranational | none | Mechanism transposing EU EED into non-EU SE European states |
| 5 | ASEAN Centre for Energy (ACE) | `asean_centre_for_energy` | supranational | none | Regional multi-country energy policy body — APAC gap |
| 6 | C40 Knowledge Hub — Data Centers | `c40_knowledge_hub` | supranational | none | Live Jan 2026 DC implementation guide for city governments |
| 7 | ISO/IEC 30134 — Data Centre KPI Standards | `iso_iec_30134_datacentre_kpi` | supranational | none | International technical standard underpinning heat-reuse measurement |

---

## New structured clients needed (tier-c)

Full spec (endpoints, CrawlResult field mapping, pagination/rate limits) for
each of the 16 rows above is in
`docs/source-expansion/draft/new-clients.md`, along with draft
`api_sources.yaml` entries (`enabled: false`). Quick-reference summary:

| source_type (proposed) | API base | Auth | Format |
|---|---|---|---|
| `oireachtas` | api.oireachtas.ie | none | JSON (OAS2) |
| `europarl_opendata` | data.europarl.europa.eu | none (500 req/5min) | JSON-LD / RDF |
| `leychile` | www.leychile.cl | none | XML |
| `nz_legislation` | api.legislation.govt.nz | api_key (email request) | JSON |
| `data_europa` | data.europa.eu | none | JSON / SPARQL |
| `scottish_parliament` | data.parliament.scot | none | JSON |
| `egov_law_jp` | laws.e-gov.go.jp | none | JSON / XML |
| `stortinget` | data.stortinget.no | none | XML / JSON |
| `eduskunta` | avoindata.eduskunta.fi | none | JSON |
| `donneesquebec_ckan` | www.donneesquebec.ca | none (CC-BY-NC license) | CSV / JSON (CKAN) |
| `rada_opendata` | data.rada.gov.ua | none | unconfirmed |
| `dkan_cy` | data.gov.cy | none | JSON (DKAN) |
| `open_law_kr` | open.law.go.kr | api_key (phone/email) | XML |
| `open_assembly_kr` | open.assembly.go.kr | api_key (per-endpoint) | JSON / XML |
| `oecd_sdmx` | sdmx.oecd.org | none | XML / JSON / CSV |
| `data_gov_sg` | www.data.gov.sg | none (unconfirmed) | JSON / CSV |

---

## Appendix: Unverified / needs-human-check (45 items)

Every item each region agent explicitly flagged as unverified, could not
reach, or chose not to propose as a candidate — consolidated with the reason
each failed verification. None of these are in the draft crawl YAMLs or
new-clients.md; they need a human (or a differently-configured fetch) before
being turned into a candidate.

### us-states.md (4)

| Item | Reason |
|---|---|
| Illinois "POWER Act" (data-center water/energy/heat-reuse-plan requirements) | Reported to have failed to pass in the 2026 session — no enacted law/docket to point at |
| Washington UTC dedicated large-load rulemaking (`wa_utc`) | No formally docketed rulemaking exists yet (still in technical-workshop/comment phase); recommended only as a lower-confidence "watch" source |
| NY DPS specific order PDF (DocRefId GUID) | PDF binary not text-extractable by the fetch tool; substance corroborated only via secondary news sources |
| Minnesota HF4888 (2025 DC heat-reuse & environmental law) | Real and verified, but `minnesota.yaml` already covers the implementing bodies structurally — not a new domain, a future bill-specific-entry opportunity |

### canada.md (2)

| Item | Reason |
|---|---|
| Nova Scotia Department of Energy (efficiency subpage) | Returned "Access denied" to both fetch tools (bot-detection suspected); department root page loads fine |
| NRC CanmetENERGY district-energy/waste-heat research page | Verified live and highly on-topic, but `base_url` (`natural-resources.canada.ca`) already exists as `nrcan_ca` — recommend appending this path to that entry's `start_paths` instead of a new domain |

### nordic.md (3)

| Item | Reason |
|---|---|
| Nordic Energy Research (nordicenergy.org) | WebFetch returned 403 on every URL (bot-blocking suspected); a live "WasteHeatSES" project page and a Flex4RES report PDF were confirmed only via WebSearch |
| Althingi (Iceland Parliament) open data | No confirmed live Althingi-specific API endpoint found — only a 2016-era resolution directing future open-data legislation |
| HOFOR (Copenhagen DH utility) | Live but customer-facing marketing content only; no waste-heat/DC/regulatory mention, does not clear the "policy document" bar |

### dach.md (5)

| Item | Reason |
|---|---|
| Thueringen Ministry direct site (umwelt.thueringen.de) | Blocked by a Link11 bot-protection CAPTCHA on every attempt (both WebFetch and browser); the ThEGA entry covers the same content as a working substitute |
| Austria E-Control (e-control.at) | Electricity/gas regulator only — no district-heating/waste-heat regulation content found on-site |
| Brandenburg MIL (mil.brandenburg.de) | Co-owns the heat-planning ordinance with MWEKE; not independently verified this pass |
| LEKA MV (leka-mv.de) | MV's energy/climate agency, analogous to ThEGA; referenced by search only, not independently fetched |
| Saarland Waermekataster tool (geoportal.saarland.de) | Referenced from the Saarland ministry page; not independently fetched/verified |

### eu-uncovered.md (10)

| Item | Reason |
|---|---|
| Bulgaria SEEA subpage (/en/about-seda-en) | TLS certificate error on fetch |
| Croatia mingo.gov.hr energy-directorate subpages | Only homepage/redirect verified; specific policy URLs not located |
| Bulgaria Ministry of Energy efficiency/DH-specific paths | Homepage confirmed live; deeper policy subpages not yet located |
| Serbia MRE exact efficiency-sector URL | Cyrillic/Latin URL variants observed; homepage/domain confirmed, exact path not confirmed |
| Slovakia economy.gov.sk energy-efficiency subpages | Homepage/ministry page confirmed; deeper paths not yet located |
| Lithuania VERT + Ministry of Energy | Both return HTTP 403 to automated fetch; real per search-snippet/third-party corroboration only |
| Ukraine data.rada.gov.ua API format | Portal + API link confirmed to exist; request/response format not fetched this session |
| European Parliament developer-corner docs page | WebFetch returned empty content twice (JS-rendered); underlying API independently verified via direct curl |
| Serbia energetskiportal.com | Appears to be a privately-run energy news/info portal, not confirmed official government — excluded per "not news blogs" guidance |
| TED (Tenders Electronic Daily) | Exposes procurement/tender notices, not policy documents — excluded as out of scope |

### uk-ireland.md (3)

| Item | Reason |
|---|---|
| CRU (Ireland) district-heating publications filter | Base_url already present (`cru_ie_dc`); filter UI is JS/AJAX-driven, no working URL-parameter filter found — recommend broadening the existing entry's `start_paths`, not a new domain |
| Dublin City Council district heating / Poolbeg scheme | Referenced in secondary sources; no live `dublincity.ie` page fetched this pass |
| NI Department for the Economy `/articles/heat-networks` | Real page, but `economy-ni.gov.uk` already exists as `uk_ni_economy` — recommend adding this path to that entry instead of a new domain |

### east-asia.md (5)

| Item | Reason |
|---|---|
| Guizhou Provincial Big Data Development and Management Bureau | Every direct fetch returned `ECONNREFUSED`; content described via WebSearch snippets only |
| Beijing DRC 2023 data-center energy-review rules (3rd start_path) | Found via WebSearch, not independently fetched this session |
| Tokyo Bureau of Urban Development landing page | Guideline's existence confirmed via press release; this specific bureau subdomain page located via search only, not independently re-fetched |
| Korea District Heating Corporation (KDHC) | WebFetch returned `ECONNREFUSED`; not confirmed reachable |
| e-Gov Law API v2 machine-readable schema | API/docs confirmed live; Swagger UI is client-rendered, exact schema not confirmed from a text fetch |

### oceania-south-asia.md (2)

| Item | Reason |
|---|---|
| Thailand DEDE (dede.go.th) | curl 200 OK but WebFetch hit a TLS cert error; English subdomain failed to resolve entirely |
| New Zealand Parliament Open Data (data.parliament.nz) | Described in search results as "working on launching our official API... soon"; curl returned 404 at root — not yet stable |

### mena-africa.md (3)

| Item | Reason |
|---|---|
| Qatar Kahramaa — District Cooling (km.qa) | `ECONNREFUSED` on every attempt; Council of Ministers Law No. 19 (2024) and a live design-code PDF referenced via search only |
| Bahrain Sustainable Energy Authority (sea.gov.bh) | DNS failure (`ENOTFOUND`) on every attempt; IEA/ESMAP profile pages cite this as the real domain |
| Kenya EPRA (epra.go.ke) | `ECONNREFUSED` on every attempt; live PDF reports on this domain surfaced via search |

### latam.md (1)

| Item | Reason |
|---|---|
| Direccion de Energia / MINAE (Costa Rica) | `www.minae.go.cr` returned 403 on every attempt; `energia.minae.go.cr` failed DNS resolution entirely — WebSearch confirms the site/content exist but nothing was reachable this session |

### supranational.md (7)

| Item | Reason |
|---|---|
| IEA Policies API (api.iea.org/policies/v2) | Backend responds but every query returned `400 Bad Request`; no public API docs found |
| Climate Policy Radar / climate-laws.org | Confirmed to exist and directly on-topic, but the provider's own site states its API is "coming soon" — not live |
| World Bank RISE | `rise.worldbank.org/library` does not resolve (DNS failure); a possible successor page loads but RISE's data reachability through it is unconfirmed |
| OECD PINE dataflow ID | The SDMX gateway itself is live/keyless, but the specific PINE dataflow's reachability through it was not confirmed (see tier-c candidate #15 above) |
| ICLEI | Active in sustainable-energy work generally, but no DC-specific content found and no database distinct enough from the C40 Knowledge Hub entry to justify a separate line item |
| InforMEA / ECOLEX | Exists and broad in scope; whether its national-law search has an API, or whether EE/DC content is findable there vs. drowned out by broader environmental-treaty scope, was not confirmed |
| Climate Neutral Data Centre Pact (climateneutraldatacentre.net) | An INDUSTRY self-regulatory pact (EU-recognized EED Art. 26 compliance mechanism), not a government/IGO source — outside this brief's scope as written |

---

## Orchestrator validation (2026-07-18)

Independent machine check of all 11 `draft/crawl/*.yaml` files against the live
code enums and the full existing source set (390 ids / 324 base_urls across
`config/domains/**`, including the 50-state `us/` subdir and `api_sources.yaml`):

- **138 draft entries, all `enabled: false`.** All required fields
  (name/id/base_url/start_paths) present. Every file parses (PyYAML).
- **0 id collisions** with the 390 existing source ids.
- **1 base_url overlap** (not an id collision): `ie_dcee_district_heating`
  shares `https://www.gov.ie` with the existing `gov_ie_dc` entry in
  `ireland.yaml`. Intentional (different start_paths / topic: DH program hub vs
  the DC reporting page). Reviewer decision: either keep as a distinct id or
  merge these start_paths into `gov_ie_dc`. Flagged inline in the draft entry.
- **8 enum values outside the current `src/core/config.py` sets** (config loader
  warns, does not reject). Recommended small additions to keep logs clean:
  - `VALID_REGIONS`: add `manitoba` (used by `manitoba_energy`), and
    `supranational` + `global` (used by `iea_4e_edna_datacentres`,
    `energy_community_acquis`, `c40_knowledge_hub`,
    `iso_iec_30134_datacentre_kpi`).
  - No invalid `category`, `tags`, or `policy_types` values remain.

Nothing here blocks review; these are the only two judgment calls a human needs
to settle before any entry is enabled.
