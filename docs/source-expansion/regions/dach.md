# DACH Subnational — Source Expansion Research

Region: Germany / Austria / Switzerland subnational (Bundesländer, Bundesländer/national
bodies, Kantone). German federal Bundestag (DIP API) already covered — not re-proposed.

Dedup check performed against `config/domains/germany.yaml`, `austria.yaml`,
`switzerland.yaml`, `api_sources.yaml` before researching. Existing coverage found:
- Germany: 8 of 16 Länder already have ministry + Landesrecht entries (Hessen, Bayern,
  NRW, Baden-Württemberg, Berlin, Hamburg, Niedersachsen, Sachsen). The 8 missing Länder
  are the focus below: Brandenburg, Bremen, Mecklenburg-Vorpommern, Rheinland-Pfalz,
  Saarland, Sachsen-Anhalt, Schleswig-Holstein, Thüringen.
- Austria: national ministry (bmk.gv.at) + federal law search (ris.bka.gv.at) already
  present. Missing: Klima- und Energiefonds, subnational (Vienna).
- Switzerland: federal (BFE/BAFU/fedlex/admin.ch), canton Zürich (5 entries), MuKEn/EnDK,
  SDEA, EnergieSchweiz already present. Missing: other cantons (Geneva, Bern, Basel-Stadt,
  Vaud picked as highest DC/heat-network relevance).

All candidates below are **crawl domains** (effort tier b) — plain government/legal
portals, no structured API available. `access: none` for every entry (open, no login,
no API key) unless noted.

---

## Verified candidates

Ranked best-first by policy relevance to data-center waste-heat reuse.

### 1. Geneva — Loi sur l'énergie (LEn), Art. 17A explicit data-center heat recovery

- **name**: "Genève — Loi sur l'énergie (LEn) rsGE L 2 30"
- **id**: `ge_len_energie`
- **base_url**: `https://silgeneve.ch`
- **start_paths**: `["/legis/data/rsg_l2_30.htm"]`
- **level**: subnational (canton)
- **access**: none
- **coverage**: region: `["eu_central", "switzerland", "geneva"]`; category:
  `legislation`; tags: `["mandatory", "waste_heat", "data_center_specific",
  "district_heating"]`; policy_types: `["law"]`; language: `fr`
