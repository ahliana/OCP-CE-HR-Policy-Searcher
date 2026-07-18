# Source Expansion Research - Wave 4: Long-Tail Countries

Branch: `feature/source-expansion-research`. Research only - no client code touched, no
domain added with `enabled: true`. All candidates below are draft additions.

## Dedup check performed

Read `config/domains/*.yaml` (all 33 country/region files + `api_sources.yaml`) and
grepped every draft crawl file under `docs/source-expansion/draft/crawl/**/*.yaml`
(waves 1-3) for `base_url` collisions against every country/territory in this wave's
brief. No collisions found for any brand-new jurisdiction. Four countries in this wave
already have a prior-wave candidate on file, so this wave only proposes genuinely
additional sources for them (or reports honestly that nothing additional exists):

- **Mongolia**: `erc_mn` (Energy Regulatory Commission - heat tariffs, Ulaanbaatar DH)
  already planned for `config/domains/mongolia.yaml`. This wave adds a distinct
  building-efficiency + draft heat-supply-law source (MCUD).
- **Cote d'Ivoire**: national energy ministry already covered. This wave adds the ICT/
  digital-transition ministry and the telecom regulator (both distinct institutions).
- **Kuwait**: `mew_kw` (Ministry of Electricity, Water and Renewable Energy) already
  planned for `config/domains/kuwait.yaml`. This wave adds the Environment Public
  Authority (industrial emissions/EIA angle).
- **Malta**: two candidates already on file (Energy and Water Agency, REWS - both note
  Malta has no district heating/cooling). This wave found one more (Building and
  Construction Authority / EPC regulation) but could **not** get a direct fetch to
  succeed (403 every attempt) - listed as unverified, not a confirmed add.
- **Iceland**: three candidates already on file (Orkustofnun, reglugerdir.is,
  Reykjavik-area DH operator, Business Iceland). Checked for anything further -
  genuinely nothing new found. Iceland appears exhausted for this wave. One relevant
  note for whoever maintains `nordic.yaml`: Orkustofnun's parent identity may be
  migrating to `uos.is` (Umhverfis- og orkustofnun) following a 2025 agency merger -
  worth a maintenance check, not a new-source claim.
- **Costa Rica**: national ministry already covered. Checked ARESEP (utility
  regulator) - live but has no efficiency/DC content, not proposed. One promising lead
  (DIGECA district-cooling strategy) could not be verified live - see unverified
  section.

---

## Verified candidates (ranked best-first)

### 1. Mauritius - Energy Efficiency Management Office (EEMO) + Ministry of Energy and Public Utilities

- **name**: "Mauritius Energy Efficiency Management Office (EEMO)"
- **proposed id**: `mauritius_eemo_energy_efficiency`
- **base_url**: `https://eemo.govmu.org`
- **start_paths**: `/` (regulations + guidelines index); companion page
  `https://publicutilities.govmu.org/Pages/Legislation/Energy.aspx` for the parent Act
- **level**: national
- **access**: none
- **coverage**: region: `mauritius`; category: `energy_efficiency`; created under the
  Energy Efficiency Act 2011. Live regulations include Minimum Energy Performance
  Standards for refrigerating appliances (2026), the **Energy Efficiency (Control of
  Non-Essential Grid-Powered Activities) Regulations (2026)** - name alone suggests
  direct relevance to always-on server/DC-type grid loads - plus sector guidelines
  (Commercial, Manufacturing, Public Sector, Hotels), energy-audit procedures, an
  appliance-labelling scheme, and Energy Observatory Reports (2015-2022). Parent
  ministry page separately hosts the Energy Efficiency Act 2011, Labelling of Regulated
  Machinery Regulations 2017, Registration of Energy Auditors Regulations 2016, Energy
  Consumer and Energy Audit Regulations 2017. language: English
- **format**: PDF + HTML
- **practical**: govmu.org domain, no robots.txt block encountered, no rate limit found
- **effort tier**: (b) plain crawl
- **why worth adding**: most mature statutory EE regime found across this entire wave -
  binding MEPS regulations and a regulation literally targeting non-essential
  grid-powered activity, closest thing to a DC-adjacent mandate found in Africa/Indian
  Ocean.
- **verified**: yes - fetched both `eemo.govmu.org` (listed regulations/guidelines
  above) and the ministry legislation page (confirmed Act + 3 named regulations with
  download links).

### 2. Panama - JTIA (Junta Técnica de Ingeniería y Arquitectura) - Reglamento de Edificación Sostenible

- **name**: "Panama JTIA - Sustainable Building Regulation (RES v.2)"
- **proposed id**: `panama_jtia_res`
- **base_url**: `https://jtiapanama.org.pa`
- **start_paths**: `/` (Normativa legal y sanciones section); gazette PDF
  `https://nube.jtiapanama.org.pa/archivos/leyes_decretos/archivo_06032023_114855.pdf`
  (Gaceta Oficial No. 29726, 23 Feb 2023)
- **level**: national
- **access**: none
- **coverage**: region: `panama`; category: `building_efficiency`. Panama's mandatory
  national Sustainable Building Regulation (RES v.2, 2022, in force since 1 Aug 2023),
  issued by JTIA (public-law engineering/architecture board, Law 15/1959) under
  authority of Law 69/2012 (UREE), coordinated with the national energy secretariat.
  Sets minimum energy-efficiency requirements for new construction nationwide,
  including industrial/commercial buildings - would apply to data-center construction.
  language: Spanish
