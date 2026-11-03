# Licence Generator

The repository includes a working, dependency-free Python validator and document assembler. It compiles a creator- and rights-ontology profile into coordinated legal, creator-investment, semantic, information-governance, technical-instrument, deterrence, recovery, and enforcement-funding drafts.

It does **not** decide legal liability, issue demands, calculate a debt, scrape suspected users, select counsel, or initiate enforcement.

The broader [project purpose](PROJECT-PURPOSE.md) includes contribution accounting, verified compensation and expense settlement, cooperative governance, and authorised licence transitions after agreed obligations are fully met. Those are development objectives beyond the current document generator. Generating a bundle does not establish that contributors have been paid or that a licence transition has occurred.

The intended human centric ecosystem also requires a rights fabric for principal human and agent relationships, biometrics and mindware, bounded guardianship authority, supported decision-making, and WellFair purposes of welfare and fairness. These concepts are explained in [Project purpose](PROJECT-PURPOSE.md) and developed as requirements in the [rights ontology specification](RIGHTS-ONTOLOGY-AND-INSTRUMENTS.md). The current generator does not implement or verify these broader capabilities merely by producing rights-related documents.

## Requirements

- Python 3.11 or later; no third-party packages are required.
- Windows users may use `license-generator.cmd`, which is unaffected by PowerShell script-execution policy. `license-generator.ps1` is also provided for environments that permit local scripts. Both launchers detect the Python runtime bundled with Codex desktop.

## Validate a profile

From the repository root:

```powershell
.\license-generator.cmd validate .\examples\public-inspection-profile.json
.\license-generator.cmd validate .\examples\controlled-deployment-profile.json --json
```

Portable Python invocation:

```text
python src/license_generator.py validate examples/public-inspection-profile.json
```

Exit codes are `0` for a valid profile, `1` for validation failure, and `2` for an input or generation error. Warnings do not make a draft invalid, but unresolved legal-review and placeholder warnings prevent responsible adoption.

## Generate an artifact bundle

The output directory must be new or empty. The generator refuses to overwrite a non-empty directory.

```powershell
.\license-generator.cmd generate .\examples\public-inspection-profile.json --out .\dist\inspection-example
```

PowerShell-native equivalent, where local scripts are permitted:

```powershell
.\license-generator.ps1 generate .\examples\public-inspection-profile.json -Out .\dist\inspection-example
```

Generated files:

- `CONTRACT-AND-IP-LICENCE.md`;
- `CREATOR-INTERESTS-AND-INVESTMENT-SCHEDULE.md`;
- `RIGHTS-ONTOLOGY-SCHEDULE.md`;
- `RIGHTS-GOVERNED-INFORMATION-AGREEMENT.md`;
- `TECHNICAL-INSTRUMENTS-SCHEDULE.md`;
- `ENFORCEMENT-AND-REMEDIES-SCHEDULE.md`;
- `RIGHTS-POLICY.jsonld`;
- `VALIDATION-REPORT.md`;
- `ACCEPTANCE-RECEIPT-TEMPLATE.json`; and
- `RELEASE-MANIFEST.json` containing SHA-256 hashes.

The acceptance receipt remains a template until an actual formation system supplies and protects verified party, capacity, authority, time, place, terms, and signature evidence.

## Input model

The normative schema is `schemas/license-profile.schema.json`. Key groups are:

- parties, creator, rights holder, Work, release, governing law and formation;
- creator autonomy, refusal, exclusion, commercial and AI-use boundaries, human/compute/token/capital/opportunity investments, provenance and economic survival;
- agents, principals, resources, persistence classes and jural relations;
- copyright grant boundaries and contractual duties;
- humanitarian purposes, Prohibited Harms, review and appeal;
- rights-governed information roles and OECD-aligned protections;
- transborder destinations, mechanisms, government access, onward transfer and suspension;
- cryptographic tokens, credentials, ledger records and legal-effect classifications;
- exclusions, evidence, deterrence, statutory and contractual remedies, profit and cost recovery, recovery-contingent enforcement funding and creator-prioritised recovery allocation; and
- authority sources with binding and mapping status.

Schema validation is followed by semantic safeguards that reject, among other things:

- orphan artificial agents;
- unknown agent, resource, token, or principal references;
- operational permission in a public-inspection profile;
- any profile that treats public inspection or technical access as permission, disables creator refusal or exclusion, erases creator investment, or omits creator recovery priority;
- pre-event contractual money asserted through public notice alone, while preserving statutory remedies and later voluntary settlement;
- payment as permission for Prohibited Harm;
- autonomous technical adjudication;
- sensitive information in the default immutable ledger design;
- active exclusions without evidence, proportionality, expiry, appeal and legal review;
- cross-border processing without government-access and suspension analysis; and
- adoption without a recorded legal approval.

## Tests

```text
python -m unittest discover -s tests -v
```

The tests cover valid examples, creator autonomy and investment, AI-use boundaries, creator-held relations, recovery priority, deterrent classification, post-event settlements, funding safeguards, reference integrity, contract formation, non-assenter debt, artificial-agent accountability, automated adjudication, ledger privacy, adoption gates, safe output handling, and generated manifest hashes.

## Adoption workflow

The [contribution lifecycle](CONTRIBUTION-LIFECYCLE.md), [contextual assertions](CONTEXTUAL-ASSERTIONS.md) and [fairness and rights review](FAIRNESS-AND-RIGHTS-REVIEW.md) are design specifications for the next phase. Their proposed records and examples are not new fields in `schemas/license-profile.schema.json`. Keep supplementary review records outside generator profiles until a versioned schema, adapter and validation tests explicitly support them. In particular, the existing creator-investment schedule is not a verified payable-obligation or settlement register.

The [QualiaDB implementation roadmap](QUALIADB-IMPLEMENTATION-ROADMAP.md) defines the staged handoff to CML, logic systems and semantic instruments. A future adapter must preserve source versions, authority, privacy restrictions and human-review status through generation. No QualiaDB runtime is currently invoked by this generator.

1. Copy an example to a project-specific profile.
2. Replace every bracketed or example value and use the actual release hash.
3. Complete title, third-party-material, jurisdiction, privacy, transfer, trade, security, exclusion and remedies review.
4. Validate until no errors remain and every warning is deliberately resolved.
5. Generate into a new directory.
6. Have qualified reviewers inspect the generated legal and semantic artifacts together, identify and remediate errors or poorly drafted wording from the development process, including agent-assisted work, and validate consistency with the relevant system behaviour before licensing transition or adoption. Passing automated validation does not establish drafting accuracy or readiness.
7. Record approval identifiers and expiry, regenerate, and independently verify hashes.
8. Implement affirmative acceptance and durable receipt issuance before relying on contractual remedies.
9. Apply the adopted artifacts only to the identified release through an explicit release decision.
