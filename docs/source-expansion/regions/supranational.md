# Supranational / Intergovernmental + Global Multi-Country Platforms

Scope: IGOs, standards bodies, and global open-data/legislation API platforms whose
policy/standards drive data-center heat reuse across many jurisdictions. Dedup
checked against `config/domains/api_sources.yaml` and `config/domains/eu.yaml`
(and skimmed `apac.yaml`, `australia.yaml`) before drafting — no base_url overlap
found; EUR-Lex NIM tracker and the 9 existing structured API clients are untouched.

All entries below are proposals only. `enabled: false` in every draft block.

---

## Verified candidates (ranked best-first)

### 1. IEA 4E EDNA — Data Centre Energy Efficiency workstream
- **name**: "IEA 4E EDNA - Data Centre Energy Efficiency"
- **id**: `iea_4e_edna_datacentres`
- **base_url**: `https://www.iea-4e.org`
- **level**: supranational (IEA Technology Collaboration Programme, multi-country)
- **access**: none (open, no key)
- **format**: HTML + PDF reports
- **effort tier**: (b) plain crawl domain
- **coverage**: region: `["supranational", "global"]`, category: `standards`,
  tags: `["efficiency", "research", "reporting"]`, policy_types: `["report", "guidance"]`,
  language: `en`
- **start_paths** (proposed): `/edna/`, `/edna/tasks/energy-efficiency-of-data-centres/`,
  `/edna/news/`
- **practical**: no robots.txt blocker observed; static HTML, low rate-limit risk;
  reports (liquid cooling, labeling schemes, policy reviews, public data collection)
  published a few times a year.
- **why worth adding**: This is the IEA's own dedicated data-center energy-efficiency
  policy workstream — the closest supranational match to this project's exact
  subject. Directly names data-center energy labeling schemes, policy reviews, and
  a "Total Energy Model" for connected devices/data centers.
- **verified**: yes. Fetched `/edna/tasks/energy-efficiency-of-data-centres/` — loads,
  discusses 2025/2026 IEA data-center policy reports (labeling schemes, public data
  collection, policy reviews, flexibility analysis). Confirmed on-topic and current.
- **append to**: new file `config/domains/supranational.yaml` (not eu.yaml — this is
  a global IGO program, not EU-specific).

### 2. CEN/CENELEC/ETSI Joint Coordination Group on Green Data Centres
- **name**: "CEN-CENELEC-ETSI Green Data Centres Coordination Group"
- **id**: `cencenelec_green_datacentres`
- **base_url**: `https://www.cencenelec.eu`
- **level**: supranational (joint European Standards Organisations activity — CEN,
  CENELEC, and ETSI together; this is the body that produces the EN 50600 series)
- **access**: none (page + brochures are free; full EN 50600 standard texts are
  paywalled through national standards bodies, same caveat as ISO below)
- **format**: HTML + PDF
- **effort tier**: (b) plain crawl domain
- **coverage**: region: `["eu", "supranational"]`, category: `standards`,
  tags: `["efficiency", "research"]`, policy_types: `["standard", "guidance", "report"]`,
  language: `en`
- **start_paths** (proposed):
  `/areas-of-work/cenelec-sectors/digital-society-cenelec/green-data-centres/`
- **practical**: static page, no auth; annual "Review of standardisation activities —
  Energy Management and Environmental Viability of Data Centres" brochure (edition
  11, 2024, is the current one) is a free PDF cataloguing the full EN 50600 KPI
  series (PUE, ERF, CUE, WUE, etc.) and in-preparation standards.
- **why worth adding**: This is the actual joint-ESO body behind EN 50600 (called
  out by name in the brief). One page indexes the entire European data-center
  standardization landscape and its free summary brochures.
- **verified**: yes. Fetched the URL above directly (note: the older
  `/standards/sectors/ict/pages/greendatacentres` and
  `/areas-of-work/cen-sectors/digital-society/green-data-centres/` paths both
  404 — CEN-CENELEC restructured their sector URLs; use the `cenelec-sectors`
  path above). Page loads, describes the CEN/CLC/ETSI CG GDC group and links the
  2024 standardization-review brochure.
- **append to**: `config/domains/eu.yaml` (this is EU/European-standards specific,
  unlike the global entries below).

### 3. Euroheat & Power — Knowledge Hub
- **name**: "Euroheat & Power Knowledge Hub"
- **id**: `euroheat_power_knowledge_hub`
- **base_url**: `https://www.euroheat.org`
- **level**: supranational (international district heating & cooling association,
  members across ~30 European + non-European countries)