- **format**: HTML (site) + PDF (gazette/resolution text)
- **practical**: standard CMS, loads cleanly. The gazette PDF sits on a `nube.`
  subdomain and downloads fine (4.4MB) though its compressed text stream didn't extract
  cleanly in this pass - identity corroborated across three independent sources.
  Revisions roughly every 3-7 years (v1: 2019, v2: 2022).
- **effort tier**: (b) plain crawl
- **why worth adding**: only concrete, mandatory, verified energy-efficiency-in-
  buildings regulation found for Panama, directly on-topic for DC construction in a
  country actively marketed as a hemispheric data-center/connectivity hub.
- **verified**: yes - navigated jtiapanama.org.pa (200) and fetched the gazette PDF
  (200, correct file, corroborated identity).

### 3. Trinidad & Tobago - TTBS Energy Efficiency Building Code

- **name**: "Trinidad and Tobago Bureau of Standards (TTBS) - Energy Efficiency Building Code"
- **proposed id**: `trinidad_tobago_ttbs_eebc`
- **base_url**: `https://gottbs.com`
- **start_paths**: `/2022/01/25/draft-national-standard-for-public-comment-trinidad-and-tobago-energy-efficiency-building-code/`
  (free scope/summary page); `/product/trinidad-and-tobago-energy-efficiency-building-code-2023-edition/`
  (official 2023-edition listing; full text is a one-time paid PDF, ~$1,190 USD)
- **level**: national
- **access**: none for scope/summary pages; the full standard text is a one-time
  purchase, not a login/subscription
- **coverage**: region: `trinidad_and_tobago`; category: `building_efficiency`.
  Trinidad and Tobago Energy Efficiency Building Code (EEBC), 2023 edition, adapted
  from the CARICOM Regional Energy Efficiency Building Code (itself based on ASHRAE
  90.1-2016) - minimum energy-efficiency design/construction requirements for new
  buildings and major retrofits (small residential exempted), directly relevant to any
  DC building shell in-country. language: English
- **format**: HTML (free pages) + PDF (paid full standard)
- **practical**: TTBS is the official statutory national standards body. 2023 edition
  is current per the product listing.
- **effort tier**: (b) plain crawl for free/scope pages; full text is paywalled
- **why worth adding**: only genuine, mandatory building-level energy-efficiency
  standard found for Trinidad & Tobago, timely given the country's active 2026 push for
  AI/data-center MOUs.
- **verified**: yes - fetched both pages (200/200).

### 4. Turkmenistan - Government Legislation Portal (Law on Energy Saving and Energy Efficiency)

- **name**: "Turkmenistan Government Portal - Legislation feed"
- **proposed id**: `turkmenistan_govportal_legislation`
- **base_url**: `https://turkmenistan.gov.tm`
- **start_paths**: `/ru/razdel/zakonodatelstvo` (reverse-chronological all-sector law
  feed); specific law page `/ru/post/82397/zakon-turkmenistana-ob-energosberezhenii-i-energoeffektivnosti`
- **level**: national
- **access**: none
- **coverage**: region: `turkmenistan`; category: `energy_efficiency`. Law "On Energy
  Saving and Energy Efficiency" (adopted 2024-03-30, published 2024-04-09) - mandatory
  energy audits (every 5 years for state-funded efficiency projects), building
  energy-efficiency classes, "energy passports," mandatory metering for new/renovated
  construction, state incentives (tax breaks, preferential credit, differentiated
  tariffs). language: Russian (Turkmen elsewhere on the portal - keywords.yaml Turkmen
  coverage should be checked)
- **format**: HTML, individual law pages at `/ru/post/{id}/{slug}`
- **practical**: robots.txt fully permissive (`Allow: /`, sitemap.xml provided). Feed
  mixes all government sectors (defense, labor, fisheries, energy, etc.) and is
  actively updated through July 2026 - a topic/keyword filter is essential.
- **effort tier**: (b) plain crawl
- **why worth adding**: the only verified live source carrying Turkmenistan's actual
  current energy-efficiency law text; there is essentially no other accessible
  Turkmen government energy-policy web presence.
- **verified**: yes - fetched the specific law page directly (full text/summary
  retrieved) and the legislation feed page (confirmed live, updated to July 2026).

  **Companion candidate** (secondary, same country): Ministry of Energy of
  Turkmenistan, id `turkmenistan_minenergo`, base_url `https://minenergo.gov.tm`,
  start_path `/rules/23` (Law on Electric Power Industry articles covering heat/
  electric energy supply contracts and tariffs), language Turkmen. verified: yes -
  fetched `/index.php/lang/en` and `/rules/23` directly.

### 5. Papua New Guinea - DICT Government Cloud Policy

- **name**: "PNG Department of Information & Communications Technology - Government Cloud Policy"
- **proposed id**: `png_dict_government_cloud_policy`
- **base_url**: `https://www.ict.gov.pg`
- **start_paths**: `/Policy/` (index); PDF `/Policies/Cloud%20Policy/Final%20Government%20Cloud%20Policy%202023%20V2.7%20-%20Final.pdf`
- **level**: national
- **access**: none (standard WordPress site; robots.txt only blocks `/wp-admin/`,
  sitemap at `/wp-sitemap.xml`)
