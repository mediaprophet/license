# Humanitarian Equity Licensing Framework

Status: working implementation and drafts for legal review

This repository develops a creator- and rights-ontology-centred licensing methodology and generator for software and related works. It treats the natural-person creator as an affected rights holder whose autonomy, labour, compute and LLM-token costs, capital, opportunity, moral and material interests, and enforcement burden must not be externalised to them for an exploiter's benefit. It supports publicly inspectable source without implied use, controlled operational grants, multi-agent information relations, transborder safeguards, cryptographic instruments, deterrence, profit and cost recovery, enforcement funding, contribution provenance, and humanitarian protections.

Nothing in this repository applies to another project or replaces an existing licence unless the authorised rights holder formally adopts identified, reviewed artifacts for an identified release. Generated documents are drafts unless their approval and adoption records establish otherwise.

## Working generator

The dependency-free Python generator validates a JSON profile and assembles a coordinated artifact bundle.

```powershell
.\license-generator.cmd validate .\examples\public-inspection-profile.json
.\license-generator.cmd generate .\examples\public-inspection-profile.json --out .\dist\inspection-example
```

The `.cmd` launcher works when PowerShell script execution is restricted. A PowerShell-native launcher is also provided; invoke it with the execution policy permitted by your organisation.

See [Licence Generator](GENERATOR.md), the machine-readable [profile schema](schemas/license-profile.schema.json), and the [public-inspection](examples/public-inspection-profile.json) and [controlled-deployment](examples/controlled-deployment-profile.json) examples.

The generator does not adjudicate liability, issue demands, calculate debts, scrape alleged infringers, or initiate enforcement.

## Foundations and architecture

- [Humanitarian foundations](HUMANITARIAN-FOUNDATIONS.md) — normative principles, semantic model, generator invariants, and source-to-rule mapping.
- [Creator interests and economic justice](CREATOR-RIGHTS-AND-ECONOMIC-JUSTICE.md) — creator autonomy, human-rights foundations, invested resources, AI-assisted production, exploitation, remedies, and enforcement funding.
- [Rights ontology and applied instruments](RIGHTS-ONTOLOGY-AND-INSTRUMENTS.md) — jural relations, multi-agent rights, legal instruments, tokens, credentials, ledgers, and executable-policy boundaries.
- [Rights and instrument ontology](ontology/rights-instrument-model.ttl) — provisional RDFS/OWL/SHACL vocabulary linked to Web Civics jural, agency, and social-commons terms.
- [Contract and IP architecture](CONTRACT-AND-IP-ARCHITECTURE.md) — contract formation, copyright grant boundaries, acceptance evidence, and non-licensee treatment.
- [Licensing framework](LICENSING-FRAMEWORK.md) — phased release policy, risks, and implementation sequence.
- [Generator schema and decision process](GENERATOR-SCHEMA.md) — input groups, validation gates, decision sequence, and outputs.

## Transborder information and sources

- [OECD transborder-data framework](OECD-TRANSBORDER-DATA-FRAMEWORK.md) — privacy, rights-governed information relations, IP, security, government access, localisation, and trade-law review.
- [OECD source manifest](OECD-SOURCE-MANIFEST.md) — instrument identifiers, source form, status discipline, and generator mappings.
- [Web Civics source manifest](WEB-CIVICS-SOURCE-MANIFEST.md) — integrity-checked linked-data sources used for the humanitarian and semantic foundations.

## Draft legal and governance instruments

- [Public inspection licence](INCUBATION-LICENCE-DRAFT.md) — proposed development-phase terms.
- [Enforcement and remedies](ENFORCEMENT-AND-REMEDIES.md) — creator restoration, deterrence, damages, account of profits, settlement pricing, cost recovery, recovery-contingent funding, evidence, and safeguards.
- [Enforcement schedule](ENFORCEMENT-SCHEDULE-DRAFT.md) — inactive clause-and-calculation template.
- [Exclusions schedule](EXCLUSIONS-SCHEDULE-DRAFT.md) — inactive actor and territorial template.
- [Contributor terms](CONTRIBUTOR-TERMS-DRAFT.md) — chain of title, relicensing, attribution, and compensation.
- [Rights and provenance register](RIGHTS-REGISTER.md) — authorship, ownership, dates, incorporated material, and authority evidence.

## Current legal status

No document in this repository is approved for production use. Example identities, release hashes, transfer mechanisms, financial amounts, governing-law selections, and review records are placeholders. Qualified legal, privacy, trade, security, humanitarian, and technical review is required in the relevant jurisdictions before adoption.
