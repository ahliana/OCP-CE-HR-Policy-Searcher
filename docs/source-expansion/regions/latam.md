# Source Expansion Research - Latin America

Researcher scope: Chile, Colombia, Argentina, Peru, Uruguay, Costa Rica (Brazil/Mexico
already shipped in `config/domains/brazil.yaml` / `mexico.yaml` - read and deduped
against, no overlapping `base_url`s found). Checked against `config/domains/api_sources.yaml`
too - no existing LatAm structured API clients.

All entries below are proposals only. `enabled: false` in any draft YAML. No client
code written, nothing added to a live scan.

---

## Verified candidates (ranked best-first)

### 1. LeyChile / BCN Legislative Web Service (Chile) - structured API, tier C

- **name**: "Ley Chile Web Service (Biblioteca del Congreso Nacional)"
- **proposed id**: `leychile_api`
- **base_url**: `https://www.leychile.cl`
- **source_type feasibility**: no existing client fits. Needs a **new** structured
  client (tier c). Endpoint shape: `GET /Consulta/obtxml?opt=7&idLey=<id>` (also
  accepts `idNorma`) returns the full norm as XML with promulgation/publication
  dates, issuing body, and full consolidated text (always the current in-force
  version, footnoted for amendments). Docs page:
  `https://www.leychile.cl/Consulta/legislacion_abierta_web_service` (also mirrored
  at `https://www.bcn.cl/leychile/consulta/legislacion_abierta_web_service`); a
  fuller spec PDF is at `https://www.leychile.cl/esquemas/accesoLeyesChilenas4.pdf`.
- **level**: national
- **access**: none - fully open, no API key, no auth.
- **coverage**: Chile's entire consolidated law/regulation corpus (`Ley`, `Decreto`,
  `Resolución`, etc.), including energy efficiency law (Ley 21.305), the 2050 energy
  policy framework, decarbonization decrees, and green hydrogen/renewables rules.
  `region: ["south_america", "chile"]`, `category: "legislative"`,
  `tags: ["mandates", "efficiency", "reporting"]`, `policy_types: ["law", "regulation"]`.
- **language**: es
- **format**: XML
- **practical**: no documented rate limit found; be conservative (this doc used
  ~3s between calls without issue). No robots.txt block observed on `leychile.cl`.
  Update frequency: continuous (BCN maintains it as the canonical consolidated-text
  source). One outbound request during verification got a transient 429 - throttle
  client-side.
- **effort tier**: (c) new structured client - would need an ID discovery strategy
  (BCN also exposes a search UI at `leychile.cl/Navegar`) since the API takes a known
  `idLey`/`idNorma`, not a keyword-search endpoint by itself.
- **why worth adding**: only genuine open-data legislative API found across all six
  countries in scope; gives full-text, always-current Chilean law text in structured
  XML rather than crawled HTML/PDF.
- **verified**: yes. Fetched
  `https://www.leychile.cl/Consulta/obtxml?opt=7&idLey=18575` directly - returned a
  well-formed `<Norma>` XML document with real legislative metadata and text.

---

### 2. Ministerio de Energía (Chile) - crawl domain, tier B

- **name**: "Ministerio de Energía - Chile"
- **proposed id**: `energia_cl`
- **base_url**: `https://energia.gob.cl`
- **start_paths**: `/mini-sitio/reglamentos`, `/eficienciaenergetica`,
  `/panel/plan-de-descarbonizacion`
- **level**: national
- **access**: none
- **coverage**: national energy policy to 2050, decarbonization plan, Energy
  Efficiency Law (Ley 21.305) implementation, green hydrogen strategy, open energy
  data portal (`energiaabierta.cl`, separate domain - not included here).
  `region: ["south_america", "chile"]`, `category: "energy_ministry"`,
  `tags: ["efficiency", "renewable_energy", "planning"]`,
  `policy_types: ["regulation", "strategy", "law"]`.
- **language**: es
- **format**: HTML/PDF
- **practical**: standard gov.cl site, no visible robots block on checked paths;
  moderate JS use on some panels - `requires_playwright` recommended `true` for the
  `/panel/*` decarbonization pages, `false` should suffice for `/eficienciaenergetica`.