- **coverage**: region: `papua_new_guinea`; category: `digital_infrastructure`.
  Government Cloud Policy (2023, v2.7) governing agency use of cloud/hosting
  infrastructure, plus Digital Government Act (2022) and Digital Transformation Policy
  (2020). Policy landing page references upcoming "Government Digital Standards"
  explicitly covering cloud services and data centers (in stakeholder review). Not an
  energy-efficiency mandate, but directly on-topic for data-center governance -
  genuinely rare for this region. language: English
- **format**: HTML index + PDF (PDFs appear image/embedded-font based, may need OCR)
- **practical**: crawl-friendly robots.txt, sitemap published, no rate-limit info
  published.
- **effort tier**: (b) plain crawl
- **why worth adding**: explicitly titled "Cloud Policy" touching data-center/hosting
  standards - rare and directly on-topic find.
- **verified**: yes - fetched `/Policy/` directly, got real linked document titles and
  exact URLs; PDF resolved (200, correct content-type/size) though text didn't extract
  cleanly.

### 6. Fiji (via Pacific Community regional hub) - National Energy Policy 2023-2030

- **name**: "Pacific Community (SPC) Regional Energy Policy Hub - PRDR SE4ALL"
- **proposed id**: `pacific_prdr_se4all_energy_hub`
- **base_url**: `https://prdrse4all.spc.int`
- **start_paths**: `/list/publication` (filterable by country + "Policies and Plans"
  category), `/countries/fiji`, `/countries/papua-new-guinea` (also covers every other
  Pacific SIDS)
- **level**: supranational (Pacific Community/SPC intergovernmental body; documents
  copyright to the national departments, e.g. "Copyright: Fiji Department of Energy")
- **access**: none (public)
- **coverage**: region: `fiji` (tag additional country slugs per document); category:
  `energy_efficiency`. Confirmed live: **Fiji National Energy Policy 2023-2030** (60pp,
  PDF, 3.28MB) with a dedicated Energy Efficiency pillar (alongside Security/Access/
  Sustainability/Governance). This is the practical route to Fiji policy content right
  now: Fiji's own `.gov.fj` estate (energy.gov.fj, fdoe.gov.fj, mims.gov.fj,
  fiji.gov.fj) is currently down/mid-migration - the main portal displays "brand-new
  website under construction" as of July 2026. language: English
- **format**: HTML landing pages + PDF attachments
- **practical**: sits behind a Cloudflare JS challenge (plain fetch gets 403; a
  browser/JS-capable renderer clears it in ~5s). **robots.txt explicitly disallows
  ClaudeBot, GPTBot, CCBot, Google-Extended, Bytespider, Amazonbot** and other AI
  crawlers (`ai-train=no, use=reference`) while allowing general search indexing -
  a real compliance flag worth a manual ToS read before wiring up scheduled fetches.
- **effort tier**: (b) plain crawl, flagged for the AI-crawler robots.txt restriction
- **why worth adding**: only reliably-reachable source for Fiji's actual
  energy-efficiency policy content while gov.fj is down, and doubles as an aggregator
  that could plausibly cover the wider Pacific SIDS long tail in one integration.
- **verified**: yes - fetched via browser after clearing the Cloudflare check; saw the
  live publication page (title, date, author, copyright holder, thematic tags, and the
  attached PDF filename/size).

### 7. Kyrgyzstan - Ministry of Energy Normative Legal Acts registry

- **name**: "Ministry of Energy of the Kyrgyz Republic - Normative Legal Acts database"
- **proposed id**: `kyrgyzstan_minenergo_nla`
- **base_url**: `https://minenergo.gov.kg`
- **start_paths**: `/normativeLegalAct` (filterable table: Law/Instruction/Order/Rules/
  Norms x Electric Energy/**Heat Energy**/Construction/Energy/Cross-sector)
- **level**: national
- **access**: none
- **coverage**: region: `kyrgyzstan`; category: `district_heating` +
  `energy_efficiency`. Law No.88 "On Energy Saving" (1998, amended through 2024), Law
  No.56 "On Energy," Law "On Electric Power Industry," plus ministerial orders/rules in
  the dedicated Heat Energy category - steam/hot-water pipeline construction and
  safe-operation rules, technical-maintenance instructions for central heating/hot-
  water systems in multi-apartment buildings. District-heating tariffs are set by this
  ministry's Fuel-Energy Complex regulation department. language: Kyrgyz (listings),
  law texts commonly bilingual Kyrgyz/Russian - confirm keywords.yaml has Kyrgyz
  coverage, not just Russian.
- **format**: HTML listing -> linked DOCX/PDF documents
- **practical**: actively maintained (newest entries dated 2026-07-01). WebFetch
  repeatedly failed with a TLS certificate-chain error on this domain, but the site is
  confirmed live via browser rendering (full filterable table with real dated
  entries) - crawler build should expect a TLS quirk and may need a browser-based
  fetcher.
