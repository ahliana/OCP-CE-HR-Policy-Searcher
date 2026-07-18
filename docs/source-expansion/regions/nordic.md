# Nordic Region - Source Expansion Findings

Scope: Sweden, Denmark, Finland, Norway, Iceland - national gaps + subnational.
Sweden Riksdagen API and Denmark Folketinget API are already covered and were not
re-proposed. Dedup checked against `config/domains/nordic.yaml`, `sweden.yaml`,
`denmark.yaml`, and `api_sources.yaml` (grepped all candidate base_urls against the
full `config/domains/` tree - no collisions found).

No client code or config changes made. Everything below is a proposal; nothing is
`enabled: true` anywhere yet.

---

## Verified candidates (ranked best-first)

### 1. NVE Guidance: Cost-Benefit Analysis of Waste Heat Utilization (Norway)

- **name**: NVE - Guide to the Waste Heat Cost-Benefit Analysis Regulation
- **proposed id**: `nve_overskuddsvarme_guide`
- **base_url**: `https://veiledere.nve.no`
- **start_paths**:
  - `/kost-nytteanalyse-av-overskuddsvarme/`
- **level**: national
- **access**: none (open, no key)
- **coverage**: This is NVE's (Norwegian Water Resources and Energy Directorate)
  official implementation guide for Forskrift 2024-09-25-2263, the regulation
  already tracked via `lovdata_no` in `nordic.yaml`. Where Lovdata gives the legal
  text, this gives the regulator's chapter-by-chapter explanation of how it is
  applied - including the explicit 2 MW data-center threshold, the >20 MW thresholds
  for thermal plants/industrial facilities/district heating, and how NVE reviews
  cost-benefit analyses before construction approval.
  - region: `nordic`, `norway`
  - category: `regulatory` (NVE is the approving regulator, not just a ministry)
  - tags: `mandatory`, `waste_heat_recovery`, `nve_approval`, `cost_benefit_analysis`, `district_heating`
  - policy_types: `guidance`, `regulation`
  - language: `no`
- **format**: HTML (structured guide, chaptered, likely paginated across sub-URLs
  under the same path - `allowed_path_patterns: ["/kost-nytteanalyse-av-overskuddsvarme/*"]`)
- **practical**: No rate-limit info published; treat as a normal government site
  (2s delay). No robots.txt check done this session - do before enabling. Static
  guide content, low update frequency expected (tied to the regulation, in force
  since 2025-04-01).
- **effort tier**: b (plain crawl domain)
- **why worth adding**: This is the single best find of the session - it's the
  regulator's own operational guidance for the exact data-center waste-heat
  mandate PolicyPulse already tracks the law for, filling the "what does NVE
  actually require in practice" gap that the bare statute text doesn't answer.
- **verified**: yes. WebFetch confirmed the page is live, is official NVE guidance,
  and explicitly quotes "datasentre med mer enn 2 MW samlet tilført elektrisk
  effekt" (data centers with more than 2 MW total supplied electrical capacity)
  as in scope, alongside the >20 MW thresholds for other facility types.

---

### 2. Iceland Regulations Database (island.is)

- **name**: Ísland.is - Regulations Database (Reglugerðasafn)
- **proposed id**: `island_is_reglugerdir`
- **base_url**: `https://island.is`
- **start_paths**:
  - `/reglugerdir`
- **level**: national
- **access**: none (open, no key)
- **coverage**: Iceland's official consolidated regulations database, run by the
  Ministry of Justice (Dómsmálaráðuneyti, contact reglugerdir@dmr.is), publishing
  everything in Section B of the Government Gazette with a working keyword search
  ("Ítarleit"). This is the missing piece for Iceland: `nordic.yaml` currently only
  has the energy agency (`orkustofnun_is`), with no legislation/regulation database
  - the same gap Finland closed with `finlex_fi` and Norway closed with `lovdata_no`.
  - region: `nordic`, `iceland`
  - category: `legislation`
  - tags: `mandates`, `district_heating`, `efficiency`
  - policy_types: `law`, `regulation`
  - language: `is`
- **format**: HTML, keyword-searchable
- **practical**: island.is is a large, JS-driven government portal (built on a
  modern SPA framework based on page structure observed) - **recommend
  `requires_playwright: true`** unless testing shows plain HTTP fetch returns full
  content. No published rate limit; use 2-3s default. No robots.txt check done.