- **effort tier**: (b) plain crawl domain
- **why worth adding**: primary national energy policy body for Chile, currently the
  largest LatAm data-center market by MW under construction.
- **verified**: yes. Fetched root - confirmed ministry site with the regulation,
  efficiency, and decarbonization sections listed above.

---

### 3. Comisión Nacional de Energía - CNE (Chile) - crawl domain, tier B

- **name**: "CNE - Comisión Nacional de Energía (Chile)"
- **proposed id**: `cne_cl`
- **base_url**: `https://www.cne.cl`
- **start_paths**: `/normativas`, `/estadisticas`
- **level**: national
- **access**: none
- **coverage**: electricity and hydrocarbon sector technical regulation portal
  ("Portal Normativo"), tariff-setting resolutions, and public consultation
  processes. Site coverage explicitly discusses data-center driven grid demand
  growth. `region: ["south_america", "chile"]`, `category: "regulatory"`,
  `tags: ["mandates", "reporting"]`, `policy_types: ["regulation", "report"]`.
- **language**: es
- **format**: HTML/PDF
- **practical**: standard gov.cl-family site; no key/login.
- **effort tier**: (b)
- **why worth adding**: Chile's electricity/hydrocarbon regulator; publishes the
  technical normativa that would carry any future DC-specific grid or efficiency
  rules, and already covers DC electricity-demand policy discussion.
- **verified**: yes. Fetched root - confirmed "Normativas"/"Portal Normativo" and
  statistics sections, plus a news item on data-center grid impact.

---

### 4. Superintendencia de Electricidad y Combustibles - SEC (Chile) - crawl domain, tier B

- **name**: "SEC - Superintendencia de Electricidad y Combustibles (Chile)"
- **proposed id**: `sec_cl`
- **base_url**: `https://www.sec.cl`
- **start_paths**: `/transparencia/marconormativo.html`
- **level**: national
- **access**: none
- **coverage**: electrical installation safety regulations (e.g. Decreto 08),
  technical pliegos (RPTD series), NCh Elec. 4/2003 low-voltage standard - the
  binding technical standards layer under CNE/Energy Ministry policy.
  `region: ["south_america", "chile"]`, `category: "standards"`,
  `tags: ["mandates"]`, `policy_types: ["standard", "regulation"]`.
- **language**: es
- **format**: HTML/PDF
- **practical**: homepage itself is mostly citizen-services framed (complaints,
  installer lookup) - the regulatory content lives under `/transparencia/` and
  `/sitio-web/wp-content/uploads/...pdf`. Confirmed via search, not homepage crawl,
  so set `max_depth` >= 2 and do not rely on homepage links alone.
- **effort tier**: (b)
- **why worth adding**: Chile's electrical-standards enforcer; lower priority than
  CNE/Energy Ministry but fills the technical-standard tier.
- **verified**: yes, but indirectly. Homepage fetch showed only citizen-service
  framing; targeted search confirmed `sec.cl/transparencia/marconormativo.html` and
  several live regulation/standard PDFs under `sec.cl`. Recommend a human confirm
  crawl depth catches these before enabling.

---

### 5. Ministerio de Minas y Energía (Colombia) - crawl domain, tier B

- **name**: "Ministerio de Minas y Energía - Colombia"
- **proposed id**: `minenergia_co`
- **base_url**: `https://www.minenergia.gov.co`
- **start_paths**: `/es/normatividad/consulta-normativa`, `/es/eficiencia-energetica`
- **level**: national
- **access**: none
- **coverage**: FENOGE (efficient-use/renewables fund), FNCER non-conventional
  renewables policy, energy efficiency programs, "Repositorio Normativo" and
  regulatory-agenda tracker. `region: ["south_america", "colombia"]`,
  `category: "energy_ministry"`, `tags: ["efficiency", "incentives", "mandates"]`,
  `policy_types: ["regulation", "strategy", "incentive"]`.