- **format**: HTML
- **practical**: no rate limit info published; single consolidated-law page (not paginated);
  official cantonal law-text host (SIL = Systeme d'Information Legislatif Genève); low
  update frequency (amended by cantonal vote).
- **effort tier**: b (crawl domain)
- **why worth adding**: Article 17A explicitly names "les chaleurs émises par les serveurs
  informatiques" (heat emitted by computer servers) as subject to Geneva's mandatory heat
  recovery framework — the single most explicit non-German DACH statutory text naming
  data centers by name. Complements the German EnEfG and Zurich cantonal law already in
  the config as validation targets.
- **verified**: yes. Fetched and confirmed via WebFetch: page title/content is Geneva's
  Loi sur l'énergie, last modified 2026-07-04. Article 17A text captured directly: "Sont
  concernées par le présent article les chaleurs émises par les serveurs informatiques,
  les activités industrielles et les activités artisanales."
- **Append to**: new file `config/domains/switzerland.yaml` (canton Geneva section,
  parallel to the existing canton Zürich section).

### 2. Basel-Stadt — Energiegesetz (EnG), large-consumer waste-heat + heat-planning duty

- **name**: "Kanton Basel-Stadt — Energiegesetz (EnG) SG 772.100"
- **id**: `bs_energiegesetz`
- **base_url**: `https://gesetzessammlung.bs.ch`
- **start_paths**: `["/app/de/texts_of_law/772.100"]`
- **level**: subnational (canton)
- **access**: none
- **coverage**: region: `["eu_central", "switzerland", "basel"]`; category:
  `legislation`; tags: `["mandatory", "waste_heat", "district_heating", "large_consumers",
  "planning"]`; policy_types: `["law"]`; language: `de`
- **format**: HTML (JS-rendered "LexWork" app — confirmed renders full text without
  requiring interaction; `requires_playwright: true` recommended)
- **practical**: no published rate limit; single consolidated-law page; low update
  frequency (last amended 2024-07-01).
- **effort tier**: b (crawl domain)
- **why worth adding**: § 17 obligates large consumers (>5 GWh/yr heat or >0.5 GWh/yr
  electricity — explicitly named source: "Serverräume und Rechenzentren" per companion
  search results) to analyze consumption and use waste heat; § 19 mandates cantonal heat
  planning (Energierichtplan) with waste-heat allocation; § 2(4) requires district heating
  to reach 80% CO2-free by 2020. Directly analogous to the Zurich EnerG already in config.
- **verified**: yes. Full text pulled via browser (JS app rendered): confirmed §§ 1-41,
  including § 17 (Grossverbraucher, 5 GWh/0.5 GWh thresholds), § 19 (kantonale
  Energieplanung, Abwärme-Anteil), § 2(4) (Fernwärme CO2-frei ab 2020).
- **Append to**: `config/domains/switzerland.yaml`, new canton Basel-Stadt section.

### 3. Vaud — Législation sur l'énergie (LVLEne), large-consumer + territorial energy planning

- **name**: "Canton de Vaud — Législation sur l'énergie (LVLEne)"
- **id**: `vd_energie_legislation`
- **base_url**: `https://www.vd.ch`
- **start_paths**:
  `["/environnement/energie/legislation/principaux-elements-de-la-loi-sur-lenergie"]`
- **level**: subnational (canton)
- **access**: none
- **coverage**: region: `["eu_central", "switzerland", "vaud"]`; category:
  `energy_ministry`; tags: `["mandatory", "waste_heat", "planning", "large_consumers"]`;
  policy_types: `["law", "guidance"]`; language: `fr`
- **format**: HTML
- **practical**: no rate limit published; note the new LVLEne (adopted Feb 2026) enters
  into force January 2027 — current page covers both the law in force through
  2026-12-31 and links to the incoming replacement; re-check after Jan 2027.
- **effort tier**: b (crawl domain)
- **why worth adding**: Art. 28c–28e LVLEne: large energy consumers (>5 GWh/yr heat or
  >0.5 GWh/yr electricity) must analyze and reduce consumption — same MuKEn-derived
  threshold as Zurich/Basel/Bern, giving another canton data point. Art. 16e–16g mandates
  territorial energy planning that integrates renewable/recovered heat into zoning.
- **verified**: yes. Full page text pulled via browser: confirmed all article citations
  above, DGE-DIREN (Direction de l'énergie) as responsible authority, Lausanne address.
- **Append to**: `config/domains/switzerland.yaml`, new canton Vaud section.

### 4. Bern — Wirtschafts-, Energie- und Umweltdirektion (WEU), energy directorate

- **name**: "Kanton Bern — Wirtschafts-, Energie- und Umweltdirektion (Energie)"
- **id**: `be_weu_energie`
- **base_url**: `https://www.weu.be.ch`
- **start_paths**: `["/de/start/themen/energie.html"]`
- **level**: subnational (canton)
- **access**: none
- **coverage**: region: `["eu_central", "switzerland", "bern"]`; category:
  `energy_ministry`; tags: `["waste_heat", "planning", "district_heating"]`;
  policy_types: `["guidance", "regulation"]`; language: `de`
- **format**: HTML
- **practical**: no published rate limit; department portal, moderate page count.
- **effort tier**: b (crawl domain)
- **why worth adding**: Revised cantonal Energiegesetz (in force since Jan 2023) and
  implementing Kantonale Energieverordnung (KEnV, BSG 741.111) — Bern is cited alongside
  Vaud/Thurgau as proposing that municipal energy plans explicitly account for
  data-center waste-heat potential. Companion legal text at
  `https://www.belex.sites.be.ch/app/de/texts_of_law/741.111` (KEnV) is a good follow-up
  crawl target once this ministry page is in.
- **verified**: yes. WebFetch confirmed page title "Energie" under WEU (Wirtschafts-,
  Energie- und Umweltdirektion), central energy-policy hub for the canton.
- **Append to**: `config/domains/switzerland.yaml`, new canton Bern section.

### 5. Rheinland-Pfalz — Ministerium für Wirtschaft, Tourismus, Energie und Klima (MWTEK)

- **name**: "Rheinland-Pfalz — Ministerium für Wirtschaft, Tourismus, Energie und Klima"
- **id**: `rlp_energy`
- **base_url**: `https://mwtek.rlp.de`
- **start_paths**: `["/themen/energie"]`
- **level**: subnational (Land)
- **access**: none
- **coverage**: region: `["eu", "eu_central", "germany", "rheinland_pfalz"]`; category:
  `energy_ministry`; tags: `["efficiency", "district_heating", "planning"]`;
  policy_types: `["regulation", "strategy"]`; language: `de`
- **format**: HTML
- **practical**: no rate limit published; recommend `rate_limit_seconds: 2.0` consistent
  with sibling Länder entries.
- **effort tier**: b (crawl domain)
- **why worth adding**: Completes German Länder coverage. RLP passed a state law
  implementing the federal Wärmeplanungsgesetz (municipal heat planning duty devolved to
  all Kreise/large cities). Note: the ministry was reorganized — the old
  "Ministerium für Klimaschutz, Umwelt, Energie und Mobilität" (mkuem.rlp.de) split;
  energy/climate moved to this new MWTEK ministry (environment/agriculture stayed at
  `mlwuf.rlp.de`, which does NOT cover energy — do not use that domain for this topic).
- **verified**: yes. WebFetch confirmed page title "Ministerium für Wirtschaft, Tourismus,
  Energie und Klima des Landes Rheinland-Pfalz" with an "Energieinfrastruktur" > "Wärmenetze"
  subsection and a "Wärmewende im Quartier" funding program.
- **Append to**: `config/domains/germany.yaml`.

### 6. Rheinland-Pfalz — Landesrecht (state law database)

- **name**: "Landesrecht Rheinland-Pfalz"
- **id**: `rlp_recht`
- **base_url**: `https://landesrecht.rlp.de`
- **start_paths**: `["/bsrp/"]`
- **level**: subnational (Land)
- **access**: none
- **coverage**: region: `["eu", "eu_central", "germany", "rheinland_pfalz"]`; category:
  `legislation`; tags: `["mandates"]`; policy_types: `["legislation"]`; language: `de`
- **format**: HTML (juris "Bürgerservice" portal)
- **practical**: `requires_playwright: true` recommended (juris portals are JS-driven,
  matches pattern of existing juris-hosted sibling entries e.g. hessen_recht).
- **effort tier**: b (crawl domain)
- **why worth adding**: Consolidated RLP state law and ordinances (juris-hosted, same
  platform pattern as the existing Hessenrecht/Bavaria entries already in config).
- **verified**: yes. WebFetch confirmed page title "Landesrecht Rheinland-Pfalz".
- **Append to**: `config/domains/germany.yaml`.

### 7. Brandenburg — Ministerium für Wirtschaft, Energie, Klimaschutz und Europa (MWEKE)

- **name**: "Brandenburg — Ministerium für Wirtschaft, Energie, Klimaschutz und Europa"
- **id**: `brandenburg_energy`
- **base_url**: `https://mweke.brandenburg.de`
- **start_paths**: `["/de/startseite/bb1.c.477963.de"]`
- **level**: subnational (Land)
- **access**: none
- **coverage**: region: `["eu", "eu_central", "germany", "brandenburg"]`; category:
  `energy_ministry`; tags: `["efficiency", "planning"]`; policy_types:
  `["regulation", "strategy"]`; language: `de`
- **format**: HTML
- **practical**: `rate_limit_seconds: 2.0` recommended.
- **effort tier**: b (crawl domain)
- **why worth adding**: Brandenburg has a dedicated Brandenburgische Wärmeplanungsverordnung
  (in force July 2024); Potsdam must file its heat plan by mid-2026. Note heat-planning
  oversight is actually split with the Ministry for Infrastructure and Regional Planning
  (MIL, `mil.brandenburg.de`) — MWEKE is the general energy/climate portfolio owner and the
  better long-term crawl root; consider adding `mil.brandenburg.de/mil/de/themen/
  querschnittsthemen/energie-und-klima/` as a follow-up if MWEKE proves thin on heat-plan
  specifics.
- **verified**: yes. WebFetch confirmed ministry name "Ministerium für Wirtschaft, Energie,
  Klimaschutz und Europa (MWEKE)" and that the page loads with live navigation/news.
- **Append to**: `config/domains/germany.yaml`.

### 8. Brandenburg — BRAVORS (state law database)

- **name**: "BRAVORS — Brandenburgisches Vorschriftensystem"
- **id**: `brandenburg_recht`
- **base_url**: `https://bravors.brandenburg.de`
- **start_paths**: `["/"]`
- **level**: subnational (Land)
- **access**: none
- **coverage**: region: `["eu", "eu_central", "germany", "brandenburg"]`; category:
  `legislation`; tags: `["mandates"]`; policy_types: `["legislation"]`; language: `de`
- **format**: HTML
- **practical**: free, no key; quick/advanced search plus chronological browse.
- **effort tier**: b (crawl domain)
- **why worth adding**: Official Brandenburg state law and regulation search (also
  indexes federal/EU documents for context).
- **verified**: yes. WebFetch confirmed title "Brandenburgisches Vorschriftensystem" with
  working quick-search / advanced-search / archive sections.
- **Append to**: `config/domains/germany.yaml`.

### 9. Sachsen-Anhalt — Ministerium für Wissenschaft, Energie, Klimaschutz und Umwelt (MWU)

- **name**: "Sachsen-Anhalt — Ministerium für Wissenschaft, Energie, Klimaschutz und Umwelt"
- **id**: `sachsen_anhalt_energy`
- **base_url**: `https://mwu.sachsen-anhalt.de`
- **start_paths**: `["/energie/kommunale-waermeplanung", "/energie"]`
- **level**: subnational (Land)
- **access**: none
- **coverage**: region: `["eu", "eu_central", "germany", "sachsen_anhalt"]`; category:
  `energy_ministry`; tags: `["district_heating", "planning", "efficiency"]`;
  policy_types: `["regulation", "strategy"]`; language: `de`
- **format**: HTML
- **practical**: `rate_limit_seconds: 2.0` recommended.
- **effort tier**: b (crawl domain)
- **why worth adding**: Direct ministry page dedicated to Sachsen-Anhalt's municipal
  heat-planning state law (cabinet-approved implementation of the federal WPG), with
  concrete deadlines (Magdeburg/Halle 2026, rest of state 2028) and ~12M EUR funding.
- **verified**: yes. WebFetch confirmed ministry name and page title "Kommunale
  Wärmeplanung – Fahrplan für das klimaneutrale Heizen", full policy detail captured.
- **Append to**: `config/domains/germany.yaml`.

### 10. Sachsen-Anhalt — Landesrecht (state law database)

- **name**: "Landesrecht Sachsen-Anhalt"
- **id**: `sachsen_anhalt_recht`
- **base_url**: `https://www.landesrecht.sachsen-anhalt.de`
- **start_paths**: `["/"]`
- **level**: subnational (Land)
- **access**: none
- **coverage**: region: `["eu", "eu_central", "germany", "sachsen_anhalt"]`; category:
  `legislation`; tags: `["mandates"]`; policy_types: `["legislation"]`; language: `de`
- **format**: HTML (juris portal)
- **practical**: `requires_playwright: true` recommended (juris platform pattern).
- **effort tier**: b (crawl domain)
- **why worth adding**: Consolidated Sachsen-Anhalt state law, same juris pattern as
  existing sibling Länder entries.
- **verified**: yes. WebFetch confirmed page title "Landesrecht Sachsen-Anhalt".
- **Append to**: `config/domains/germany.yaml`.

### 11. Schleswig-Holstein — Ministerium für Energiewende, Klimaschutz, Umwelt und Natur (MEKUN)

- **name**: "Schleswig-Holstein — Energiewende im Wärmesektor (MEKUN)"
- **id**: `schleswig_holstein_energy`
- **base_url**: `https://www.schleswig-holstein.de`
- **start_paths**: `["/DE/landesregierung/themen/energie/energiewende/Waerme"]`
- **level**: subnational (Land)
- **access**: none
- **coverage**: region: `["eu", "eu_central", "germany", "schleswig_holstein"]`;
  category: `energy_ministry`; tags: `["district_heating", "planning", "mandatory"]`;
  policy_types: `["regulation", "strategy"]`; language: `de`
- **format**: HTML
- **practical**: `rate_limit_seconds: 2.0` recommended.
- **effort tier**: b (crawl domain)
- **why worth adding**: State's Energiewende- und Klimaschutzgesetz (EWKG), amended
  March 2025, mandates heat planning for all 1,104 municipalities; the state co-runs
  the Wärmekompetenzzentrum Schleswig-Holstein (WKZ.SH, since March 2025) to support
  implementation — good ongoing source of guidance documents.
- **verified**: yes. WebFetch confirmed page title "Energiewende im Wärmesektor" under
  MEKUN, with EWKG amendment date and WKZ.SH details captured.
- **Append to**: `config/domains/germany.yaml`.

### 12. Schleswig-Holstein — Gesetze-Rechtsprechung (state law database)

- **name**: "Gesetze-Rechtsprechung Schleswig-Holstein"
- **id**: `schleswig_holstein_recht`
- **base_url**: `https://www.gesetze-rechtsprechung.sh.juris.de`
- **start_paths**: `["/bssh/"]`
- **level**: subnational (Land)
- **access**: none
- **coverage**: region: `["eu", "eu_central", "germany", "schleswig_holstein"]`;
  category: `legislation`; tags: `["mandates"]`; policy_types: `["legislation"]`;
  language: `de`
- **format**: HTML (juris portal)
- **practical**: `requires_playwright: true` recommended.
- **effort tier**: b (crawl domain)
- **why worth adding**: Over 1,400 consolidated state laws/ordinances including the
  EWKG referenced above.
- **verified**: yes. WebFetch confirmed page title "Gesetze-Rechtsprechung
  Schleswig-Holstein".
- **Append to**: `config/domains/germany.yaml`.

### 13. Saarland — Wärmewende-Portal (Ministerium für Wirtschaft, Innovation, Digitales und Energie, MWIDE)

- **name**: "Saarland — Wärmewende (MWIDE)"
- **id**: `saarland_energy`
- **base_url**: `https://www.saarland.de`
- **start_paths**: `["/mwide/DE/portale/waermewende/home"]`
- **level**: subnational (Land)
- **access**: none
- **coverage**: region: `["eu", "eu_central", "germany", "saarland"]`; category:
  `energy_ministry`; tags: `["district_heating", "planning", "waste_heat"]`;
  policy_types: `["regulation", "guidance"]`; language: `de`
- **format**: HTML
- **practical**: WebFetch (automated tool fetch) returned HTTP 403 (bot-blocked); page
  loads normally in a real browser — confirmed via live browser render. Crawler should
  set a realistic User-Agent / expect this site may need `requires_playwright: true`.
- **effort tier**: b (crawl domain)
- **why worth adding**: Dedicated Wärmewende advisory office (Beratungsstelle
  Wärmewende) plus a "Landesstudie Wärmewende im Saarland — Status quo, Potenziale und
  Handlungsfelder" report; includes a public Wärmekataster tool
  (`geoportal.saarland.de/article/Waermekataster/`) worth a follow-up crawl entry.
- **verified**: yes. WebFetch to this exact URL was blocked (403), but the page was
  loaded and its full text confirmed via the browser tool: title "Wärmewende Saarland",
  content on Landesstudie, Beratungsstelle contact (waermewende@wirtschaft.saarland.de),
  FAQ and funding sections all present.
- **Append to**: `config/domains/germany.yaml`.

### 14. Saarland — Landesrecht (state law database)

- **name**: "Bürgerservice Saarland (Landesrecht)"
- **id**: `saarland_recht`
- **base_url**: `https://recht.saarland.de`
- **start_paths**: `["/bssl/search"]`
- **level**: subnational (Land)
- **access**: none
- **coverage**: region: `["eu", "eu_central", "germany", "saarland"]`; category:
  `legislation`; tags: `["mandates"]`; policy_types: `["legislation"]`; language: `de`
- **format**: HTML (juris portal)
- **practical**: WebFetch reached the page (no error) and returned the correct portal
  title; `requires_playwright: true` recommended. Over 1,100 consolidated laws per juris
  product description.
- **effort tier**: b (crawl domain)
- **why worth adding**: Only Saarland state law source in the corpus; completes German
  Länder law-database coverage.
- **verified**: yes. WebFetch confirmed page title "Bürgerservice Saarland" (the juris
  citizen-service law-search portal, consistent with the branding juris uses across all
  16 Länder's public law search tools).
- **Append to**: `config/domains/germany.yaml`.

### 15. Mecklenburg-Vorpommern — Ministerium für Energie, Infrastruktur und Digitalisierung

- **name**: "Mecklenburg-Vorpommern — Ministerium für Energie, Infrastruktur und Digitalisierung"
- **id**: `mv_energy`
- **base_url**: `https://www.regierung-mv.de`
- **start_paths**: `["/Landesregierung/em/"]`
- **level**: subnational (Land)
- **access**: none
- **coverage**: region: `["eu", "eu_central", "germany", "mecklenburg_vorpommern"]`;
  category: `energy_ministry`; tags: `["efficiency", "planning"]`; policy_types:
  `["regulation", "strategy"]`; language: `de`
- **format**: HTML
- **practical**: `rate_limit_seconds: 2.0` recommended.
- **effort tier**: b (crawl domain)
- **why worth adding**: MV is implementing a state heat-planning ordinance (expected
  early 2025) adapted for rural/low-density heat-network economics — a different policy
  posture than the dense Länder already in config, useful contrast data. LEKA MV
  (state energy/climate agency, `leka-mv.de`) is a good follow-up crawl target.
- **verified**: yes. WebFetch confirmed ministry name "Ministerium für Energie,
  Infrastruktur und Digitalisierung" and that the page is a live government portal with
  an Energieportal MV sub-link.
- **Append to**: `config/domains/germany.yaml`.

### 16. Mecklenburg-Vorpommern — Landesrecht (state law database)

- **name**: "Landesrecht Mecklenburg-Vorpommern"
- **id**: `mv_recht`
- **base_url**: `https://www.landesrecht-mv.de`
- **start_paths**: `["/bsmv/search"]`
- **level**: subnational (Land)
- **access**: none
- **coverage**: region: `["eu", "eu_central", "germany", "mecklenburg_vorpommern"]`;
  category: `legislation`; tags: `["mandates"]`; policy_types: `["legislation"]`;
  language: `de`
- **format**: HTML (juris/LARIS portal)
- **practical**: `requires_playwright: true` recommended. Free read access.
- **effort tier**: b (crawl domain)
- **why worth adding**: Completes German Länder law-database coverage (LARIS —
  Landesrechtsinformationssystem M-V).
- **verified**: yes. WebFetch confirmed page title "Landesrecht Mecklenburg-Vorpommern".
- **Append to**: `config/domains/germany.yaml`.

### 17. Bremen — Wärmewende (Senatorin für Umwelt, Klima und Wissenschaft)

- **name**: "Bremen — Wärmewende im Land Bremen"
- **id**: `bremen_energy`
- **base_url**: `https://umwelt.bremen.de`
- **start_paths**: `["/klima/klima-energie/waermewende-2383782"]`
- **level**: subnational (Land/city-state)
- **access**: none
- **coverage**: region: `["eu", "eu_central", "germany", "bremen"]`; category:
  `energy_ministry`; tags: `["district_heating", "planning"]`; policy_types:
  `["strategy", "guidance"]`; language: `de`
- **format**: HTML
- **practical**: `rate_limit_seconds: 2.0` recommended.
- **effort tier**: b (crawl domain)
- **why worth adding**: Bremen's Klimaschutzstrategie 2038 and municipal heat-planning
  draft (published for public comment, large heat pumps at the Weser river and treatment
  plant projected to cover 36% of heat demand); city-state law requires heat plan by
  June 2026.
- **verified**: yes. WebFetch confirmed page title "Wärmewende im Land Bremen" with
  content on municipal heat planning strategy.
- **Append to**: `config/domains/germany.yaml`.

### 18. Bremen — Vorschriften (state law portal)

- **name**: "Bremische Vorschriften — Gesetzesportal"
- **id**: `bremen_recht`
- **base_url**: `https://www.transparenz.bremen.de`
- **start_paths**: `["/vorschriften-72741"]`
- **level**: subnational (Land/city-state)
- **access**: none
- **coverage**: region: `["eu", "eu_central", "germany", "bremen"]`; category:
  `legislation`; tags: `["mandates"]`; policy_types: `["legislation"]`; language: `de`
- **format**: HTML
- **practical**: hosted on Bremen's Transparenzportal (open-data/transparency portal,
  not a dedicated juris instance) — different platform shape than sibling Länder, worth
  noting for the crawler's parser assumptions.
- **effort tier**: b (crawl domain)
- **why worth adding**: Over 600 consolidated Bremen laws/ordinances; completes German
  Länder law coverage.
- **verified**: yes. WebFetch confirmed page title "Bremische Vorschriften -
  Gesetzesportal" listing recent legal provisions.
- **Append to**: `config/domains/germany.yaml`.

### 19. Thüringen — ThEGA Kommunale Wärmeplanung + Abwärmekataster

- **name**: "Thüringer Energie- und GreenTech-Agentur (ThEGA) — Kommunale Wärmeplanung"
- **id**: `thueringen_thega`
- **base_url**: `https://www.thega.de`
- **start_paths**: `["/themen/klimafreundliche-waerme/kommunale-waermeplanung/"]`
- **level**: subnational (Land, state-mandated agency)
- **access**: none
- **coverage**: region: `["eu", "eu_central", "germany", "thueringen"]`; category:
  `program`; tags: `["district_heating", "waste_heat", "planning", "data_center_specific"]`;
  policy_types: `["guidance", "program"]`; language: `de`
- **format**: HTML
- **practical**: `rate_limit_seconds: 2.0` recommended; page links to numerous PDF
  presentations (workshops) that could be added as deep-crawl targets later.
- **effort tier**: b (crawl domain)
- **why worth adding**: ThEGA operates on behalf of the Thüringer Energieministerium and
  runs the state's Abwärmekataster (waste-heat cadastre in the Energieatlas Thüringen) —
  lets companies register waste-heat sources for reuse by third parties, directly
  relevant to the taxonomy. Also documents the Thüringer Wärmeplanungskostenerstattungs-
  verordnung (ThürWPKEVO). Chosen over the ministry's own site
  (`umwelt.thueringen.de`) because that domain is gated by a Link11 CAPTCHA challenge
  (see Unverified section).
- **verified**: yes. Full page text pulled via browser: confirmed Abwärmekataster
  description, ThürWPKEVO reference, Wärmenetze/Abwärmenutzung program links, ministry
  attribution ("im Auftrag des Thüringer Energieministeriums").
- **Append to**: `config/domains/germany.yaml`.

### 20. Thüringen — Landesrecht (state law database)

- **name**: "Landesrecht Thüringen (Bürgerservice)"
- **id**: `thueringen_recht`
- **base_url**: `https://landesrecht.thueringen.de`
- **start_paths**: `["/bsth/search"]`
- **level**: subnational (Land)
- **access**: none
- **coverage**: region: `["eu", "eu_central", "germany", "thueringen"]`; category:
  `legislation`; tags: `["mandates"]`; policy_types: `["legislation"]`; language: `de`
- **format**: HTML (juris portal)
- **practical**: `requires_playwright: true` recommended.
- **effort tier**: b (crawl domain)
- **why worth adding**: Completes German Länder law-database coverage (16 of 16 Länder
  will then have a law-search source once this and the other 7 above ship).
- **verified**: yes. Confirmed via browser load: page title "Bürgerservice Thüringen"
  (same juris citizen-service pattern independently confirmed for Saarland).
- **Append to**: `config/domains/germany.yaml`.

### 21. Austria — Klima- und Energiefonds (national incentive fund)

- **name**: "Klima- und Energiefonds Österreich — Förderungen"
- **id**: `at_klimafonds`
- **base_url**: `https://www.klimafonds.gv.at`
- **start_paths**: `["/foerderungen/"]`
- **level**: national
- **access**: none
- **coverage**: region: `["eu", "eu_central", "austria"]`; category: `economic_dev`;
  tags: `["incentives", "efficiency", "waste_heat"]`; policy_types: `["incentive"]`;
  language: `de`
- **format**: HTML
- **practical**: `rate_limit_seconds: 2.0` recommended; funding calls rotate/expire, so a
  moderate re-crawl cadence (weekly/monthly) is appropriate.
- **effort tier**: b (crawl domain)
- **why worth adding**: Austria's national climate/energy fund runs recurring grant
  programs directly on-topic (e.g. "Betriebliche Niedertemperaturwärme und -kälte" —
  15M EUR; large heat/cold storage systems — 75M EUR) — this is the national incentive
  counterpart to the existing bmk.gv.at (regulation) and ris.bka.gv.at (law) entries.
- **verified**: yes. WebFetch confirmed page title "Förderungen – Klima- und
  Energiefonds" with a live list of 10 active funding programs.
- **Append to**: `config/domains/austria.yaml`.

### 22. Austria — Vienna MA20 Energieplanung (subnational, Austria's largest DC hub)

- **name**: "Wien — Energieplanung (MA 20)"
- **id**: `at_wien_ma20`
- **base_url**: `https://www.wien.gv.at`
- **start_paths**: `["/kontakt/ma20-publikationen"]`
- **level**: subnational (Bundesland/city, Vienna is its own Bundesland)
- **access**: none
- **coverage**: region: `["eu", "eu_central", "austria", "wien"]`; category:
  `district_heating`; tags: `["district_heating", "waste_heat", "data_center_specific",
  "planning"]`; policy_types: `["guidance", "report"]`; language: `de`
- **format**: HTML + PDF (linked brochures/studies)
- **practical**: `rate_limit_seconds: 2.0`; note `wien.gv.at` intermittently returns a
  "Server Fehler" page for some deep-link paths (observed on
  `/kontakte/ma20/energieraumplanung.html`) — the publications index path above was
  confirmed stable.
- **effort tier**: b (crawl domain)
- **why worth adding**: Vienna is Austria's primary data-center market (Digital Realty's
  Floridsdorf facility already feeds waste heat via a 3 MW heat-pump system into district
  heating for a hospital; Vienna's EU AI Gigafactory bid explicitly proposed feeding
  server waste heat into district heating for ~200,000 households) and MA20 is the city
  authority producing the Wiener Wärmeplan 2040 and related energy-spatial-planning
  guidance. First subnational Austrian entry in the corpus.
- **verified**: yes. Browser-loaded page text confirmed title "Broschüren, Berichte,
  Studien der Energieplanung - Stadt Wien" with live publication links (Energie in
  Zahlen, Wärmepumpen-Leitfaden, etc.). The companion Wiener Wärmeplan 2040 PDF at
  `wien.gv.at/pdf/ma20/wwp-a3-web-l11.pdf` was also fetched successfully (9.8MB live
  PDF, confirms the document exists at that path) though its content wasn't
  machine-readable in this pass — worth adding as a `start_paths` entry alongside the
  publications index.