- **effort tier**: b (plain crawl domain) - seed with a district-heating/waste-heat
  keyword search URL similar to how `finlex_fi` seeds on "kaukolampo", e.g. a
  fjarvarma/geothermal-district-heating search query, plus the base browse page.
- **why worth adding**: Closes Iceland's national legislation-database gap, the
  same category of fix already applied to Finland and Norway.
- **verified**: yes. WebFetch confirmed the page is Iceland's official regulations
  portal, government-run, with working advanced search, launched 2001 and
  currently on its third consolidated version (2021).

---

### 3. Storting Open Data API (Norway parliament)

- **name**: Stortinget Open Data API
- **proposed id**: `stortinget_api`
- **base_url**: `https://data.stortinget.no`
- **source_type feasibility**: No existing client fits directly. This is the
  Norwegian-parliament structural equivalent of `riksdagen` (Sweden) and
  `folketing` (Denmark), which already have dedicated clients in `src/sources/`.
  A **new** `stortinget` client would need the same shape: cases/bills (Saker),
  votes (Voteringer), hearings (Høringer), publications, committees.
- **level**: national
- **access**: none (open, no key required; attribution requested)
- **coverage**:
  - region: `nordic`, `norway`
  - category: `legislation`
  - tags: `mandates`
  - policy_types: `legislation`
  - language: `no`
- **format**: XML/JSON via API (confirmed API + technical documentation exists on
  the site, plus raw dataset downloads)
- **practical**: Contact +47 23 31 33 33 / web@stortinget.no per the site. No
  published rate limit found this session - check the API docs page directly
  before building the client. Historical XML docs/votes back to 2008.
- **effort tier**: c (needs a new structured client - not a drop-in fit for any
  existing one)
- **why worth adding**: Norway is the one Nordic "big three" (Sweden/Denmark/Norway)
  national parliament without a structured API source yet, and it's the
  parliament that passed the data-center waste-heat CBA law amendment - this
  would let PolicyPulse query Storting bill/vote data the same way it already
  does for Sweden and Denmark.
- **verified**: yes. WebFetch confirmed data.stortinget.no is Stortinget's
  official open-data platform, described as "uttrekk fra databaser som benyttes i
  Stortingets parlamentariske saksbehandling," with API access and technical
  documentation, and free public data use with attribution.

---

### 4. Eduskunta Avoin Data API (Finland parliament)

- **name**: Eduskunta Open Data API (Finland)
- **proposed id**: `eduskunta_api`
- **base_url**: `https://avoindata.eduskunta.fi`
- **source_type feasibility**: No existing client fits. Same category as #3 above
  - the Finnish-parliament equivalent of `riksdagen`/`folketing`. Would need a new
  `eduskunta` client.
- **level**: national
- **access**: none (open, no key)
- **coverage**:
  - region: `nordic`, `finland`, `eu`
  - category: `legislation`
  - tags: `mandates`
  - policy_types: `legislation`
  - language: `fi` (interface also described as English-friendly per search results)
  - Confirmed live tables/datasets include: `MemberOfParliament`, `SaliDBIstunto`
    (sessions), `SaliDBPuheenvuoro` (speeches), `SaliDBAanestys`/`SaliDBKohtaAanestys`
    (votes), `SaliDBAsiakirja` (documents), `SaliDBTiedote` (notices), `VaskiData`,
    plus attachment/seating/primary-key metadata tables.
- **format**: JSON (confirmed - a direct table-listing endpoint returned a JSON
  array of dataset names)
- **practical**: No published rate limit found this session. Docs referenced at
  `https://www.parliament.fi/fi/avoin-data/mita-on-avoin-data` and
  `https://www.eduskunta.fi/avoin-data` (both returned 403 to automated fetch in
  this session - likely bot-blocking, not down; confirm manually before building).