- **language**: es
- **format**: HTML/PDF
- **practical**: standard gov.co site, no key/login.
- **effort tier**: (b)
- **why worth adding**: national energy ministry for Colombia, a fast-growing LatAm
  DC market (Bogotá metro); FENOGE/FNCER funds are directly incentive-relevant.
- **verified**: yes. Fetched root - confirmed normativa, efficiency, and FENOGE/FNCER
  sections.

---

### 6. UPME - Unidad de Planeación Minero Energética (Colombia) - crawl domain, tier B

- **name**: "UPME - Unidad de Planeación Minero Energética (Colombia)"
- **proposed id**: `upme_co`
- **base_url**: `https://www1.upme.gov.co`
- **start_paths**: `/DemandaEnergetica`, `/Paginas/PROURE.aspx`
- **level**: national
- **access**: none
- **coverage**: National Energy Plan (PEN 2025-2055), PROURE rational/efficient
  energy-use program action plans, generation/demand statistics via SIMEC.
  `region: ["south_america", "colombia"]`, `category: "energy_ministry"`,
  `tags: ["efficiency", "planning", "research"]`,
  `policy_types: ["strategy", "report", "program"]`.
- **language**: es
- **format**: HTML/PDF
- **practical**: note the live host redirected `www.upme.gov.co` to `www1.upme.gov.co`
  in testing - use the `www1` host as `base_url`.
- **effort tier**: (b)
- **why worth adding**: Colombia's energy planning body; PROURE is the direct
  efficiency-mandate analogue to Brazil's PROCEL already in `brazil.yaml`.
- **verified**: yes. Fetched root - confirmed PEN, PROURE, and SIMEC content.

---

### 7. CREG - Comisión de Regulación de Energía y Gas (Colombia) - crawl domain, tier B

- **name**: "CREG - Comisión de Regulación de Energía y Gas (Colombia)"
- **proposed id**: `creg_co`
- **base_url**: `https://www.creg.gov.co`
- **start_paths**: `/gestor-normativo`
- **level**: national
- **access**: none
- **coverage**: electricity/gas resolutions, draft resolutions, administrative
  circulars via "Gestor Normativo". `region: ["south_america", "colombia"]`,
  `category: "regulatory"`, `tags: ["mandates", "reporting"]`,
  `policy_types: ["regulation"]`.
- **language**: es
- **format**: HTML/PDF
- **practical**: standard gov.co site, no key/login.
- **effort tier**: (b)
- **why worth adding**: Colombia's electricity/gas regulator - resolutions are the
  binding-rule layer under MinEnergia/UPME policy.
- **verified**: yes. Fetched root - confirmed "Gestor normativo" with resolutions,
  draft resolutions, and circulars.

---

### 8. Secretaría de Energía (Argentina) - crawl domain, tier B

- **name**: "Secretaría de Energía - Argentina"
- **proposed id**: `energia_ar`
- **base_url**: `https://www.argentina.gob.ar`
- **start_paths**: `/economia/energia`
- **level**: national
- **access**: none
- **coverage**: national energy policy design, energy-efficiency subsecretariat,
  targeted energy subsidy scheme (SEF), Federal Energy Council, energy statistics
  portal. `region: ["south_america", "argentina"]`, `category: "energy_ministry"`,
  `tags: ["efficiency", "incentives", "planning"]`,
  `policy_types: ["regulation", "strategy", "incentive"]`.
- **language**: es
- **format**: HTML/PDF
- **practical**: standard argentina.gob.ar site, no key/login. Note `base_url` is
  the shared `argentina.gob.ar` portal (same pattern as `enre_ar` below) - use
  `allowed_path_patterns: ["/economia/energia/*"]` to keep the crawl scoped.
- **effort tier**: (b)
- **why worth adding**: national energy ministry for Argentina.
- **verified**: yes. Fetched `/economia/energia` - confirmed policy/program content.

---

### 9. ENRE - Ente Nacional Regulador de la Electricidad (Argentina) - crawl domain, tier B

