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

Wave 1 (11 region files) + Wave 2 (7 files: legislation-apis, grid-operators,
standards-bodies, countries-wave2, deep-subnational, us-local,
multilateral-portals) + Wave 3 (7 files: water-cooling, carbon-ets,
dc-incentives, permitting-eia, more-legislation-apis, digital-infra-strategies,
municipal-heat-zoning) combined:

| Metric | Wave 1 | Wave 2 | Wave 3 | Combined |
|---|---|---|---|---|
| **Total verified candidates (unique, deduped)** | **154** | **158** | **99** | **411** |
| Tier a (drops into existing client) | 0 | 0 | 0 | 0 |
| Tier b (plain crawl domain) | 138 | 141 | 91 | 370 |
| Tier c (needs a new structured client) | 16 | 17 | 8 | 41 |
| Duplicates merged | 1 | 3 | 1 | 5 |
| Unverified / needs-human-check items (appendix) | 45 | 75 (+8 "checked, none found") | 39 | 159 (+8) |

Wave-3's 1 merge: `loudoun_county_dc_standards` (permitting-eia.md #9) was an
EXACT duplicate (same base_url, same both start_paths) of wave-1's
`us_loudoun_county_va` already drafted in `draft/crawl/us-states.yaml` — not
re-drafted. See "## Wave 3" below for the full writeup, including one
additional borderline case (`gla_heat_networks_london`) flagged but NOT
dropped/merged (net-new start_paths on an existing base_url).

Wave-1's 1 merge: data.europa.eu Search API, independently proposed in both
`eu-uncovered.md` and `supranational.md`, merged into one entry
(`data_europa_eu_search_api`). Wave-2's 3 merges are all cross-wave
(wave-2 agents re-finding wave-1 draft entries) — see "## Wave 2" below for
the full writeup.

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

---

## Wave 2

Second research pass: 7 additional research files under
`docs/source-expansion/regions-wave2/` (`legislation-apis.md`,
`grid-operators.md`, `standards-bodies.md`, `countries-wave2.md`,
`deep-subnational.md`, `us-local.md`, `multilateral-portals.md`), targeting
gaps wave 1 didn't cover: national legislature APIs, grid operators/ISOs/TSOs,
standards bodies, ~35 additional countries, deeper subnational tiers in large
federations, US county/municipal governments, and multilateral/regional bodies
plus national open-data-portal APIs. Same transcription-and-organization
scope as wave 1 — no new sources invented, nothing enabled.

### Wave 2 totals

| Metric | Count |
|---|---|
| **Total verified candidates (unique, deduped)** | **158** |
| Tier a (drops into existing client) | 0 |
| Tier b (plain crawl domain) | 141 |
| Tier c (needs a new structured client) | 17 |
| Cross-wave/cross-agent duplicates merged | 3 |
| Unverified / needs-human-check items (appendix) | 75 |
| Additionally: "checked, confirmed no source exists" (us-local.md only, not counted as candidates or unverified) | 8 |

### By source file

| Source file | Verified | Tier b | Tier c | Unverified |
|---|---|---|---|---|
| legislation-apis.md | 7 | 0 | 7 | 7 |
| grid-operators.md | 18 | 18 | 0 | 3 |
| standards-bodies.md | 15 | 15 | 0 | 7 |
| countries-wave2.md | 39 | 39 | 0 | 17 |
| deep-subnational.md | 53 (50 net-new after 3 cross-wave merges) | 50 | 0 | 12 |
| us-local.md | 11 | 11 | 0 | 15 (+8 checked/none) |
| multilateral-portals.md | 18 | 8 | 10 | 14 |
| **Total** | **161 raw / 158 net-new** | **141** | **17** | **75** |

### Cross-wave / cross-agent duplicates merged (3)

All 3 surfaced in `deep-subnational.md`'s Switzerland sub-pass, which
independently re-found the same Swiss cantonal sources wave 1's `dach.md`
agent had already drafted (both agents worked from the same underlying
cantonal energy-law corpus). None are drafted a second time in
`draft/crawl/wave2/deep-subnational.yaml` — see that file's header comment
for the full writeup. Verified via a `base_url` diff across every wave-1 and
wave-2 draft/config file (see "Dedup" methodology note below) — no other
overlaps found anywhere else across the 6 tier-b wave-2 files or the 2
tier-c source files.

| # | Wave-2 id (dropped/merged) | Wave-1 id (kept) | base_url | Resolution |
|---|---|---|---|---|
| 1 | `ge_len_energie` (Geneva) | `ge_len_energie` (dach.yaml) | `https://silgeneve.ch` | EXACT duplicate — same id, same base_url, same start_path. Dropped entirely, not re-drafted. |
| 2 | `be_weu_energie` (Bern) | `be_weu_energie` (dach.yaml) | `https://www.weu.be.ch` | EXACT duplicate — same id, same base_url, same start_path. Dropped entirely, not re-drafted. |
| 3 | `vd_legislation_energie` (Vaud) | `vd_energie_legislation` (dach.yaml) | `https://www.vd.ch` | Same underlying source, different id/deeper page. Dropped as a new entry; the one new fact wave 2 added — a second start_path (`/djes/nouvelle-loi-sur-lenergie`) covering the incoming LVLEne law (adopted Feb 2026, in force Jan 2027, F/G-retrofit-by-2042 and fossil-heating-ban-by-2047) — should be folded into the existing wave-1 `vd_energie_legislation` entry by a human reviewer rather than shipped as a duplicate-base_url entry. |

Note: `bs_aue` (Basel-Stadt, `www.bs.ch`) surfaced in the same deep-subnational
pass and is **not** a duplicate of wave-1's `bs_energiegesetz`
(`gesetzessammlung.bs.ch`) — different host, different content (the cantonal
office administering the law vs. the statute text itself) — kept as a
genuinely new wave-2 entry.

**Dedup methodology**: every `base_url` across all 6 wave-2 tier-b YAML files
was diffed (exact string match + a normalized match stripping
`https://`/`www.`/trailing slash) against: (1) all 390 `id`s / base_urls
live in `config/domains/**`, (2) all 138 wave-1 draft crawl entries in
`docs/source-expansion/draft/crawl/*.yaml`, (3) wave-1's 16 tier-c specs in
`draft/new-clients.md`, and (4) every other wave-2 file. Zero collisions
found anywhere except the 3 rows above. The 2 tier-c wave-2 source files
(`legislation-apis.md`, and the API half of `multilateral-portals.md`) were
independently diffed the same way against the 9 shipped `source_type`s + 16
wave-1 tier-c `source_type`s — zero collisions.


### Master table — tier-c APIs first, then tier-b crawl, ranked best-first within each tier

Full technical spec for every tier-c row:
`docs/source-expansion/draft/new-clients-wave2.md`. Full YAML for every
tier-b row (exact `_template.yaml` schema, `enabled: false`):
`docs/source-expansion/draft/crawl/wave2/<source-file-name>.yaml`.