- **effort tier**: c (needs a new structured client)
- **why worth adding**: Completes the set - all three largest Nordic national
  parliaments (Sweden, Denmark, Norway via #3, Finland here) would have structured
  API coverage, and Finland is the Nordic country furthest along on data-center
  waste-heat district-heating integration in practice.
- **verified**: yes. WebFetch to `https://avoindata.eduskunta.fi/api/v1/tables/`
  returned a live JSON array of dataset/table names (listed above), confirming
  the API is up and queryable. The landing page and both documentation pages
  linked above returned 403 to the fetch tool and should be re-checked manually
  before client work starts.

---

### 5. Stockholm Exergi - Open District Heating (Värmeåtervinning)

- **name**: Stockholm Exergi - Open District Heating (waste-heat purchase program)
- **proposed id**: `stockholm_exergi_odh`
- **base_url**: `https://www.stockholmexergi.se`
- **start_paths**:
  - `/varmeatervinning/` (redirect target of the historical `opendistrictheating.com` site, which now 301s here)
- **level**: subnational / local (Stockholm)
- **access**: none (open, no key; informational + product-sheet PDF)
- **coverage**: Stockholm Exergi is majority owned by the City of Stockholm and
  operates the "Öppen Fjärrvärme" (Open District Heating) program that lets data
  centers and other businesses sell waste heat into the municipal district
  heating network under standardized contracts. This is exactly the kind of
  "energy company with policy/tariff docs" the brief calls out.
  - region: `nordic`, `sweden`
  - category: `district_heating`
  - tags: `heat_reuse`, `incentives`, `district_heating`, `waste_heat_data`
  - policy_types: `guidance`, `incentive`
  - language: `sv` (English content exists but the historical English domain now
    redirects into the Swedish site)
- **format**: HTML + downloadable PDF product/contract-model sheet
- **practical**: No rate limit published; treat as standard commercial site (2s).
  No robots.txt check done. Content updates infrequently (program has run since
  2014).
- **effort tier**: b (plain crawl domain)
- **why worth adding**: It's live documentation of the actual mechanism (pricing
  ~SEK 2M/MW/year, temperature-indexed compensation, two contract models,
  proximity requirement) by which 30+ Stockholm data centers already sell waste
  heat into district heating - the practical, operational counterpart to the
  Riksdagen law (`riksdagen_se_dc`) and Energimyndigheten reporting requirement
  already tracked for Sweden.
- **verified**: yes. WebFetch (after following the 301 redirect from
  opendistrictheating.com) confirmed the page describes the Open District Heating
  program, its data-center/grocery-store use case, the temperature-indexed
  pricing model, the two contract models, and a downloadable product sheet.

---

### 6. Finnish Energy (Energiateollisuus) - District Heating Statistics & Policy

- **name**: Finnish Energy (Energiateollisuus) - district heating section
- **proposed id**: `energiateollisuus_fi`
- **base_url**: `https://energia.fi`
- **start_paths**:
  - `/en/statistics/statistics-on-district-heating/`
  - `/en/energy-policy/`
- **level**: national
- **access**: none (open, no key)
- **coverage**: Finnish Energy is the national industry association for the
  energy sector (electricity + district heating utilities). Confirmed to publish
  legislative statements, sector recommendations, and an "Energy policy" nav
  section (climate roadmap, EU policy, Nordic cooperation) in addition to the
  annual district-heating statistical publication.
  - region: `nordic`, `finland`, `eu`
  - category: `district_heating`
  - tags: `district_heating`, `reporting`, `efficiency`
  - policy_types: `guidance`, `report`
  - language: `en` (English section confirmed; Finnish primary site also exists)
- **format**: HTML + downloadable statistical PDFs/Excel
- **practical**: No rate limit published; standard 2s. No robots.txt check done.
  Statistics publication is annual; policy statements are published ad hoc.
- **effort tier**: b (plain crawl domain)
- **why worth adding**: It's the trade body whose member utilities operate the
  district heating networks receiving data-center waste heat across Finland
  (Helen, Fortum, etc.) and it explicitly takes legislative positions - a useful
  cross-check against the Ministry (`tem_fi`) and regulator (`energiavirasto_fi`)
  sources already tracked.
- **verified**: yes. WebFetch confirmed Finnish Energy is an industry association
  publishing "statements on legislative matters," "recommendations and
  instructions," and maintains a dedicated "Energy policy" nav section, in
  addition to district-heating statistics.

---

### 7. Veitur - Reykjavik-area District Heating Network (Iceland)

- **name**: Veitur - District Heating Network (Reykjavik capital area + regions)
- **proposed id**: `veitur_is`
- **base_url**: `https://www.veitur.is`
- **start_paths**:
  - `/en/dreifikerfi-heitt-vatn`
