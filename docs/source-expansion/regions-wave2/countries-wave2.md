# Source Expansion Research - Wave 2: Countries Not Yet Covered

Branch: `feature/source-expansion-research`. Research only - no client code touched,
no domain added with `enabled: true`. All candidates below are draft additions.

Scope: 30 countries not covered anywhere in wave 1 (all EU states, UK/Ireland, US,
Canada, Nordics, Japan/Korea/China/Taiwan/HK/Singapore, Australia/NZ/India/Malaysia/
Indonesia/Philippines/Thailand/Vietnam, Chile/Colombia/Argentina/Peru/Uruguay/Costa
Rica, Brazil/Mexico, UAE/Saudi/Qatar/Kuwait/Bahrain/Oman/Israel/Turkey/Egypt,
Kenya/Nigeria/Morocco/Ghana/South Africa - all already shipped or drafted, see
`docs/source-expansion/draft/crawl/mena-africa.yaml` and `config/domains/`).

Researched in three parallel batches:
- **Central Asia + wider Europe non-EU**: Kazakhstan, Uzbekistan, Azerbaijan, Bosnia
  and Herzegovina, North Macedonia, Albania, Moldova, Georgia, Armenia, Russia
- **More Africa**: Ethiopia, Tanzania, Senegal, Cote d'Ivoire, Tunisia, Algeria,
  Rwanda, Zambia, Botswana, Namibia
- **More Asia + Gulf/ME extras**: Pakistan, Bangladesh, Sri Lanka, Cambodia,
  Myanmar, Mongolia, Nepal, Jordan, Lebanon, Iraq

## Dedup check performed

