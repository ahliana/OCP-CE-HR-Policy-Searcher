# Source Expansion Research - Shared Brief

Branch: `feature/source-expansion-research`. Research + draft config only. No client
code, nothing enabled in a live scan. Every deliverable is a document or draft YAML
with `enabled: false`.

## What PolicyPulse searches for

Government **data-center waste-heat-reuse** policy, and the adjacent policy that drives
it: district heating / heat networks, waste-heat recovery, data-center energy
efficiency (PUE/ERE), thermal energy reuse, grid heat, energy-efficiency mandates,
carbon/emissions rules that touch data centers, and incentives/grants for any of the
above. See `config/keywords.yaml` for the exact term taxonomy (EN + many languages).

A source is worth adding only if it publishes, or lets us query, **policy documents**
(laws, regulations, directives, incentives, standards, guidance, official reports) in
that space. Not news blogs, not vendor marketing, not academic-only sites.

## The two ways a source plugs in

1. **Crawl domain** - a website we crawl. Schema in `config/domains/_template.yaml`.
   Required: `name`, `id`, `base_url`, `start_paths`. This is the default when a site
   has no API but publishes policy pages/PDFs.

2. **Structured API source** - a queryable API/open-data endpoint. Schema in
   `config/domains/api_sources.yaml`; routed by `source_type` to a client in
   `src/sources/` (registered in `src/sources/__init__.py`). Prefer this whenever a
   real API exists. If the API fits an existing client's shape, note that; otherwise
   it needs a NEW client (a tier-c spec, no code yet).

Existing structured clients (do not re-propose): riksdagen, uk_bills, legisinfo,
folketing, eurlex_nim, legiscan, govinfo, regulations_gov, dip.

## Access / auth model (so we know "log in vs just pull")

Report exactly one of, per source:
- **none** - open, no key, just fetch.
- **api_key** - free/paid API key. Give the signup URL and the env-var name you'd use.
- **login** - needs an account/session. Our `config/credentials.yaml` supports three
  `auth_type`s: `form` (Playwright fills a login form), `basic` (HTTP basic), `cookie`
  (injected session cookies). Say which fits and what fields are needed.

## Dedup - do not re-propose what we already have

Before proposing anything for your region, READ the matching existing files under
`config/domains/` (e.g. germany.yaml, nordic.yaml, apac.yaml, eu.yaml) and skip any
`base_url` already present. 227 crawl domains + 9 APIs already ship. Net-new only.
Note which existing file each new entry should be appended to (or a new country file).

## Required fields per candidate (capture ALL of these)

- `name`, proposed `id` (lowercase_underscores, unique), `base_url`
- `start_paths` (for crawl) OR `source_type` feasibility (for API)
- **level**: supranational | national | subnational(state/province/Land/region) | local
- **access**: none | api_key(signup URL, env var) | login(auth_type + fields)
- **coverage**: what policy it exposes; map to our taxonomy - `region`, `category`,
  `tags`, `policy_types` (see `_template.yaml` for allowed values), `language`
- **format**: JSON | XML | HTML | PDF
- **practical**: rate limits, docs URL, robots.txt / ToS constraints, update frequency
- **effort tier**: (a) drops into an existing structured client, (b) plain crawl
  domain, (c) needs a new structured client
- **why worth adding** (one line)
- **verified**: you fetched/loaded the URL and it resolves and is on-topic (yes/no +
  what you saw). Do NOT list placeholder or unverified/hallucinated endpoints - if you
  cannot confirm it is live, say so explicitly and put it in an "unverified" list.

## Output

Write your region file to `docs/source-expansion/regions/<region>.md` with two
sections: **Verified candidates** (full fields above, ranked best-first) and
**Unverified / needs-human-check**. Return a 5-line summary: region, # verified
candidates, # tier-a / tier-b / tier-c, and the single highest-value find.