- **effort tier**: (b) plain crawl (TLS handling caveat)
- **why worth adding**: only continuously-updated national legal-acts index for
  Kyrgyzstan energy/heat policy, with a Heat Energy category matching district-heating
  scope directly.
- **verified**: yes - loaded via browser tool, saw the live filterable table with
  entries (Law No.88, Law No.56, Heat Energy category rules) dated up to 2026-07-01.

### 8. Tajikistan - Ministry of Energy and Water Resources (MEWR)

- **name**: "Ministry of Energy and Water Resources of the Republic of Tajikistan"
- **proposed id**: `tajikistan_mewr`
- **base_url**: `http://www.mewr.tj` (https attempt intermittently ECONNREFUSED; http
  fallback succeeded)
- **start_paths**: `/` (dedicated "Energy Saving and Energy Efficiency" section plus a
  legislation/decrees database); PDFs under `/wp-content/uploads/files/...`
- **level**: national
- **access**: none
- **coverage**: region: `tajikistan`; category: `energy_efficiency` +
  `district_heating`. Law No.29 "On Energy Saving" (2002), Law "On Energy" (2000), Law
  "On Use of Renewable Energy Sources" (2010), ministry decrees/reports on district
  heating in Dushanbe (~9% of population, Dushanbe-2 CHP plant), power-sector reform
  master plans. language: Russian and Tajik
- **format**: HTML + PDF (WordPress site, confirmed via `/wp-content/` paths)
- **practical**: robots.txt permissive (only blocks MJ12bot/SemrushBot/AhrefsBot).
  Build with retry logic - https connection flaked once.
- **effort tier**: (b) plain crawl
- **why worth adding**: only ministry-level government source for Tajikistan's
  energy-saving law and Dushanbe district-heating policy; country currently has zero
  PolicyPulse coverage.
- **verified**: yes - fetched `http://www.mewr.tj/` directly, confirmed official
  ministry site with News, Legislation database, Government decrees/orders, and the
  Energy Saving and Energy Efficiency section.

### 9. Mongolia (extra) - Ministry of Urban Development, Construction and Housing (MCUD)

- **name**: "Ministry of Urban Development, Construction and Housing (Mongolia)"
- **proposed id**: `mongolia_mcud`
- **base_url**: `https://mcud.gov.mn`
- **start_paths**: `/a/{id}` (announcements, e.g. `/a/809`), `/p/{id}` (department
  pages), `/resource/mcud/File/...` and `/resource/mcud/LegalDocumentAttachment/...`
  (PDF law repository)
- **level**: national
- **access**: none
- **coverage**: region: `mongolia`; category: `building_efficiency` +
  `district_heating`. Distinct from the already-planned `erc_mn` (tariffs/Ulaanbaatar
  DH network). Building Energy Efficiency Certificate Issuance Procedure (joint order,
  Dec 2021) establishing green-building energy-class certification (Class B/C) tied to
  green lending; Construction Codes/Standards on building-envelope thermal insulation
  (MNS 25-01-20, effective 2021); draft national "Law on Heat Supply" mirrored from
  Parliament's drafting system (centralized/decentralized heat-supply classification,
  tariff methodology - under Parliament consideration as of Feb 2026, **not yet
  enacted**, flag as draft status). language: Mongolian (Cyrillic); thin English
  toggle exists - keywords.yaml Mongolian coverage should be checked.
- **format**: HTML (announcements) + PDF (law/standards documents)
- **practical**: robots.txt fully permissive. Homepage renders nav-only on a plain
  fetch (JS-driven routing) - crawl via the `/a/{id}` and `/p/{id}` sequential-ID
  pattern plus discovered `/resource/mcud/File/` links, not just the homepage.
- **effort tier**: (b) plain crawl
- **why worth adding**: only Mongolia source covering building-level efficiency
  mandates and district-heating law text that the already-planned ERC tariff source
  does not touch.
- **verified**: yes - fetched `/a/809` (full Building Energy Efficiency Certificate
  content), `/p/149` (department page), `/robots.txt` (permissive), and `/?locale=en`
  (confirmed ministry branding/nav). Draft heat-supply-law text also confirmed at
  `https://d.parliament.mn/tusul/1b66bb01-5e66-4c57-8c40-e25c65e0e65e`.

### 10. Zimbabwe - ZERA National Energy Efficiency Policy

- **name**: "Zimbabwe Energy Regulatory Authority (ZERA) - Policies/Standards"
- **proposed id**: `zimbabwe_zera_energy_efficiency`
- **base_url**: `https://www.zera.co.zw`
- **start_paths**: `/policies/`, `/standards/`, `/acts/`; PDF
  `/wp-content/uploads/simple-file-list/POLICIES/NEEP-2-compressed.pdf` (National
  Energy Efficiency Policy)
- **level**: national
- **access**: none
- **coverage**: region: `zimbabwe`; category: `energy_efficiency`. ZERA's statutory
  mandate (Energy Regulatory Authority Act, Cap 13:23) explicitly includes energy
  efficiency; site hosts the National Energy Efficiency Policy (MEPS for
  refrigerators/HVAC/lighting), Energy Policy, National Renewable Energy Policy,
  Biofuels Policy. language: English
