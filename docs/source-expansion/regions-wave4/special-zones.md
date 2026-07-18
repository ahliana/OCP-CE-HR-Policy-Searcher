# Special Economic Zones / Free Zones / Digital Parks — Wave 4

Scope: special economic zone, free zone, industrial-park, and tech-park **authorities**
(not third-party investment promoters, not private zone developers unless they are the
designated master developer/regulator) that publish their own energy, efficiency,
sustainability, or heat/cooling requirements for tenants — a governance layer distinct
from national energy ministries. Research + draft only, per
`docs/source-expansion/BRIEF.md`. Nothing below is enabled in any config file.

Dedup performed against: `config/domains/*.yaml` (incl. `uae.yaml`, `saudi_arabia.yaml`,
`india.yaml`, `mexico.yaml`, `south_africa.yaml`, `apac.yaml`), and
`docs/source-expansion/draft/crawl/**/*.yaml`. No existing entries use any zone-authority
base_url (masdar.ae, kizad/kezadgroup.com, neom.com, dso.ae, qfz.gov.qa, duqm.gov.om,
sczone.eg, cyberview.com.my, stockholmdataparks.com, etc.) — all candidates below are
net-new. `mexico.yaml`/wave-2 already covers Queretaro at the *state fiscal* level, not a
zone authority, so it is not re-proposed here.

**Totals: 10 verified candidates, 6 unverified/needs-human-check. Tier breakdown: 0
tier-a, 10 tier-b, 0 tier-c** (every candidate is a plain crawl domain — no zone
authority in this wave exposes a queryable API).

**Single highest-value find**: **Stockholm Data Parks** — a joint program of the City of
Stockholm, district-heat utility Stockholm Exergi, grid operator Ellevio, and dark-fiber
provider Stokab that designates specific industrial-park sites for data centers *on
condition* they sell waste heat into the city district-heating network via Stockholm
Exergi's Open District Heating platform. This is the clearest "zone authority mandates
heat reuse" governance layer found in this wave — the site literally frames it as
"a data center industry where no heat is wasted" and reports 20+ connected suppliers
recovering enough heat for 30,000+ apartments.

---

## Verified candidates (ranked best-first)

### 1. Stockholm Data Parks (Sweden)

- name: "Stockholm Data Parks"
- id: `stockholm_data_parks`
- base_url: `https://stockholmdataparks.com`
- start_paths: `/` , `/about/` (site is a WordPress blog/news structure — crawl root +
  news archive)
- level: local (City of Stockholm program, run jointly with municipal utilities)
- access: none
- coverage: designates industrial-park sites in Stockholm for data centers on the
  condition they connect to Stockholm Exergi's Open District Heating platform and sell
  recovered waste heat into the city network; goal is 10% of Stockholm's heating from
  recovered DC waste heat; part of the city's fossil-fuel-free-by-2040 plan
- region: `["nordic", "sweden"]` | category: `district_heating` | tags: `efficiency,
  planning, incentives` | policy_types: `program, guidance` | language: en
- format: HTML (news/blog posts, no single consolidated policy PDF found)
- practical: no rate limit documented; content is a running news feed of new heat-reuse
  connections, best captured as several start_paths / periodic recrawl
- effort tier: b
- why worth adding: this is the exact "zone authority mandating heat reuse" pattern the
  brief calls out as highest value — a municipal/utility program that steers DC siting
  and conditions it on heat offtake, not a national ministry
- verified: yes — fetched directly, confirmed live, jointly run by City of Stockholm +
  Stockholm Exergi + Ellevio + Stokab, describes the Open District Heating heat-sale
  mechanism and the 2040 fossil-free goal
- append to: new `config/domains/nordic.yaml` Stockholm section (existing `nordic.yaml`
  is Nordic-wide/national; add a subnational/local block) or a new `sweden.yaml`

### 2. Dubai Silicon Oasis (DSO) — Sustainability (UAE)

- name: "Dubai Silicon Oasis Authority — Sustainability"
- id: `dso_ae_sustainability`
- base_url: `https://www.dso.ae`
- start_paths: `/sustainability`
- level: local (Dubai free zone authority, under Dubai Development Authority)
- access: none
- coverage: DSO's own sustainability page reporting 60+ LEED-certified buildings on the
  zone, 100% energy-efficient LED street lighting, multiple solar-powered buildings, a
  115.7 million kg cumulative CO2 reduction figure, and an "Industrial Symbiosis"
  tenant-waste-exchange partnership (The Surpluss); the zone already hosts a live 6MW
  Tier III data center (du Data Center, Silicon Oasis)