- **access**: none
- **format**: HTML (some content gated behind membership/newsletter prompts, but
  articles render without login)
- **effort tier**: (b) plain crawl domain
- **coverage**: region: `["eu", "supranational"]`, category: `district_heating`,
  tags: `["efficiency", "research", "planning"]`,
  policy_types: `["report", "guidance"]`, language: `en`
- **start_paths** (proposed): `/knowledge-hub/`, `/dhc/knowledge-hub/`
- **practical**: no auth wall on content itself; rate-limit politely (2-3s) — page
  invites membership signup but doesn't block reading.
- **why worth adding**: Euroheat & Power's Knowledge Hub is the best single
  aggregator of data-center-waste-heat-to-district-heating case studies found in
  this pass — e.g. a named comparative analysis of DC waste-heat scenarios for DH
  networks, and country-specific case studies (Amsterdam, Braunschweig).
- **verified**: yes. Fetched
  `/dhc/knowledge-hub/comparative-analysis-of-scenarios-of-data-center-waste-heat-utilization-for-district-heating-networks-of-different-generations`
  — loads (published 2025-05-26), directly on-topic (data center waste heat +
  district heating).
- **append to**: `config/domains/eu.yaml` (membership skews European, though the
  association describes itself as international).

### 4. Energy Community Secretariat — Legal Acquis (Energy Efficiency)
- **name**: "Energy Community Secretariat - Acquis (Energy Efficiency)"
- **id**: `energy_community_acquis`
- **base_url**: `https://www.energy-community.org`
- **level**: supranational (treaty body extending the EU energy acquis, incl. the
  Energy Efficiency Directive, to the Western Balkans, Ukraine, Moldova, Georgia)
- **access**: none (site is Cloudflare-protected — passed the bot-check via a real
  browser session but returned 403 to a plain HTTP fetch; scanner will need
  `requires_playwright: true` and may still need to solve a JS challenge)
- **format**: HTML + PDF
- **effort tier**: (b) plain crawl domain
- **coverage**: region: `["eu", "balkans", "supranational"]`, category: `legislative`,
  tags: `["mandates", "efficiency"]`, policy_types: `["directive", "law", "report"]`,
  language: `en`
- **start_paths** (proposed): `/enc-lex/law/acquis.html`,
  `/enc-lex/law/acquis/energy-efficiency.html` (unconfirmed sub-path — verify exact
  slug when crawler is built; the acquis page lists an "Energy efficiency" category
  link but I did not click through to confirm its exact URL)
- **practical**: Cloudflare "Just a moment..." challenge appears on first hit
  without a real browser; needs Playwright and possibly a real-UA/session warm-up.
  Rate-limit conservatively (3s+).
- **why worth adding**: This is the mechanism by which the EU Energy Efficiency
  Directive (Article 12 DC reporting, Article 26.6 waste-heat obligations) gets
  transposed into non-EU Southeast European states — a genuinely new jurisdiction
  set not covered by any existing eu.yaml or country file.
- **verified**: yes, with caveat. Confirmed page content via a full browser session
  (title "Energy Community acquis - Energy Community Homepage", body text
  enumerating acquis categories including "Energy efficiency"). A direct
  non-browser fetch returned 403 (Cloudflare), so the scanner must run this one
  with Playwright enabled.
- **append to**: new file `config/domains/supranational.yaml`.

### 5. ASEAN Centre for Energy (ACE)
- **name**: "ASEAN Centre for Energy"
- **id**: `asean_centre_for_energy`
- **base_url**: `https://aseanenergy.org`
- **level**: supranational (regional IGO — energy policy body for the 10 ASEAN
  member states)
- **access**: none
- **format**: HTML + PDF publications
- **effort tier**: (b) plain crawl domain
- **coverage**: region: `["apac", "asean", "supranational"]`,
  category: `energy_ministry`, tags: `["efficiency", "planning", "research"]`,
  policy_types: `["report", "guidance"]`, language: `en`
- **start_paths** (proposed): `/knowledge-hub`, `/topics`, `/apaec`
  (ASEAN Plan of Action for Energy Cooperation)
- **practical**: no auth; standard corporate site, moderate depth needed since
  publications are catalogued under `/knowledge-hub`.
- **why worth adding**: Fills a real APAC gap — a regional multi-country energy
  policy body (unlike australia.yaml/apac.yaml which are single-country). Publishes
  building/industrial energy-efficiency financing reports and references data-center
  energy-rating guidelines as a recommended regional policy direction.