- **format**: PDF (some scanned/image-based) + HTML
- **practical**: no robots block hit; PDFs may need OCR; infrequent update cadence.
- **effort tier**: (b) plain crawl
- **why worth adding**: substantial, regulator-confirmed EE framework - best African EE
  regulator find in this wave outside Mauritius.
- **verified**: yes - fetched `/policies/` (listed 5 docs), `/standards/`, and the NEEP
  PDF itself (resolved, valid 2.2MB PDF on-domain).

### 11. Djibouti - ARMD Multisectoral Regulator

- **name**: "Autorité de Régulation Multisectorielle de Djibouti (ARMD)"
- **proposed id**: `djibouti_armd_regulator`
- **base_url**: `https://www.armd.dj/en`
- **start_paths**: `/en` (legislative/regulatory texts, opinions & decisions, reports &
  studies)
- **level**: national
- **access**: none
- **coverage**: region: `djibouti`; category: `ict_energy_regulator`. ARMD is the
  single regulator for telecommunications, ICT, energy/electricity, renewable energy,
  and gas - explicitly relevant given Djibouti's role as a submarine-cable landing hub
  and its stated "digital and energy hub of the Red Sea" mandate. language: French
  (English section exists)
- **format**: HTML + PDF
- **practical**: relatively new institution (created 2020, council seated 2024/2025),
  low document volume so far, no rate limiting observed.
- **effort tier**: (b) plain crawl
- **why worth adding**: only regulator in Djibouti with combined ICT+energy
  jurisdiction - exactly the cross-cutting body to watch as Djibouti's cable/data
  economy matures.
- **verified**: yes - fetched armd.dj/en, confirmed mandate and publications sections
  live.

### 12. Belarus - Ministry of Energy

- **name**: "Ministry of Energy of the Republic of Belarus"
- **proposed id**: `belarus_minenergo`
- **base_url**: `https://www.minenergo.gov.by`
- **start_paths**: homepage + normative-acts ("НПА") section
- **level**: national
- **access**: none
- **coverage**: region: `belarus`; category: `district_heating` +
  `energy_efficiency`. Council of Ministers Resolution No. 609 (11 Sep 2019) "On
  Issues in the Field of Heat Supply" governs consumer/heat-supplier relations,
  heating-network connection, heat-energy payment; Law "On Energy Saving" (1998,
  amended 2014/2015); new Sustainable Energy and Energy Efficiency state program for
  2026-2030. language: Russian
- **format**: HTML + PDF
- **practical**: government domain, no robots/ToS issue seen, low update frequency for
  legislation.
- **effort tier**: (b) plain crawl
- **why worth adding**: only real government source for Belarus heat-supply/energy-
  saving law - fills a currently-uncovered jurisdiction.
- **verified**: yes - fetched `minenergo.gov.by` directly, confirmed official ministry
  identity and normative-acts references. Note: Resolution 609's own text was only
  found on a non-authoritative mirror (cis-legislation.com) - use minenergo.gov.by as
  the crawl root, not that mirror. RUP "Minskenergo" (web.minskenergo.by) is a
  state-owned operating utility, not a policy body - checked, not proposed.

### 13. Kosovo - Ministry of Economy

- **name**: "Ministry of Economy (Ministria e Ekonomisë), Kosovo"
- **proposed id**: `kosovo_me_gov`
- **base_url**: `https://me.rks-gov.net`
- **start_paths**: `/en/` (Department of Energy), `/en/legjislacioni/` (Legislation,
  "Energjia" category)
- **level**: national
- **access**: none
- **coverage**: region: `kosovo`; category: `energy_efficiency` +
  `building_efficiency`. Law No. 06/L-079 on Energy Efficiency (established the Kosovo
  Energy Efficiency Fund); Law No. 08/L-242 on Energy Performance of Buildings.
  Kosovo runs coal/petroleum-based district heating in 4 municipalities; a Dec 2022
  project added solar-assisted district heating for ~38,000 residents (first in the
  Western Balkans). language: Albanian (some English)
- **format**: HTML + PDF
- **practical**: active site, news dated through July 2026, no obvious rate limits.
- **effort tier**: (b) plain crawl
- **why worth adding**: direct national ministry hosting binding EE and building-
  performance laws plus district-heating context.
- **verified**: yes - fetched `/en/` and the legislation page directly, confirmed
  official gov domain and Department of Energy structure (specific law PDFs sit one
  click deeper than rendered in this pass).

### 14. Montenegro - Ministry of Energy and Mining

- **name**: "Montenegro Ministry of Energy and Mining"
- **proposed id**: `montenegro_men`
- **base_url**: `https://www.gov.me/en/men`
- **start_paths**: `/en/men`
- **level**: national
- **access**: none
- **coverage**: region: `montenegro`; category: `energy_efficiency`. Oversees energy,
  energy efficiency, mining, geology, hydrocarbons, concessions. Montenegro is
  transposing EPBD (EU 2024/1275) and EED (EU 2023/1791) with a roadmap requiring law
  amendments by 31 March 2027 (zero-emission building standards, MEPS,
  energy-poverty measures). Pljevlja district-heating project (6.3km new pipelines)
  also referenced. language: Montenegrin/Serbian, some English
- **format**: HTML + PDF
- **effort tier**: (b) plain crawl
- **why worth adding**: national ministry with an explicit, dated EU-transposition
  roadmap for building efficiency standards.