- **level**: subnational / local (Reykjavik capital area + several regional systems)
- **access**: none (open, no key)
- **coverage**: Veitur (subsidiary of Orkuveita Reykjavíkur / Reykjavik Energy)
  operates geothermal district heating across the Reykjavik capital area plus
  seven independent regional systems. This is Iceland's dominant district-heating
  operator, complementing the national energy authority (`orkustofnun_is`).
  - region: `nordic`, `iceland`
  - category: `district_heating`
  - tags: `district_heating`, `efficiency`
  - policy_types: `report`
  - language: `en`
- **format**: HTML
- **practical**: No rate limit published; standard 2s. No robots.txt check done.
- **effort tier**: b (plain crawl domain)
- **why worth adding**: Lowest-priority of this batch - confirmed live and
  on-topic (district heating infrastructure/coverage) but thin on policy content
  (no tariff or regulatory detail on the page itself, only a footer link to
  "Rates"). Worth adding for completeness/coverage of Iceland subnational DH, but
  do not expect much yield versus the other six candidates above.
- **verified**: yes, with caveat. WebFetch confirmed the page is live and
  describes Veitur's district heating service areas and geothermal supply
  process, but explicitly does NOT contain tariff or regulatory-framework detail
  on this specific page (only a footer link to a separate Rates section, not
  independently verified this session).

---

## Unverified / needs-human-check

- **Nordic Energy Research** (`https://www.nordicenergy.org`) - Nordic Council of
  Ministers-funded body. WebSearch confirmed a live, relevant
  "WasteHeatSES" project page (waste heat integration into Nordic/Baltic smart
  energy systems) and a "Flex4RES" district-heating flexibility report PDF at
  `https://www.nordicenergy.org/app/uploads/2025/07/Flex4RES-WP2-DH-report.pdf`.
  However, **WebFetch returned HTTP 403 on every URL under this domain in this
  session** (`/publications/`, `/projects/waste-heat-in-smart-energy-systems/`),
  which reads as bot-blocking rather than the site being down. Could not directly
  confirm on-page content. Recommend a human (or a differently-configured fetch)
  check `nordicenergy.org/projects/waste-heat-in-smart-energy-systems/` and the
  publications page before proposing a config entry. If it's just user-agent
  blocking, this is a supranational (Nordic Council of Ministers) source worth
  adding at `level: supranational`.

- **Althingi (Iceland Parliament) open data** - Searched for an Icelandic
  equivalent of the Riksdagen/Folketing/Storting/Eduskunta open-data APIs. Found
  only a 2016-era parliamentary resolution directing the government to prepare
  open-data legislation, and Iceland's general open-data policy framework
  (`opingogn.is`) - no confirmed live Althingi-specific API endpoint. **Not
  proposed as a candidate** - if one exists it wasn't discoverable this session;
  worth a follow-up search specifically for "Alþingi vefþjónusta" or checking
  `althingi.is` for a developer/data page directly.

- **HOFOR (Copenhagen district heating utility)** - checked
  `https://www.hofor.dk/english/hofor-utilities/district-heating/`; page is live
  but is customer-facing marketing/informational content with **no mention of
  waste heat, data centers, or regulatory framework** - does not clear the "policy
  document" bar per the brief. Not proposed. (Copenhagen-area waste-heat/data-center
  deals are actually with VEKS and CTR per news coverage, not HOFOR directly -
  worth a separate look at `veks.dk` / `ctr.dk` in a future pass if this region
  gets revisited.)

---

## Summary of proposed config file placement

| id | target file | new file needed? |
|---|---|---|
| `nve_overskuddsvarme_guide` | `config/domains/nordic.yaml` | no |
| `island_is_reglugerdir` | `config/domains/nordic.yaml` | no |
| `stortinget_api` | `config/domains/api_sources.yaml` (new `source_type: stortinget`, new client needed) | no |
| `eduskunta_api` | `config/domains/api_sources.yaml` (new `source_type: eduskunta`, new client needed) | no |
| `stockholm_exergi_odh` | `config/domains/sweden.yaml` | no |
| `energiateollisuus_fi` | `config/domains/nordic.yaml` | no |
| `veitur_is` | `config/domains/nordic.yaml` | no |

All entries above are proposals only - `enabled: false` when/if drafted into YAML,
per the shared brief. No YAML files were modified in this session.