- **verified**: yes. Homepage loads, confirmed live publications including
  "From Potential to Pipeline: Enhancing the Energy Efficiency Financing Ecosystem"
  and "Programme for Energy Efficiency in Buildings (PEEB)". Note:
  `aseanenergy.org/aeds` and `/aeds/` (the ASEAN Energy Database System, mentioned
  in secondary sources) both 404'd in this session — do not add that URL without
  re-checking; use the confirmed `/knowledge-hub` path instead.
- **append to**: `config/domains/apac.yaml`.

### 6. C40 Cities Knowledge Hub — Data Centers guidance
- **name**: "C40 Knowledge Hub - Data Centers and Climate"
- **id**: `c40_knowledge_hub`
- **base_url**: `https://www.c40knowledgehub.org`
- **level**: supranational (global mayors' climate network, 40+ member megacities,
  guidance used well beyond members)
- **access**: none (Salesforce Community site; login/register prompts appear but
  content itself is publicly readable without signing in)
- **format**: HTML
- **effort tier**: (b) plain crawl domain; **requires_playwright: true** — the page
  is a Salesforce Lightning SPA that returned a bare "CSS Error" shell to a plain
  fetch and only rendered content through a real browser session.
- **coverage**: region: `["supranational", "global"]`, category: `economic_dev`,
  tags: `["planning", "carbon"]`, policy_types: `["guidance", "report"]`,
  language: `en`
- **start_paths** (proposed):
  `/s/article/Data-centers-and-the-climate-landscape-An-actionable-resource-for-US-mayors`,
  `/s/` (knowledge hub search/index)
- **practical**: JS-heavy Salesforce Community platform; plain HTTP fetch is
  insufficient (confirmed below), Playwright required. No visible rate limit
  stated; be conservative (3s+).
- **why worth adding**: A live (published January 2026) implementation guide
  specifically on data centers, local policy levers (zoning, permitting), grid,
  and climate impact aimed at city governments — directly in-taxonomy and
  currently just a single US-focused article, but the Knowledge Hub as a whole
  is the type of source likely to add more city-level data-center guides over time
  across C40's 40+ member cities globally.
- **verified**: yes. Confirmed via full browser session — page title "Data centers
  and the climate landscape: An actionable resource for US mayors", body text
  covers zoning/permitting/site-review policy levers for data-center siting,
  electricity/grid impact, water use. A plain WebFetch to the same URL failed
  (rendered only a client-side "CSS Error" placeholder), confirming Playwright is
  mandatory for this domain.
- **append to**: new file `config/domains/supranational.yaml`.

### 7. ISO/IEC 30134 series — Data Centre Key Performance Indicators (standards catalog)
- **name**: "ISO/IEC 30134 - Data Centre KPI Standards Catalog"
- **id**: `iso_iec_30134_datacentre_kpi`
- **base_url**: `https://www.iso.org`
- **level**: supranational (global standards body, ISO/IEC JTC 1/SC 39)
- **access**: none for catalog/abstract pages; **full standard text is paywalled**
  (CHF 100 per part, confirmed on the ERF part) — this source only yields metadata/
  abstracts, not full policy text, unless a licensed copy is separately obtained.
- **format**: HTML (catalog record); PDF full text is paid
- **effort tier**: (b) plain crawl domain, low depth (catalog pages only)
- **coverage**: region: `["supranational", "global"]`, category: `standards`,
  tags: `["efficiency"]`, policy_types: `["standard"]`, language: `en`
- **start_paths** (proposed): `/standard/71717.html` (Part 6, ERF),
  `/committee/6889696.html` (ISO/IEC JTC 1/SC 39 committee page, indexes all
  30134 parts: PUE, REF, ITEEsv, ITEUsv, ERF, CER, CUE, WUE)
- **practical**: static catalog pages, no auth for metadata; do not attempt to
  crawl/download the paywalled PDFs.
- **why worth adding**: ISO/IEC 30134-6 (Energy Reuse Factor) is the international
  technical standard underpinning "heat reuse" measurement globally — worth
  indexing even though only abstracts are free, since the abstract text itself
  ("ratio of energy being reused... to sum of all energy consumed") is exactly the
  taxonomy's core subject-matter language, useful for catching new/revised parts
  as they publish.
- **verified**: yes. Fetched `/standard/71717.html` directly — loads, confirms
  ISO/IEC 30134-6:2021 abstract, status "to be revised" with
  `ISO/IEC AWI 30134-6` already underway, and CHF 100 paywall for full PDF.
- **append to**: new file `config/domains/supranational.yaml`.

---

## Structured API candidates (tier-c — need a NEW client; none fit existing shapes)