Before researching, each batch read `docs/source-expansion/draft/crawl/mena-africa.yaml`
(covers Israel, Turkey, Nigeria, Egypt, Ghana, Kuwait, Morocco, Oman, RCREEE, AFREC -
RCREEE's 17-state Arab membership includes Jordan/Iraq/Lebanon/Tunisia/Algeria but that
is regional-body coverage only, not a national source, per the brief's own convention),
`docs/source-expansion/draft/crawl/eu-uncovered.yaml` (covers Serbia, Ukraine, Cyprus,
Malta, Slovakia, Croatia, Slovenia, Bulgaria, Latvia), `docs/source-expansion/draft/crawl/
oceania-south-asia.yaml` (covers Australia, NZ, India, Philippines, Malaysia, Indonesia,
Vietnam), all other `draft/crawl/*.yaml` files, `draft/new-clients.md`, and every file
under `config/domains/`. No `base_url` collisions found - all 39 candidates below are
net-new. (One incidental hit: `config/domains/us/georgia.yaml` is the US state of
Georgia - unrelated to the country of Georgia researched here.)

## Region-mapping note (read before building config)

`src/core/config.py`'s `VALID_REGIONS` has no bucket for Central Asia, the Caucasus,
or most of the individual countries below (only broad `europe`, `apac`, `middle_east`,
`africa` exist, plus a handful of named countries like `uae`/`saudi_arabia`/
`south_africa`). Per the precedent set in `mena-africa.yaml` (Nigeria/Ghana/Morocco all
map to the broad `africa` bucket with country identity preserved in `id`/`name`/notes),
this file does the same:

- Balkans + Moldova -> `["europe", "eu_east"]` (Energy Community Contracting
  Parties / EU candidate countries transposing EU energy acquis - same logic used for
  Serbia/Ukraine in `eu-uncovered.yaml`)
- Central Asia (Kazakhstan, Uzbekistan) and Caucasus (Azerbaijan, Georgia, Armenia) ->
  **no existing bucket fits well**. Flagged rather than force-mapped, per the brief's
  own guidance (see `INVENTORY.md`'s treatment of "supranational"/"global"). Recommend
  adding `central_asia` and `caucasus` as new `VALID_REGIONS` entries before enabling
  these domains - forcing them into `apac` or `middle_east` would be geographically
  wrong and would pollute those filters at query time.
- Africa (Ethiopia, Tanzania, Senegal, Cote d'Ivoire, Tunisia, Algeria, Rwanda, Zambia,
  Botswana, Namibia) -> `["africa"]`, country identity in id/name/notes
- South/Southeast/Central Asia (Pakistan, Bangladesh, Sri Lanka, Cambodia, Myanmar,
  Mongolia, Nepal) -> `["apac"]`
- Gulf/ME extras (Jordan, Lebanon, Iraq) -> `["middle_east"]`
- Russia -> no bucket assigned; effectively unreachable this pass anyway (see below)

One new config file per country recommended throughout, following the established
one-country-per-file convention (`nigeria.yaml`, `ghana.yaml`, `morocco.yaml`, etc.).

---

## Verified candidates (ranked best-first)

### 1. Algeria - APRUE (Agence Nationale pour la Promotion et la Rationalisation de l'Utilisation de l'Energie)

- **name**: "APRUE - National Agency for the Promotion and Rationalization of Energy Use"
- **proposed id**: `aprue_dz`
- **base_url**: `https://aprue.org.dz`
- **start_paths**: `/en/public-programs/national-energy-management-program/industry/`,
  `/en/public-programs/national-energy-management-program/buildings/`,
  `/en/legislative-and-regulatory-texts/` (confirm exact slugs at crawl-build time)
- **level**: national
- **access**: none
- **coverage**: region: `["africa"]`; category: `energy_ministry`; tags:
  `["efficiency", "mandates", "planning", "research"]`; policy_types: `["regulation",
  "standard", "guidance", "report"]`; language: `fr` (partial `en`)
- **format**: HTML + PDF
- **practical**: robots.txt permissive (allows all, sitemap at `/sitemap_index.xml`);
  no published rate limit, recommend 2-3s; site appears actively maintained.
- **effort tier**: b
- **why worth adding**: dedicated national efficiency implementation agency since 1985 -
  runs the National Energy Management Program (buildings/industry/transport), an Energy
  Management Observatory, and an approved-energy-auditor registry. Strongest
  single-agency efficiency-mandate source found across the whole Africa batch.
- **verified**: yes. WebFetch confirmed "Legislative and Regulatory Texts" section,
  National Energy Management Program subsections for industry/buildings, Energy
  Management Observatory.

### 2. Kazakhstan - Adilet Legal Information System

- **name**: "Adilet Legal Information System (Ministry of Justice, Kazakhstan)"
- **proposed id**: `adilet_zan_kz`
- **base_url**: `https://adilet.zan.kz`
- **start_paths**: `/eng/docs/Z1200000541` (Law on Energy Saving and Increase in Energy
  Efficiency), `/eng/docs/Z2300000193` (Law on Digital Assets - mining registry/
  licensing), plus a search for Law No. 194-VII (electricity supply to digital miners)
- **level**: national
- **access**: none
- **coverage**: region: **flag - recommend `central_asia`** (see mapping note above);
  category: `legislative`; tags: `["mandates", "efficiency", "reporting"]`;
  policy_types: `["law", "regulation"]`; language: `en`/`kk`/`ru`
- **format**: HTML/PDF
- **practical**: no rate-limit info found; this is Kazakhstan's canonical legal
  database (like a national Gazette), high update frequency.
- **effort tier**: b
- **why worth adding**: Kazakhstan is the one country in this wave with an explicit,
  named data-center-energy policy regime - electricity price zones, a state crypto-
  mining registry, and quarterly MW-consumption disclosure requirements at data
  centers. Directly on-topic, not adjacent.
- **verified**: partial. WebFetch hit a TLS certificate-chain error on every attempt
  (https and http) - same failure mode as a prior Bulgaria SEEA precedent in
  `eu-uncovered.yaml`. Content strongly corroborated via WebSearch instead, which
  returned direct quotes of the operative law text (energy consumption quotas,
  quarterly MW reporting at data centers, tax rate) sourced from this exact domain/doc
  IDs. Flag for a human to re-check with a proper cert store before enabling.

### 3. Tunisia - ANME (Agence Nationale pour la Maitrise de l'Energie)

- **name**: "ANME - National Agency for Energy Management (Tunisia)"
- **proposed id**: `anme_tn`
- **base_url**: `https://www.anme.tn`
- **start_paths**: `/fr/content/industrie`, `/cadre-reglementaire` (confirm exact slug)
- **level**: national
- **access**: none
- **coverage**: region: `["africa"]`; category: `energy_ministry`; tags:
  `["efficiency", "mandates", "incentives", "planning"]`; policy_types: `["law",
  "regulation", "standard", "incentive"]`; language: `fr`, `ar`
- **format**: HTML + PDF
- **practical**: robots.txt (Drupal-standard) blocks only `/admin/`, `/search/`, auth
  pages; no documented rate limit, recommend 2-3s.
- **effort tier**: b
- **why worth adding**: Law No. 2009-7 (mandatory periodic energy audits for large
  consumers) plus its implementing decree, National Energy Management Fund, appliance
  labeling, and thermal building regulation - direct statutory efficiency-mandate
  content with a 2030 target (30% demand reduction).
- **verified**: yes. WebFetch confirmed "Cadre Reglementaire" section, subsidy/guide
  forms, certified-auditor lists, and the 2030 targets.

### 4. Azerbaijan - Ministry of Energy - Laws

- **name**: "Ministry of Energy of Azerbaijan - Laws"
- **proposed id**: `minenergy_az_laws`
- **base_url**: `https://minenergy.gov.az`
- **start_paths**: `/en/qanunlar`
- **level**: national
- **access**: none
- **coverage**: region: **flag - recommend `caucasus`**; category: `energy_ministry`;
  tags: `["mandates", "efficiency"]`; policy_types: `["law"]`; language: `en`/`az`
- **format**: HTML
- **practical**: not rate-limit tested; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: ~20 laws listed directly on the page, including Law No.
  359-VIQ (Efficient Use of Energy Resources and Energy Efficiency, in force 2022) and
  the Electricity Law - a clean, paginated legislative archive.
- **verified**: yes. WebFetch confirmed title "Laws | Ministry of Energy of
  Azerbaijan", listed law numbers/dates matching search results, pagination present.

### 5. Senegal - AEME (Agence pour l'Economie et la Maitrise de l'Energie)

- **name**: "AEME - Agency for Energy Economy and Management (Senegal)"
- **proposed id**: `aeme_sn`
- **base_url**: `https://www.aeme.sn`
- **start_paths**: `/textes-legislatifs-et-reglementaires` (confirm slug),
  `/normes-sur-la-maitrise-de-lenergie`
- **level**: national
- **access**: none
- **coverage**: region: `["africa"]`; category: `energy_ministry`; tags:
  `["efficiency", "mandates", "planning"]`; policy_types: `["regulation", "standard",
  "guidance", "report"]`; language: `fr`
- **format**: HTML + PDF
- **practical**: robots.txt (WordPress-standard) blocks only `/wp-admin/`, sitemap at
  `/wp-sitemap.xml`; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: operational arm of Senegal's national energy management
  policy since 2011 - dedicated "Textes legislatifs et reglementaires" and "Normes sur
  la maitrise de l'energie" sections, plus a national 28% energy-savings assessment.
- **verified**: yes. WebFetch confirmed both named sections plus "Rapports
  d'activites" and "Etudes".

### 6. Azerbaijan - Energy Regulatory Agency (AERA) - Energy Efficiency

- **name**: "Energy Regulatory Agency of Azerbaijan (AERA) - Energy Efficiency"
- **proposed id**: `regulator_gov_az`
- **base_url**: `https://regulator.gov.az`
- **start_paths**: `/en/elektrik/enerji-semereliliyi-ve-enerjiye-qenaet`
- **level**: national
- **access**: none
- **coverage**: region: **flag - `caucasus`**; category: `regulatory`; tags:
  `["mandates", "efficiency", "district_heating"]`; policy_types: `["regulation",
  "guidance"]`; language: `en`/`az`
- **format**: HTML
- **practical**: not rate-limit tested; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: independent regulator's own energy-efficiency page - smart
  heat/gas/electricity metering mandates, consumer heat-consumption disclosure rules,
  and an Energy Efficiency Fund section.
- **verified**: yes. WebFetch confirmed title "Energy efficiency | AERA", content on
  smart heat meters and the Energy Efficiency Fund matched.

### 7. Cote d'Ivoire - DGE (Direction Generale de l'Energie)

- **name**: "DGE - Directorate General of Energy (Ministry of Mines, Petroleum and
  Energy, Cote d'Ivoire)"
- **proposed id**: `dge_ci`
- **base_url**: `https://www.dgenergie.ci`
- **start_paths**: `/lois-et-reglements` (confirm exact slug - homepage nav shows
  "LOIS & REGLEMENTS" with Lois/Decrets/Arretes subsections), `/documentation`
- **level**: national
- **access**: none
- **coverage**: region: `["africa"]`; category: `energy_ministry`; tags: `["mandates",
  "efficiency", "reporting"]`; policy_types: `["law", "regulation", "report"]`;
  language: `fr`
- **format**: HTML + PDF
- **practical**: robots.txt returned 404 (no file, unrestricted); recommend 2-3s.
- **effort tier**: b
- **why worth adding**: publishes an actual downloadable mandatory-energy-audit
  arrete ("Arrete Interministeriel N deg;156/MMPE/MCLU/MT/MINEDDTE/MCI du 23 Avril
  2024" on audit conditions/auditor qualifications) plus a full Laws/Decrees/Orders
  and Reports/Statistics archive.
- **verified**: yes. WebFetch confirmed the LOIS & REGLEMENTS section with three
  subsections and cited the specific energy-audit arrete by number.

### 8. Moldova - ANRE (National Agency for Energy Regulation)

- **name**: "ANRE - National Agency for Energy Regulation (Moldova)"
- **proposed id**: `anre_md`
- **base_url**: `https://anre.md`
- **start_paths**: `/en`
- **level**: national
- **access**: none
- **coverage**: region: `["europe", "eu_east"]`; category: `district_heating`; tags:
  `["mandates", "reporting"]`; policy_types: `["regulation", "law"]`; language:
  `en`/`ro`
- **format**: HTML + PDF
- **practical**: not rate-limit tested; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: full tariff-setting authority for Chisinau district heating,
  dedicated "Regulatory framework" section (EU directives, government decisions, laws,
  ANRE decisions) - a real district-heating regulator with legislative depth.
- **verified**: yes. WebFetch confirmed title, Consumer/thermal-energy section,
  Regulatory framework navigation.

### 9. Pakistan - NEECA (National Energy Efficiency & Conservation Authority)

- **name**: "NEECA - National Energy Efficiency and Conservation Authority (Pakistan)"
- **proposed id**: `neeca_pk`
- **base_url**: `https://www.neeca.gov.pk`
- **start_paths**: `/` (site uses CMS-hashed detail URLs, not clean slugs - confirm
  exact policy-doc paths at crawl-build time; ECBC-2023 building code, National Energy
  Efficiency & Conservation Policy 2023, and PELR labeling regs all confirmed
  on-domain)
- **level**: national
- **access**: none
- **coverage**: region: `["apac"]`; category: `energy_ministry`; tags: `["efficiency",
  "mandates"]`; policy_types: `["strategy", "regulation", "standard"]`; language: `en`
- **format**: HTML/PDF
- **practical**: no rate-limit info found; robots.txt not checked this pass - check
  before enabling.
- **effort tier**: b
- **why worth adding**: federal authority with the sharpest on-topic hit in the
  South-Asia batch - a 2023 Energy Conservation Building Code plus mandatory audits/
  energy-labeling regime, the closest thing to a data-center-adjacent efficiency
  mandate found this round.
- **verified**: yes. WebFetch confirmed ECBC-2023, National Energy Efficiency and
  Conservation Policy 2023, Action Plan 2023-30, PELR labeling regs, sector pages
  (Building/Industrial/Power/Transport/Agriculture).

### 10. Bangladesh - SREDA (Sustainable and Renewable Energy Development Authority)

- **name**: "SREDA - Sustainable and Renewable Energy Development Authority
  (Bangladesh)"
- **proposed id**: `sreda_bd`
- **base_url**: `https://sreda.gov.bd`
- **start_paths**: `/` (nav is Bengali-labeled: Energy Efficiency & Conservation
  section, Laws/Rules/Regulations/Policies section - exact slugs to confirm at
  crawl-build time)
- **level**: national
- **access**: none
- **coverage**: region: `["apac"]`; category: `energy_ministry`; tags: `["efficiency",
  "mandates", "reporting"]`; policy_types: `["law", "regulation", "strategy"]`;
  language: `bn` (some `en` pages)
- **format**: HTML/PDF
- **practical**: not rate-limit tested; robots.txt not checked.
- **effort tier**: b
- **why worth adding**: the statutory nodal agency for demand-side energy efficiency
  under the Energy Efficiency and Conservation Rules 2014/Master Plan - energy
  management guidelines for office buildings, mandatory energy audits, EE labeling.
- **verified**: yes. WebFetch confirmed dedicated Energy Efficiency & Conservation
  nav, Laws/Rules/Regulations/Policies section, energy management guidelines,
  certified auditor lists.

### 11. North Macedonia - Ministry of Energy, Mining and Mineral Resources

- **name**: "Ministry of Energy, Mining and Mineral Resources (North Macedonia)"
- **proposed id**: `energy_gov_mk`
- **base_url**: `https://energy.gov.mk`
- **start_paths**: `/en-GB`
- **level**: national
- **access**: none
- **coverage**: region: `["europe", "eu_east"]`; category: `energy_ministry`; tags:
  `["mandates", "efficiency", "incentives"]`; policy_types: `["law", "regulation"]`;
  language: `en`/`mk`
- **format**: HTML/PDF
- **practical**: not rate-limit tested; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: brand-new ministry (est. June 2024), split out of the old
  Ministry of Economy - zero prior coverage anywhere in this project. Dedicated
  "Laws"/"Draft Laws" nav, a live Energy Efficiency Fund rollout, and a
  vulnerable-consumer efficiency voucher program.
- **verified**: yes. WebFetch confirmed title, Regulations/Documents nav structure,
  EE Fund content.

### 12. Bosnia and Herzegovina - SERC (State Electricity Regulatory Commission)

- **name**: "State Electricity Regulatory Commission (SERC, Bosnia and Herzegovina)"
- **proposed id**: `serc_ba`
- **base_url**: `https://www.derk.ba`
- **start_paths**: `/en`, `/en/legislation`
- **level**: national
- **access**: none
- **coverage**: region: `["europe", "eu_east"]`; category: `regulatory`; tags:
  `["mandates", "reporting"]`; policy_types: `["law", "regulation"]`; language:
  `en`/`bs`/`hr`/`sr`
- **format**: HTML/PDF
- **practical**: not rate-limit tested; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: state-level electricity regulator (BiH's constitutional
  structure splits energy between state/entity levels) - a detailed Legislation page
  listing named transmission/system-operator laws, tariff procedures, licensing.
- **verified**: yes. WebFetch confirmed title, itemized law list with dates/amendment
  years, dated "last updated July 16, 2026."

### 13. Zambia - ERB (Energy Regulation Board)

- **name**: "Energy Regulation Board (ERB, Zambia)"
- **proposed id**: `erb_zm`
- **base_url**: `https://www.erb.org.zm`
- **start_paths**: `/regulation`, `/documents`, `/statistics`
- **level**: national
- **access**: none
- **coverage**: region: `["africa"]`; category: `regulatory`; tags: `["mandates",
  "reporting"]`; policy_types: `["law", "regulation", "report"]`; language: `en`
- **format**: HTML + PDF
- **practical**: robots.txt (WordPress-standard) blocks `/wp-admin/` only, sitemap at
  `/sitemap_index.xml`; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: statutory regulator under the Energy Regulation Act 2019
  (downloadable), searchable Documents library, active Newsroom with dated regulatory
  directives (cited "DIRECTIVE NO.1 OF 2025").
- **verified**: yes. WebFetch confirmed Energy Regulation Act 2019 PDF link,
  Documents/Statistics/Newsroom sections.

### 14. Zambia - Ministry of Energy

- **name**: "Ministry of Energy (Zambia)"
- **proposed id**: `moe_zm`
- **base_url**: `https://www.moe.gov.zm`
- **start_paths**: `/?page_id=2346` (Downloads - confirm cleaner slug at build time),
  `/`
- **level**: national
- **access**: none
- **coverage**: region: `["africa"]`; category: `energy_ministry`; tags:
  `["efficiency", "planning", "reporting"]`; policy_types: `["strategy", "report",
  "guidance"]`; language: `en`
- **format**: HTML + PDF
- **practical**: robots.txt not checked this session; recommend 2-3s until confirmed.
- **effort tier**: b
- **why worth adding**: hosts Zambia's Energy Efficiency Strategy and Action Plan 2022
  as a directly downloadable PDF - a full national EE strategy document, a rare
  direct-download find in this batch.
- **verified**: yes - PDF at `moe.gov.zm/wp-content/uploads/2022/08/Zambia-Energy-
  Efficiency-Strategy-and-Action-Plan-2022.pdf` fetched successfully (binary
  confirmed, not a 404/placeholder); homepage separately confirmed live with
  Publications/Downloads nav.

### 15. Mongolia - ERC (Energy Regulatory Commission)

- **name**: "ERC - Energy Regulatory Commission (Mongolia)"
- **proposed id**: `erc_mn`
- **base_url**: `https://erc.gov.mn`
- **start_paths**: `/en/files?tag=16` (Policies, regulations and rules),
  `/en/files?tag=17` (Other policy and rules), `/en/`
- **level**: national
- **access**: none
- **coverage**: region: `["apac"]`; category: `regulatory`; tags: `["district_heating",
  "efficiency", "mandates"]`; policy_types: `["regulation", "law"]`; language: `en`
  (`mn` primary)
- **format**: HTML/PDF
- **practical**: not rate-limit tested; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: the only cold-climate country in the South/Southeast-Asia
  batch - regulates BOTH electricity and district heat tariffs, actively working a
  heat-meter transition for Ulaanbaatar's district heating system, dedicated Energy
  Conservation section. Squarely on the district-heating taxonomy, not just adjacent
  efficiency policy.
- **verified**: yes. WebFetch confirmed heat tariff pages, a Feb 2026 heat-meter news
  item, Energy Conservation section, three legal-document categories.

### 16. Moldova - Ministry of Energy

- **name**: "Ministry of Energy of the Republic of Moldova"
- **proposed id**: `energie_gov_md`
- **base_url**: `https://energie.gov.md`
- **start_paths**: `/en/content/about-ministry`, `/en/content/energy-efficiency`
- **level**: national
- **access**: none
- **coverage**: region: `["europe", "eu_east"]`; category: `energy_ministry`; tags:
  `["mandates", "efficiency", "incentives"]`; policy_types: `["strategy", "guidance",
  "law"]`; language: `en`/`ro`
- **format**: HTML
- **practical**: not rate-limit tested; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: standalone ministry since a Feb 2023 reorg; page explicitly
  covers Energy Strategy to 2050, National Energy Efficiency Program, Energy
  Efficiency Fund, and EU Directive 2018/2002 transposition obligations.
- **verified**: yes. WebFetch confirmed title and content on all programs named above.

### 17. Lebanon - LCEC (Lebanese Center for Energy Conservation)

- **name**: "LCEC - Lebanese Center for Energy Conservation"
- **proposed id**: `lcec_lb`
- **base_url**: `https://lcec.org.lb`
- **start_paths**: `/EPC`, `/`
- **level**: national
- **access**: none
- **coverage**: region: `["middle_east"]`; category: `energy_ministry`; tags:
  `["efficiency", "incentives"]`; policy_types: `["standard", "law", "program"]`;
  language: `en`
- **format**: HTML/PDF
- **practical**: not rate-limit tested; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: Lebanon's national energy-efficiency agency (technical arm of
  the Ministry of Energy and Water) - wrote the first National Energy Efficiency
  Action Plan in the Arab world, runs the EPC-L building energy certification scheme
  and a green-building finance program.
- **verified**: yes. WebFetch confirmed EPC-L Scheme page, Distributed Renewable
  Energy Law 318/2023 resource, publications/download center.

### 18. Uzbekistan - LEX.UZ (National Database of Legislation)

- **name**: "LEX.UZ - National Database of Legislation (Uzbekistan)"
- **proposed id**: `lex_uz`
- **base_url**: `https://lex.uz`
- **start_paths**: `/en`
- **level**: national
- **access**: none
- **coverage**: region: **flag - recommend `central_asia`**; category: `legislative`;
  tags: `["mandates", "efficiency"]`; policy_types: `["law", "regulation"]`; language:
  `en`/`uz`/`ru`
- **format**: HTML
- **practical**: has an advanced search with structured filters (act type/date/
  branch) but no confirmed public API - tier-b for now, worth revisiting as tier-c if
  an API surfaces.
- **effort tier**: b
- **why worth adding**: Uzbekistan's actual legislative search engine (not just the
  ministry's static page) - advanced search across Laws/Presidential acts/Government
  decisions/Ministry acts, filterable by legislative branch, the best route to actual
  energy-efficiency law text.
- **verified**: yes. WebFetch confirmed title "LEX.UZ - Legislation of Uzbekistan",
  described universal + advanced search with named filter fields.

### 19. Jordan - MEMR (Ministry of Energy and Mineral Resources)

- **name**: "MEMR - Ministry of Energy and Mineral Resources (Jordan)"
- **proposed id**: `memr_jo`
- **base_url**: `https://www.memr.gov.jo`
- **start_paths**: `/Default/En`, `/En/List/Open_Data`
- **level**: national
- **access**: none
- **coverage**: region: `["middle_east"]`; category: `energy_ministry`; tags:
  `["efficiency", "renewable_energy", "planning"]`; policy_types: `["strategy", "law",
  "report"]`; language: `en`
- **format**: HTML/PDF
- **practical**: not rate-limit tested; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: operates the Jordan Renewable Energy & Energy Efficiency Fund
  (JREEEF), which funds efficiency in residential/hospital/industrial/service sectors;
  Energy Sector Strategy, Legislations section, and a licensed-energy-auditor
  registry. Jordan is a Gulf/ME "extra" not covered by RCREEE membership alone.
- **verified**: yes. WebFetch confirmed JREEEF references, Energy Sector Strategy,
  Legislations/Laws-Bylaws-Instructions sections, licensed energy-audit companies
  list.

### 20. Albania - Ministry of Infrastructure and Energy

- **name**: "Ministry of Infrastructure and Energy (Albania)"
- **proposed id**: `infrastruktura_gov_al`
- **base_url**: `https://www.infrastruktura.gov.al`
- **start_paths**: `/en/`
- **level**: national
- **access**: none
- **coverage**: region: `["europe", "eu_east"]`; category: `energy_ministry`; tags:
  `["mandates", "planning"]`; policy_types: `["law", "guidance"]`; language: `en`/`sq`
- **format**: HTML/PDF
- **practical**: not rate-limit tested; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: a draft law (2026 rollout) mandates district heating/cooling
  and CHP consideration for new buildings, plus a dedicated "Legjislacioni"
  (Legislation) nav section.
- **verified**: yes. WebFetch confirmed title, Legislation section, Energy service
  listing.

### 21. Tanzania - Ministry of Energy (Nishati)

- **name**: "Ministry of Energy (Nishati), Tanzania"
- **proposed id**: `nishati_tz`
- **base_url**: `https://www.nishati.go.tz`
- **start_paths**: `/pages/policy-and-strategy` (confirm slug; homepage nav shows
  "Acts and Regulations" under both Electricity/Renewable Energy and Petroleum)
- **level**: national
- **access**: none
- **coverage**: region: `["africa"]`; category: `energy_ministry`; tags:
  `["efficiency", "mandates", "planning", "reporting"]`; policy_types: `["law",
  "regulation", "strategy", "report"]`; language: `en` (some `sw`)
- **format**: HTML + PDF
- **practical**: not checked this session; recommend 2-3s pending confirmation.
- **effort tier**: b
- **why worth adding**: the National Energy Efficiency Action Plan 2019 (2020-2025,
  MEPS/labeling for refrigerators/HVAC/lighting/motors) sits under this ministry;
  confirmed dedicated "Acts and Regulations" and "Policy and strategy" sections.
- **verified**: yes. WebFetch confirmed both "Publications > Policy and strategy" and
  "Acts and Regulations" under Electricity/Renewable Energy.

### 22. Nepal - AEPC (Alternative Energy Promotion Centre)

- **name**: "AEPC - Alternative Energy Promotion Centre (Nepal)"
- **proposed id**: `aepc_np`
- **base_url**: `https://www.aepc.gov.np`
- **start_paths**: `/`
- **level**: national
- **access**: none
- **coverage**: region: `["apac"]`; category: `energy_ministry`; tags: `["efficiency",
  "renewable_energy", "incentives"]`; policy_types: `["standard", "regulation",
  "guidance"]`; language: `en`
- **format**: HTML/PDF
- **practical**: not rate-limit tested; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: Nepal's government energy-efficiency mandate holder (under
  the Ministry of Energy, Water Resources and Irrigation) - dedicated Energy
  Efficiency menu (audits, energy management systems, standards/labeling) plus a
  Resource Centre with Policy & Frameworks / AEPC Regulations.
- **verified**: yes. WebFetch confirmed Energy Efficiency menu (Audit, Energy
  Management System, Standards/Labeling), Resource Centre with Policy & Frameworks and
  AEPC Regulations.

### 23. Cote d'Ivoire - ANARE-CI (Autorite Nationale de Regulation du secteur de l'Electricite)

- **name**: "ANARE-CI - National Regulatory Authority for the Electricity Sector
  (Cote d'Ivoire)"
- **proposed id**: `anare_ci`
- **base_url**: `https://anare.ci`
- **start_paths**: `/documents/lois-et-reglementation/les-arretes/`, `/le-regulateur/`
- **level**: national
- **access**: none
- **coverage**: region: `["africa"]`; category: `regulatory`; tags: `["mandates",
  "reporting"]`; policy_types: `["law", "regulation", "directive"]`; language: `fr`
- **format**: HTML + PDF
- **practical**: robots.txt fully open (bare `User-agent: *`, no disallow); recommend
  2-3s.
- **effort tier**: b
- **why worth adding**: national electricity regulator (est. under Ordonnance 2013),
  an archive of ~20 downloadable regulatory orders 2012-2024 (connection procedures,
  licensing conditions, eligible-customer status). Complements DGE (#7 above) with the
  regulator-side enforcement instruments rather than ministry-side policy/strategy -
  distinct enough from DGE to keep both.
- **verified**: yes. WebFetch confirmed a page listing specific arrete numbers/titles
  with PDF links, "Lois et reglements" nav with Lois/Decrets/Arretes subsections.

### 24. Sri Lanka - SLSEA (Sustainable Energy Authority)

- **name**: "Sri Lanka Sustainable Energy Authority (SLSEA)"
- **proposed id**: `slsea_lk`
- **base_url**: `https://www.energy.gov.lk`
- **start_paths**: `/en/`, `/en/energy-management/introducing-standards`
- **level**: national
- **access**: none
- **coverage**: region: `["apac"]`; category: `energy_ministry`; tags: `["efficiency",
  "mandates"]`; policy_types: `["standard", "law", "guidance"]`; language: `en`
- **format**: HTML/PDF
- **practical**: not rate-limit tested; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: warm-climate/cooling-relevant - statutory power (Act No. 35
  of 2007) to enforce a code of practice on efficient energy use in buildings,
  publishes the Energy Efficiency Building Code, and runs a National Energy
  Benchmarking Portal.
- **verified**: yes. WebFetch confirmed Energy Management section (Establishing
  Systems, Introducing Standards, Labelling Programme), National Energy Policy
  references, building energy code.

### 25. Georgia - Ministry of Economy and Sustainable Development

- **name**: "Ministry of Economy and Sustainable Development (Georgia)"
- **proposed id**: `economy_ge`
- **base_url**: `https://www.economy.ge`
- **start_paths**: `/?lang=en`
- **level**: national
- **access**: none
- **coverage**: region: **flag - recommend `caucasus`**; category: `energy_ministry`;
  tags: `["mandates", "efficiency"]`; policy_types: `["law", "guidance"]`; language:
  `en`/`ka`
- **format**: HTML
- **practical**: not rate-limit tested; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: absorbed the Ministry of Energy's functions in 2017 and is the
  current holder of the energy portfolio (EU Association Agreement energy-
  efficiency/renewables obligations); dedicated "Energy" subsection under Economic
  Policy.
- **verified**: yes. WebFetch confirmed ministry identity, Energy subsection, listed
  affiliated state energy entities.

### 26. Cambodia - MME (Ministry of Mines and Energy)

- **name**: "Ministry of Mines and Energy (Cambodia)"
- **proposed id**: `mme_kh`
- **base_url**: `https://mme.gov.kh`
- **start_paths**: `/`
- **level**: national
- **access**: none
- **coverage**: region: `["apac"]`; category: `energy_ministry`; tags: `["efficiency",
  "planning", "renewable_energy"]`; policy_types: `["strategy", "regulation"]`;
  language: `en`/`km`
- **format**: HTML/PDF
- **practical**: not rate-limit tested; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: warm-climate country - MME leads Cambodia's National Energy
  Efficiency Policy 2022-2030 (19% consumption reduction target by 2030); "Resources >
  Rules and Regulations" section confirmed.
- **verified**: yes. WebFetch confirmed the General Department of Energy's policy/
  planning role, Resources (Rules and Regulations) section, and the National Energy
  Efficiency Policy 2022 (independently corroborated as a standalone PDF via Open
  Development Cambodia).

### 27. Bosnia and Herzegovina - Ministry of Foreign Trade and Economic Relations (state-level Energetika portfolio)

- **name**: "Ministry of Foreign Trade and Economic Relations (BiH) - Energetika"
- **proposed id**: `mvteo_gov_ba`
- **base_url**: `https://www.mvteo.gov.ba`
- **start_paths**: `/` (language-gate splash - a human should pick the
  post-selection Energetika path)
- **level**: national
- **access**: none
- **coverage**: region: `["europe", "eu_east"]`; category: `energy_ministry`; tags:
  `["mandates", "planning"]`; policy_types: `["strategy"]`; language: `bs`/`hr`/`sr`/`en`
- **format**: HTML/PDF
- **practical**: homepage is a language-selector gate; a human needs to pick the
  correct post-language-selection path before enabling.
- **effort tier**: b
- **why worth adding**: publishes the Framework Energy Strategy of BiH until 2035
  (confirmed live as a 194-page PDF on this domain) with a district-heating strategy
  section.
- **verified**: yes, partial - homepage nav 404'd on an `/en` path, but the strategy
  PDF itself downloaded successfully (7.7MB, 194 pages), confirming the domain hosts
  real, current strategy documents.

### 28. Namibia - ECB (Electricity Control Board)

- **name**: "Electricity Control Board (ECB, Namibia)"
- **proposed id**: `ecb_na`
- **base_url**: `https://www.ecb.org.na`
- **start_paths**: `/economic-regulation/`, `/about-us/`
- **level**: national
- **access**: none
- **coverage**: region: `["africa"]`; category: `regulatory`; tags: `["mandates",
  "reporting", "planning"]`; policy_types: `["regulation", "report", "guidance"]`;
  language: `en`
- **format**: HTML + PDF
- **practical**: not checked this session; recommend 2-3s pending confirmation.
- **effort tier**: b
- **why worth adding**: national electricity regulator, publishes Legal Instruments,
  an Integrated Strategic Business Plan, and Smart Grid Policy / National
  Electrification Policy PDFs.
- **verified**: yes. WebFetch confirmed "Legal Instruments," "Integrated Strategic
  Business Plan," Studies/Peer Reviewed Documents sections.

### 29. Rwanda - RURA (Rwanda Utilities Regulatory Authority) - energy sector

- **name**: "Rwanda Utilities Regulatory Authority (RURA) - Energy Sector"
- **proposed id**: `rura_rw`
- **base_url**: `https://www.rura.rw`
- **start_paths**: `/sectors/energy/overview`,
  `/sectors/energy/sub-sectors-and-services/electricity`
- **level**: national
- **access**: none
- **coverage**: region: `["africa"]`; category: `regulatory`; tags: `["efficiency",
  "mandates", "reporting"]`; policy_types: `["guidance", "regulation", "report"]`;
  language: `en`
- **format**: HTML + PDF
- **practical**: not checked this session; recommend 2-3s pending confirmation.
- **effort tier**: b
- **why worth adding**: published dedicated "Guidelines for Promoting Energy
  Efficiency Measures" (2013) plus Electricity Licensing Regulations under Law
  N deg;21/2011 (amended by Law N deg;52/2018) - the clearest EE-specific regulatory
  artifact found for Rwanda.
- **verified**: yes. WebFetch confirmed "Regulatory Instruments," "Sector Reports,"
  "Publications" sections and the four-subsector energy mandate.

### 30. Ethiopia - MoWE (Ministry of Water and Energy)

- **name**: "Ministry of Water and Energy (MoWE), Ethiopia"
- **proposed id**: `mowe_et`
- **base_url**: `https://www.mowe.gov.et`
- **start_paths**: `/en/about`, `/en`
- **level**: national
- **access**: none
- **coverage**: region: `["africa"]`; category: `energy_ministry`; tags: `["planning",
  "efficiency"]`; policy_types: `["strategy", "report", "guidance"]`; language: `en`
- **format**: HTML + PDF
- **practical**: not checked this session; recommend 2-3s pending confirmation.
- **effort tier**: b
- **why worth adding**: parent ministry for Ethiopia's energy policy/strategy
  formulation and the Energy Efficiency and Conservation Fund framework (Energy
  Regulation Ch.6); confirmed live with an "Energy Development Documents" resource
  category.
- **verified**: yes, partial. WebFetch confirmed the live site and the three-sector
  structure with an Energy Development documents subsection, but specific policy PDFs
  were not individually opened this session - homepage nav only.

### 31. Myanmar - MOEE (Ministry of Electricity and Energy)

- **name**: "Ministry of Electricity and Energy (MOEE), Myanmar"
- **proposed id**: `moee_mm`
- **base_url**: `https://moep.gov.mm`
- **start_paths**: `/`
- **level**: national
- **access**: none
- **coverage**: region: `["apac"]`; category: `energy_ministry`; tags: `["mandates",
  "efficiency", "planning"]`; policy_types: `["law", "regulation", "strategy"]`;
  language: `en`/`my`
- **format**: HTML/PDF
- **practical**: not rate-limit tested; robots.txt not checked. **Flag**: this is the
  current State Administration Council (post-2021) government's ministry site -
  expect intermittent availability, consistent with the brief's general warning that
  Myanmar government sites are often unstable.
- **effort tier**: b
- **why worth adding**: Electricity Law, Grid Code, National Electrification Plan, and
  stated energy-efficiency initiatives all confirmed live under one ministry. Note:
  `energy.gov.mm` (a similarly-named but separate domain) is the oil/gas-focused
  Ministry of Energy - do not conflate the two.
- **verified**: yes. WebFetch confirmed Electricity Law, Grid Code, NEP Plan, Power
  Planning/Transmission/Hydropower department pages.

### 32. Uzbekistan - Ministry of Energy

- **name**: "Ministry of Energy of the Republic of Uzbekistan"
- **proposed id**: `gov_uz_minenergy`
- **base_url**: `https://gov.uz`
- **start_paths**: `/en/minenergy`
- **level**: national
- **access**: none
- **coverage**: region: **flag - `central_asia`**; category: `energy_ministry`; tags:
  `["mandates", "efficiency"]`; policy_types: `["law", "regulation"]`; language:
  `en`/`uz`
- **format**: HTML/PDF
- **practical**: not rate-limit tested; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: designated authority for the amended Law on Rational Use of
  Energy (2020); Documents section lists laws, ministry-of-justice-registered
  regulations, and resolutions.
- **verified**: yes. WebFetch confirmed title and Documents-section nav items.
  Caveat: no data-center-specific content surfaced - general energy-efficiency
  framework only.

### 33. Cambodia - EAC (Electricity Authority of Cambodia)

- **name**: "Electricity Authority of Cambodia (EAC)"
- **proposed id**: `eac_kh`
- **base_url**: `https://eac.gov.kh`
- **start_paths**: `/site/index?lang=en`
- **level**: national
- **access**: none
- **coverage**: region: `["apac"]`; category: `regulatory`; tags: `["mandates",
  "reporting"]`; policy_types: `["law", "regulation", "standard"]`; language:
  `en`/`km` (site states Khmer text prevails on discrepancy)
- **format**: HTML/PDF
- **practical**: not rate-limit tested; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: national electricity regulator complementing MME (#26) -
  dedicated Law & Regulation, Power Technical Standard, and Circular sections; issues
  tariff/licensing decisions relevant to any future data-center grid-connection
  policy.
- **verified**: yes. WebFetch confirmed Law & Regulation / Power Technical Standard /
  Circular / Annual Report nav sections.

### 34. Armenia - PSRC (Public Services Regulatory Commission)

- **name**: "Public Services Regulatory Commission (Armenia)"
- **proposed id**: `psrc_am`
- **base_url**: `https://www.psrc.am`
- **start_paths**: `/contents/fields/electric_energy/el_energy_tariffs`
- **level**: national
- **access**: none
- **coverage**: region: **flag - `caucasus`**; category: `regulatory`; tags:
  `["mandates", "reporting"]`; policy_types: `["regulation"]`; language:
  `hy`/`en`/`ru`
- **format**: HTML
- **practical**: not rate-limit tested; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: sole regulator for electricity, gas, water, and thermal
  energy/district heating tariffs in Armenia - the only Armenian body confirmed to
  actually regulate district heating.
- **verified**: yes, partial. WebFetch confirmed title and the electricity-tariff
  subsection directly; the thermal-energy/district-heating subsection (likely a
  parallel `fields/thermal_energy` path) was corroborated by search results but not
  independently fetched - flag for a human to confirm the exact URL.

### 35. Jordan - EMRC (Energy and Minerals Regulatory Commission)

- **name**: "Energy and Minerals Regulatory Commission (EMRC, Jordan)"
- **proposed id**: `emrc_jo`
- **base_url**: `https://www.emrc.gov.jo`
- **start_paths**: `/`
- **level**: national
- **access**: none
- **coverage**: region: `["middle_east"]`; category: `regulatory`; tags: `["mandates",
  "renewable_energy"]`; policy_types: `["regulation", "law"]`; language: `ar`
- **format**: HTML/PDF
- **practical**: mostly Arabic-only content; not rate-limit tested; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: legal successor to Jordan's Electricity Regulatory
  Commission - licensing authority for electricity/renewables, a national electricity
  conservation campaign, laws/regulations section; complements MEMR (#19) with the
  regulator side.
- **verified**: yes. WebFetch confirmed electricity-sector licensing, renewable-
  energy licensing division, national electricity conservation campaign, laws/
  regulations section (Arabic-language homepage).

### 36. Nepal - ERC (Electricity Regulation Commission)

- **name**: "Electricity Regulation Commission (ERC, Nepal)"
- **proposed id**: `erc_np`
- **base_url**: `https://erc.gov.np`
- **start_paths**: `/`
- **level**: national
- **access**: none
- **coverage**: region: `["apac"]`; category: `regulatory`; tags: `["mandates",
  "reporting"]`; policy_types: `["law", "regulation"]`; language: `ne`
- **format**: HTML/PDF
- **practical**: not rate-limit tested; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: statutory electricity regulator (Electricity Regulatory
  Commission Act 2017) - Acts and Rules, Regulations, Guidelines, Grid Code sections
  all confirmed; drafting an Energy Efficiency Policy per its 2024-2029 roadmap (not
  yet published).
- **verified**: yes. WebFetch confirmed Acts and Rules, Regulations, Guidelines, Grid
  Code, tariff/charge-order sections.

### 37. Botswana - BERA (Energy Regulatory Authority)

- **name**: "Botswana Energy Regulatory Authority (BERA)"
- **proposed id**: `bera_bw`
- **base_url**: `https://www.bera.co.bw`
- **start_paths**: `/` (a Documents section is referenced under the Media nav - exact
  slug not independently confirmed)
- **level**: national
- **access**: none
- **coverage**: region: `["africa"]`; category: `regulatory`; tags: `["mandates",
  "planning"]`; policy_types: `["regulation", "standard"]`; language: `en`
- **format**: HTML + PDF
- **practical**: not checked; recommend 2-3s pending confirmation.
- **effort tier**: b
- **why worth adding**: sole national energy regulator under the Botswana Energy
  Regulatory Act 2016, covering electricity/gas/coal/petroleum/renewables licensing
  and standards.
- **verified**: partial - homepage confirmed live and on-topic (identity, mandate,
  tagline), but the Documents subsection content itself was not independently loaded
  this session (nav item mentioned, not traversed). Recommend a human/deeper
  crawl-time check of the actual Documents path before enabling; base site is real and
  government-operated.

### 38. Sri Lanka - PUCSL (Public Utilities Commission)

- **name**: "Public Utilities Commission of Sri Lanka (PUCSL)"
- **proposed id**: `pucsl_lk`
- **base_url**: `https://www.pucsl.gov.lk`
- **start_paths**: `/`
- **level**: national
- **access**: none
- **coverage**: region: `["apac"]`; category: `regulatory`; tags: `["mandates",
  "reporting", "renewable_energy"]`; policy_types: `["regulation", "law"]`; language:
  `en`
- **format**: HTML/PDF
- **practical**: not rate-limit tested; recommend 2-3s.
- **effort tier**: b
- **why worth adding**: economic/technical/safety regulator for electricity (Sri
  Lanka Electricity Act No. 20 of 2009) - tariff decisions, legal documents (acts/
  regulations/guidelines), feed-in-tariff reviews. Weaker on efficiency-specific
  content than SLSEA (#24) but complements it on the regulatory/tariff side.
- **verified**: yes. WebFetch confirmed tariff decisions (incl. a May 2026 electricity
  tariff decision), legal documents section, feed-in tariff reviews.

### 39. Kazakhstan - Ministry of Energy

- **name**: "Ministry of Energy of the Republic of Kazakhstan"
- **proposed id**: `gov_kz_energo`
- **base_url**: `https://www.gov.kz`
- **start_paths**: `/memleket/entities/energo?lang=en`
- **level**: national
- **access**: none
- **coverage**: region: **flag - `central_asia`**; category: `energy_ministry`; tags:
  `["mandates", "efficiency"]`; policy_types: `["law", "regulation"]`; language:
  `en`/`kk`/`ru`
- **format**: HTML
- **practical**: `requires_playwright: true` strongly recommended.
- **effort tier**: b
- **why worth adding**: primary national ministry, would be the natural companion to
  Adilet (#2 above).
- **verified**: partial - low confidence. Every fetch attempt returned only the bare
  page `<title>` with zero body content across three different sub-paths - a heavy
  JS single-page app that renders nothing to a plain fetch. Domain/ministry identity
  is solid (multiple independent sources confirm this is the real ministry portal),
  but actual page content was never inspected. A human with Playwright/rendered-
  browser access needs to confirm before enabling.

---

## Unverified / needs-human-check

- **GNERC (Georgian National Energy and Water Supply Regulatory Commission)**,
  `gnerc.org` - Georgia's actual energy/district-heating tariff regulator and
  probably the single best Georgian candidate on paper (explicit DH provisions in its
  enabling Law on Energy and Water Supply). Every fetch attempt (https/http, `/en/
  home`, bare domain, `www.` prefix) returned `connect ECONNREFUSED` - the host
  actively refused connection from this environment across ~4 attempts. Flag as
  possibly geo/IP-blocked; a human should check from a different network.
- **ERC.org.mk (Energy and Water Services Regulatory Commission, North Macedonia)** -
  the district-heating-specific regulator (Skopje's DH tariffs). Returned HTTP 403 on
  every path tried - consistent bot-detection blocking. Domain/agency identity is
  well-corroborated by search (ERRA membership page, its own annual reports), but
  content itself unreachable by this tool.
- **FERK (Regulatory Commission for Energy in Federation of BiH)**, `ferk.ba` -
  fetch returned an empty body with no error; inconclusive (could be a redirect/JS
  gate the tool didn't follow). Needs a human re-check.
- **Ministry of Territorial Administration and Infrastructure (Armenia)**, `mtad.am` -
  current holder of Armenia's energy policy portfolio per search results (search also
  surfaced a possibly-defunct `minenergy.am` - unclear if that's a stale mirror or the
  ministry was renamed/merged; conflicting signals). WebFetch confirmed the site is
  live and real, but its homepage nav showed no visible energy-specific section - a
  human needs to dig into "Functions" or "Programs and priorities."
- **Ministry of Energy (Russia)**, `minenergo.gov.ru/en` - resolves and returns HTTP
  200 with a confirmed real page title, so not flatly geo-blocked, but every fetch
  (home, `/en/activity`, `/en/activity/energoeffektivnost`) returned literally zero
  body content beyond the title - appears to be a heavily JS-rendered SPA that this
  fetch tool cannot execute. Content could not be confirmed at all. A human with a
  real rendered browser (or Playwright) should re-check.
- **publication.pravo.gov.ru (Russia's federal law-publication system)** - both fetch
  attempts failed outright with no response at all, the strongest signal among all
  wave-2 countries of an actual connectivity/geo block from this research
  environment. Very likely unreachable from a US-based environment; consistent with
  the brief's own expectation that Russia fetch access may be blocked.
- **elicense.kz / egov.kz digital-mining-license portal (Kazakhstan)** - confirmed
  real and live, but it's a transactional licensing application system, not a
  repository of policy documents/laws - doesn't meet the brief's "publishes or lets
  us query policy documents" bar. Context only, not a proposed source.
- **Ethiopian Energy Authority (EEA)**, `eea.gov.et` - the statutorily correct
  regulator (Proclamation 810/2013) for Ethiopia's efficiency/conservation mandates
  and the single best-fit candidate for Ethiopia, but DNS resolution failed
  (`ENOTFOUND`) on both the bare domain and `www.` variant, tried twice. Third-party
  sources reference it as real and active. Recommend a human re-check from a
  different network/DNS resolver before enabling.
- **Ministry of Mines and Energy (Namibia)**, `mme.gov.na` - repeated
  `ECONNREFUSED` (2 attempts) - likely geo-fencing/firewall against the research
  environment's IP rather than the site being down, since ECB (#28, same country)
  resolved fine. Hosts the National Energy Policy (July 2017) and Smart Grid Policy
  PDFs if reachable. ECB already covers Namibia adequately in the meantime.
- **Ministry of Minerals and Energy (Botswana)**, `gov.bw/ministries/ministry-
  minerals-and-energy` - returned HTTP 503, likely bot-detection/rate-limiting on the
  gov.bw cloud portal. BERA (#37) already covers Botswana's regulatory side.
- **Ministry of Infrastructure (MININFRA), Rwanda**, `mininfra.gov.rw` - resolved and
  is genuinely the parent ministry (published a February 2025 Energy Policy PDF per
  search results), but the homepage fetch showed only a generic "Publications" nav
  link with no specific documents surfaced - too thin to confirm independently. RURA
  (#29) is the stronger, already-verified Rwanda candidate.
- **Zambia ERB "documents" library** - mentioned as a subsection of ERB (#13) but not
  independently opened as its own URL; flag `/documents` as a candidate additional
  start_path for a human to confirm structure at crawl-build time.
- **Iraq - Ministry of Electricity**, `moelc.gov.iq` - real domain confirmed via
  search, but every fetch attempt (plain WebFetch, and a live browser session) was
  intercepted by a bot-detection "Secure Gateway" interstitial that never resolved to
  real content. Recommend human check with a longer-wait/JS-solving browser session.
  No usable content seen - do not add to config yet.
- **Iraq - KRG Ministry of Electricity**, `gov.krd/moel-en` - Kurdistan Regional
  Government's electricity ministry. Direct WebFetch returned 403; a live browser
  session DID load the homepage cleanly (confirmed title, News/Publications/Services
  nav, current news items), but navigating into Publications redirected back to the
  homepage shell (heavy client-side routing) - no policy-document content
  independently confirmed. Would need `requires_playwright` and deeper navigation,
  and is subnational (Kurdistan Region only, not federal Iraq) if added.
- **Iraq: no national-level source cleared verification this round.** Both
  candidates found are real government bodies but neither produced fetchable,
  on-topic policy content in this session. Genuine gap pending a human/browser
  recheck, consistent with the brief's own warning that Iraq gov sites are often
  unstable.
- **Bangladesh - BERC**, `berc.org.bd` - national energy/electricity/gas/petroleum
  regulator (BERC Act 2003), tariff-setting and licensing authority. Both WebFetch
  and a live browser navigation failed with a TLS certificate error - the site's SSL
  configuration appears broken or self-signed. Content is very likely real and
  relevant but recommend a human check with relaxed-TLS or an alternate network
  before enabling.
- **Pakistan - NEPRA**, `nepra.org.pk` - national electricity regulator, publishes
  the National Electricity Policy 2021 and tariff determinations (confirmed via
  search-engine PDF links). Direct WebFetch returned HTTP 403 (bot detection); not
  independently re-confirmed with a browser this session. Pakistan already has one
  solid verified source (NEECA, #9); this would be a secondary/regulatory-side
  addition, not essential.

---

## Summary by sub-batch

- **Central Asia + wider Europe non-EU** (10 countries): 14 verified candidates (9
  fully verified, 5 partial with explicit caveats), all tier-b, 0 tier-a, 0 tier-c.
  7 unverified/blocked entries. Russia produced zero clean verifications - both the
  ministry site and the federal law portal were effectively unreachable/unrenderable
  from this environment. Highest-value find: Kazakhstan's Adilet entries for the
  Digital Assets Law / mining-registry regime - the only source directly regulating
  data-center-adjacent electricity consumption in this sub-batch.
- **More Africa** (10 countries): 12 verified candidates, all tier-b, all
  `access: none`. 5 flagged unverified/needs-human-check (2 DNS failures, 1
  connection-refused, 1 HTTP 503, 1 too-thin-to-confirm). No country produced zero
  candidates. Highest-value find: APRUE (Algeria) - a dedicated national
  energy-efficiency implementation agency with an auditor registry and a
  legislative-texts archive.
- **More Asia + Gulf/ME extras** (10 countries): 13 verified candidates, all tier-b.
  Iraq produced zero verified candidates (both federal and KRG electricity ministries
  blocked by bot-detection/broken routing). Highest-value find: Mongolia's ERC - the
  only source in this sub-batch squarely on the district-heating taxonomy rather than
  general efficiency/electricity regulation.