- **verified**: yes - fetched directly, confirmed ministry scope statement.

  **Companion candidate** (same country, not independently confirmed): Directorate for
  Energy Efficiency, id `montenegro_dee`, base_url `http://energetska-efikasnost.me/en/`
  - hosts the actual Law on Efficient Use of Energy and Law on Energy Efficiency
  (Official Gazette 29/2010) with building-certification/audit rulebooks. Every direct
  fetch attempt returned HTTP 403 (likely WAF); content is corroborated only via
  WebSearch snippets quoting the site's own legal text. Listed here for completeness
  but treat as **not independently verified** - retry via browser before adding.

### 15. Brunei - Department of Energy (Prime Minister's Office)

- **name**: "Brunei Department of Energy"
- **proposed id**: `brunei_energy_gov_bn`
- **base_url**: `https://www.energy.gov.bn`
- **start_paths**: homepage; Energy Transition Division page; Energy Efficiency and
  Conservation (EEC) Unit content
- **level**: national
- **access**: none
- **coverage**: region: `brunei`; category: `energy_efficiency`. Energy Efficiency
  (Standards and Labelling) Act, Chapter 233. EEC Unit developing a full EE/
  conservation regulatory framework via a National EEC Committee. Joint EEC Building
  Guidelines for non-residential buildings (mandatory for government buildings,
  voluntary for commercial). Publishes an "Energy Efficiency and Conservation
  Handbook." language: English/Malay
- **format**: HTML + PDF
- **effort tier**: (b) plain crawl
- **why worth adding**: fills an uncovered SE Asian jurisdiction with a real EE statute
  and active building-guideline regulatory work.
- **verified**: yes - fetched directly, confirmed official PMO department site and the
  Cap. 233 Act reference plus EEC guideline content.

### 16. Bhutan - Ministry of Energy and Natural Resources (MoENR)

- **name**: "Ministry of Energy and Natural Resources, Bhutan"
- **proposed id**: `bhutan_moenr`
- **base_url**: `https://www.moenr.gov.bt`
- **start_paths**: homepage; Energy section; Downloads (Acts/Rules/Regulations/
  Policies/Guidelines)
- **level**: national
- **access**: none
- **coverage**: region: `bhutan`; category: `energy_efficiency`. National Energy
  Policy 2025 ("Empowering Energy Security & Sustainable Growth"); Energy Innovation &
  Management Division sets Minimum Energy Performance Standards (MEPS), runs energy
  audits of residential/commercial buildings and industry, launched a Standards and
  Labeling (S&L) Scheme; also references a National Energy Efficiency and Conservation
  Policy. language: English/Dzongkha
- **format**: HTML + PDF
- **effort tier**: (b) plain crawl
- **why worth adding**: national EE policy body with a live MEPS/S&L program.
- **verified**: yes - fetched twice, confirmed live content described above.

### 17. Maldives - Utility Regulatory Authority (URA)

- **name**: "Maldives Utility Regulatory Authority (URA)"
- **proposed id**: `maldives_ura`
- **base_url**: `https://www.ura.gov.mv`
- **start_paths**: homepage; Energy sector regulations page
- **level**: national
- **access**: none
- **coverage**: region: `maldives`; category: `energy_efficiency`. Administers the
  Maldives Energy Act (Law No. 18/2021, in force 11 Oct 2021) - issues Energy
  Efficiency Certificates, can mandate energy audits for users above 100 kWh/month via
  registered auditors, sets standards for energy/electricity, water & sanitation,
  waste, petroleum. language: English/Dhivehi
- **format**: HTML + PDF
- **practical**: the direct PDF link to the Act itself 404'd - may need sourcing via
  FAOLEX/ESCAP policy database as a fallback, or a corrected URL from crawling the
  downloads section.
- **effort tier**: (b) plain crawl
- **why worth adding**: the actual legal authority issuing efficiency certificates -
  more precise than the parent ministry page for the certificate mechanism itself.
- **verified**: yes for domain/identity/regulatory scope (fetched homepage directly);
  the specific Act PDF link was not verified (404).

  **Companion candidate** (same country): Ministry of Climate Change, Environment and
  Energy, id `maldives_environment_gov_mv`, base_url `https://www.environment.gov.mv`,
  start_path `/v2/en/department/170`. Runs the "Hakathari" Energy Efficiency Standards
  and Labelling Programme (1-5 star appliance ratings), Energy Roadmap 2024-2033.
  verified: yes - fetched directly.

### 18. Mozambique - MIREME National Energy Efficiency Strategy

- **name**: "Mozambique Ministry of Mineral Resources and Energy (MIREME)"
- **proposed id**: `mozambique_mireme_energy_efficiency`
- **base_url**: `https://mireme.gov.mz`
- **start_paths**: `/documento/` (document archive)
- **level**: national
- **access**: none
- **coverage**: region: `mozambique`; category: `energy_efficiency`. Resolução n.º
  44/2023 de 25 de Outubro - Estratégia de Eficiência Energética (first coordinated EE
  program for Mozambique), plus Renewable Energy Policy and Electricity Law 12/2022.
  ARENE (the separate electricity/fuels regulator) was checked - has a legislation
  section but no EE content, so MIREME is the correct target. language: Portuguese