- **name**: "ENRE - Ente Nacional Regulador de la Electricidad (Argentina)"
- **proposed id**: `enre_ar`
- **base_url**: `https://www.argentina.gob.ar`
- **start_paths**: `/enre`
- **level**: national
- **access**: none
- **coverage**: national electricity-sector regulator - tariffs, service-quality
  and technical regulation. `region: ["south_america", "argentina"]`,
  `category: "regulatory"`, `tags: ["mandates", "reporting"]`,
  `policy_types: ["regulation"]`.
- **language**: es
- **format**: HTML/PDF
- **practical**: `allowed_path_patterns: ["/enre/*"]` to keep the crawl scoped to
  this sub-site of the shared argentina.gob.ar portal.
- **effort tier**: (b)
- **why worth adding**: Argentina's electricity regulator - the binding-rule
  counterpart to the Secretaría de Energía's policy above.
- **verified**: yes. Fetched `/enre` - confirmed electricity/regulation content.

---

### 10. MINEM - Ministerio de Energía y Minas (Peru) - crawl domain, tier B

- **name**: "MINEM - Ministerio de Energía y Minas (Peru)"
- **proposed id**: `minem_pe`
- **base_url**: `https://www.gob.pe`
- **start_paths**: `/minem`
- **level**: national
- **access**: none
- **coverage**: national energy/mining ministry - energy policy, efficiency,
  regulation. `region: ["south_america", "peru"]`, `category: "energy_ministry"`,
  `tags: ["efficiency", "planning"]`, `policy_types: ["regulation", "strategy"]`.
- **language**: es
- **format**: HTML/PDF
- **practical**: gob.pe is Peru's unified government portal - `allowed_path_patterns:
  ["/minem/*"]`. The site returns a bot-detection "418" response to some
  fetch-tool user agents; a standard browser UA resolves fine (confirmed 200,
  content contains "energia"/"eficiencia" keywords). Recommend `requires_playwright:
  true` or a browser-like User-Agent header for the crawler.
- **effort tier**: (b)
- **why worth adding**: Peru's national energy ministry, another growing Lima-area
  DC market.
- **verified**: yes. `curl` with a browser User-Agent returned HTTP 200 and page
  text containing "Eficiencia"/"energia" terms (AI-fetch tool was blocked by
  bot-detection; raw fetch confirms the site and content are real).

---

### 11. OSINERGMIN (Peru) - crawl domain, tier B

- **name**: "OSINERGMIN - Organismo Supervisor de la Inversión en Energía y Minería (Peru)"
- **proposed id**: `osinergmin_pe`
- **base_url**: `https://www.gob.pe`
- **start_paths**: `/osinergmin`
- **level**: national
- **access**: none
- **coverage**: electricity/energy/mining regulator - resolutions, tariffs, technical
  supervision. `region: ["south_america", "peru"]`, `category: "regulatory"`,
  `tags: ["mandates", "reporting"]`, `policy_types: ["regulation"]`.
- **language**: es
- **format**: HTML/PDF
- **practical**: same gob.pe caveats as MINEM above - scope with
  `allowed_path_patterns: ["/osinergmin/*"]`, use a browser UA / `requires_playwright:
  true`.
- **effort tier**: (b)
- **why worth adding**: Peru's electricity/energy regulator.
- **verified**: yes. `curl` with a browser User-Agent returned HTTP 200 and page
  text containing "electricidad"/"energia"/"regulacion" terms.

---

### 12. MIEM - Ministerio de Industria, Energía y Minería (Uruguay) - crawl domain, tier B

- **name**: "MIEM - Ministerio de Industria, Energía y Minería (Uruguay)"
- **proposed id**: `miem_uy`
- **base_url**: `https://www.gub.uy`
- **start_paths**: `/ministerio-industria-energia-mineria`
- **level**: national
- **access**: none
- **coverage**: national energy policy, energy-efficiency certificate program,
  Energy Sector Fund (research/innovation grants), open-data observatory.
  `region: ["south_america", "uruguay"]`, `category: "energy_ministry"`,
  `tags: ["efficiency", "incentives", "research"]`,
  `policy_types: ["regulation", "strategy", "incentive"]`.
