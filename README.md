# License and rights management for cooperative ecosystems

Status: licensing and rights fabric in development; prototype document generator available; ecosystem prerequisites and adoption review incomplete

**Development and drafting notice:** This work remains in development and uses agents in its research, drafting, and implementation processes. Its wording, terminology, specific details, and statements may contain errors, inconsistencies, omissions, or poorly drafted formulations, including agent-introduced errors. Identifying, reviewing, correcting, and validating these issues is part of the underlying development work. The relevant documentation, legal instruments, and system behaviour must be reconciled and validated before related functional components can transition their licensing to make use of these systems. Published drafts and generated artifacts do not, by themselves, establish readiness for that transition.

`license` develops the Humanitarian Equity Licensing Framework: a methodology, rights model, and supporting software for intellectual property licensing and digital rights management across related ecosystem projects, particularly software. Its scope connects copyright with contract and international trade law, other applicable rights, and human rights including dignity, privacy, and personhood.

The intended outcome is to support cooperative and collaborative projects, including humanitarian information and communications technology (ICT), while recognising contributors' work and applied resources. Projects should be able to record agreed compensation and expenses, establish when the relevant obligations have been fully met, and then authorise a different licence for an identified resulting work or derivative. Attribution, human rights, and the authority to license remain part of that process.

**Start with [Project purpose and ecosystem licensing transitions](PROJECT-PURPOSE.md).** Related projects can link to that explanation of the interim approach, intended outcome, and software still needed to deliver it.

**Public explanation:** [mediaprophet.github.io/license](https://mediaprophet.github.io/license/). The website is published from this repository's Markdown; see [publishing instructions](site/README.md).

The intended framework depends on constituent ecosystem work, including QualiaDB's logic systems, CML and semantic instruments, alongside authority, privacy, contribution, settlement and governance capabilities. Those dependencies must be developed, integrated and validated for the intended use before projects can rely on the corresponding licensing and rights fabric functions. This dependency is a reason for the temporary alternative licences currently used by related projects. Completing the documentation or running the prototype generator does not complete that underlying work.

The framework also develops a rights fabric for human centric information systems, connected to **WellFair** purposes of welfare and fairness. The individual human is the **principal** in relation to their own human agency and rights. Other agents may act for that human or for other humans, entities, or legal persons; their actual principal and authority must be explicit. Enabling humans to own their own biometrics is central to this direction. Here, biometrics extends to **mindware**: the objective and subjective foundations through which a human experiences and understands reality, forms intentions, and exercises agency. Third-party ownership or control of these characteristics and properties must not invalidate the principal human's rights. The intended systems must connect permitted uses, limitations, and consequences of misuse to applicable law, including in guardianship and other agency relationships. The underlying capabilities remain in development.

The rights fabric concerns an agent's right to act, identify, influence, interfere, profile, manipulate, or otherwise affect a human, as well as any authority to represent them. A human exercising stewardship over their identifiers may permit use of specified computational representations for specified purposes and terms. That grant authorises those uses and no others; access to a representation does not create general permission to act upon the human or repurpose their identifiers.

## Interim licensing in related projects

Other ecosystem projects currently use Creative Commons licences as temporary alternatives while the constituent systems needed to use the intended licensing and rights fabric are completed. The interim approach reflects that dependency and the framework's development status. Each project's own licence notice identifies its actual terms. This statement does not specify a Creative Commons licence for this repository or add conditions to another project's existing grant.

The public inspection licence and other instruments in this repository are proposed options for expressly adopted releases. They do not describe the permissions already granted by those other projects. The current generator validates profiles and assembles draft documents; the broader contribution, compensation, governance, and licence-transition systems remain development objectives.

Nothing in this repository applies to another project or replaces an existing licence unless the authorised rights holder formally adopts identified, reviewed artifacts for an identified release. Generated documents are drafts unless their approval and adoption records establish otherwise.

## Content development and next implementation phase

The current content revision develops the useful proposals from the earlier Humanitarian Equity Framework into reviewable specifications. The [source adoption record](HUMANITARIAN-EQUITY-SOURCE-MANIFEST.md) explains what is retained, revised or superseded. The [project plan](PROJECT-PLAN.md) records scope and delivery, and the [review record](CONTENT-REVIEW.md) records findings, verification and remaining work.

| Start here when you need to… | Reference |
| --- | --- |
| Record work, resources, acceptance, valuation, obligations and settlement | [Contribution lifecycle](CONTRIBUTION-LIFECYCLE.md) |
| Review human welfare, fairness, resource burdens and practical remedy | [Fairness and rights review](FAIRNESS-AND-RIGHTS-REVIEW.md) |
| Handle evidence, inferences, credentials, allegations and challenges | [Contextual assertions](CONTEXTUAL-ASSERTIONS.md) |
| Prepare implementation with QualiaDB, CML and semantic instruments | [QualiaDB implementation roadmap](QUALIADB-IMPLEMENTATION-ROADMAP.md) |

These specifications prepare the next phase. They are not additional input fields accepted by the existing generator and do not establish a working payment or rights-enforcement service. The roadmap identifies source versions, candidate integration points and the checks required before semantic tools can support reviewed first drafts.

## Prototype document generator

The dependency-free Python generator validates a JSON profile and assembles a coordinated artifact bundle.

```powershell
.\license-generator.cmd validate .\examples\public-inspection-profile.json
.\license-generator.cmd generate .\examples\public-inspection-profile.json --out .\dist\inspection-example
```

The `.cmd` launcher works when PowerShell script execution is restricted. A PowerShell-native launcher is also provided; invoke it with the execution policy permitted by your organisation.

See [Licence Generator](GENERATOR.md), the machine-readable [profile schema](schemas/license-profile.schema.json), and the [public-inspection](examples/public-inspection-profile.json) and [controlled-deployment](examples/controlled-deployment-profile.json) examples.

The generator does not adjudicate liability, issue demands, calculate debts, scrape alleged infringers, or initiate enforcement.

## Foundations and architecture

- [Project purpose and ecosystem licensing transitions](PROJECT-PURPOSE.md) — reusable explanation for related projects, interim Creative Commons use, cooperative compensation, and intended software capabilities.
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