- region: `["middle_east", "uae", "dubai"]` | category: `economic_dev` | tags:
  `efficiency, renewable_energy, reporting` | policy_types: `report, standard` |
  language: en
- format: HTML
- practical: no rate limit documented; note DSOA's old domain `dsoa.ae` 301-redirects to
  `dso.ae` — use `dso.ae` as base_url
- effort tier: b
- why worth adding: a zone authority self-reporting concrete efficiency/CO2 metrics for
  a zone that already hosts data-center tenants — closest thing to a DC-hosting free
  zone publishing its own sustainability scorecard in the Gulf
- verified: yes — fetched directly, confirmed live, quoted figures above
- append to: `uae.yaml` (new Dubai Silicon Oasis section)

### 3. Cyberview — Sustainability (Cyberjaya, Malaysia)

- name: "Cyberview Sdn Bhd — Sustainability (Cyberjaya master developer)"
- id: `cyberview_my_sustainability`
- base_url: `https://www.cyberview.com.my`
- start_paths: `/sustainability/`
- level: local (Malaysia-government-owned master developer/regulator of Cyberjaya, the
  country's largest data-center hub)
- access: none
- coverage: Cyberview (not MDEC) is the actual zone-authority/master-developer for
  Cyberjaya; page references an ESG framework, a "carbon-neutral by 2030" ambition for
  Cyberjaya, and (per secondary search results, not yet confirmed on-page) a centralized
  chilled-water district-cooling scheme run by Pendinginan Megajana Sdn Bhd serving 45+
  buildings, plus active exploration of renewable/green-power access specifically for
  Cyberjaya data centers
- region: `["apac", "malaysia"]` | category: `economic_dev` | tags: `efficiency,
  renewable_energy, planning, data_center_specific` | policy_types: `strategy, report` |
  language: en
- format: HTML (detail is in linked "Sustainability Bulletins" / ESG framework PDFs not
  yet located)
- practical: no rate limit documented; the page itself is thin — the ESG framework and
  ESG bulletins are linked sub-resources a crawl should pick up at depth 2
- effort tier: b
- why worth adding: distinct from MDEC (national digital-economy agency, already
  reference-checked in wave 3) — Cyberview is the zone-level authority actually steering
  Cyberjaya's DC-specific cooling and power infrastructure
- verified: yes — fetched directly, confirmed live and on-topic; specific cooling/carbon
  figures come from search snippets (MIDA news, LinkedIn) not yet re-confirmed on-page,
  so treat those specific numbers as lower-confidence than the base URL itself
- append to: new `malaysia.yaml` (no existing Malaysia file; wave 3 proposed
  `my_mida_desac` for the same new file)

### 4. Special Economic Zone at Duqm — Environmental Guidelines (Oman)

- name: "SEZ at Duqm — Environmental Guidelines"
- id: `duqm_om_environmental_guidelines`
- base_url: `https://duqm.gov.om`
- start_paths: `/en/environmental-guidelines`, `/en/sezad/environment/links-downloads`
- level: national (Oman's national Special Economic Zone Authority at Duqm, SEZAD)
- access: none
- coverage: publishes real guideline PDFs directly from the zone authority: an
  Environmental & Social Impact Assessment (ESIA) Guideline (2022), a Climate Change
  Guideline covering "Identification of Risks and Impacts & Resource Efficiency —
  Greenhouse Gases" (2021), and a "Cumulative Impact Assessment, Resource Efficiency,
  and Pollution Prevention Guideline" — all binding on companies developing in the zone
- region: `["middle_east", "oman"]` | category: `regulatory_authority` | tags:
  `mandates, efficiency, carbon, reporting` | policy_types: `regulation, guidance` |
  language: en
- format: HTML index → PDF (the PDFs are large scanned/composite documents — a
  screening pass should extract linked PDF text, not just the index page)
- practical: no rate limit documented; PDFs are large (multi-MB); the Cumulative Impact
  Assessment PDF fetched fine as a binary but needs proper PDF text extraction rather
  than the general-purpose web-fetch summarizer used here
- effort tier: b
- why worth adding: a genuine SEZ *regulatory authority* (SEZAD) publishing its own
  environmental/resource-efficiency guideline documents — the closest match in the Gulf
  to a zone authority with actual (if generic, not DC-specific) mandatory guidance
- verified: yes — index page fetched directly and confirmed live, listing named/dated
  guideline documents with working download links; one linked PDF was fetched
  (confirmed it resolves and is a real ~8MB document) but its text content could not be
  cleanly extracted by the summarizing fetch tool — flagging for a human/PDF-aware pass
- append to: new `oman.yaml`

### 5. Qatar Free Zones Authority — Sustainability (Qatar)

- name: "Qatar Free Zones Authority — Sustainability"
- id: `qfz_qa_sustainability`
- base_url: `https://qfz.gov.qa`
- start_paths: `/why-qfz/sustainability/`
- level: national (Qatar's national free-zones authority, covering Ras Bufontas and Um
  Alhoul zones)
- access: none
- coverage: QFZA reports holding ISO 50001 (Energy Management), ISO 14001
  (Environmental Management), and ISO 45001 certifications; page describes zone power
  generated from natural gas (lowest-carbon fossil option per QFZA framing) and new
  warehouse rooftops with ~40% solar-panel coverage; a 2025 Samsung C&T MOU explicitly
  names data centers as a target for future sustainable-infrastructure collaboration
- region: `["middle_east", "qatar"]` | category: `regulatory_authority` | tags:
  `efficiency, renewable_energy, reporting` | policy_types: `standard, report` |
  language: en (site also has an Arabic version at the same paths)
- format: HTML
- practical: no rate limit documented; page is bilingual (ar/en) — content returned
  during verification was partly Arabic even on the `/en/`-adjacent path, so confirm
  the correct language-specific path when building start_paths
- effort tier: b
- why worth adding: a national free-zone regulator holding a genuine ISO 50001 energy-
  management certification (a formal, auditable energy standard) and actively
  courting data-center investment under that sustainability banner
- verified: yes — fetched directly, confirmed live and on-topic, content quoted above
- append to: new `qatar.yaml`

### 6. NEOM — Environment (Our World) (Saudi Arabia)

- name: "NEOM — Environment (Our World)"
- id: `neom_sa_environment`
- base_url: `https://www.neom.com`
- start_paths: `/en-us/about/our-values/code-of-conduct/our-world/environment`
- level: subnational (giga-project / special zone directly under Saudi PIF; Oxagon is
  NEOM's industrial/data-center hub)
- access: none
- coverage: page is high-level (values/CSR framing) rather than a technical standard;
  secondary sources (search results, not the page itself) reference NEOM's "Interim
  Sustainability Requirements for the Built Environment" (doc code
  NEOM-NEV-PRC-501) invoking LEED, Envision, Mostadam, the International Green
  Construction Code, Saudi Green Building Code 1001, and Saudi Energy Code 601 as
  compliance pathways — Oxagon is where NEOM's $5B DataVolt AI data-center project
  (net-zero, 100% renewable-powered) is sited
- region: `["middle_east", "saudi_arabia"]` | category: `economic_dev` | tags:
  `efficiency, renewable_energy, strategy` | policy_types: `strategy, guidance` |
  language: en
- format: HTML
- practical: no rate limit documented; the actual technical standards document
  (NEOM-NEV-PRC-501) was NOT found hosted on neom.com in this pass — it only turned up
  via a third-party document-sharing site (Scribd), which is not a source we can crawl
  with confidence it's the authoritative/current version — see unverified list
- effort tier: b
- why worth adding: NEOM/Oxagon is the single largest announced sustainable-DC project
  tied to a special zone in this entire wave ($5B, net-zero, renewable-powered); the
  official page is thin today but is the right anchor to recrawl as NEOM publishes more
- verified: yes (page itself, thin content) — see unverified list for the specific
  standards document, which is NOT verified as officially hosted
- append to: `saudi_arabia.yaml` (new NEOM/Oxagon section)

### 7. General Authority for the Suez Canal Economic Zone — SCZONE (Egypt)

- name: "SCZONE — General Authority for Suez Canal Economic Zone"
- id: `sczone_eg`
- base_url: `https://sczone.eg`
- start_paths: `/en/` (homepage; confirm exact "Rules & Regulations" and sector pages
  once site nav is mapped — not fully resolved in this pass)
- level: national (Egypt's national economic-zone authority for the Suez Canal corridor)
- access: none
- coverage: lists "Data Centers" explicitly as one of its targeted investment sectors
  alongside Green Hydrogen and Solar PV; site has "Rules & Regulations" and "E-Services"
  sections (contents not yet confirmed); SCZONE has separately signed renewable-power
  supply agreements for zone tenants via its SCZONE Infrastructure Company / SCZone
  Utilities subsidiary
- region: `["africa", "egypt"]` | category: `economic_dev` | tags: `renewable_energy,
  data_center_specific, planning` | policy_types: `strategy, regulation` | language: en
  (+ ar)
- format: HTML
- practical: no rate limit documented; homepage confirmed live but the deeper
  Rules & Regulations page content was not directly fetched in this pass
- effort tier: b
- why worth adding: the only MENA zone authority in this wave that names "Data Centers"
  as an explicit targeted sector on its own site, paired with a real renewable-power
  utility subsidiary serving zone tenants
- verified: yes (homepage only) — confirmed live, on-topic sector list seen in search
  snippet; the specific Rules & Regulations subpage needs a follow-up fetch before
  relying on it for policy text
- append to: new `egypt.yaml`

### 8. Khalifa Economic Zones Abu Dhabi — KEZAD (formerly KIZAD) (UAE)

- name: "Khalifa Economic Zones Abu Dhabi (KEZAD)"
- id: `kezad_ae`
- base_url: `https://www.kezadgroup.com`
- start_paths: `/` (homepage; no dedicated sustainability/regulatory-framework subpage
  confirmed live in this pass)
- level: local (Abu Dhabi zone authority, operated by AD Ports Group)
- access: none
- coverage: site references KEZAD's "SDG Model Zone Partner 2023-2024" recognition and
  general "Sustainable Development" positioning; no tenant-facing energy/environmental
  regulation text was found on the crawled homepage content itself
- region: `["middle_east", "uae", "abu_dhabi"]` | category: `economic_dev` | tags:
  `renewable_energy, planning` | policy_types: `report` | language: en
- format: HTML
- practical: no rate limit documented
- effort tier: b
- why worth adding: lowest-confidence of the UAE zone entries in this wave — included
  because it is the direct successor/rebrand of KIZAD (which UAE district-cooling and
  green-industrial-zone coverage already references in secondary sources), but the
  official site itself does not yet expose the specific regulatory text a scan would
  need — recommend a deeper crawl (depth 2-3) before expecting much yield
- verified: yes (site is live, official, on-topic sustainability framing) — but no
  specific tenant mandate content confirmed
- append to: `uae.yaml` (new KEZAD/Abu Dhabi section, distinct from existing
  `doe_abudhabi` entry)

### 9. Tanger Med Special Agency — Energy Transition (Morocco)

- name: "Tanger Med Special Agency — Energy Transition"
- id: `tangermed_ma_energy`
- base_url: `https://www.tangermed.ma`
- start_paths: `/en/csr/energy-transition/`
- level: national (Morocco's special free-zone/port authority for the Tanger Med
  industrial and free-zone platform, including Tanger Free Zone)
- access: none
- coverage: Tanger Med Utilities (a Tanger Med Group subsidiary) is financing/building
  ~11MW of photovoltaic capacity "on behalf of its customers" (i.e., zone tenants);
  broader Group commitments to decarbonized energy supply, energy efficiency, and
  circular economy are described at the corporate/CSR level
- region: `["africa", "morocco"]` | category: `economic_dev` | tags:
  `renewable_energy, efficiency` | policy_types: `strategy, program` | language: en
  (+ fr)
- format: HTML
- practical: no rate limit documented
- effort tier: b
- why worth adding: a real (if not yet mandatory) zone-utility-run renewable-energy
  program for tenants, and Morocco has separately announced a national push for
  carbon-neutral data centers by 2035 anchored partly in its free-zone platforms
- verified: yes — fetched directly, confirmed live and on-topic; content is
  organizational/Group-level rather than a binding tenant mandate
- append to: new `morocco.yaml`

### 10. PEZA — Implementing Rules and Regulations (Philippines)

- name: "PEZA — Implementing Rules and Regulations"
- id: `peza_ph_irr`
- base_url: `https://www.peza.gov.ph`
- start_paths: `/implementing-rules-and-regulations`, `/issuances`
- level: national (Philippine Economic Zone Authority, the national ecozone regulator)
- access: none
- coverage: PEZA requires an Environmental Compliance Certificate (ECC, issued by
  DENR-EMB) for ecozone development and enforces geohazard/environmental-clearance
  compliance for developers, factories, utilities, and facility-construction
  applicants; PEZA has publicly promoted a "green, sustainable, and disaster-free
  ecozones" transformation initiative; no PEZA-specific PUE/DC-energy standard was
  found
- region: `["apac", "philippines"]` | category: `regulatory_authority` | tags:
  `mandates, reporting` | policy_types: `regulation, guidance` | language: en
- format: HTML → linked DOC/PDF issuances
- practical: no rate limit documented; `/implementing-rules-and-regulations` and
  `/issuances` are the two candidate index pages — actual ECC/environmental issuance
  text lives in linked docs, not yet individually confirmed
- effort tier: b
- why worth adding: PEZA is actively recruiting DC/renewable-energy investment
  (Camarines Norte data-center-plus-desalination project cited in a 2025 press
  release) and is the binding environmental-compliance gate for any ecozone facility,
  including data centers — general-purpose but on-topic
- verified: yes (index pages exist and are on the official domain) — specific
  issuance/regulation text not yet individually fetched, so treat named documents as
  lower confidence than the base URL
- append to: new `philippines.yaml`

---

## Unverified / needs-human-check

- **Konza Technopolis Development Authority (Kenya)** — `konza.go.ke` returned an HTTP
  403 (likely bot-detection) and `dev.konza.go.ke` (seen in a search result) does not
  resolve (DNS failure). Secondary sources describe Konza's own green-building
  requirements and a geothermal-powered data center groundbreaking, but no official
  authority page could be verified live in this pass. Recommend a human/browser check
  of `konza.go.ke` directly.

- **NEOM Interim Sustainability Requirements for the Built Environment**
  (doc NEOM-NEV-PRC-501-01.00) — referenced by name and code in search results, but the
  only accessible copy found was hosted on a third-party document-sharing site
  (scribd.com), not on `neom.com`. Do not crawl the Scribd copy — authenticity/currency
  cannot be confirmed. If NEOM publishes this on its own domain, it would be a strong
  upgrade to entry #6 above.

- **King Abdullah Economic City (KAEC), Saudi Arabia** — `kaec.net` returned an HTTP 403
  during verification (likely bot-detection/WAF). Secondary sources describe general
  sustainability infrastructure (solar-powered desalination, PV recycling targets) but
  no data-center-specific policy was confirmed, and the site itself could not be
  fetched. Needs a human/browser check.

- **NEPZA — Nigeria Export Processing Zones Authority** (`nepza.gov.ng`) — official site
  confirmed live and on-topic for free-zone regulation generally (utilities,
  incentives), but no energy-efficiency, sustainability, or data-center-specific policy
  content was found on the fetched page. The one zone-specific regulation text found
  (Lagos Free Trade Zone Regulation 2016) is hosted on the private zone
  developer's site (`lagosfreezone.com`), not on `nepza.gov.ng` itself — would need
  confirmation that NEPZA, not just the zone company, is the publisher before treating
  it as an authority source. No Nigeria-specific data-center energy provision was
  confirmed in either document.

- **BP Batam / Nongsa Digital Park (Indonesia)** — `ptsp.bpbatam.go.id` is a genuine BP
  Batam (Batam free-zone authority) page and does state a commitment to renewable-
  energy integration and ESG standards tied to data-center growth in Nongsa, but the
  page itself is a June 2026 news article, not a policy/regulation document per the
  brief's definition. Nongsa Digital Park's own site (`nongsadigital.com`) is a private
  SEZ operator, not the government zone authority. A human should look for BP Batam's
  actual "Peraturan" (regulation) publications rather than its news feed.

- **Chile / Colombia / Brazil free-trade-zone (zona franca) authorities** — no
  government zone-authority page publishing its own energy/sustainability rules for
  data centers was found in this pass. What surfaced (`zonafrancaoccidente.com`,
  investment-promotion articles) are private zone operators/promoters, explicitly out
  of scope per the brief. Colombia's national free-zone tax regime is a Ministry-level
  policy, not a zone-authority one, and is out of scope for this wave. Recommend
  treating LatAm zone authorities as a likely dead end unless a human finds a specific
  government-run zone (e.g., a public Zona Franca de Bogotá regulator distinct from the
  private operator) with its own published rules.

---

## Notes for whoever picks this up

- Several candidates above (Cyberview, SCZONE, KEZAD, PEZA) are **verified live and
  on-topic at the base-URL level** but the specific numeric/regulatory claims quoted in
  their "coverage" fields come partly from search-result snippets rather than a direct
  page fetch of the deeper sub-page. Flagged inline per entry — a deeper crawl (depth
  2-3) is the right next step for these before expecting strong recall.
- New country files implied: `oman.yaml`, `qatar.yaml`, `malaysia.yaml`,
  `egypt.yaml`, `morocco.yaml`, `philippines.yaml`. `uae.yaml` and `saudi_arabia.yaml`
  already exist and get new sections instead.
- PDF-heavy sources (Duqm in particular) were fetched successfully as files but the
  general-purpose web-fetch summarizer could not extract clean text from a scanned/
  composite PDF — the production crawler's PDF text-extraction path should handle this
  better than the verification tool used here; don't read the "could not extract text"
  note as the source being bad, just as this tool's limitation.