- **language**: es
- **format**: HTML/PDF
- **practical**: gub.uy is Uruguay's unified government portal - scope with
  `allowed_path_patterns: ["/ministerio-industria-energia-mineria/*"]`.
- **effort tier**: (b)
- **why worth adding**: Uruguay's national energy ministry; energy-efficiency
  certificate scheme is directly on-taxonomy. Uruguay is a smaller but notably
  100%-renewable-grid DC pitch market.
- **verified**: yes. `curl` confirmed HTTP 200 and page text with 262 occurrences of
  "energia" plus "Eficiencia"/"Normativa" terms.

---

### 13. URSEA - Unidad Reguladora de Servicios de Energía y Agua (Uruguay) - crawl domain, tier B

- **name**: "URSEA - Unidad Reguladora de Servicios de Energía y Agua (Uruguay)"
- **proposed id**: `ursea_uy`
- **base_url**: `https://www.gub.uy`
- **start_paths**: `/unidad-reguladora-servicios-energia-agua`
- **level**: national
- **access**: none
- **coverage**: electricity/gas/water/fuel regulator - technical regulation,
  licensing, efficiency oversight. `region: ["south_america", "uruguay"]`,
  `category: "regulatory"`, `tags: ["mandates", "efficiency", "reporting"]`,
  `policy_types: ["regulation"]`.
- **language**: es
- **format**: HTML/PDF
- **practical**: scope with `allowed_path_patterns:
  ["/unidad-reguladora-servicios-energia-agua/*"]`.
- **effort tier**: (b)
- **why worth adding**: Uruguay's energy-services regulator.
- **verified**: yes. `curl` confirmed HTTP 200 and page text with 263 occurrences of
  "energia" plus "Eficiencia"/"Normativa" terms.

---

### 14. ARESEP (Costa Rica) - crawl domain, tier B

- **name**: "ARESEP - Autoridad Reguladora de los Servicios Públicos (Costa Rica)"
- **proposed id**: `aresep_cr`
- **base_url**: `https://aresep.go.cr`
- **start_paths**: `/` (site's regulation content is linked from the homepage;
  no deeper stable path confirmed - recommend a human pick specific sub-paths from
  the homepage nav before enabling)
- **level**: national
- **access**: none
- **coverage**: electricity tariff-setting and service-quality regulation for Costa
  Rica. `region: ["north_america", "central_america", "costa_rica"]`,
  `category: "regulatory"`, `tags: ["mandates", "reporting"]`,
  `policy_types: ["regulation"]`.
- **language**: es
- **format**: HTML/PDF
- **practical**: no key/login; standard `.go.cr` site.
- **effort tier**: (b)
- **why worth adding**: Costa Rica's electricity regulator - relevant given Costa
  Rica's near-100%-renewable grid is an active DC marketing angle.
- **verified**: yes. `curl` confirmed HTTP 200 and page text containing 17
  occurrences of "electricidad" plus "normativa"/"energia" terms.

---

### 15. SUIN-Juriscol (Colombia) - crawl domain / legislation portal, tier B

- **name**: "SUIN-Juriscol - Sistema Único de Información Normativa (Colombia)"
- **proposed id**: `suin_juriscol_co`
- **base_url**: `https://www.suin-juriscol.gov.co`
- **start_paths**: `/`
- **level**: national
- **access**: none
- **coverage**: Colombia's unified consolidated-legislation search system (laws,
  decrees, all sectors) - not energy-specific, but the authoritative full-text
  source for Colombian legislation, useful for pulling energy/efficiency laws
  found via keyword search. `region: ["south_america", "colombia"]`,
  `category: "legislative"`, `tags: ["mandates"]`,
  `policy_types: ["law", "regulation"]`.
- **language**: es
- **format**: HTML/PDF
- **practical**: no key/login; a self-signed/incomplete TLS chain was encountered
  by one fetch tool (`curl -k` succeeded, standard requests library should verify
  fine against most default CA bundles - worth a connectivity check before
  enabling). No public JSON/XML API discovered (unlike LeyChile) - crawl only.