---

## Unverified / needs-human-check

- **Thüringen Ministry direct site** — `https://umwelt.thueringen.de/themen/energie/
  waermeplanung` (Thüringer Ministerium für Umwelt, Energie, Naturschutz und Forsten).
  Blocked by a Link11 bot-protection CAPTCHA on every fetch attempt (both WebFetch and a
  real browser session hit the challenge page). The ThEGA entry above (#19) covers the
  same policy content as a working substitute; a human with a real browser session could
  likely pass the CAPTCHA once and confirm this domain for future automated access, but
  it should not be crawled automatously without solving that first.
- **Austria E-Control** (`https://www.e-control.at`) — national electricity/gas
  regulator. Investigated because Fernwärme price-transparency data (waermepreise.at) now
  flows to E-Control under a 2023 EAG amendment, but E-Control's own site scope is
  explicitly electricity + gas; no district-heating/waste-heat regulation content was
  found on the site itself. Not included as a verified candidate — flagging in case a
  future Fernwärme-transparency mandate gives E-Control direct regulatory content.
- **Brandenburg MIL** (`https://mil.brandenburg.de/mil/de/themen/querschnittsthemen/
  energie-und-klima/`) — Ministry for Infrastructure and Regional Planning, which
  co-owns Brandenburg's heat-planning ordinance alongside MWEKE (added as #7). Not
  independently verified in this pass; worth adding if MWEKE's heat-plan coverage proves
  thin.
- **LEKA MV** (`https://www.leka-mv.de`) — Mecklenburg-Vorpommern's state energy/climate
  agency, analogous to ThEGA (#19) and Saarland's Wärmewende advisory office. Referenced
  by search results but not independently fetched/verified in this pass.
- **Saarland Wärmekataster tool** (`https://geoportal.saarland.de/article/
  Waermekataster/`) — geospatial heat-demand tool referenced from the Saarland ministry
  page (#13); not independently fetched/verified.

---

## Summary of what's now covered vs. still missing after this batch

After appending the 22 verified candidates above:
- **Germany**: all 16 Länder have at least a ministry/heat-planning source and a
  Landesrecht (state law) source (8 pre-existing + 8 new in this batch).
- **Austria**: national coverage (ministry, federal law, incentive fund) plus one
  subnational entry (Vienna). 8 of 9 Austrian Bundesländer (all but Vienna) remain
  uncovered — a good target for a future pass if OCP wants deeper Austrian subnational
  coverage, though Vienna is disproportionately the relevant DC hub.
- **Switzerland**: federal + 5 cantons now covered (Zürich pre-existing; Geneva, Bern,
  Basel-Stadt, Vaud new). ~21 other cantons remain uncovered; Geneva/Bern/Basel/Vaud/
  Zürich together cover Switzerland's largest population and economic centers.