- **format**: PDF + HTML archive index
- **practical**: WordPress site, no robots block observed, low/annual update
  frequency.
- **effort tier**: (b) plain crawl
- **why worth adding**: only confirmed government-issued, government-hosted energy
  efficiency strategy document found for Mozambique.
- **verified**: yes - fetched `/documento/` directly, saw the Resolução 44/2023 entry
  listed with dated companion resolutions.

### 19. Cote d'Ivoire (extra) - Ministry of Digital Transition + ARTCI

- **name**: "Ministère de la Transition Numérique et de l'Innovation Technologique (Côte d'Ivoire)"
- **proposed id**: `cotedivoire_transition_numerique_ministry`
- **base_url**: `https://telecom.gouv.ci/new/`
- **start_paths**: `/index.php/accueil`, `/publications/sous-categorie/1`
- **level**: national
- **access**: none
- **coverage**: region: `cote_d_ivoire`; category: `digital_infrastructure`. Distinct
  from Côte d'Ivoire's energy ministry (already covered in a prior wave). Hosts the
  Stratégie Nationale de la Gouvernance des Données (SNGD 2030) - covers cloud/data
  hosting policy and the national data center - plus a National AI Strategy, National
  Cybersecurity Strategy 2021-2025, and an e-waste management plan for ICT equipment.
  language: French
- **format**: PDF (large image-based scans, likely need OCR) + HTML
- **practical**: numbered `/publications/sous-categorie/N` structure worth crawling in
  full.
- **effort tier**: (b) plain crawl
- **why worth adding**: genuinely distinct from the energy ministry - covers the
  ICT-side data-center/cloud-hosting policy angle the energy source wouldn't.
- **verified**: yes - fetched the accueil page (confirmed ministry identity +
  publication titles) and directly fetched the SNGD 2030 PDF (resolved live, 7.7MB,
  on-domain).

  **Companion candidate** (same country): ARTCI (telecom/ICT regulator), id
  `cotedivoire_artci_ict_regulator`, base_url `https://www.artci.ci`. Publishes legal
  texts, decisions, service specifications, infrastructure/QoS observatory data - no
  explicit data-center-energy document surfaced, but it's the regulator most likely to
  issue future DC-touching infrastructure rules. verified: yes for domain root; one
  specific deep-link path tried was dead (not used as a start_path).

### 20. Cameroon - ARSEL Electricity/Energy-Efficiency Regulator

- **name**: "Agence de Régulation du Secteur de l'Électricité (ARSEL), Cameroon"
- **proposed id**: `cameroon_arsel_electricity_regulator`
- **base_url**: `https://arsel-cm.org`
- **start_paths**: `/documents/en/` (Laws, Decrees, Arrêtés, Regulatory Decisions,
  Strategic Plans, Studies)
- **level**: national
- **access**: none
- **coverage**: region: `cameroon`; category: `energy_efficiency`. ARSEL commissioned
  Cameroon's national EE policy/strategy/action plan for the electricity sector
  (target: 25% electricity-consumption reduction by 2025, covering public buildings,
  industry/services efficiency, household awareness, regulatory reform). language:
  French (limited English)
- **format**: PDF + HTML
- **practical**: search-indexed deep links to the specific EE PDF and category
  subpages 404'd on direct fetch (site appears to have restructured since being
  indexed) - only the base domain and `/documents/en/` index are confirmed live;
  crawl should re-discover the document from the live index rather than trusting
  cached URLs. MINEE (minee.cm, Ministry of Water and Energy) also verified live as a
  bilingual fallback/complement.
- **effort tier**: (b) plain crawl (needs live re-discovery, not cached deep links)
- **why worth adding**: confirmed national EE policy/strategy/action-plan document
  exists and is government-issued, even though the exact stable URL needs recrawling.
- **verified**: partial - domain and `/documents/en/` index confirmed live; the
  specific EE PDF itself 404'd on 3 attempted paths, so listed honestly as
  domain-verified rather than document-verified.

---

## Unverified / needs-human-check

- **Northern Cyprus (TRNC) - KKTC Ekonomi ve Enerji Bakanlığı**, base_url
  `https://ekonomi.gov.ct.tr`. Domain and ministry identity confirmed live (Turkish-
  only), manages TRNC energy infrastructure (Teknecik Power Plant, fuel pricing,
  industrial-zone permitting), but the one legislation section actually fetched
  (`/Mevzuat`) showed only industrial-registration/consumer-protection/R&D content -
  no energy-specific laws were visible there despite "Enerji" in the ministry's name.
  **Political-sensitivity flag**: TRNC is a self-declared entity recognized only by
  Turkey; the UN, EU, and nearly all states treat this territory as part of the
  Republic of Cyprus, whose Ministry of Energy, Commerce and Industry is already a
  separate existing candidate (`energy.gov.cy`, region `cyprus`). This is reported
  factually per instructions, without further editorializing - recommend a human
  decide whether/how to represent this as a distinct region slug before any crawl
  config is written, and a deeper crawl to actually locate energy-specific content
  before treating it as verified.