- **effort tier**: (b)
- **why worth adding**: broad legislative coverage complement to the energy-specific
  ministry/regulator sites; needed since Colombia has no LeyChile-equivalent open
  API.
- **verified**: yes. `curl` confirmed HTTP 200 and page text containing
  "Normativa"/"legislacion" terms (38 and 26 occurrences respectively).

---

### 16. InfoLEG (Argentina) - crawl domain / legislation portal, tier B

- **name**: "InfoLEG - Información Legislativa y Documental (Argentina)"
- **proposed id**: `infoleg_ar`
- **base_url**: `https://www.infoleg.gob.ar`
- **start_paths**: `/`
- **level**: national
- **access**: none
- **coverage**: Argentina's national legislative/documentary database (Ministry of
  Justice) - laws, decrees, resolutions, Official Bulletin entries across all
  sectors, Creative Commons licensed. `region: ["south_america", "argentina"]`,
  `category: "legislative"`, `tags: ["mandates"]`,
  `policy_types: ["law", "regulation"]`.
- **language**: es
- **format**: HTML/PDF
- **practical**: no key/login. Searched for a documented JSON/XML API (there is a
  `servicios.infoleg.gob.ar` service subdomain referenced in search results, e.g.
  `servicios.infoleg.gob.ar/infolegInternet/verNorma.do?id=<n>`) but found no
  published API documentation or stable query contract - treat as crawl-only
  (tier b), not a structured API candidate, unless a human finds developer docs.
- **effort tier**: (b)
- **why worth adding**: broad legislative coverage complement to the Secretaría de
  Energía/ENRE sites above, same role as SUIN-Juriscol for Colombia.
- **verified**: yes. Fetched root over HTTPS with a browser User-Agent - HTTP 200,
  confirmed legislative-database content ("Normativa", norm-type/number search,
  Official Bulletin search).

---

## Unverified / needs-human-check

### Dirección de Energía / MINAE (Costa Rica)

- **candidate name**: "Dirección de Energía - MINAE (Costa Rica)"
- **candidate base_url**: `https://energia.minae.go.cr` (main ministry site
  `https://www.minae.go.cr` also considered)
- **why unverified**: both `www.minae.go.cr` and `energia.minae.go.cr` failed to
  resolve/load from this environment - `www.minae.go.cr` returned HTTP 403 on every
  attempt (curl and WebFetch, with and without a browser User-Agent), and
  `energia.minae.go.cr` failed DNS resolution (`ENOTFOUND` / `curl` exit 6).
  Web search independently confirms the site exists and is Costa Rica's energy
  policy directorate, with a "Marco legal sobre energía" (legal framework) page at
  `energia.minae.go.cr/?page_id=1444` and references to Directriz 011-MINAE /
  Directriz 017 (public-sector energy-efficiency-plan mandates) - but none of this
  could be independently confirmed live from here.
- **coverage if real**: national energy policy ministry, energy-efficiency
  directives for public institutions - would be Costa Rica's equivalent to
  MIEM (Uruguay) / MINEM (Peru) above.
- **recommendation**: a human should try loading `https://energia.minae.go.cr/`
  and `https://www.minae.go.cr/` directly in a browser (possible Cloudflare
  bot-block or geo/IP-based restriction on this environment) before adding.

---

## Dedup notes

- Read `config/domains/brazil.yaml` (mme_br, aneel_br, epe_br, procel_br) and
  `config/domains/mexico.yaml` (sener_mx, conuee_mx) - no `base_url` overlap with
  any candidate above.
- Read `config/domains/api_sources.yaml` - no existing LatAm `source_type` clients;
  `leychile_api` above would be the first.
- No existing structured client fits the LeyChile XML shape (closest existing
  client is `eurlex_nim`, but that's directive-transposition-status specific, not
  a generic norm-fetch-by-ID service) - confirmed tier (c).
- Brazil/Mexico subnational: none proposed - no clearly net-new, on-topic state-level
  source surfaced during this pass; out of scope given the country-level sources
  above were not yet exhausted.