| # | Name | id | Level | Access | Source file | Why |
|---|---|---|---|---|---|---|
| 1 | Tweede Kamer Open Data / Gegevensmagazijn (Netherlands) | `tweede_kamer_odata` | national | none | legislation-apis.md | HIGHEST-VALUE tier-c find of wave 2 - live 'warmtenet' (heat network) query returned a real heat-network-subsidy amendment, keyless OData v4 |
| 2 | Sejm API (Poland) | `sejm_api` | national | none | legislation-apis.md | Keyword-filterable, keyless, modern REST API over the full corpus of Polish bills and session records |
| 3 | Federal Register of Legislation API (Australia) | `au_legislation_frl_api` | national | none | legislation-apis.md | Only true national full-text legislation search API for Australia, covers Acts AND subordinate regulations |
| 4 | Camara dos Deputados Dados Abertos API (Brazil) | `camara_dos_deputados_api` | national | none | legislation-apis.md | Keyword search directly returned on-topic bills incl. a solar-heating-mandate proposal |
| 5 | Congreso de los Diputados Open Data (Spain) | `congreso_es_opendata` | national | none | legislation-apis.md | Real-time-generated structured JSON/XML/CSV of every bill category in the Spanish Congress |
| 6 | Curia Vista OData Web Services (Switzerland) | `curia_vista_odata` | national | none | legislation-apis.md | Surfaces federal motions/postulates on DC energy efficiency not visible via the extensive cantonal crawl domains |
| 7 | Assemblee Nationale Open Data (France) | `assemblee_nationale_opendata` | national | none | legislation-apis.md | Full legislative-dossier text (not just metadata) for every French bill in progress, zero auth |
| 8 | data.gouv.fr Open Data API (France) | `data_gouv_fr_api` | national | none | multilateral-portals.md | Highest policy-relevance Target-2 hit: several results are real regulatory instruments (mandatory DH connection zones), not just statistics |
| 9 | dati.gov.it Open Data API (Italy) | `dati_gov_it_api` | national | none | multilateral-portals.md | CKAN; mixed statistical/administrative results incl. one real incentive-program dataset |
| 10 | data.gov.ie Open Data API (Ireland) | `data_gov_ie_api` | national | none | multilateral-portals.md | CKAN; local-authority retrofit + CSO EE-installation statistics |
| 11 | Open Government Canada CKAN API | `open_canada_ca_api` | national | none | multilateral-portals.md | CKAN; NRCan commercial/institutional energy-use survey + EnerGuide data, complements legisinfo_api |
| 12 | datos.gob.mx Open Data API (Mexico) | `datos_gob_mx_api` | national | none | multilateral-portals.md | CKAN; CFE/CENACE electricity-consumption and marginal-price datasets |
| 13 | datos.gob.es apidata (Spain) | `datos_gob_es_api` | national | none | multilateral-portals.md | Linked Data API (not CKAN), exact-title-match search; electricity producer registry dataset confirmed |
| 14 | data.gov.uk CKAN Action API (general query) | `data_gov_uk_ckan_api` | national | none | multilateral-portals.md | 1,793 live results for a heat-network+DC query; would auto-surface new UK heat-network datasets vs. the one hardcoded uk_hnpd entry |
| 15 | Data.gov (GSA gateway to CKAN Action API, US) | `data_gov_us_api` | national | api_key | multilateral-portals.md | Corrects the assumption that data.gov is keyless; 4,363 results incl. a real NYC energy-benchmarking-law compliance dataset |
| 16 | Climate Watch NDC Content API (World Resources Institute) | `climatewatch_ndc` | supranational | none | multilateral-portals.md | HOLD - keyless, live endpoints confirmed, but energy-efficiency category_ids still need enumerating before building |
| 17 | Eurostat REST Dissemination API - Energy Balances | `eurostat_energy` | supranational | none | multilateral-portals.md | HOLD - keyless SDMX-JSON gateway confirmed live, but the exact waste-heat SIEC/NRG_BAL code needs confirming before building |
| 18 | ERCOT — Large Load Integration (Texas) | `ercot_large_load` | national | none | grid-operators.md | ERCOT's Batch Zero large-load (>=75MW) queue - 137 pending requests, ~140,000MW by 2036 |
| 19 | NYISO — Large Load Interconnection Queue (New York) | `nyiso_large_load` | national | none | grid-operators.md | NYISO's own DC-labeled queue growth: 1 project/500MW (2018) to 29/~6,055MW (2025) |
| 20 | AEMO — Digital Demand Surge / Data Centre Connections (Australia) | `aemo_datacentre` | national | none | grid-operators.md | AEMO's dedicated data-centre-growth page: 11 projects >5MW, 5.4GW in the NEM queue |
| 21 | ENTSO-E — Data Centres and the Power System (Supranational, EU) | `entsoe_datacentres` | supranational | none | grid-operators.md | Pan-EU TSO association report framing DC grid-connection codes for all national TSOs |
| 22 | RTE — Data Centers in France (Reseau de Transport d'Electricite) | `rte_datacenters` | national | none | grid-operators.md | France TSO fast-track DC connection programme, ~18GW reserved across ~80 projects |
| 23 | Amprion — Grid Connection for Industrial Facilities and Data Centers (Germany) | `amprion_datacenter` | national | none | grid-operators.md | New joint German TSO 'Reifegradverfahren' maturity-level DC connection procedure |
| 24 | 50Hertz — Grid Connection (Germany, eastern control zone) | `50hertz_datacenter` | national | none | grid-operators.md | Same joint Reifegradverfahren; Berlin/eastern-Germany DC cluster, Virtus/Wustermark example |
| 25 | TransnetBW — Reifegradverfahren / Grid Access and Tariffs (Germany, Baden-Wuerttemberg) | `transnetbw_datacenter` | national | none | grid-operators.md | Third of four joint-procedure German TSOs; points-based technical/economic assessment |
| 26 | TenneT — Connection Services (Netherlands / Germany) | `tennet_connection` | national | none | grid-operators.md | NL/DE TSO general connection page; fills Netherlands' zero-grid-operator gap (weak match) |
| 27 | Elia — Grid Hosting Capacity (Belgium) | `elia_hosting_capacity` | national | none | grid-operators.md | Belgian TSO; CREG proposing a dedicated data-centre connection category with capacity caps |
| 28 | Terna — Data Center Insight (Italy) | `terna_datacenter` | national | none | grid-operators.md | >300 DC connection requests exceeding 50GW; EUR16.6B investment plan 2024-2028 |
| 29 | Fingrid — Grid Connection Agreement Phases (Finland) | `fingrid_connection` | national | none | grid-operators.md | Finnish TSO connection process; paused new >10MW connections due to DC demand |
| 30 | Svenska kraftnaet — Connect to the Transmission Grid (Sweden) | `svk_connection` | national | none | grid-operators.md | Swedish TSO; DCs were just over half of ~9,000MW in 2025 connection applications (weak match) |
| 31 | Statnett — Grid Connection Process (Norway) | `statnett_connection` | national | none | grid-operators.md | Norwegian TSO; DCs are largest single volume of national grid-connection requests (weak match) |
| 32 | Red Electrica (REE) — Grid Access and Connection (Spain) | `ree_access_connection` | national | none | grid-operators.md | Spanish TSO; documented 'cascade effect' where one DC request blocks neighboring capacity |
| 33 | ISO New England — Interconnection Service (US) | `isone_interconnection` | national | none | grid-operators.md | Rounds out 4-of-4 US ISO/RTO coverage; generation-focused, weakest match in file |
| 34 | SPP — Generator Interconnection (US, Southwest Power Pool) | `spp_gi` | national | none | grid-operators.md | SPP generator-interconnection queue process; completes 4-of-4 remaining US RTO/ISO coverage |
| 35 | Transpower — Grid Connection Process (New Zealand) | `transpower_connections` | national | none | grid-operators.md | NZ system operator connection process; fills a complete NZ grid-operator gap |
| 36 | National Standards Information Public Service Platform (China, SAMR/SAC) | `china_std_samr` | national | none | standards-bodies.md | HIGHEST-VALUE find of the wave - free full text of GB 40879 mandatory DC PUE limits |
| 37 | CENELEC Technical Committee CLC/TC 215 (drafts EN 50600) | `cenelec_clc_tc215` | national | none | standards-bodies.md | Official CENELEC committee record for the body that drafts EN 50600 |
| 38 | ASHRAE Standards and Guidelines | `ashrae_standards` | national | none | standards-bodies.md | Standards 90.4 and 127, the two standards the brief names by number, free addenda |
| 39 | IEC Webstore — ISO/IEC 30134 Data Centre KPI series | `iec_webstore_30134` | national | none | standards-bodies.md | IEC's own commercial webstore for ISO/IEC 30134 series, distinct from wave-1's ISO catalog |
| 40 | Electronic Code of Federal Regulations — 10 CFR Part 431 | `ecfr_10_cfr_431` | national | none | standards-bodies.md | Canonical binding federal text (10 CFR 431) behind DOE's equipment efficiency programme |
| 41 | Better Buildings & Better Plants Initiative — Data Centers Sector | `betterbuildings_datacenters` | national | none | standards-bodies.md | DOE's dedicated data-center energy-efficiency program site, distinct subdomain |
| 42 | Bureau of Indian Standards — Standards Portal | `bis_standards_india` | national | none | standards-bodies.md | India's first (Feb 2026) data-center-specific national standard (CER methodology) |
| 43 | NEN — De Europese norm voor datacenters EN 50600 (Netherlands) | `nen_en_50600` | national | none | standards-bodies.md | Free directory listing the full current EN 50600 part structure |
| 44 | SIS (Swedish Institute for Standards) — SS-EN 50600 series | `sis_en_50600` | national | none | standards-bodies.md | Sweden's EN 50600 storefront listing; lowest marginal value, included for completeness |
| 45 | BSI Knowledge — BS EN 50600-4-6:2020 (Energy Reuse Factor, UK) | `bsi_en_50600_4_6` | national | none | standards-bodies.md | Current-status BS EN 50600-4-6 (Energy Reuse Factor) with a real free abstract |
| 46 | AFNOR Editions boutique — NF EN 50600 series (France) | `afnor_en_50600` | national | none | standards-bodies.md | France's EN 50600 storefront, named explicitly by the brief |
| 47 | DIN Media — DIN EN 50600 series (Germany) | `din_en_50600` | national | none | standards-bodies.md | Germany's DIN EN 50600 catalog; companion to CENELEC's CLC/TC 215 (DKE holds secretariat) |
| 48 | The Green Grid | `the_green_grid` | supranational | none | standards-bodies.md | Industry body that originated PUE/ERE/ERF/WUE/CUE - flagged per brief's judgment call |
| 49 | Uptime Institute | `uptime_institute` | supranational | none | standards-bodies.md | Industry body; Tier Standard + a Heat Reuse Management Primer report |
| 50 | JDCC (Japan Data Center Council) PUE Guideline | `jdcc_pue_guideline` | national | none | standards-bodies.md | Industry PUE guideline tied to Japan's binding Energy Conservation Law reporting mandate |
| 51 | APRUE - National Agency for the Promotion and Rationalization of Energy Use (Algeria) | `aprue_dz` | national | none | countries-wave2.md | Algeria's dedicated national efficiency implementation agency; highest-value Africa find |
| 52 | Adilet Legal Information System (Ministry of Justice, Kazakhstan) | `adilet_zan_kz` | national | none | countries-wave2.md | Kazakhstan's legal database; explicit DC-energy policy regime (mining registry, MW disclosure) |
| 53 | ANME - National Agency for Energy Management (Tunisia) | `anme_tn` | national | none | countries-wave2.md | Tunisia's Law No.2009-7 mandatory energy audits for large consumers, 2030 target |
| 54 | Ministry of Energy of Azerbaijan - Laws | `minenergy_az_laws` | national | none | countries-wave2.md | ~20 Azerbaijan energy laws incl. Law No.359-VIQ on energy efficiency |
| 55 | AEME - Agency for Energy Economy and Management (Senegal) | `aeme_sn` | national | none | countries-wave2.md | Senegal's operational EE-policy arm since 2011; legislative-texts + norms sections |
| 56 | Energy Regulatory Agency of Azerbaijan (AERA) - Energy Efficiency | `regulator_gov_az` | national | none | countries-wave2.md | Azerbaijan regulator's EE page - smart heat/gas/electricity metering mandates |
| 57 | DGE - Directorate General of Energy (Cote d'Ivoire) | `dge_ci` | national | none | countries-wave2.md | Cote d'Ivoire mandatory-energy-audit arrete plus full Laws/Decrees/Orders archive |
| 58 | ANRE - National Agency for Energy Regulation (Moldova) | `anre_md` | national | none | countries-wave2.md | Full tariff-setting authority for Chisinau district heating |
| 59 | NEECA - National Energy Efficiency and Conservation Authority (Pakistan) | `neeca_pk` | national | none | countries-wave2.md | Pakistan's 2023 Energy Conservation Building Code + mandatory audit/labeling regime |
| 60 | SREDA - Sustainable and Renewable Energy Development Authority (Bangladesh) | `sreda_bd` | national | none | countries-wave2.md | Bangladesh's statutory demand-side EE nodal agency under the 2014 EE&C Rules |
| 61 | Ministry of Energy, Mining and Mineral Resources (North Macedonia) | `energy_gov_mk` | national | none | countries-wave2.md | Brand-new (Jun 2024) N. Macedonia ministry; zero prior project coverage |
| 62 | State Electricity Regulatory Commission (SERC, Bosnia and Herzegovina) | `serc_ba` | national | none | countries-wave2.md | BiH state-level electricity regulator; detailed Legislation page |
| 63 | Energy Regulation Board (ERB, Zambia) | `erb_zm` | national | none | countries-wave2.md | Zambia's statutory regulator under the Energy Regulation Act 2019 |
| 64 | Ministry of Energy (Zambia) | `moe_zm` | national | none | countries-wave2.md | Zambia's Energy Efficiency Strategy and Action Plan 2022, direct-download PDF |
| 65 | ERC - Energy Regulatory Commission (Mongolia) | `erc_mn` | national | none | countries-wave2.md | Mongolia regulates BOTH electricity and district-heat tariffs; Ulaanbaatar heat-meter transition |
| 66 | Ministry of Energy of the Republic of Moldova | `energie_gov_md` | national | none | countries-wave2.md | Moldova's standalone energy ministry; Energy Strategy to 2050, EE Fund |
| 67 | LCEC - Lebanese Center for Energy Conservation | `lcec_lb` | national | none | countries-wave2.md | Lebanon's national EE agency; first Arab-world National EE Action Plan, EPC-L scheme |
| 68 | LEX.UZ - National Database of Legislation (Uzbekistan) | `lex_uz` | national | none | countries-wave2.md | Uzbekistan's actual legislative search engine (Laws/Presidential acts/Government decisions) |
| 69 | MEMR - Ministry of Energy and Mineral Resources (Jordan) | `memr_jo` | national | none | countries-wave2.md | Jordan's Renewable Energy & EE Fund (JREEEF), Energy Sector Strategy |
| 70 | Ministry of Infrastructure and Energy (Albania) | `infrastruktura_gov_al` | national | none | countries-wave2.md | Albania draft law mandating district heating/cooling and CHP for new buildings |
| 71 | Ministry of Energy (Nishati), Tanzania | `nishati_tz` | national | none | countries-wave2.md | Tanzania's National EE Action Plan 2019; MEPS/labeling for appliances |
| 72 | AEPC - Alternative Energy Promotion Centre (Nepal) | `aepc_np` | national | none | countries-wave2.md | Nepal's EE mandate holder; audits, energy management systems, standards/labeling |
| 73 | ANARE-CI - National Regulatory Authority for the Electricity Sector (Cote d'Ivoire) | `anare_ci` | national | none | countries-wave2.md | Cote d'Ivoire electricity regulator; ~20 downloadable regulatory orders 2012-2024 |
| 74 | Sri Lanka Sustainable Energy Authority (SLSEA) | `slsea_lk` | national | none | countries-wave2.md | Sri Lanka's statutory EE-building-code authority; National Energy Benchmarking Portal |
| 75 | Ministry of Economy and Sustainable Development (Georgia) | `economy_ge` | national | none | countries-wave2.md | Georgia's current energy-portfolio ministry; EU Association Agreement obligations |
| 76 | Ministry of Mines and Energy (Cambodia) | `mme_kh` | national | none | countries-wave2.md | Cambodia's National Energy Efficiency Policy 2022-2030, 19% reduction target |
| 77 | Ministry of Foreign Trade and Economic Relations (BiH) - Energetika | `mvteo_gov_ba` | national | none | countries-wave2.md | BiH Framework Energy Strategy to 2035 (194pp PDF) incl. district-heating section |
| 78 | Electricity Control Board (ECB, Namibia) | `ecb_na` | national | none | countries-wave2.md | Namibia's national electricity regulator; Smart Grid Policy PDFs |
| 79 | Rwanda Utilities Regulatory Authority (RURA) - Energy Sector | `rura_rw` | national | none | countries-wave2.md | Rwanda's EE guidelines (2013) plus Electricity Licensing Regulations |
| 80 | Ministry of Water and Energy (MoWE), Ethiopia | `mowe_et` | national | none | countries-wave2.md | Ethiopia's parent energy ministry; Energy Efficiency and Conservation Fund framework |
| 81 | Ministry of Electricity and Energy (MOEE), Myanmar | `moee_mm` | national | none | countries-wave2.md | Myanmar Electricity Law, Grid Code, National Electrification Plan (flag: SAC-era site) |
| 82 | Ministry of Energy of the Republic of Uzbekistan | `gov_uz_minenergy` | national | none | countries-wave2.md | Uzbekistan's primary energy ministry; Law on Rational Use of Energy (2020) |
| 83 | Electricity Authority of Cambodia (EAC) | `eac_kh` | national | none | countries-wave2.md | Cambodia's electricity regulator; Law & Regulation, Power Technical Standard sections |
| 84 | Public Services Regulatory Commission (Armenia) | `psrc_am` | national | none | countries-wave2.md | Armenia's sole tariff regulator for electricity/gas/water/district heating |
| 85 | Energy and Minerals Regulatory Commission (EMRC, Jordan) | `emrc_jo` | national | none | countries-wave2.md | Jordan electricity/renewables licensing authority; national conservation campaign |
| 86 | Electricity Regulation Commission (ERC, Nepal) | `erc_np` | national | none | countries-wave2.md | Nepal's statutory electricity regulator; drafting an EE Policy for 2024-2029 |
| 87 | Botswana Energy Regulatory Authority (BERA) | `bera_bw` | national | none | countries-wave2.md | Botswana's sole national energy regulator under the 2016 Energy Regulatory Act |
| 88 | Public Utilities Commission of Sri Lanka (PUCSL) | `pucsl_lk` | national | none | countries-wave2.md | Sri Lanka's electricity tariff/licensing regulator, complements SLSEA |
| 89 | Ministry of Energy of the Republic of Kazakhstan | `gov_kz_energo` | national | none | countries-wave2.md | Kazakhstan's primary energy ministry (low confidence, heavy JS SPA, unread content) |
| 90 | West Bengal Data Centre Policy Portal (Sahayata) | `wb_dc_policy` | subnational | none | deep-subnational.md | HIGHEST VALUE in India batch - standalone West Bengal Data Centre Policy 2021 portal |
| 91 | Uttar Pradesh Data Centre Policy 2021 (Invest UP) | `up_dc_policy` | subnational | none | deep-subnational.md | UP's first dedicated DC policy - Rs 20,000cr target, 250MW, tax/land subsidies |
| 92 | Odisha Data Centre Policy 2022 (Invest Odisha) | `odisha_dc_policy` | subnational | none | deep-subnational.md | Odisha DC Policy 2022 - land subsidy, capital grants up to Rs 25cr |
| 93 | Gujarat IT/ITeS Policy (Directorate of ICT & e-Governance) | `gujarat_it_policy` | subnational | none | deep-subnational.md | Gujarat IT/ITeS Policy 2022-27 explicitly covering data centers + Cable Landing Stations |
| 94 | Maharashtra Industries Dept - IT & ITES Policy 2023 (Data Centre chapter) | `maharashtra_industry` | subnational | none | deep-subnational.md | Maharashtra's DC provisions live inside the IT & ITES Policy 2023, not a standalone doc |
| 95 | Maharashtra Industrial Development Corporation (MIDC) - Industrial Policies & Incentives | `midc_in` | subnational | none | deep-subnational.md | MIDC - implementing body earmarking land for Maharashtra's Data Centre Parks |
| 96 | Uttar Pradesh New & Renewable Energy Development Agency (UPNEDA) | `upneda_in` | subnational | none | deep-subnational.md | UP's renewable-energy nodal agency (solar, bioenergy, biodiesel, RPO) |
| 97 | Odisha Electronics & Information Technology Department | `odisha_it_dept` | subnational | none | deep-subnational.md | Odisha IT dept - broader policy/rules repository incl. Data Policy 2.0 |
| 98 | Odisha Renewable Energy Development Agency (OREDA) | `oreda_in` | subnational | none | deep-subnational.md | Odisha's renewable-energy nodal agency (rooftop solar, biogas, RESCO) |
| 99 | Gujarat Dept. of Science & Technology (Viksit Gujarat - Data Centre Policy 2026-29) | `gujarat_dst` | subnational | none | deep-subnational.md | Nodal agency for brand-new (Jul 2026) 'Viksit Gujarat' DC policy, 8GW target |
| 100 | ReCFIT - Renewables, Climate and Future Industries Tasmania | `recfit_tas` | subnational | none | deep-subnational.md | Tasmania's actual energy/climate policy division; Renewable Energy Action Plan |
| 101 | Office of the Tasmanian Economic Regulator (OTTER) | `otter_tas` | subnational | none | deep-subnational.md | Tasmania's economic regulator; Electricity Supply Industry Act 1995 |
| 102 | Tasmanian Legislation Online | `legislation_tas` | subnational | none | deep-subnational.md | Authoritative full-text Tasmanian Acts/Statutory Rules repository |
| 103 | Climate Choices (ACT Government) | `climate_choices_act` | subnational | none | deep-subnational.md | ACT's live energy/climate content; mandatory EE Improvement Scheme |
| 104 | ACT Legislation Register | `legislation_act` | subnational | none | deep-subnational.md | ACT Legislation Register; surfaces the Energy Efficiency (Cost of Living) Act 2012 |
| 105 | Assembleia Legislativa do Estado de Sao Paulo - decree repository | `al_sp_legislacao` | subnational | none | deep-subnational.md | Sao Paulo Decreto 64.771/2020 - DC-specific ICMS tax exemption on server imports |
| 106 | SEMIL - Energy & Mining Subsecretariat of Sao Paulo State | `semil_energia_sp` | subnational | none | deep-subnational.md | Sao Paulo's state energy ministry counterpart to federal MME |
| 107 | ARSESP - Sao Paulo state utility regulator | `arsesp_sp` | subnational | none | deep-subnational.md | Sao Paulo's state electricity regulator, ANEEL counterpart |
| 108 | Secretaria de Estado de Fazenda do Rio de Janeiro - Legislacao | `legislacao_fazenda_rj` | subnational | none | deep-subnational.md | Rio de Janeiro Lei 10.431/2024 - a second Brazilian state DC tax-incentive law |
| 109 | Secretaria da Fazenda do Parana - Programa Parana Competitivo | `fazenda_pr_competitivo` | subnational | none | deep-subnational.md | Parana's ICMS-credit incentive program covering renewable-energy investment |
| 110 | Ley de Fomento a la Inversion y al Empleo - Congreso de Nuevo Leon | `fomento_inversion_empleo_nl` | subnational | none | deep-subnational.md | Nuevo Leon's investment/employment law - payroll-tax subsidies, land discounts |
| 111 | Prontuario de Legislacion Administrativa y Fiscal - Queretaro | `queretaro_prontuario_fiscal` | subnational | none | deep-subnational.md | Queretaro fiscal-law compendium, closest state-level source for Mexico's #1 DC hub |
| 112 | SEDESU - Queretaro Secretariat of Sustainable Development | `sedesu_qro` | subnational | none | deep-subnational.md | Queretaro's sustainable-development secretariat (thin content, DC forum co-leader) |
| 113 | Secretaria de Economia del Estado de Nuevo Leon | `economia_nl` | subnational | none | deep-subnational.md | Nuevo Leon economy secretariat, quoted on DC energy readiness (weak fit) |
| 114 | Aragon - Plan de Interes General de Aragon (Region MSFT) | `aragon_piga_msft` | subnational | none | deep-subnational.md | Aragon's official dossier for 3 Microsoft DC campuses (EIA, HV approvals) |
| 115 | Aragon - regional energy legislation index | `aragon_legislacion_energia` | subnational | none | deep-subnational.md | Aragon's regional energy legislation index (Decreto-Ley 1/2023, Ley 5/2024) |
| 116 | Catalonia - Institut Catala d'Energia (ICAEN) | `icaen_catalunya` | subnational | none | deep-subnational.md | Catalonia's full energy authority site - PROENCAT 2050, PLATER siting plan |
| 117 | Madrid - FENERCOM (Fundacion de la Energia de la Comunidad de Madrid) | `fenercom_madrid` | subnational | none | deep-subnational.md | Madrid regional foundation publishing efficiency guides and incentive programs |
| 118 | Madrid - Estrategia de Energia, Clima y Aire 2023-2030 | `madrid_estrategia_energia_clima` | subnational | none | deep-subnational.md | Madrid's enacted Estrategia de Energia, Clima y Aire 2023-2030 (Orden 2126/2023) |
| 119 | Boletin Oficial de Aragon (BOA) | `boa_aragon` | subnational | none | deep-subnational.md | Aragon's official gazette - publication venue for DIGA approvals (borderline tier-c) |
| 120 | Lombardy - PEAR/PREAC regional energy-environmental plan | `lombardia_pear_preac` | subnational | none | deep-subnational.md | Lombardy's binding regional energy plan (PEAR/PREAC), Italy's largest DC market |
| 121 | Basel-Stadt - Amt fuer Umwelt und Energie (AUE) | `bs_aue` | subnational | none | deep-subnational.md | Basel-Stadt's cantonal environment/energy office administering the Energiegesetz |
| 122 | Geneva - Etat de Geneve energy-transition policy hub | `ge_transition_energetique` | subnational | none | deep-subnational.md | Geneva's energy-transition policy hub, companion to the wave-1 LEn law entry |
| 123 | SaveEnergyNB (New Brunswick) | `saveenergynb` | subnational | none | deep-subnational.md | New Brunswick joint efficiency program - Business/Commercial/Industrial rebates |
| 124 | takeCHARGE (Newfoundland and Labrador) | `takecharge_nl` | subnational | none | deep-subnational.md | Newfoundland and Labrador joint efficiency program, incl. isolated-system businesses |
| 125 | Efficiency Nova Scotia | `efficiency_ns` | subnational | none | deep-subnational.md | Nova Scotia's arms-length efficiency utility - Building Optimization Program |
| 126 | Government of Saskatchewan - Building/Energy Code + Large-Emitter Carbon Program | `saskatchewan_energy_standards` | subnational | none | deep-subnational.md | Saskatchewan's NECB 2020 building code adoption + OBPS large-emitter carbon program |
| 127 | SaskPower - Commercial Energy Optimization Program | `saskpower_ceop` | subnational | none | deep-subnational.md | SaskPower's Commercial Energy Optimization Program, up to $100k per project |
| 128 | New Brunswick Energy & Utilities Board (EUB) | `nbeub` | subnational | none | deep-subnational.md | New Brunswick's utility regulator - rate decisions, IRP reviews since 1991 |
| 129 | Newfoundland and Labrador Board of Commissioners of Public Utilities (PUB NL) | `pub_nl` | subnational | none | deep-subnational.md | Newfoundland's utility board - electricity rate orders (HTTP-only host) |
| 130 | Nova Scotia Energy and Regulatory Boards Tribunal (successor to NSUARB) | `nserbt_ns` | subnational | none | deep-subnational.md | Nova Scotia's utility regulator (successor to NSUARB) - rate-setting for NS Power |
| 131 | Government of New Brunswick - Laws (Electricity Act, Part 6 Division E - Energy Efficiency) | `nb_laws_electricity_act` | subnational | none | deep-subnational.md | New Brunswick Electricity Act Part 6 Division E - Energy Efficiency provisions |
| 132 | SaskEnergy - Rebates & Programs | `saskenergy_rebates` | subnational | none | deep-subnational.md | SaskEnergy natural-gas-side rebates, complements SaskPower's electric-side program |
| 133 | Newfoundland and Labrador Department of Energy and Mines | `nl_energy_mines` | subnational | none | deep-subnational.md | Newfoundland ministry-level energy/mining portal (weakest of the 11 Canada finds) |
| 134 | Osaka Prefecture - Climate Change Countermeasures Promotion Ordinance | `osaka_ondanka_jourei` | subnational | none | deep-subnational.md | Osaka's mandatory climate-action-plan filing for large energy users incl. DCs |
| 135 | Saitama Prefecture - Target-Setting Type Emissions Trading System | `saitama_torihikiseido` | subnational | none | deep-subnational.md | Saitama's mandatory cap-and-trade, same threshold as Tokyo's scheme |
| 136 | Chiba Prefecture - Global Warming Countermeasures Promotion Division | `chiba_ontai` | subnational | none | deep-subnational.md | Chiba's decarbonization subsidy program (weakest of the 3 Japan finds, no mandate yet) |
| 137 | Ningxia - Zhongwei Data Center Development Implementation Plan | `ningxia_zhongwei_dc` | subnational | none | deep-subnational.md | Zhongwei's mandatory PUE<=1.15 for new large DCs - most stringent mandate in the wave |
| 138 | Ningxia Development and Reform Commission | `ningxia_fzggw` | subnational | none | deep-subnational.md | Ningxia's development commission - the agency behind the Zhongwei DC plan |
| 139 | Inner Mongolia Energy Bureau - Green Power Direct Connection for Data Centers | `nmg_energy_greenpower` | subnational | none | deep-subnational.md | Inner Mongolia mandate: >=80% green power for new DC loads in the Helingeer cluster |
| 140 | Grant County PUD — Evolving Industry (Data Center) Rate Schedules (Washington) | `us_grant_county_pud_wa` | local | none | us-local.md | Grant County PUD's data-center-specific rate schedule (April 2026 restructure) |
| 141 | Linn County, Iowa — Data Centers in Unincorporated Linn County | `us_linn_county_ia` | local | none | us-local.md | Linn County's Feb 2026 DC zoning ordinance incl. mandatory water/cooling study |
| 142 | City of New Albany, Ohio — Data Centers (dedicated portal) | `us_new_albany_oh` | local | none | us-local.md | New Albany's dedicated data-center policy microsite, unique in the whole wave |
| 143 | Storey County, Nevada — Tahoe-Reno Industrial Center Development Agreement | `us_storey_county_nv` | local | none | us-local.md | Storey County's TRIC development agreement - zoning + tax-abatement framework |
| 144 | Fairfax County, Virginia — Data Centers (Adopted Zoning Ordinance Amendment) | `us_fairfax_county_va` | local | none | us-local.md | Fairfax's 2024 DC zoning amendment incl. LEED/on-site-renewable energy standards |
| 145 | City of South Fulton, Georgia — Data Center Ordinance | `us_south_fulton_ga` | local | none | us-local.md | South Fulton's enacted DC ordinance - buffers, screening, Special Use Permits |
| 146 | Frederick County, Maryland — Data Centers Workgroup | `us_frederick_county_md` | local | none | us-local.md | Frederick's Data Centers Workgroup and Critical Digital Infrastructure Overlay Zone |
| 147 | Maricopa County, Arizona — Adopted (Modernized) Zoning Ordinance | `us_maricopa_county_az` | local | none | us-local.md | Maricopa's first-ever formal 'Data Center' zoning land-use definition |
| 148 | City of Chandler, Arizona — Data Center Ordinance (No. 5033) | `us_chandler_az` | local | none | us-local.md | Chandler's Ordinance 5033 - one of the earliest (2023) DC noise/generator ordinances |
| 149 | Prince George's County, Maryland — Qualified Data Center Task Force | `us_prince_georges_county_md` | local | none | us-local.md | Prince George's Data Center Task Force - led to a 2-year DC moratorium |
| 150 | Morrow County, Oregon — Zoning Ordinance | `us_morrow_county_or` | local | none | us-local.md | Morrow County's zoning ordinance - mechanism behind Oregon's largest DC corridor |
| 151 | ECREEE - ECOWAS Centre for Renewable Energy and Energy Efficiency | `ecreee_regional` | supranational | none | multilateral-portals.md | ECOWAS regional EE/renewables body - West Africa counterpart to RCREEE/AFREC |
| 152 | EACREEE - East African Centre of Excellence for Renewable Energy and Efficiency | `eacreee_regional` | supranational | none | multilateral-portals.md | East African Community regional body - cooling-appliance MEPS program |
| 153 | CCREEE - Caribbean Centre for Renewable Energy and Energy Efficiency | `ccreee_regional` | supranational | none | multilateral-portals.md | CARICOM regional energy body - fulfills the brief's Caribbean ask |
| 154 | SACREEE - SADC Centre for Renewable Energy and Energy Efficiency | `sacreee_regional` | supranational | none | multilateral-portals.md | SADC regional body - Industrial Energy Efficiency Programme (SIEEP) |
| 155 | OLADE - Latin American and Caribbean Energy Organization | `olade_regional` | supranational | none | multilateral-portals.md | 27-member Ibero-American/LatAm energy IGO - Energy Outlook reports, statistics |
| 156 | Cool Coalition (UNEP) - Cooling Policy Hub | `cool_coalition` | supranational | none | multilateral-portals.md | UNEP-hosted global cooling coalition - National Cooling Action Plans, MEPS groups |
| 157 | Climate Change Laws of the World (Grantham Research Institute / LSE) | `climate_laws_lse` | supranational | none | multilateral-portals.md | 196-country climate-law database (LSE Grantham); NOT the same as the unlaunched CPR API |
| 158 | SEforALL - Research and Analysis | `seforall_research` | supranational | none | multilateral-portals.md | UN-affiliated global SDG7 research hub, incl. cooling-sector 'Chilling Prospects' |

### Wave 2 tier-c client index

| source_type (proposed) | API base | Auth | Format |
|---|---|---|---|
| `tweede_kamer_odata` | gegevensmagazijn.tweedekamer.nl | none | JSON (OData v4) |
| `sejm_api` | api.sejm.gov.pl | none | JSON |
| `au_legislation_frl_api` | api.prod.legislation.gov.au | none | JSON (OData-flavored) |
| `camara_dos_deputados_api` | dadosabertos.camara.leg.br | none | JSON / XML |
| `congreso_es_opendata` | www.congreso.es | none | JSON / XML / CSV |
| `curia_vista_odata` | ws.parlament.ch | none | JSON (OData v2/v3) |
| `assemblee_nationale_opendata` | data.assemblee-nationale.fr | none | JSON / XML (bulk ZIP) |
| `data_gouv_fr_api` | www.data.gouv.fr | none | JSON (udata, not CKAN) |
| `ckan_action_api` (shared, 5 instances: Italy/Ireland/Canada/Mexico/UK) | dati.gov.it / data.gov.ie / open.canada.ca / www.datos.gob.mx / www.data.gov.uk | none | JSON (CKAN Action API) |
| `datos_gob_es_api` | datos.gob.es | none | JSON (Linked Data / DCAT-AP-ES) |
| `data_gov_us_gsa_api` | api.gsa.gov/technology/datagov/v3 | api_key (free, DATA_GOV_API_KEY) | JSON |
| `climatewatch_ndc` | www.climatewatchdata.org | none | JSON — HOLD (indicator IDs TBD) |
| `eurostat_energy` | ec.europa.eu/eurostat/api/dissemination | none | JSON (SDMX-JSON) — HOLD (waste-heat code TBD) |

Consolidation recommendation carried from `new-clients-wave2.md`: build ONE
generic `ckan_action_api` client parameterized by `base_url` for the Italy/
Ireland/Canada/Mexico/UK rows (identical `package_search` request/response
shape) rather than five bespoke clients.


### Wave 2 appendix: unverified / needs-human-check (75 items)

Every item each wave-2 agent explicitly flagged as unverified, could not
reach, or chose not to propose as a candidate — consolidated with the reason
each failed verification. None of these are in the wave-2 draft crawl YAMLs
or `new-clients-wave2.md`; they need a human (or a differently-configured
fetch) before being turned into a candidate.

#### legislation-apis.md (7)

| Item | Reason |
|---|---|
| Italy — Camera dei Deputati Open Data (`dati.camera.it`) | Portal live but every query (JSON suffix, SPARQL endpoint) hit an Akamai bot-challenge page — automated access actively blocked |
| Italy — Senato Open Data (`dati.senato.it`) | Root 302-redirects and resolves (200), but specific dataset/query endpoints not enumerated this pass |
| Austria — Parlament Open Data / CKAN (`data.gv.at`) | Human landing page live; the CKAN organisation subdomain timed out and a `package_search` query returned an HTML error page instead of JSON |
| Belgium — Chamber of Representatives (`dekamer.be`) | No dedicated chamber-specific open-data API found; `data.gov.be` is a generic cross-agency catalog, not chamber-specific |
| Czech Republic — Poslanecka snemovna (`psp.cz`) | Opendata section is live but only offers static historical ZIP dumps per electoral term, not a live query API |
| Portugal — Assembleia da Republica (`parlamento.pt`) | Official landing page live; third-party docs describe 21+ REST endpoints, but the page itself is JS-rendered (SharePoint-style) — no extractable API links via plain fetch |
| Mexico — Camara de Diputados / Senado | No official structured JSON/XML API confirmed; `sil.gobernacion.gob.mx` is a browsing portal only |

#### grid-operators.md (3)

| Item | Reason |
|---|---|
| TenneT Netherlands — Schiphol-region congestion/DC-specific page | News (NL Times) describes a court-confirmed connection pause near Schiphol, but no still-live TenneT-hosted page carrying this content directly was located this pass — only third-party reporting |
| Svenska kraftnaet / Statnett news sections | Both TSOs' general connection-process pages verified live, but a dedicated DC-specific news article (analogous to RTE's/Terna's/AEMO's) was not independently located |
| REE Spanish-language "Customers" section (`ree.es/es/clientes/consumidor/acceso-conexion`) | Not fetched this pass; likely carries fuller procedural detail than the English overview page |

#### standards-bodies.md (7)

| Item | Reason |
|---|---|
| Italy — UNI (`store.uni.com`) | Homepage live but JS-heavy; a specific EN 50600 / ISO-IEC TS 22237 catalog page could not be located |
| Japan — JIS/JISC dedicated data-center standard | No JIS-numbered standard specific to DC energy efficiency/PUE found; JSA Group Webdesk is a general storefront, not DC-specific |
| NIST | `nist.gov/energy-efficiency` is live but general buildings/residential, not data-center-specific; no dedicated NIST DC standard found |
| ETSI's own standard-numbered deliverables | EN 50600 is CENELEC-numbered, not ETSI-numbered; no distinct ETSI-specific standard catalog found beyond what CLC/TC 215 already captures |
| BIS India exact standard number/URL (candidate `bis_standards_india`) | Portal verified live; the specific Feb-2026 CER-standard detail page not located |
| Uptime Institute's specific heat-reuse-primer URL (candidate `uptime_institute`) | `/publications` section verified live; the specific report URL not re-fetched |
| AFNOR specific NF EN 50600 part URLs (candidate `afnor_en_50600`) | Boutique homepage verified live; specific part URLs from search results returned the homepage instead when re-fetched |

#### countries-wave2.md (17)

| Item | Reason |
|---|---|
| GNERC (Georgia energy/water regulator), `gnerc.org` | `ECONNREFUSED` on every attempt (~4 tries, https/http, multiple paths) — possibly geo/IP-blocked |
| ERC.org.mk (N. Macedonia district-heating regulator) | HTTP 403 on every path — bot-detection blocking |
| FERK (BiH Federation energy regulator), `ferk.ba` | Empty body with no error — inconclusive, possibly a redirect/JS gate |
| Ministry of Territorial Administration (Armenia), `mtad.am` | Site live and real per search, but homepage nav showed no visible energy-specific section; conflicting signals with a possibly-defunct `minenergy.am` |
| Ministry of Energy (Russia), `minenergo.gov.ru` | Resolves (200, real title) but every fetch returned zero body content — heavily JS-rendered SPA |
| publication.pravo.gov.ru (Russia federal law portal) | Both fetch attempts failed outright with no response — likely geo-blocked from this research environment |
| elicense.kz / egov.kz (Kazakhstan mining-license portal) | Real and live, but a transactional licensing system, not a policy-document repository — doesn't meet the brief's bar |
| Ethiopian Energy Authority (EEA), `eea.gov.et` | DNS resolution failed (`ENOTFOUND`) on both bare domain and www variant, tried twice |
| Ministry of Mines and Energy (Namibia), `mme.gov.na` | Repeated `ECONNREFUSED` — likely geo-fencing (ECB, same country, resolved fine) |
| Ministry of Minerals and Energy (Botswana) portal path | HTTP 503, likely bot-detection/rate-limiting; BERA already covers Botswana's regulatory side |
| Ministry of Infrastructure (MININFRA), Rwanda, `mininfra.gov.rw` | Resolves and is genuinely the parent ministry, but only a generic "Publications" nav link surfaced — too thin to confirm; RURA is the stronger Rwanda candidate |
| Zambia ERB "documents" library subsection | Mentioned as part of `erb_zm` but not independently opened as its own URL |
| Iraq — Ministry of Electricity, `moelc.gov.iq` | Every attempt intercepted by a bot-detection "Secure Gateway" interstitial |
| Iraq — KRG Ministry of Electricity, `gov.krd/moel-en` | Direct fetch 403'd; browser session loaded the homepage but Publications redirected back to the homepage shell (heavy client-side routing); also subnational (Kurdistan Region only) |
| Bangladesh — BERC (`berc.org.bd`) | TLS certificate error on both WebFetch and a live browser session |
| Pakistan — NEPRA (`nepra.org.pk`) | HTTP 403 (bot detection); Pakistan already has one solid verified source (NEECA) |
| Iraq: no national-level source cleared verification | Both federal and KRG electricity ministries blocked; genuine coverage gap pending a follow-up with a real network/browser |

#### deep-subnational.md (12)

| Item | Reason |
|---|---|
| Gujarat CMO press release / "Viksit Gujarat" policy PDF | Announced ~Jul 9 2026; direct CMO fetch `ECONNREFUSED`; no PDF-hosting URL found yet on any `.gujarat.gov.in` domain |
| MAITRI (Maharashtra state investment portal), `maitri.maharashtra.gov.in` | Surfaced in search hosting a slides PDF; direct WebFetch failed twice with `ECONNREFUSED` |
| Basel-Stadt Energiegesetz full text (SG 772.100), `gesetzessammlung.bs.ch` | Resolves (200) but is a JS SPA ("LexWork") — WebFetch got only a page-shell title |
| Bern KEnG full text (BSG 741.1), `belex.sites.be.ch` | Same "LexWork" SPA-shell issue as Basel-Stadt above |
| Aragon Direccion General de Energia y Minas organism page | URLs from search results resolved to unrelated/stale post-reorg content or 404'd |
| Vaud full statute text (LVLEne PDF), `lexfind.ch/tolv/249856/fr` | Only summary/index pages fetched (`vd_legislation_energie`, merged not re-added); raw consolidated law text not independently fetched |
| Geneva OCEN standalone office page | Not searched for; likely unnecessary given `ge_len_energie` and `ge_transition_energetique` already cover this canton well |
| CHA moratorium proposal on Aragon data centers (water/energy tax) | Explicitly EXCLUDED — a political party's *proposed* tax, not enacted policy; flagged so it isn't mistakenly re-added later |
| Nova Scotia Dept. of Energy — Efficiency and Conservation subpage, `energy.novascotia.ca` | Re-tested this pass, still "Access denied" (browser-confirmed); domain-wide bot detection, not path-specific |
| Guizhou Provincial Big Data Development and Management Bureau, `dsj.guizhou.gov.cn` | `ECONNREFUSED`; widened test to 5 other Guizhou-hosted domains, all on the same IP block, all failed identically — an infrastructure-cluster-wide block, not a single-bureau issue |
| India (general): Gujarat/Maharashtra specific policy-doc URLs at build time | Several India entries note exact slugs not confirmed (`odisha_it_dept` Act/Rules section, `gujarat_dst` 2026-29 policy doc) — flagged inline in the relevant YAML notes, not separate line items here |
| Botswana Ministry of Minerals and Energy, `gov.bw` path | Also flagged under countries-wave2.md above (HTTP 503) — cross-referenced, not double-counted |

#### us-local.md (15 bot-blocked but corroborated by independent news/legal-alert sources)

| Item | Reason |
|---|---|
| Culpeper County, VA — Technology Zones page | 403 on fetch; content confirmed via cached search snippets + Data Center Frontier coverage |
| Fauquier County, VA — Data Center Development Policy | County's own site 403'd on every path; the policy itself is only confirmed hosted at a third-party mirror (not an acceptable `base_url`) |
| City of Fort Worth, TX — Data Centers page | 403 on fetch; dedicated page confirmed by exact search-result title |
| City of Atlanta, GA — Ordinance 25-O-1063 | 403 on fetch; also available via the city's Legistar instance |
| City of Chicago, IL — Sustainable Data Centers Working Group | 403 on fetch; exact title/URL confirmed via search |
| City of Reno, NV — Title 18 data-center CUP standards | Zoning-code and council-news URLs both 404'd for the fetch tool |
| Village of Elk Grove Village, IL — codes/standards page | 403 on fetch |
| City of Hillsboro, OR — Data Centers page | 403 on fetch; exact title match confirmed via search |
| Douglas County, GA — DC zoning moratorium resolution | No live page found on the county's own domain; resolution PDF only confirmed at a third-party mirror |
| Fulton County, GA (proper) — Data Center Review Committee | No dedicated ordinance page found; only a general, non-DC-specific ordinances index confirmed |
| Iron County, UT — data-center/solar moratorium PDF | PDF fetched successfully but content could not be text-extracted |
| City of Mesa, AZ — Data Center & PAD Text Amendments | PDF fetched but binary/unreadable to the fetch tool; corroborated only by a Legistar item title |
| City of Quincy, WA — Ordinance 22-570 | Fetched via a state OFM ordinance-archive mirror, not the city's own site; could not confirm DC-specificity |
| Box Elder County, UT and Cache County, UT — 180-day DC moratoriums | Widely reported (Stratos Project fight) but no direct fetch attempted this pass |
| San Antonio, TX — draft zoning amendments | Actively drafting as of Mar 2026 but no ordinance adopted yet; no dedicated city page found |

**Additionally, us-local.md explicitly checked and found NO source** (do not
re-check next wave without a new signal) — not counted in the 75 above since
these are confirmed-absent, not unverified-pending: Goodyear AZ (only a
generic TOD/Freeway overlay), City of Dallas TX (no dedicated ordinance,
generic industrial zoning), Abilene TX (no dedicated ordinance despite
OpenAI/Stargate construction), Cook County IL (only a generic property-tax
program, not DC-specific), Umatilla County OR (no county-specific zoning/
energy page; the only government hit is state-level ODOE), East Wenatchee WA
(no DC provisions in Title 17), Des Moines/West Des Moines/Council Bluffs/
Altoona IA (heavy hyperscale presence but no standing ordinance found for
any of the four), Omaha and Papillion NE (no DC-specific zoning ordinance).

#### multilateral-portals.md (14)

| Item | Reason |
|---|---|
| World Bank ESMAP (`esmap.org`) | 403 on both attempts; real/active per search but no DC/waste-heat-specific ESMAP page surfaced |
| GlobalABC (`globalabc.org`) | 403 on both attempts; known real (UNEP-hosted), publishes the Global Status Report for Buildings and Construction |
| African Development Bank (AfDB) | 403 on the energy-sectors path; real SEFA fund and EE publications confirmed via search only |
| Asian Development Bank (ADB) | 403 on the energy-topics path; genuinely on-topic ADB documents (district-heating/industrial-waste-heat) confirmed via search only |
| EBRD Green Cities / Green Economy Transition | Guessed URL paths 404'd; program is real and well-documented externally but the correct current path wasn't found this pass |
| Inter-American Development Bank (IDB) | 403 on the energy-topics path |
| European Investment Bank (EIB) | 403 on the energy-efficiency priorities path |
| Pacific Community (SPC) | 403 on the energy path; the brief's Pacific/SPC ask remains open |
| International Institute of Refrigeration (IIR/IIF) | Homepage loaded successfully, but district-cooling/DC-specific policy material not prominent; FRIDOC database and "files on regulations" link need a dedicated follow-up |
| World Bank RISE, Climate Policy Radar API, OECD PINE dataflow ID, ICLEI, InforMEA/ECOLEX | Already flagged unverified in wave-1's `supranational.md`; not re-tested this pass |
| Germany — govdata.de | CKAN API shape documented/real but every fetch returned `ECONNREFUSED` — networking-layer failure, not a confirmed-down site |
| Australia — data.gov.au | Every attempt (CKAN API, HTML search, `robots.txt`) returned HTTP 403 — session-level bot-blocking suspected |
| Netherlands — data.overheid.nl | CKAN API reachable (`"success": true`) but the English-language query tried returned 0 results — try Dutch terms before ranking |
| Brazil — dados.gov.br | Classic CKAN path returned HTTP 401; portal's own help article describes a "consumer profile" registration step — likely `api_key`-gated now, not keyless as the brief assumed |

---

## Wave 2 enum-additions recap

Wave 2 needed the following values that are NOT yet in `src/core/config.py`'s
`VALID_REGIONS` (all mapped to the closest allowed value in the drafted
YAML, with the intended specific value preserved in each entry's `id`/notes
— see each wave2 YAML file's header comment for the full per-file mapping
rationale):

- `central_asia` (Kazakhstan, Uzbekistan — mapped to `apac` meanwhile)
- `caucasus` (Azerbaijan, Georgia, Armenia — mapped to `europe` meanwhile)
- `district_cooling` as a **category** (Cool Coalition — mapped to
  `district_heating` meanwhile; VALID_CATEGORIES has no cooling-specific
  value today)
- Individual region/canton/province/state strings with no bucket today,
  same pattern as wave-1's already-flagged gap (only a handful of
  Indian/Australian/Canadian/German/Swiss subnational units are
  individually registered): `aragon`, `catalonia`, `madrid`, `lombardy`,
  `geneva`, `basel_stadt`, `saskatchewan`, `nova_scotia`, `new_brunswick`,
  `newfoundland_and_labrador`, `tasmania`, `act` (Australian Capital
  Territory), `sao_paulo`, `rio_de_janeiro`, `parana`, `queretaro`,
  `nuevo_leon`, `china` (country-level — China has no `VALID_REGIONS`
  entry at all, unlike most other countries in this project)
- `caribbean` / `caricom` (CCREEE — mapped to `north_america` meanwhile,
  an imperfect fit per that entry's own notes)
- `supranational` / `global` (carried forward from wave 1's already-flagged
  gap — used again by ENTSO-E, ASHRAE, IEC Webstore, Green Grid, Uptime
  Institute, OLADE, Cool Coalition, Climate Laws LSE, SEforALL, Climate
  Watch NDC)

No invalid `tags` or `policy_types` values were needed this wave — every
wave-2 candidate's tags/policy_types fit entirely within the existing
`VALID_TAGS`/`VALID_POLICY_TYPES` sets.

---

## Orchestrator validation - Wave 2 (2026-07-18)

Machine check across ALL draft crawl files (wave 1 + wave 2 = 279 entries) against
live code enums and the 390 existing sources:

- **279 entries, all `enabled: false`.** All parse (PyYAML). **0 id collisions.**
- **1 base_url overlap with existing config**: `gov.ie` (the wave-1 Ireland case,
  already flagged inline).
- **4 intra-draft duplicate base_urls** - two entries share one national unified
  portal (different departments / start_paths): `argentina.gob.ar`, `gob.pe`,
  `gub.uy` (wave-1 latam), `aragon.es` (wave-2 deep-subnational). Not id collisions;
  legitimate (one portal hosts many ministries) but reviewer may prefer to merge each
  pair's start_paths into a single entry.
- **3 enum values** still outside `src/core/config.py` after the assembler's
  closest-value mapping: `region: global`, `region: manitoba`, `region: supranational`
  (config loader warns, does not reject). Recommended additions to `VALID_REGIONS`.

---

## Orchestrator validation - Wave 3 (2026-07-18)

Machine check of the 92 wave-3 draft crawl entries against live enums, the 390
existing sources, and all prior-wave drafts:

- **92 entries, all `enabled: false`.** All parse. **0 id collisions** with existing
  config; **0 cross-wave id or base_url duplicates** with waves 1-2.
- **0 enum violations** - every region/category/tag/policy_type value maps to
  `src/core/config.py` (cleanest wave; no new enum additions needed from wave 3).
- **12 additive base_url overlaps with existing config** - unique ids sharing a domain
  with an unrelated existing entry (gov.uk depts: uk_ets/secr/esos/dsit; eur-lex CSRD;
  CARB; BAFU; METI; alberta.ca; imda.gov.sg; azleg.gov; london.gov.uk). This is the
  codebase's established multi-entry-per-domain pattern; each notes its sibling id. Not
  collisions - additive by design.
- Wave-3 tier-c (8 new API clients): federal_register_api (keyless), congress_gov_api
  (key), openstates_api (key), kenya_law_api, oparl (municipal), epa_ghgrp_envirofacts_api
  (keyless), ga_epd_permit_search, eea_industrial_emissions_portal.