### 8. data.europa.eu — Search API (EU open-data meta-catalog)
- **name**: "data.europa.eu Search API"
- **id**: `data_europa_eu_search_api`
- **base_url**: `https://data.europa.eu`
- **docs URL**: `https://dataeuropa.gitlab.io/data-provider-manual/api-documentation/`
  (also see `https://data.europa.eu/en/which-apis-are-available-and-where-can-i-find-information-about-them`)
- **level**: supranational (aggregates open-data catalogs from all EU member states
  + EU institutions)
- **access**: **none** — keyless, no signup, no rate-limit key required
- **source_type feasibility**: needs a NEW client. Endpoint shape:
  `GET /api/hub/search/search?q=<query>&limit=<n>` returns JSON with dataset
  title/description/publisher/distribution-URL/keywords across ~1M+ EU-wide open
  datasets. A SPARQL endpoint (`/sparql`) is also available for more precise
  DCAT-AP metadata queries (e.g. filter by dcat:theme = energy).
- **format**: JSON (search API), RDF/SPARQL (semantic endpoint)
- **coverage**: region: `["eu", "supranational"]`, category: `regulatory`,
  tags: `["research", "reporting"]`, policy_types: `["report"]`
- **practical**: no documented hard rate limit found in this pass; standard courtesy
  throttling advised. Full-text search is metadata-only (titles/descriptions), not
  full document text — most hits are statistical datasets (e.g. "Share of renewable
  energy and waste heat" energy-balance tables), not laws/directives. This is a
  **discovery layer** over national statistical/open-data portals, not primarily a
  legislation database.
- **why worth adding**: One integration surfaces energy/waste-heat datasets from
  every EU member state's national open-data portal simultaneously — genuinely
  "one integration, many jurisdictions" — but expect mostly statistical/report
  datasets rather than legal text; lower priority than the crawl-domain finds above
  for this project's specific "policy documents" requirement.
- **verified**: yes. Queried
  `https://data.europa.eu/api/hub/search/search?q=waste%20heat%20data%20centre&limit=5`
  directly — returned live JSON, 1,012,093 total indexed results, sample hits
  included Austrian and Dutch energy/waste-heat statistical datasets with working
  distribution URLs and CC-BY-4.0 licensing.
- **append to**: `config/domains/api_sources.yaml` as a new `source_type:
  "data_europa"` (needs client to be written — no existing client's shape matches
  a full-text-search-over-DCAT-catalog pattern).

### 9. OECD SDMX API (general statistical API; PINE database access is indirect)
- **name**: "OECD SDMX Statistics API"
- **id**: `oecd_sdmx_api`
- **base_url**: `https://sdmx.oecd.org`
- **docs URL**: `https://data.oecd.org/api/sdmx-json-documentation/` and
  `https://www.oecd.org/en/data/insights/data-explainers/2024/09/api.html`
- **level**: supranational (OECD + selected non-member economies)
- **access**: **none** — keyless, "free of charge... subject to OECD Terms and
  Conditions" per OECD's own API documentation
- **source_type feasibility**: needs a NEW client (SDMX-JSON/XML, not a shape any
  existing client — riksdagen/uk_bills/etc. — handles). Endpoint pattern:
  `GET /public/rest/data/{agency},{dataset},{version}/{selection}`
- **format**: XML/JSON/CSV (SDMX standard, format selectable via `format=` param)
- **coverage**: region: `["supranational", "global"]`, category: `regulatory`,
  tags: `["research", "carbon", "efficiency"]`, policy_types: `["report"]`
- **practical**: this endpoint is a general statistics gateway, not policy-text
  search. The specific dataset most relevant to this project — **PINE (Policy
  Instruments for the Environment)**, 4,600+ environmental policy instruments
  across 150 countries, portal at `oe.cd/pine` — is mainly disseminated through a
  Shiny dashboard (`oecd-main.shinyapps.io/pinedatabase`) rather than a clean SDMX
  flow; I could not confirm PINE itself is queryable through the generic SDMX
  endpoint in this session (only confirmed the SDMX gateway itself is live and
  keyless, via a climate/cities dataflow list, not PINE specifically).
- **why worth adding**: keyless, well-documented, genuinely global API gateway;
  worth building a generic OECD SDMX client eventually, but PINE's practical
  reachability through it needs a follow-up session with someone testing the
  actual PINE dataflow ID against `sdmx.oecd.org` before committing engineering
  time.
- **verified**: partially. Confirmed `sdmx.oecd.org/public/rest/dataflow/all?references=none`
  returns a valid, keyless SDMX 2.1 structure message (tested with a
  climate/cities dataflow list). Did NOT confirm the PINE dataflow specifically
  resolves through this endpoint — flagged in Unverified section below too.
- **append to**: `config/domains/api_sources.yaml` as a new `source_type:
  "oecd_sdmx"` — but hold until PINE dataflow ID is confirmed reachable (see
  Unverified section).

---

## Unverified / needs-human-check

- **IEA Policies API (`api.iea.org/policies/v2`)** — a real backend endpoint exists
  (confirmed it responds, not a 404/DNS failure) and IEA's own Global Energy
  Policies Hub page (iea.org/data-and-statistics/data-tools/global-energy-policies-hub,
  confirmed live, 6,500+ policies across 84 countries) clearly calls some API to
  populate its filters. However every query I tried (`?csv=true`, no params,
  `?policyId=1`) returned `400 Bad Request` with the message "policyId must be a
  number" regardless of what was passed — I could not reverse-engineer the correct
  request shape (likely needs specific headers, a POST body, or an id from the
  page's own internal listing call I didn't capture). No public API docs found;
  IEA lists `policies@iea.org` as a contact for data inquiries. **Do not build a
  client against this until someone captures the real browser network trace from
  iea.org/policies with devtools open**, or IEA confirms a documented endpoint.

- **Climate Policy Radar / climate-laws.org API** — climate-laws.org (the
  Grantham Research Institute/LSE "Climate Change Laws of the World" database,
  177 countries, 5,000+ laws, now powered by Climate Policy Radar's NLP) is
  exactly the kind of "one integration, many jurisdictions" climate-law source
  the brief calls out by name. However, Climate Policy Radar's own site
  states their API is explicitly **"coming soon"** — not live as of this research
  pass. Re-check `climatepolicyradar.org` and `app.climatepolicyradar.org` in a
  future pass; if launched, this should be a top-tier (a-or-c) candidate.

- **World Bank RISE (Regulatory Indicators for Sustainable Energy)** — covers
  energy-efficiency regulatory scoring for 111 countries and would be very
  relevant (has an explicit energy-efficiency pillar), but the URL commonly cited
  for it, `rise.worldbank.org/library`, **does not resolve (DNS failure)** in this
  session — it appears to have been retired/migrated. A successor page may exist
  at `data360.worldbank.org/en/dataset/WB_RISE` (that domain does load and links
  to a generic World Bank Data360 `/en/api`), but I did not confirm RISE's specific
  data is reachable through that API. Needs a follow-up check directly against
  `data360.worldbank.org/en/api` docs.

- **OECD PINE dataflow ID** — see candidate #9 above; the SDMX gateway itself is
  confirmed live and keyless, but I did not confirm the specific PINE
  (environmental policy instruments) dataflow resolves through it.

- **ICLEI (Local Governments for Sustainability)** — confirmed to exist and active
  in sustainable-energy work generally, but I found no data-center-specific content
  and no database distinct enough from the C40 Knowledge Hub entry above to justify
  a separate line item. Not recommended without a more specific page/dataset found.

- **InforMEA / ECOLEX (UNEP-backed multilateral environmental agreements +
  190,000-national-law database)** — confirmed to exist (informea.org, ecolex.org)
  and broad in scope (500+ MEAs, chemicals/biodiversity/climate treaties), but I
  did not confirm this session whether ECOLEX's national-law full-text search has
  an API, or whether energy-efficiency/data-center content is findable there vs.
  being drowned out by its much broader environmental-treaty scope. Worth a
  dedicated follow-up if someone wants to check `ecolex.org`'s search/API
  specifically for data-center/waste-heat hits.

- **Climate Neutral Data Centre Pact (`climateneutraldatacentre.net`)** — surfaced
  during CEN/CENELEC research; this is an **industry self-regulatory pact**
  (data-center operators/associations, EU-Commission-recognized as an EED
  Article 26 compliance mechanism) rather than a government/IGO policy source, so
  it sits outside this brief's scope as written. Flagging in case the project
  later wants to track industry co-regulation alongside government policy — not
  included as a candidate here.

---

## Summary of proposed new region file

Recommend a **new file** `config/domains/supranational.yaml` for entries #1, #4,
#6, #7 (IEA 4E EDNA, Energy Community, C40 Knowledge Hub, ISO/IEC 30134), since
none of them is EU-specific or APAC-specific the way the existing regional files
are organized. Entries #2 and #3 (CEN/CENELEC/ETSI, Euroheat & Power) append to
the existing `eu.yaml`. Entry #5 (ASEAN Centre for Energy) appends to the existing
`apac.yaml`. Entries #8 and #9 (data.europa.eu, OECD SDMX) append to
`api_sources.yaml` as new `source_type` values once their clients are built.