- **Malta (extra) - Building and Construction Authority (BCA), EPC regulation**,
  base_url `https://bca.gov.mt`, start_paths `/epcs/`, `/regulations/`. Would cover
  Subsidiary Legislation 623.01 - Energy Performance of Buildings Regulations
  (Legal Notice 47/2018 + later amendments, implementing EU Directive 2018/844,
  new minimum requirements from 1 July 2024) - a genuinely distinct topic (building
  EPC) from Malta's two existing candidates (which document the absence of DH/DC
  networks). Every fetch attempt (root, both subpages, two PDFs) returned HTTP 403.
  Confirmed only via WebSearch snippets quoting specific legal-notice numbers and
  dates - strong indirect evidence it's real, but not independently fetched. Retry via
  browser before adding.

- **Laos - Ministry of Energy and Mines (MEM)**, base_url `https://www.mem.gov.la`.
  Domain is confirmed genuinely real (bare `mem.gov.la` returned a TLS
  certificate-mismatch error naming `www.mem.gov.la` as the valid cert holder - proof
  of a real government-issued cert), but every attempt to fetch actual content from
  `www.mem.gov.la` (4 paths tried) returned HTTP 500. Claimed coverage - Department of
  Energy Policy and Planning, an in-progress EE/conservation decree, and Decree No.
  292 on Carbon Emissions - is corroborated by multiple independent WebSearch results
  (specific indexed subpage titles, a GGGI article quoting the decree) but not
  directly rendered. Retry via browser tooling before finalizing.

- **Greenland - Naalakkersuisut (Home Rule Government), Business and Energy
  portfolio**, base_url `https://naalakkersuisut.gl`. Root domain confirmed live and
  correctly identified (home-rule portal, Kalaallisut default with Danish toggle,
  lists departments including a Business/Trade one). The specific energy-department
  subpage and a plain department-listing page both returned blank content on repeated
  fetch attempts (likely a JS-rendered SPA) - could not confirm any actual
  energy-policy text. Separately identified Nukissiorfiit (state-owned utility,
  targeting 100% green energy by 2030, currently 72% renewable) - this is an
  *operating utility*, not a policy body, so not proposed as a policy source even if
  it does have public data. Needs a browser-based retry on the energy subpage before
  treating as a candidate.

- **Costa Rica (extra) - DIGECA National District Cooling Strategy**. The single most
  promising Costa-Rica-extra lead: a UNDP/GEF-backed "Estrategia Nacional de
  Distritos de Frío" run by DIGECA (an agency under MINAE, distinct from the
  already-covered generic ministry page), with a public-hospital (CCSS) pilot. URLs
  found via search (`digeca.go.cr/proyectos/...`, case-study PDF, brochure PDF) could
  not be reached - both WebFetch and browser navigation returned connection errors
  (ECONNREFUSED / navigation denied) on the deep page and domain root, across two
  separate attempts. Worth a manual/retry check from a different network - it is
  otherwise exactly the kind of new, on-topic, district-cooling-specific source this
  wave was looking for.

- **Montenegro - Directorate for Energy Efficiency** (`energetska-efikasnost.me`) -
  see full detail under candidate #14 above; listed there as a companion but
  effectively unverified (403 on every direct fetch, corroborated only via search).

---

## Checked - no on-topic coverage found (honest negative results)

- **Uganda**: Ministry of Energy and Mineral Development (`energyandminerals.go.ug`)
  and its geoscience subdomain failed to resolve (DNS failure / Cloudflare 522) across
  multiple attempts, despite search evidence of a 2023 Energy Policy and EE Strategy
  hosted there. Uganda's ICT ministry and NITA-U resolved live but have no
  DC-energy-efficiency content. No verified candidate this wave; worth a retry later.
- **Angola**: MINTTICS (telecom/IT ministry) verified live with a legislation section,
  but no DC/energy-efficiency/digital-infrastructure policy document found. Angola
  data-center news (Sonangol, Raxio Tier III, government DC launch) is vendor/project
  news, not policy - correctly excluded.
- **Democratic Republic of Congo**: ARE (electricity regulator) and MRHE (Ministry of
  Hydraulic Resources and Energy) both verified live, hosting general electricity-
  sector law (Law 14/011 and decrees), but neither surfaced an efficiency mandate,
  standard, or data-center-relevant document. Not proposed to avoid padding with
  generic electricity-law content.
- **Pacific SIDS bloc** (Vanuatu, Samoa, Solomon Islands, Tonga, Kiribati, Nauru,
  Marshall Islands, Palau, Cook Islands, Tuvalu, Micronesia): spot-checked via
  targeted search - all have only generic national electrification/renewable-energy/
  grid-efficiency policy (relevant to power-sector decarbonization broadly), zero
  data-center, waste-heat, district-cooling, or PUE/ERE-specific government policy.
  Consistent with these countries' near-total absence of data-center infrastructure.
  Coverage for this sub-taxonomy is essentially absent across this bloc; not worth
  further effort beyond the SPC regional hub already listed (candidate #6), which
  indexes each country's general energy-policy documents if ever needed.
- **Iceland (extra)**: nothing new found beyond the three existing candidates - see
  dedup note above.
- **Costa Rica (extra, ARESEP)**: live and real (grid-operation procedures, renewable-
  penetration methodology, autonomous-generation law) but nothing on energy
  efficiency, large-consumer requirements, or data centers - not proposed.
