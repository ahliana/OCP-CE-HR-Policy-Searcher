# Deep Subnational Coverage — Wave 2

Scope: deeper subnational tiers in large federations where wave-1 was shallow -
India states, Australia states/territories, Brazil/Mexico states, Spain
autonomous communities, Italy regions, additional Swiss cantons, additional
Canadian provinces, Japan prefectures, China "East Data West Compute" hub
provinces. Research + draft only, per `docs/source-expansion/BRIEF.md`. Nothing
below is enabled in any config file; this is a candidate list for a human
to review before drafting YAML.

Dedup performed against: all of `config/domains/*.yaml` (incl. `us/`),
`docs/source-expansion/draft/crawl/*.yaml`, and `docs/source-expansion/draft/new-clients.md`.
Six parallel research passes (India, Australia, Brazil/Mexico, Spain+Italy+Switzerland,
Canada, Japan+China) each did their own dedup check against the relevant existing
files before searching; base_urls below do not collide with anything already
shipped or already drafted in wave 1.

**Totals: 53 verified candidates, 12 unverified/needs-human-check. All 53 are
effort tier (b) - plain crawl domains; zero tier-a (no existing structured
client fits), zero firm tier-c (one borderline case noted under Spain).**

**Single highest-value find**: Geneva's *Loi sur l'energie* (`ge_len_energie`,
`silgeneve.ch`) - a canton-level statute that explicitly classifies data-center
server cooling and mandates participation in district heat-recovery networks
for large energy consumers. Of everything found across all six passes, it is
the only source that legislates the exact behavior ("data center -> waste heat
-> district network") PolicyPulse exists to track, rather than adjacent
efficiency/incentive policy.

---

## India (Maharashtra, Uttar Pradesh, Gujarat, West Bengal, Odisha)

Existing shipped India coverage (do not re-propose): mop_in (powermin.gov.in),
bee_in (beeindia.gov.in), cea_in (cea.nic.in), meity_in (meity.gov.in),
karnataka_dc_policy + kredl_in, tn_dc_policy, telangana_dc + tgredco_in,
maharashtra_energy. Already-drafted-but-unshipped (skip): rerc_in/rrecl_in
(Rajasthan), hareda_in (Haryana), wbreda_in (West Bengal - renewable energy
only), geda_in (Gujarat - renewable energy only), cerc_in, india_code,
prs_india.

Region note: only `karnataka`/`tamil_nadu`/`telangana`/`maharashtra` are
individual values in this project's `VALID_REGIONS`. Uttar Pradesh, Gujarat,
West Bengal, and Odisha have no dedicated region string - map to
`["apac", "india"]` and preserve state identity in id/name/notes.

### Verified candidates (ranked best-first)

1. **West Bengal Data Centre Policy Portal (Sahayata)** - HIGHEST VALUE IN
   THIS BATCH
   - id: `wb_dc_policy` | base_url: `https://sahayata.itewb.gov.in`
   - start_paths: `/pages/data-centre-policy-2021`, `/pages/vision-mission`, `/`
   - level: subnational (state) | access: none
   - region: `["apac","india"]` | category: `policy` | tags: `data_center_specific, incentives` | policy_types: `incentive, strategy` | language: en
   - format: HTML + PDF
   - practical: no rate limit documented; official Dept. of IT & Electronics (DoIT&E) portal dedicated solely to this policy; `requires_playwright: true` recommended (matches sibling India entries)
   - effort tier: b
   - why: standalone WB Data Centre Policy 2021 portal, distinct from the general IT dept site and from `wbreda_in` (renewable energy, already drafted). Hosts the notification, full policy text, Advisory Group Constitution Order, and State Empowered Committee Order as direct downloads.
   - verified: yes - WebFetch confirmed all four documents, official DoIT&E branding.
   - append to: `india.yaml` (new West Bengal section)

2. **Uttar Pradesh Data Centre Policy 2021 (Invest UP)**
   - id: `up_dc_policy` | base_url: `https://invest.up.gov.in`
   - start_paths: `/up-data-centre-policy-2021/`
   - level: subnational | access: none
   - region: `["apac","india"]` | category: `policy` | tags: `data_center_specific, incentives` | policy_types: `incentive, strategy` | language: en (Hindi version also present)
   - format: HTML + PDF
   - practical: actively maintained (updated through Dec 2024, incl. First Amendment 2022); `requires_playwright: true` recommended
   - effort tier: b
   - why: UP's first dedicated DC policy - Rs 20,000 crore investment target, 250MW capacity, capital/interest/land subsidies, stamp-duty and electricity-duty exemptions.
   - verified: yes - WebFetch confirmed policy text, incentive structure, downloadable PDFs/Government Orders.
   - append to: `india.yaml` (new Uttar Pradesh section)

3. **Odisha Data Centre Policy 2022 (Invest Odisha)**
   - id: `odisha_dc_policy` | base_url: `https://investodisha.gov.in`
   - start_paths: `/datacentre-policy`
   - level: subnational | access: none
   - region: `["apac","india"]` | category: `policy` | tags: `data_center_specific, incentives` | policy_types: `incentive, strategy` | language: en
   - format: HTML + PDF
   - practical: nodal agency is OCAC under the E&IT dept; `requires_playwright: true` recommended
   - effort tier: b
   - why: land subsidy, capital grants up to Rs 25 crore, power-bill reductions, tax reimbursements, single-window clearance - Odisha is actively courting DC investment.
   - verified: yes - WebFetch confirmed policy sections and a downloadable PDF.
   - append to: `india.yaml` (new Odisha section)

4. **Gujarat IT/ITeS Policy (Directorate of ICT & e-Governance)**
   - id: `gujarat_it_policy` | base_url: `https://directorit.gujarat.gov.in`
   - start_paths: `/IT-Policy`
   - level: subnational | access: none
   - region: `["apac","india"]` | category: `policy` | tags: `data_center_specific, incentives` | policy_types: `incentive, strategy` | language: en
   - format: HTML + PDF
   - practical: October 2024 addendum listed; `requires_playwright: true` recommended
   - effort tier: b
   - why: Gujarat's dedicated IT/ITeS Policy (2022-27) - explicitly covers "technologically advanced Data Centers" and Cable Landing Station development; distinct from `geda_in` (renewable energy, already drafted).
   - verified: yes - WebFetch confirmed IT/ITeS Policy document, GCC Policy, Startup & Innovation Policy, DC/CLS provisions.
   - append to: `india.yaml` (new Gujarat section)

5. **Maharashtra Industries Dept - IT & ITES Policy 2023 (with Data Centre chapter)**
   - id: `maharashtra_industry` | base_url: `https://industry.maharashtra.gov.in`
   - start_paths: `/`, `/sites/default/files/2025-09/it-policy-booklet_1_11zon.pdf`
   - level: subnational | access: none
   - region: `["apac","india","maharashtra"]` | category: `policy` | tags: `data_center_specific, incentives` | policy_types: `incentive, strategy` | language: en
   - format: HTML + PDF (8.2MB, image-heavy - note for OCR/parsing)
   - practical: `requires_playwright: true` recommended
   - effort tier: b
   - why: confirmed there is NO standalone "Maharashtra Data Centre Policy 2023" - DC provisions live inside the IT & ITES Policy 2023 itself (cross-confirmed via legal-industry sources). This dept site is the correct target, distinct from the already-shipped `maharashtra_energy`. Includes Oct 2024 GR amendment adding "Green Integrated Data Centre Park" incentives.
   - verified: yes - WebFetch confirmed official branding, policy listing, IT/ITES 2023 PDF location (PDF itself returned as binary/image, page hosting it confirmed real).
   - append to: `india.yaml` (new Maharashtra section, alongside existing `maharashtra_energy`)

6. **Maharashtra Industrial Development Corporation (MIDC) - Industrial Policies & Incentives**
   - id: `midc_in` | base_url: `https://www.midcindia.org`
   - start_paths: `/en/investors/industrial-policies-and-incentives/`
   - level: subnational | access: none
   - region: `["apac","india","maharashtra"]` | category: `economic_dev` | tags: `data_center_specific, incentives, planning` | policy_types: `incentive, program` | language: en
   - format: HTML + PDF
   - practical: page lists ~20 sector policies, filter for DC-relevant ones; `requires_playwright: true` recommended
   - effort tier: b
   - why: implementing body earmarking land for the state's Data Centre Parks (per IT/ITES Policy 2023) - distinct entity/base_url from both `maharashtra_energy` and `maharashtra_industry`.
   - verified: yes - WebFetch confirmed official MIDC branding and the IT/ITES Policy 2023 entry referencing data centers.
   - append to: `india.yaml` (Maharashtra section)

7. **Uttar Pradesh New & Renewable Energy Development Agency (UPNEDA)**
   - id: `upneda_in` | base_url: `https://upneda.in`
   - start_paths: `/`
   - level: subnational | access: none
   - region: `["apac","india"]` | category: `energy_ministry` | tags: `renewable_energy, incentives` | policy_types: `incentive, program` | language: en
   - format: HTML + PDF
   - practical: multiple mirror domains exist (`upneda.org.in`, `solar.upneda.in`); `requires_playwright: true` recommended
   - effort tier: b
   - why: UP's state renewable-energy nodal agency (solar, bioenergy, biodiesel, RPO compliance) - no UP energy-agency coverage exists yet.
   - verified: yes - WebFetch confirmed official portal, Saur UP/Bio Energy/Biodiesel/RPO sub-portals.
   - append to: `india.yaml` (Uttar Pradesh section)

8. **Odisha Electronics & Information Technology Department**
   - id: `odisha_it_dept` | base_url: `https://it.odisha.gov.in`
   - start_paths: `/en` (Act/Rules/Policies section slug not confirmed - start root, max_depth 2)
   - level: subnational | access: none
   - region: `["apac","india"]` | category: `policy` | tags: `data_center_specific, planning` | policy_types: `strategy, guidance` | language: en
   - format: HTML + PDF
   - practical: also references newer "Odisha State Data Policy 2.0" (2026) and draft "ODEV 2030"; `requires_playwright: true` recommended
   - effort tier: b
   - why: parent IT department complementing the dedicated DC-policy page (#3) - broader policy/rules repository.
   - verified: yes - WebFetch confirmed department site, Act/Rules/Policies section, named documents.
   - append to: `india.yaml` (Odisha section)

9. **Odisha Renewable Energy Development Agency (OREDA)**
   - id: `oreda_in` | base_url: `https://oredaodisha.com`
   - start_paths: `/`
   - level: subnational | access: none
   - region: `["apac","india"]` | category: `energy_ministry` | tags: `renewable_energy, incentives` | policy_types: `incentive, program` | language: en
   - format: HTML + PDF
   - practical: est. 1984, under Odisha Dept. of Science & Technology; `requires_playwright: true` recommended
   - effort tier: b
   - why: Odisha's renewable-energy nodal agency (rooftop solar, biogas, PM Surya Ghar, RESCO) - fills the energy-agency gap alongside the IT/DC entries.
   - verified: yes - WebFetch confirmed official site, program listings.
   - append to: `india.yaml` (Odisha section)

10. **Gujarat Dept. of Science & Technology (nodal agency, "Viksit Gujarat - Data Centre Policy 2026-29")**
    - id: `gujarat_dst` | base_url: `https://dst.gujarat.gov.in`
    - start_paths: `/`, `/Home/GujaratStateDataCenter`
    - level: subnational | access: none
    - region: `["apac","india"]` | category: `policy` | tags: `data_center_specific, planning` | policy_types: `strategy, incentive` | language: en
    - format: HTML + PDF
    - practical: `requires_playwright: true` recommended
    - effort tier: b
    - why: nodal agency for a brand-new (~July 9, 2026) "Viksit Gujarat" DC policy (8GW target, Rs 6 lakh crore investment target) - extremely current.
    - verified: PARTIAL - domain and Gujarat State Data Center (GSDC) subpage confirmed live/official; the exact 2026-29 policy document URL was not located (may not be posted yet). Recommend a human follow-up before enabling.
    - append to: `india.yaml` (Gujarat section, alongside #4)

### Unverified / needs human check (India)

- **Gujarat CMO press release / "Viksit Gujarat" policy PDF** - announced by
  CM Bhupendra Patel ~July 9, 2026 per `cmogujarat.gov.in` and multiple news
  outlets incl. `newsonair.gov.in`; direct fetch of the CMO press page
  returned `ECONNREFUSED`; no PDF-hosting URL found on any `.gujarat.gov.in`
  domain yet. Needs a human/browser check once indexed.
- **MAITRI (Maharashtra state investment portal)**, `maitri.maharashtra.gov.in`
  - surfaced in search hosting `IT_Slides_Website.pdf`; direct WebFetch failed
  twice with `ECONNREFUSED`. Needs human/browser recheck (possible
  bot-detection/geo-block).

---

## Australia (Tasmania, Australian Capital Territory)

Existing shipped (skip): nsw_energy, nsw_ida_dc, sa_energy_dc, energy_au
(national). Already-drafted-but-unshipped (skip): aer_au, aemc_au,
energy_policy_wa, qld_treasury_energy, vic_energy (WA/QLD/VIC).

Region note: only `new_south_wales`/`south_australia` are individual values
in `VALID_REGIONS`. Tasmania and ACT map to `["apac","australia"]`.

### Verified candidates (ranked best-first)

1. **ReCFIT - Renewables, Climate and Future Industries Tasmania**
   - id: `recfit_tas` | base_url: `https://www.recfit.tas.gov.au`
   - start_paths: `/`, `/policies_strategies_plans`, `/policies_strategies_plans/renewable-energy/renewable_energy_action_plan`
   - level: subnational (Tasmania) | access: none
   - region: `["apac","australia"]` | category: `energy_ministry` | tags: `renewable_energy, planning, efficiency` | policy_types: `strategy, report` | language: en
   - format: HTML + PDF
   - practical: WebFetch returned 403 (bot detection) but `curl` with browser UA returned 200 with correct titles on all three paths - `requires_playwright: true` recommended. robots.txt permissive (only admin/search-cache blocked).
   - effort tier: b
   - why: Tasmania's actual dedicated energy/climate policy division (replaces the now-unstable `stategrowth.tas.gov.au`, mid machinery-of-government restructure into "Building Tasmania"). Publishes the Renewable Energy Action Plan and the legislated 200%-renewable-output target (2020).
   - verified: yes (via curl; WebFetch blocked)
   - append to: new `config/domains/australia.yaml` Tasmania section (or new file per human preference)

2. **Office of the Tasmanian Economic Regulator (OTTER)**
   - id: `otter_tas` | base_url: `https://www.economicregulator.tas.gov.au`
   - start_paths: `/electricity`, `/`, `/for-customers/current-regulated-prices`
   - level: subnational (Tasmania) | access: none
   - region: `["apac","australia"]` | category: `regulatory` | tags: `mandates, reporting` | policy_types: `regulation, report` | language: en
   - format: HTML + PDF ("Energy in Tasmania" annual report)
   - practical: robots.txt disallows `/search`, `/*?*` only; direct WebFetch succeeded
   - effort tier: b
   - why: administers the Electricity Supply Industry Act 1995 and Tasmanian Electricity Code - sets feed-in tariffs, licenses suppliers, regulates retail prices. Note: this is the successor name to "Office of the Tasmanian Energy Regulator."
   - verified: yes - WebFetch confirmed Act citation, code/licensing/pricing sections
   - append to: Tasmania section

3. **Tasmanian Legislation Online**
   - id: `legislation_tas` | base_url: `https://www.legislation.tas.gov.au`
   - start_paths: `/browse/inforce`, `/browse/asmade`, `/browse/bills`
   - level: subnational | access: none
   - region: `["apac","australia"]` | category: `legislative` | tags: `mandates` | policy_types: `law` | language: en
   - format: HTML (consolidated legislation)
   - practical: robots.txt disallows only `/admin/`; sitemap at `/sitemap.xml`
   - effort tier: b
   - why: authoritative full-text repository of Tasmanian Acts/Statutory Rules - fills the primary-legislation gap for the state.
   - verified: yes - WebFetch confirmed root content and all three browse paths
   - append to: Tasmania section

4. **Climate Choices (ACT Government)**
   - id: `climate_choices_act` | base_url: `https://www.climatechoices.act.gov.au`
   - start_paths: `/`, `/energy/energy-efficiency`, `/policy-programs/energy-efficiency-improvement-scheme`
   - level: subnational (ACT) | access: none
   - region: `["apac","australia"]` | category: `energy_ministry` | tags: `efficiency, mandates, incentives` | policy_types: `regulation, incentive, guidance` | language: en
   - format: HTML + PDF
   - practical: WebFetch 403'd, `curl` confirmed 200 on all three paths - `requires_playwright: true` recommended. robots.txt sets `Crawl-delay: 3`.
   - effort tier: b
   - why: where ACT's live energy/climate policy content actually sits post-EPSDD-merger (now under the City and Environment Directorate) - mandatory Energy Efficiency Improvement Scheme, Home Energy Support rebates, net-zero-by-2045 program. `environment.act.gov.au` 404s on all climate/energy guesses - content moved here.
   - verified: yes (via curl; WebFetch blocked)
   - append to: new ACT section

5. **ACT Legislation Register**
   - id: `legislation_act` | base_url: `https://www.legislation.act.gov.au`
   - start_paths: `/`, `/a/2012-17` (Energy Efficiency (Cost of Living) Improvement Act 2012)
   - level: subnational | access: none
   - region: `["apac","australia"]` | category: `legislative` | tags: `mandates` | policy_types: `law, regulation` | language: en
   - format: HTML + PDF
   - practical: robots.txt sets `Crawl-delay: 10`; blocks search-results/app-chrome paths only
   - effort tier: b
   - why: official ACT Legislation Act 2001 "approved website" - Acts, subordinate laws, disallowable/notifiable instruments, bills; surfaces the Energy Efficiency (Cost of Living) Improvement Act and its many amending instruments directly.
   - verified: yes - WebFetch confirmed root content; curl confirmed `/a/2012-17`
   - append to: ACT section

### Unverified / needs human check (Australia)

None from this pass - all five candidates confirmed live via at least one
direct-fetch method.

---

## Brazil (Sao Paulo) and Mexico (Queretaro, Nuevo Leon)

Existing shipped (skip, federal level only): mme_br, aneel_br, epe_br,
procel_br, sener_mx, conuee_mx.

### Verified candidates (ranked best-first)

1. **Assembleia Legislativa do Estado de Sao Paulo - decree repository (Brazil)**
   - id: `al_sp_legislacao` | base_url: `https://www.al.sp.gov.br`
   - start_paths: `/repositorio/legislacao/decreto/2020/`, `/repositorio/legislacao/decreto/2023/` (add years as they publish)
   - level: subnational (Sao Paulo) | access: none
   - region: `["south_america"]` | category: `legislative` | tags: `incentives, efficiency` | policy_types: `law, regulation, incentive` | language: pt
   - format: HTML
   - practical: no rate limit encountered; static decree pages, rarely edited once published; needs periodic new-year path additions
   - effort tier: b
   - why: verbatim state-level DC-specific tax law - Decreto 64.771/2020 (ICMS suspension/deferral/exemption on DC server/switch-gear imports, CNAE 6311-9/00) and its 2023 amendment (extends to optical transceivers). Directly answers the Sao Paulo ICMS angle.
   - verified: yes - fetched decree text directly, confirmed governor signature, CNAE code, effective date
   - append to: new `config/domains/brazil.yaml` Sao Paulo section

2. **SEMIL - Energy & Mining Subsecretariat of Sao Paulo State**
   - id: `semil_energia_sp` | base_url: `https://semil.sp.gov.br`
   - start_paths: `/sem/`, `/sem/energia/`
   - level: subnational | access: none
   - region: `["south_america"]` | category: `energy_ministry` | tags: `efficiency, renewable_energy, planning, carbon` | policy_types: `regulation, strategy, report` | language: pt
   - format: HTML + PDF
   - practical: large multi-secretariat portal - recommend `allowed_path_patterns: ["/sem/*"]`
   - effort tier: b
   - why: Sao Paulo's direct state-level energy-ministry counterpart to federal MME - State Energy Policy Council (Cepe), State Energy Plan 2050, Balanco/Boletim/Anuario Energetico.
   - verified: yes - WebFetch confirmed Cepe, PEE, Balanco Energetico, solar PV call, climate-committee content
   - append to: Sao Paulo section

3. **ARSESP - Sao Paulo state utility regulator**
   - id: `arsesp_sp` | base_url: `https://www.arsesp.sp.gov.br`
   - start_paths: `/SitePages/Legislacao.aspx`, `/Paginas/energia/energia-eletrica.aspx`
   - level: subnational | access: none
   - region: `["south_america"]` | category: `regulatory` | tags: `mandates, reporting` | policy_types: `regulation` | language: pt
   - format: HTML + PDF
   - practical: legislation search is a filterable list UI (year/type/sector) - `requires_playwright: true` or a query-string start path may help
   - effort tier: b
   - why: state electricity regulator, direct Sao Paulo counterpart to federal ANEEL; searchable Deliberacoes/Portarias archive (200+ entries back to 2000).
   - verified: yes - WebFetch confirmed regulator identity and a large searchable archive
   - append to: Sao Paulo section

4. **Secretaria de Estado de Fazenda do Rio de Janeiro - Legislacao**
   - id: `legislacao_fazenda_rj` | base_url: `https://legislacao.fazenda.rj.gov.br`
   - start_paths: `/leis-ordinarias-estaduais/`
   - level: subnational (Rio de Janeiro) | access: none
   - region: `["south_america"]` | category: `legislative` | tags: `incentives` | policy_types: `law, incentive` | language: pt
   - format: HTML
   - practical: organized by year (1979-2026) with search + thematic filters
   - effort tier: b
   - why: a second Brazilian state (beyond Sao Paulo) with an explicit DC tax-incentive law - Lei 10.431/2024, differentiated ICMS deferral for DC servers/switches/optical transceivers, valid through 2032.
   - verified: yes - fetched root, confirmed year-indexed database; companion confirmation via ALERJ news coverage of Lei 10.431/24
   - append to: new Rio de Janeiro section

5. **Secretaria da Fazenda do Parana - Programa Parana Competitivo**
   - id: `fazenda_pr_competitivo` | base_url: `https://www.fazenda.pr.gov.br`
   - start_paths: `/Pagina/Parana-Competitivo`
   - level: subnational (Parana) | access: none
   - region: `["south_america"]` | category: `economic_dev` | tags: `incentives, renewable_energy` | policy_types: `regulation, incentive` | language: pt
   - format: HTML + PDF (decree PDF at `sefanet.pr.gov.br`)
   - practical: standard state gov site
   - effort tier: b
   - why: state ICMS-credit transfer incentive program (Decreto 7.721/2024) explicitly covering renewable-energy-plant investment - a third Brazilian state worth noting.
   - verified: yes - fetched root, confirmed program and decree provisions
   - append to: new Parana section

6. **Ley de Fomento a la Inversion y al Empleo - Congreso de Nuevo Leon (Mexico)**
   - id: `fomento_inversion_empleo_nl` | base_url: `https://www.hcnl.gob.mx`
   - start_paths: `/trabajo_legislativo/leyes/leyes/ley_de_fomento_a_la_inversion_y_al_empleo_para_el_estado_de_nuevo_leon/`
   - level: subnational (Nuevo Leon) | access: none
   - region: `["north_america"]` | category: `legislative` | tags: `incentives` | policy_types: `law, incentive` | language: es
   - format: HTML (PDF also linked)
   - practical: static official Congress law page
   - effort tier: b
   - why: NL's investment/employment-promotion law - payroll-tax subsidies, registration-fee waivers, land-purchase discounts, and a Consejo de Desarrollo Economico that scores projects partly on environmental-technology adoption; last reformed Sept 2025.
   - verified: yes - fetched directly, confirmed reform date and incentive/environmental provisions
   - append to: new `config/domains/mexico.yaml` Nuevo Leon section

7. **Prontuario de Legislacion Administrativa y Fiscal - Queretaro (Mexico)**
   - id: `queretaro_prontuario_fiscal` | base_url: `https://www.queretaro.gob.mx`
   - start_paths: `/en/prontuario-2025` (annual path - update year each year)
   - level: subnational (Queretaro) | access: none
   - region: `["north_america"]` | category: `legislative` | tags: `incentives, reporting` | policy_types: `law, regulation` | language: es
   - format: HTML index -> PDF
   - practical: static "Visualizar" link list, annual re-publish
   - effort tier: b
   - why: Queretaro has no separate state energy secretariat (energy is federal via CFE/SENER) - this fiscal-law compendium (Ley de Ingresos, Codigo Fiscal, finance-ministry regulations) is the closest state-level policy-document source for Mexico's #1 DC hub.
   - verified: yes - fetched directly, confirmed 40 listed documents with working links
   - append to: Queretaro section

8. **SEDESU - Queretaro Secretariat of Sustainable Development (Mexico)**
   - id: `sedesu_qro` | base_url: `https://queretaro.gob.mx`
   - start_paths: `/en/web/sedesu`
   - level: subnational | access: none
   - region: `["north_america"]` | category: `economic_dev` | tags: `planning` | policy_types: `report, guidance` | language: es
   - format: HTML + PDF
   - practical: content thinner than expected - mostly vehicle-emissions-verification scheduling; recommend a human spot-check for a more specific incentive sub-page
   - effort tier: b
   - why: official state body co-leading the National Forum on Energy and Sustainability with the Mexican Data Centers Association (Queretaro holds ~65% of Mexico's installed DC capacity per that forum).
   - verified: yes, but coverage thin - confirmed identity, no specific DC-incentive document found yet
   - append to: Queretaro section

9. **Secretaria de Economia del Estado de Nuevo Leon (Mexico)** - lowest priority
   - id: `economia_nl` | base_url: `https://www.nl.gob.mx`
   - start_paths: `/es/economia`
   - level: subnational | access: none
   - region: `["north_america"]` | category: `economic_dev` | tags: `planning` | policy_types: `guidance` | language: es
   - format: HTML
   - practical: none noted
   - effort tier: b
   - why: office publicly quoted on DC energy readiness and 1.5 GW of new 2026 generation capacity tied partly to DC/AI demand, but landing page itself is generic business services - actual incentive mechanism is #6 above.
   - verified: yes, weak fit - confirmed department identity only
   - append to: Nuevo Leon section

### Unverified / needs human check (Brazil/Mexico)

- **La Sombra de Arteaga** (Queretaro's official state gazette),
  `lasombradearteaga.segobqueretaro.gob.mx` - domain resolves but is
  frame-based; fetch tool could not render frame targets to reach actual
  gazette content. Would be a stronger source than the prontuario compendium
  if a human/browser can follow the frames.
- **INFOQRO** (Queretaro transparency portal), `infoqro.mx` - confirmed
  genuine government entity, serves a real Ley de Ingresos 2026 PDF, but its
  core mission is transparency requests, not law publication; the same
  document is already reachable via #7 above. Lower priority / fallback only.

---

## Spain (Aragon, Madrid, Catalonia), Italy (Lombardy), Switzerland (Geneva, Vaud, Basel-Stadt, Bern)

Existing shipped (skip): miteco_es, boe_es (Spain national), mase_it,
normattiva_it (Italy national), bfe_ch, ch_eng_fedlex, ch_admin_eng,
bfe_energy_policy, bfe_district_heat, bafu_buildings, muken_2014, endk_muken,
sdea_main, energieschweiz_dc/abwaerme/fernwaerme, and all Zurich-specific
(zh.ch / zhlex.zh.ch / www2.zhlex.zh.ch) entries - do not touch Zurich again.

### Verified candidates (ranked best-first)

1. **Geneva Cantonal Energy Law (LEn) - HIGHEST VALUE IN THIS BATCH, AND
   OVERALL BEST FIND OF THE WHOLE DEEP-SUBNATIONAL PASS**
   - id: `ge_len_energie` | base_url: `https://silgeneve.ch`
   - start_paths: `/legis/data/rsg_l2_30.htm`, `/legis/data/rsg_l2_30p01.htm` (implementing regulation REn)
   - level: subnational (canton) | access: none
   - region: `["eu_central","switzerland","geneva"]` | category: `legislative`/`regulatory` | tags: `mandates, efficiency, district_heating` | policy_types: `law, regulation` | language: fr
   - format: HTML (consolidated statute text)
   - practical: no robots.txt blocking observed; static HTML, no JS required
   - effort tier: b
   - why: full statutory text explicitly classifying data-center/server cooling as "process refrigeration" (Art. 6 para 24), mandating the canton promote heat-recovery-to-district-network schemes (Art. 17A), and defining "large consumers" (>5 GWh heat or >0.5 GWh electricity/year, Art. 6/14) with mandatory energy audits. The only source in the entire wave-2 pass that names data centers by statute AND mandates waste-heat-network participation.
   - verified: yes - WebFetch returned full article text confirming all provisions above
   - append to: new `config/domains/switzerland.yaml` Geneva section

2. **Aragon - Plan de Interes General de Aragon "Region MSFT"**
   - id: `aragon_piga_msft` | base_url: `https://www.aragon.es`
   - start_paths: `/-/piga-microsoft`
   - level: subnational (region) | access: none
   - region: `["eu","eu_south","spain","aragon"]` | category: `economic_dev`/`regulatory` | tags: `planning, efficiency` | policy_types: `directive, report` | language: es
   - format: HTML + linked PDFs (EIA/SEA docs)
   - practical: static page, may need max_depth 2 for linked PDFs
   - effort tier: b
   - why: official administrative dossier for three interconnected Microsoft DC campuses (La Muela, Villamayor de Gallego, Zaragoza) - environmental impact assessments, high-voltage supply approvals, Declaration of General/Autonomous Interest (Dec 2023-Feb 2025). Aragon is one of Europe's largest emerging hyperscaler hubs.
   - verified: yes - WebFetch confirmed official page, project scope, DIGA history
   - append to: new `config/domains/spain.yaml` Aragon section

3. **Aragon - regional energy legislation index**
   - id: `aragon_legislacion_energia` | base_url: `https://www.aragon.es`
   - start_paths: `/-/legislacion-sobre-energia`
   - level: subnational | access: none
   - region: `["eu","eu_south","spain","aragon"]` | category: `legislative` | tags: `mandates, incentives, efficiency` | policy_types: `law, regulation` | language: es
   - format: HTML with BOA/BOE PDF links
   - practical: static, low update frequency
   - effort tier: b
   - why: direct regional legislative index - Decreto-Ley 1/2023 (energy transition), Ley 5/2024 (energy communities/self-consumption), efficiency-subsidy decrees, Energy Plans 2005-2012/2013-2020.
   - verified: yes - WebFetch enumerated specific laws with numbers/dates
   - append to: Aragon section

4. **Catalonia - Institut Catala d'Energia (ICAEN)**
   - id: `icaen_catalunya` | base_url: `https://icaen.gencat.cat`
   - start_paths: `/ca/energia/normativa/`, `/ca/energia/usos_energia/edificis/lenergia-als-edificis/normativa`, `/ca/participacio/llei-de-transicio-energetica-de-catalunya-i-transformacio-de-linstitut-catala-denergia-en-lagencia-denergia-de-catalunya/index.html`
   - level: subnational | access: none
   - region: `["eu","eu_south","spain","catalonia"]` | category: `energy_ministry` | tags: `efficiency, mandates, planning, incentives` | policy_types: `law, regulation, guidance, report` | language: ca (also es content) - check `keywords.yaml` for Catalan-language taxonomy coverage
   - format: HTML + linked PDFs
   - practical: legacy `.content/` PDF paths alongside modern nav - may need max_depth 2
   - effort tier: b
   - why: Catalonia is a top-3 Spanish DC-investment region (Barcelona metro); full energy-authority site - PROENCAT 2050, PINECCAT 2030, PLATER siting plan, GENERCAT public-building efficiency plan, building-efficiency normativa, and a pending energy-transition bill (would rename ICAEN to Agencia Catalana d'Energia).
   - verified: yes - three separate WebFetch calls confirmed homepage, normativa sub-page, transition-law page
   - append to: new Catalonia section

5. **Lombardy - PEAR/PREAC regional energy-environmental plan**
   - id: `lombardia_pear_preac` | base_url: `https://www.regione.lombardia.it`
   - start_paths: `/ambiente-e-territorio/energia/programma-energetico-ambientale-regionale`
   - level: subnational (region) | access: none
   - region: `["eu","eu_south","italy","lombardy"]` | category: `energy_ministry` | tags: `planning, efficiency, carbon` | policy_types: `regulation, report` | language: it
   - format: HTML + linked PDFs
   - practical: the `wps/portal` URL variant redirects unpredictably to the homepage - use the confirmed path above, not the WPS-portal one. No DC-specific provisions found (general energy/climate plan).
   - effort tier: b
   - why: Milan/Lombardy is Italy's largest DC market; binding regional energy plan (PEAR 2014-2020, successor PREAC approved Dec 2022, 43.8% GHG reduction target vs 2005 by 2030) - fills the "national level only" gap for Italy.
   - verified: yes - WebFetch confirmed plan history, decree numbers, four thematic pillars
   - append to: new `config/domains/italy.yaml` Lombardy section

6. **Madrid - FENERCOM (Fundacion de la Energia de la Comunidad de Madrid)**
   - id: `fenercom_madrid` | base_url: `https://www.fenercom.com`
   - start_paths: `/`, `/presentacion/`, `/informacion/`
   - level: subnational | access: none
   - region: `["eu","eu_south","spain","madrid"]` | category: `economic_dev` | tags: `incentives, efficiency` | policy_types: `incentive, guidance, report` | language: es
   - format: HTML + PDF technical guides
   - practical: standard WordPress-style site
   - effort tier: b
   - why: public foundation of the Madrid regional government (assigned to Directorate-General for Environment/Agriculture/Interior) - the actual publisher of Madrid's efficiency/incentive content (Madrid's own energy-dept pages are thin procedural directories with no real documents). Publishes technical efficiency guides and active incentive programs (Plan Renove Electrodomesticos 2025, MOVES III, Plan Renove Ventanas).
   - verified: yes - WebFetch confirmed foundation status and current program list
   - append to: new Madrid section

7. **Madrid - Estrategia de Energia, Clima y Aire 2023-2030**
   - id: `madrid_estrategia_energia_clima` | base_url: `https://www.comunidad.madrid`
   - start_paths: `/transparencia/informacion-institucional/planes-programas/estrategia-energia-clima-y-aire-comunidad-madrid-2023`
   - level: subnational | access: none
   - region: `["eu","eu_south","spain","madrid"]` | category: `energy_ministry` | tags: `efficiency, planning, carbon` | policy_types: `directive, report` | language: es
   - format: HTML landing page + large PDFs (main doc >10MB, 7 technical annexes)
   - practical: main PDF exceeds typical fetch size limits - crawler should handle large-PDF parsing or extract from the HTML summary instead
   - effort tier: b
   - why: Madrid's actual enacted regional strategy (Orden 2126/2023, published in BOCM Jan 2024, replaces "Plan Azul+") - a formal government strategy document, complementing FENERCOM's foundation-level guides.
   - verified: yes - WebFetch confirmed transparency-portal landing page, legal basis, linked PDF set
   - append to: Madrid section

8. **Vaud - cantonal energy legislation (current + incoming LVLEne)**
   - id: `vd_legislation_energie` | base_url: `https://www.vd.ch`
   - start_paths: `/environnement/energie/legislation`, `/djes/nouvelle-loi-sur-lenergie`
   - level: subnational (canton) | access: none
   - region: `["eu_central","switzerland","vaud"]` | category: `legislative`/`energy_ministry` | tags: `mandates, efficiency` | policy_types: `law, regulation` | language: fr
   - format: HTML
   - practical: DGE-DIREN is the implementing body
   - effort tier: b
   - why: current law (in force through Dec 2026) has the same large-consumer threshold as Zurich/Bern/Geneva (>5 GWh heat / >0.5 GWh electricity/yr); new LVLEne law (adopted Feb 2026, in force Jan 2027) mandates F/G-rated-building retrofits by 2042 and a fossil-heating ban by 2047. No explicit waste-heat/DC clause found (unlike Geneva).
   - verified: yes - both pages fetched, thresholds and new-law provisions confirmed
   - append to: Geneva/Vaud section of switzerland.yaml

9. **Bern - Wirtschafts-, Energie- und Umweltdirektion, energy department**
   - id: `be_weu_energie` | base_url: `https://www.weu.be.ch`
   - start_paths: `/de/start/themen/energie.html`
   - level: subnational (canton) | access: none
   - region: `["eu_central","switzerland","bern"]` | category: `energy_ministry` | tags: `mandates, efficiency` | policy_types: `law, regulation, guidance` | language: de
   - format: HTML
   - practical: none noted
   - effort tier: b
   - why: MuKEn-adopting canton, links to Kantonales Energiegesetz (KEnG, BSG 741.1) and Verordnung (KEnV, BSG 741.111) - same large-consumer framework as Zurich/Geneva (>5 GWh heat / >0.5 GWh electricity/site/yr, mandatory consumption-optimization per Art. 40 KEnG).
   - verified: yes - WebFetch confirmed department identity and law links (full statute text not independently fetched - see unverified below)
   - append to: Bern section

10. **Basel-Stadt - Amt fur Umwelt und Energie (AUE)**
    - id: `bs_aue` | base_url: `https://www.bs.ch`
    - start_paths: `/wsu/aue`
    - level: subnational (canton) | access: none
    - region: `["eu_central","switzerland","basel_stadt"]` | category: `energy_ministry` | tags: `efficiency, planning` | policy_types: `guidance, regulation` | language: de
    - format: HTML
    - practical: the `aue.bs.ch` subdomain variant hit a TLS certificate error - stick to `www.bs.ch/wsu/aue`
    - effort tier: b
    - why: cantonal environment/energy office administering the Energiegesetz (SG 772.100) - water protection, energy conservation, building-energy guidance, heating-replacement subsidies. Basel-Stadt is a growing cantonal DC market adjacent to well-covered Zurich.
    - verified: yes (for `www.bs.ch/wsu/aue` only)
    - append to: Basel-Stadt section

11. **Boletin Oficial de Aragon (BOA)** - borderline tier-b/c
    - id: `boa_aragon` | base_url: `https://www.boa.aragon.es`
    - start_paths: `/cgi-bin/EBOA/BRSCGI?CMD=VERLST&BASE=BZHT&SEC=BUSQUEDA_AVANZADA`
    - level: subnational | access: none
    - region: `["eu","eu_south","spain","aragon"]` | category: `legislative` | tags: `mandates, legislation` | policy_types: `law, regulation` | language: es
    - format: HTML search UI + PDF
    - practical: CGI-based parameter-driven search (`BRSCGI`), same tooling family as the already-shipped `boe_es` - a targeted query string per keyword may work better than open-ended crawling
    - effort tier: b (c if a query-parameter-driven client is preferred over blind crawling)
    - why: Aragon's own regional gazette - the actual publication venue for the DIGA approvals (see #2) and energy-transition decree-laws in full text
    - verified: yes - successfully fetched a real gazette PDF confirming the mechanism works; DIGA/energy-specific issue numbers found via WebSearch snippets only (not independently re-fetched)
    - append to: Aragon section

12. **Geneva - Etat de Geneve energy-transition policy hub**
    - id: `ge_transition_energetique` | base_url: `https://www.ge.ch`
    - start_paths: `/dossier/transition-energetique-geneve`
    - level: subnational | access: none
    - region: `["eu_central","switzerland","geneva"]` | category: `energy_ministry` | tags: `district_heating, efficiency, planning` | policy_types: `strategy, guidance` | language: fr
    - format: HTML
    - practical: possibly benefits from `requires_playwright: true` (peer ge.ch pages use dynamic nav, not confirmed necessary here)
    - effort tier: b
    - why: companion crawl entry to the Geneva LEn law text (#1) - Plan directeur de l'energie 2020-2030, links to "Rejets thermiques" (waste heat) and "Chauffer et rafraichir Geneve" (district heating/cooling) sub-pages, Loi 13222 (2024) building-retrofit financing.
    - verified: yes - WebFetch confirmed content, program names, sub-page links
    - append to: Geneva section

### Unverified / needs human check (Spain/Italy/Switzerland)

- **Basel-Stadt Energiegesetz full text** (SG 772.100),
  `gesetzessammlung.bs.ch/app/de/texts_of_law/772.100` - resolves (HTTP 200)
  but is a JS single-page app ("LexWork" platform); WebFetch got only a
  page-shell title. WebSearch snippets confirm this is genuinely
  Basel-Stadt's Energiegesetz. Needs `requires_playwright: true` and a
  human/browser confirmation of rendered content.
- **Bern KEnG full text** (BSG 741.1),
  `belex.sites.be.ch/app/de/texts_of_law/741.1` - same "LexWork" SPA-shell
  issue; WebSearch confirms large-consumer/Art. 40 provisions but direct
  fetch couldn't render them. Needs Playwright-based verification.
- **Aragon Direccion General de Energia y Minas** - direct organism page
  URLs from search results resolved to unrelated content (stale post-reorg
  links) or 404'd. Needs a human to find the current live URL (contact
  confirmed: Paseo Maria Agustin 36, Zaragoza) - candidates #2/#3 above are
  solid substitutes meanwhile.
- **Vaud full statute text** (Loi vaudoise sur l'energie / LVLEne PDF) - only
  summary/index pages were fetched (#8); raw consolidated law text at
  `lexfind.ch/tolv/249856/fr` or the LVLEne PDF itself not independently
  fetched. Needed if article-level detail is required.
- **Geneva OCEN standalone office page** - not searched for; likely
  unnecessary given #1 and #12 already cover this canton well.
- **CHA moratorium proposal on Aragon data centers** (a political party's
  *proposed* water/energy tax on DC water/energy use, per Xataka/Onda
  Aragonesa coverage) - explicitly EXCLUDED as a proposal/news item, not
  enacted policy; flagged only so it isn't mistakenly re-discovered and
  added later as if it were law.

---

## Canada (Saskatchewan, Nova Scotia, New Brunswick, Newfoundland and Labrador)

Existing shipped (skip): nrcan_ca, cer_ca, eccc_ca, nrcan_oee (federal);
ontario_energy, oeb_ca, ieso_ca (Ontario); bc_energy, cleanbc (BC);
quebec_energy, hydroquebec_ee (Quebec); alberta_energy, auc_ca (Alberta).
Already-drafted-but-unshipped (skip): aeso_large_load, bcuc_thermal,
vancouver_neu, markham_district_energy, toronto_district_energy,
nrc_codes_canada, regie_energie_qc, ola_bills, manitoba_energy,
donneesquebec_bills (tier-c).

Region note: `saskatchewan`/`nova_scotia`/`new_brunswick`/
`newfoundland_and_labrador` are not in `VALID_REGIONS` (same gap already
flagged for `manitoba`) - map to `["north_america","canada"]`, preserve
province identity in id/name/notes.

### Verified candidates (ranked best-first)

1. **SaveEnergyNB (New Brunswick)**
   - id: `saveenergynb` | base_url: `https://www.saveenergynb.ca`
   - start_paths: `/`, `/en/for-business/`
   - level: subnational | access: none
   - region: `["north_america","canada"]` | category: `economic_dev` | tags: `incentives, efficiency` | policy_types: `incentive, program` | language: en
   - format: HTML
   - practical: loaded cleanly, no block. Delivered jointly by NB Power + Govt of NB + Govt of Canada.
   - effort tier: b
   - why: Business Rebate Program (25% back), Commercial Buildings Retrofit ($1.25M cap), Industrial Energy Efficiency Program ($1M cap), New Construction Program ($250k/building) - concrete incentive policy; NB currently has zero entries in canada.yaml.
   - verified: yes - WebFetch confirmed full program listings
   - append to: `canada.yaml` new New Brunswick section

2. **takeCHARGE (Newfoundland and Labrador)**
   - id: `takecharge_nl` | base_url: `https://takechargenl.ca`
   - start_paths: `/`
   - level: subnational | access: none
   - region: `["north_america","canada"]` | category: `economic_dev` | tags: `incentives, efficiency` | policy_types: `incentive, program` | language: en
   - format: HTML
   - practical: loaded cleanly, no block
   - effort tier: b
   - why: joint NL Hydro/Newfoundland Power program - Business Efficiency Program up to $50,000, plus an Isolated System Business Efficiency Program for off-grid communities; NL also has zero existing entries.
   - verified: yes - WebFetch confirmed program details
   - append to: new Newfoundland and Labrador section

3. **Efficiency Nova Scotia**
   - id: `efficiency_ns` | base_url: `https://www.efficiencyns.ca`
   - start_paths: `/programs-rebates`, `/programs-rebates/business-energy-rebates`, `/programs-rebates/building-optimization-program`, `/programs-rebates/pay-for-performance-program`
   - level: subnational | access: none
   - region: `["north_america","canada"]` | category: `economic_dev` | tags: `incentives, efficiency` | policy_types: `incentive, program` | language: en
   - format: HTML, JS-rendered - `requires_playwright: true` recommended (WebFetch returned only the `<title>`)
   - practical: arms-length efficiency utility created by government in 2009
   - effort tier: b
   - why: working alternate entry point for NS efficiency content (the ministry subdomain `energy.novascotia.ca` remains blocked - see unverified below). Building Optimization Program and Pay-for-Performance Program are directly large-facility/DC-relevant.
   - verified: yes - confirmed via browser render (nav listing all four programs)
   - append to: new Nova Scotia section

4. **Government of Saskatchewan - Building/Energy Code + Large-Emitter Carbon Program**
   - id: `saskatchewan_energy_standards` | base_url: `https://www.saskatchewan.ca`
   - start_paths: `/business/housing-development-construction-and-property-management/building-and-technical-standards/national-building-and-fire-code-information`, `/business/environmental-protection-and-sustainability/a-made-in-saskatchewan-climate-change-strategy/guidance-for-emitters`
   - level: subnational | access: none
   - region: `["north_america","canada"]` | category: `standards` | tags: `efficiency, mandates, carbon, reporting` | policy_types: `standard, regulation` | language: en
   - format: HTML + PDF
   - practical: every `saskatchewan.ca` URL returned HTTP 403 to WebFetch (domain-wide bot detection); loaded fully via real browser, no login wall - `requires_playwright: true` recommended
   - effort tier: b
   - why: NECB 2020 adoption (Jan 2024, sets Tier-1 large-building efficiency floor applicable to DC construction) and Output-Based Performance Standards (OBPS) carbon program (mandatory registration/reporting for electricity facilities >10,000 tCO2e/yr, industrial >25,000 tCO2e/yr).
   - verified: yes, via browser on both paths
   - append to: new Saskatchewan section

5. **SaskPower - Commercial Energy Optimization Program**
   - id: `saskpower_ceop` | base_url: `https://www.saskpower.com`
   - start_paths: `/power-savings-and-programs/business/programs/commercial-energy-optimization-program`, `/power-savings-and-programs`
   - level: subnational | access: none
   - region: `["north_america","canada"]` | category: `grid_operator` | tags: `incentives, efficiency` | policy_types: `incentive, program` | language: en
   - format: HTML + PDF
   - practical: loaded cleanly via WebFetch; program runs to March 31, 2027 with rolling annual deadlines - expect content churn on renewal
   - effort tier: b
   - why: $0.13/kWh (non-lighting) and $15/GJ natural-gas incentives, up to $100,000 per fuel type per project - directly applicable to large facility/DC retrofits.
   - verified: yes - WebFetch confirmed incentive tiers and eligibility
   - append to: Saskatchewan section

6. **New Brunswick Energy & Utilities Board (EUB)**
   - id: `nbeub` | base_url: `https://nbeub.ca`
   - start_paths: `/electricity-decisions`, `/electricity-home`, `/all-current-matters-decisions`
   - level: subnational | access: none
   - region: `["north_america","canada"]` | category: `regulatory` | tags: `mandates, reporting` | policy_types: `regulation, report` | language: en
   - format: HTML + PDF (decision archive back to 1991)
   - practical: loaded cleanly, no block
   - effort tier: b
   - why: NB Power rate decisions, Integrated Resource Plan reviews, generation-facility approvals - regulatory counterpart to `saveenergynb`.
   - verified: yes - WebFetch confirmed decision archive content
   - append to: New Brunswick section

7. **Newfoundland and Labrador Board of Commissioners of Public Utilities (PUB NL)**
   - id: `pub_nl` | base_url: `http://www.pub.nl.ca` (HTTP only - no HTTPS available)
   - start_paths: `/`, `/PU_ordersArchive.php`
   - level: subnational | access: none
   - region: `["north_america","canada"]` | category: `regulatory` | tags: `mandates, reporting` | policy_types: `regulation, report` | language: en
   - format: HTML + PDF (numbered "P.U." orders)
   - practical: plain HTTP only - WebFetch's automatic HTTPS upgrade caused ECONNREFUSED; confirmed working over `http://` via real browser. Whoever wires this up must verify the crawler config accepts a non-HTTPS base_url.
   - effort tier: b
   - why: electricity rate orders for NL Hydro/Newfoundland Power (2026 NL Hydro General Rate Application, 2027 Newfoundland Power Capital Budget) - regulatory counterpart to `takecharge_nl`.
   - verified: yes, via browser only (not WebFetch)
   - append to: Newfoundland and Labrador section

8. **Nova Scotia Energy and Regulatory Boards Tribunal (successor to NSUARB)**
   - id: `nserbt_ns` | base_url: `https://nserbt.ca`
   - start_paths: `/mandates/electricity/customer-page/changes-power-rates`, `/mandates/electricity/municipal-utilities-overview`
   - level: subnational | access: none
   - region: `["north_america","canada"]` | category: `regulatory` | tags: `mandates, reporting` | policy_types: `regulation, report` | language: en
   - format: HTML + PDF (decisions/orders, e.g. "2025 NSUARB 51")
   - practical: old host `nsuarb.novascotia.ca` now 301-redirects here (board rebranded/merged); WebFetch followed the redirect cleanly
   - effort tier: b
   - why: NS's utility regulator - rate-setting for NS Power and municipal electric utilities, fills the NS-regulator gap the way BCUC/OEB/AUC do elsewhere.
   - verified: yes - WebFetch loaded content confirming mandate/rate-review process after redirect
   - append to: Nova Scotia section

9. **Government of New Brunswick - Laws (Electricity Act, Part 6 Division E - Energy Efficiency)**
   - id: `nb_laws_electricity_act` | base_url: `https://laws.gnb.ca`
   - start_paths: `/en/ShowTdm/cs/2013-c.7`
   - level: subnational | access: none
   - region: `["north_america","canada"]` | category: `legislative` | tags: `mandates` | policy_types: `law, regulation` | language: en/fr
   - format: HTML (statute text)
   - practical: loaded cleanly. CAVEAT: the older 1992 Energy Efficiency Act (E-9.11) is repealed (2011) - do not use that path as current law; the active provision is Electricity Act (2013, c.7) Part 6 Division E, plus a referenced 2022 regulation ("2022-74 - Energy Efficiency") a human should confirm/add.
   - effort tier: b
   - why: only genuine NB legislative source found - energy-efficiency/demand-response provisions embedded directly in the Electricity Act.
   - verified: yes for the 2013-c.7 TOC page (Part 6 Division E confirmed present)
   - append to: New Brunswick section

10. **SaskEnergy - Rebates & Programs**
    - id: `saskenergy_rebates` | base_url: `https://www.saskenergy.com`
    - start_paths: `/ways-save/rebates-programs`, `/ways-save/homes-beyond-code`
    - level: subnational | access: none
    - region: `["north_america","canada"]` | category: `grid_operator` | tags: `incentives, efficiency` | policy_types: `incentive, program` | language: en
    - format: HTML
    - practical: loaded cleanly via WebFetch
    - effort tier: b
    - why: natural-gas-side rebates (boiler rebates $4,000+, "Homes Beyond Code") complementing `saskpower_ceop`'s electric-side program - narrower/lower priority.
    - verified: yes
    - append to: Saskatchewan section

11. **Newfoundland and Labrador Department of Energy and Mines**
    - id: `nl_energy_mines` | base_url: `https://www.gov.nl.ca`
    - start_paths: `/em/`
    - level: subnational | access: none
    - region: `["north_america","canada"]` | category: `energy_ministry` | tags: `planning, reporting` | policy_types: `guidance, report` | language: en
    - format: HTML + PDF
    - practical: loaded cleanly. CAVEAT: older sources call this "Department of Industry, Energy and Technology" (IET) - the `/iet/department/` path resolves to the same content; possible 2026 machinery-of-government rename in progress, a human should confirm current org chart.
    - effort tier: b
    - why: rounds out NL with a ministry-level source (energy/petroleum/mining policy portal, legislation links) - weakest of the eleven, largely a navigation hub.
    - verified: yes, lowest confidence due to naming ambiguity
    - append to: Newfoundland and Labrador section

### Unverified / needs human check (Canada)

- **Nova Scotia Department of Energy and Mines - Efficiency and Conservation
  subpage** (`energy.novascotia.ca/energy-efficiency/efficiency-and-conservation`)
  - re-tested this pass, still returns "Access denied" (browser-confirmed).
  Domain-wide bot detection on `energy.novascotia.ca`, not path-specific. Not
  re-proposed since #3 and #8 above deliver equivalent/better content from
  unblocked hosts.

---

## Japan (Osaka, Chiba, Saitama) and China (Guizhou, Inner Mongolia, Ningxia)

Existing shipped (skip): meti_jp, enecho_jp, elaws_jp (Japan national),
motie_kr, law_kr (South Korea). Already-drafted-but-unshipped (skip):
tokyo_toshiseibi_dc, tokyo_kankyo_capandtrade (Tokyo), beijing_gov_dc,
shanghai_gov_dc, miit_cn, govcn_dc (China).

Region note: `japan` is a valid individual region string; Osaka/Chiba/Saitama
map to `["apac","japan"]`. China provinces have no individual
`VALID_REGIONS` entry - map to `["apac"]`, preserve province identity in
id/name/notes.

### Verified candidates (ranked best-first)

1. **Ningxia - Zhongwei Data Center Development Implementation Plan**
   - id: `ningxia_zhongwei_dc` | base_url: `https://www.nx.gov.cn`
   - start_paths: `/zt/nxxtgjqyjjgzlfzxgjzctx/zcfb/202305/t20230523_4118499.html`
   - level: subnational (autonomous region) | access: none
   - region: `["apac"]` | category: `regulatory` | tags: `mandatory, pue_limits, renewable_energy, incentives` | policy_types: `regulation, incentive` | language: zh
   - format: HTML
   - practical: no robots.txt issue; standard gov.cn HTML, no JS rendering needed
   - effort tier: b
   - why: new large/extra-large data centers must hit PUE <=1.15 and >=65% renewable-energy use; PUE >1.3 construction/expansion is prohibited outright. Substantial incentives (green power pricing, land priority, RMB 100M/yr backbone bond funding, RMB 11M/yr operating subsidy). Zhongwei is one of the 8 national "East Data West Compute" hub nodes - most concrete/stringent PUE mandate found in any of the 8 hub provinces.
   - verified: yes - fetched directly, PUE figures and incentive amounts confirmed on the page itself
   - append to: `config/domains/china.yaml` (the not-yet-created file the east-asia draft already proposes) Ningxia section

2. **Ningxia Development and Reform Commission**
   - id: `ningxia_fzggw` | base_url: `https://fzggw.nx.gov.cn`
   - start_paths: `/`, `/zcgh/zzqzc/index_1.html`, `/tzgg/`
   - level: subnational | access: none
   - region: `["apac"]` | category: `regulatory` | tags: `mandatory, carbon, efficiency, renewable_energy` | policy_types: `regulation, guidance` | language: zh
   - format: HTML
   - practical: homepage/listing pages fetched cleanly; the one specific 2022 "Ningxia Data Center Construction Guide" notice found via search 404'd on direct fetch (likely archived/moved) - do not use that exact path
   - effort tier: b
   - why: the named agency behind #1 - publishes computing-hub-node policy opinions, energy-rights trading reform, carbon-peak plan; broader crawl surface will catch newer DC-specific notices (2026-dated items visible in listings).
   - verified: yes for base domain and listing pages (real document titles/dates seen); the specific DC-guide URL is unverified
   - append to: Ningxia section, alongside #1

3. **Inner Mongolia Energy Bureau - Green Power Direct Connection for Data Centers**
   - id: `nmg_energy_greenpower` | base_url: `https://nyj.nmg.gov.cn`
   - start_paths: `/tzgg/202601/t20260115_2848788.html`, `/zwgk/`
   - level: subnational | access: none
   - region: `["apac"]` | category: `energy_ministry` | tags: `mandatory, renewable_energy, data_center_specific` | policy_types: `regulation` | language: zh
   - format: HTML
   - practical: confirmed reachable and current (2026-dated documents visible); no Playwright needed. IMPORTANT: the general provincial portal (`www.nmg.gov.cn`) and its Industry/IT (`gxt.nmg.gov.cn`) and Science/Tech (`kjt.nmg.gov.cn`) subdomains all returned HTTP 403 on direct fetch - only the Energy Bureau subdomain was reachable; do not propose those other subdomains without a human re-check.
   - effort tier: b
   - why: document 内能源新能发〔2026〕1号 (Jan 13, 2026) mandates new DC loads in the Helingeer/Hohhot national hub-node cluster achieve >=80% green-power consumption via direct connection/green trading/green certificates, with existing loads ramping up gradually. Inner Mongolia is one of the 8 national hubs with among China's strictest PUE rules due to its coal-heavy grid.
   - verified: yes - fetched directly, 80% green-power quote for the Helingeer cluster confirmed verbatim
   - append to: Inner Mongolia section

4. **Osaka Prefecture - Climate Change Countermeasures Promotion Ordinance**
   - id: `osaka_ondanka_jourei` | base_url: `https://www.pref.osaka.lg.jp`
   - start_paths: `/o120020/chikyukankyo/ondankaboushi_jourei/index.html`, `/kurashi/kankyou/energy/index.html`
   - level: subnational (prefecture) | access: none
   - region: `["apac","japan"]` | category: `regulatory` | tags: `mandatory, carbon, reporting` | policy_types: `regulation` | language: ja
   - format: HTML/PDF
   - practical: no access issues; standard prefectural HTML
   - effort tier: b
   - why: mandatory climate-action-plan and performance-report filing for "specified business operators" (large energy users, capturing large DCs), plus a separate environmental-consideration filing for large-building construction. Osaka is Japan's #2 DC market - direct analogue to Tokyo's already-drafted cap-and-trade scheme.
   - verified: yes - ordinance name, reporting requirement, filing requirement confirmed on page. Exact energy-use threshold for "specified" status only visible in linked PDFs (not independently re-fetched) - one confidence notch below full numeric verification.
   - append to: new `config/domains/japan.yaml` Osaka section (or `apac.yaml` per human file-placement call - see note below)

5. **Saitama Prefecture - Target-Setting Type Emissions Trading System**
   - id: `saitama_torihikiseido` | base_url: `https://www.pref.saitama.lg.jp`
   - start_paths: `/a0502/torihikiseido.html`, `/a0502/keikaku.html`, `/a0502/index.html`
   - level: subnational | access: none
   - region: `["apac","japan"]` | category: `regulatory` | tags: `mandatory, carbon, reporting` | policy_types: `regulation` | language: ja
   - format: HTML/PDF
   - practical: no access issues
   - effort tier: b
   - why: mandatory cap-and-trade for large-scale business sites, using the SAME 1,500kL crude-oil-equivalent threshold as Tokyo's cap-and-trade and the national METI/ANRE DC-PUE benchmark - large Saitama data centers are covered entities. 4th compliance period FY2025-2029, same period as Tokyo's - structurally the closest parallel to Tokyo's scheme found anywhere in Japan.
   - verified: yes - threshold, reduction-target/trading mechanics, compliance period all confirmed on page
   - append to: Saitama section

6. **Chiba Prefecture - Global Warming Countermeasures Promotion Division** - lowest priority of the Japan finds
   - id: `chiba_ontai` | base_url: `https://www.pref.chiba.lg.jp`
   - start_paths: `/ontai/`, `/ontai/hojo/datsutanso-sokushin.html`
   - level: subnational | access: none
   - region: `["apac","japan"]` | category: `regulatory` | tags: `incentives, carbon, efficiency` | policy_types: `incentive, guidance` | language: ja
   - format: HTML
   - practical: no access issues
   - effort tier: b
   - why: business decarbonization-equipment subsidy program and 46%-by-FY2030 GHG reduction plan; NO mandatory large-facility reporting scheme found (unlike Tokyo/Saitama/Osaka), though WebSearch indicates Chiba is drafting a GHG-reporting ordinance (not yet enacted). Chiba hosts Japan's largest hyperscale DC cluster (Inzai) but currently has the weakest prefectural DC-adjacent policy of the three - worth tracking, not a strong current find.
   - verified: yes for the subsidy program and reduction plan; the in-development reporting ordinance is WebSearch-only (not yet an enacted document)
   - append to: Chiba section

File-placement note (Japan): the researcher recommends splitting Japan out
into its own `config/domains/japan.yaml` given Tokyo (x2, already drafted) +
these three prefectures would make 5 Japan-specific entries - or keep
appending to `apac.yaml` if a single file is preferred. Human call either way.

### Unverified / needs human check (Japan/China)

- **Guizhou Provincial Big Data Development and Management Bureau**
  (`dsj.guizhou.gov.cn`) - STILL UNREACHABLE. Retried this pass:
  `connect ECONNREFUSED 117.187.129.229:443`. Widened the test to five other
  Guizhou-hosted domains - `www.guizhou.gov.cn`, `www.gzrd.gov.cn`,
  `www.bijie.gov.cn`, `www.gzss.gov.cn`, `www.guiyang.gov.cn` - all resolve
  to the same `117.187.129.x` IP block and all failed identically; one
  Guizhou-hosted site on different infrastructure (`www.kaiyang.gov.cn`, a
  small county) DID load fine. This means the entire provincial/Guiyang-metro
  government hosting cluster is unreachable from this research environment -
  not a blanket China block, not specific to this one bureau. Per
  WebSearch only (NOT independently fetched, do not treat as confirmed):
  Guizhou's Provincial People's Congress reportedly passed a "Big Data
  Development and Application Promotion Regulation" effective 2026-01-01
  requiring departments to promote green/low-carbon DC development, plus a
  separate "several policies to encourage data industry development"
  document referencing a DC energy-monitoring platform, continuous PUE
  measurement, and an 80-万-rack/PUE<=1.2-by-2025 target for new
  large/hyperscale DCs. Recommend a human re-check from an unrestricted
  network before adding anything for Guizhou.

---

## Cross-cutting notes for whoever drafts YAML from this

- Several new country/province files are implied but not yet created:
  `brazil.yaml` needs a Sao Paulo/Rio/Parana section (existing file is
  federal-only), `mexico.yaml` needs Queretaro/Nuevo Leon sections,
  `spain.yaml` needs Aragon/Madrid/Catalonia sections, `italy.yaml` needs a
  Lombardy section, `switzerland.yaml` needs Geneva/Vaud/Bern/Basel-Stadt
  sections, `australia.yaml` needs Tasmania/ACT sections, `canada.yaml`
  needs Saskatchewan/Nova Scotia/New Brunswick/Newfoundland-and-Labrador
  sections, `india.yaml` needs Uttar Pradesh/Gujarat/West Bengal/Odisha
  sections (Maharashtra section already exists, needs two more entries
  added to it). `china.yaml` and `japan.yaml` do not exist yet at all (both
  were already proposed as new files by the wave-1 east-asia draft; this
  pass adds more content to each).
- A recurring `VALID_REGIONS` gap: individual-state/province region strings
  don't exist for most of the jurisdictions researched here (only a handful
  of Indian/Australian/Canadian states are individually registered). Every
  candidate above uses the broader valid region bucket and preserves exact
  jurisdiction identity in `id`/`name`/`notes` - a human may want to extend
  `VALID_REGIONS` (`src/core/config.py`) before or during YAML drafting.
- Recurring bot-detection pattern: Australian and Canadian provincial sites
  in particular block WebFetch/curl-style requests but load fine in a real
  browser - `requires_playwright: true` is recommended wherever this was
  observed, flagged individually above.
