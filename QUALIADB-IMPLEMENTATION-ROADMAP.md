# QualiaDB, CML and semantic instrument implementation roadmap

Status: first-draft integration requirements; implementation and cross-repository conformance testing pending

Reviewed: 3 November 2026

## 1. Relationship and scope

The purpose of identifying this related work is to make the licensing framework's dependencies and development status intelligible. QualiaDB, CML and semantic instruments inform how its terminology and intended functions can be expressed and implemented. The constituent capabilities required for an intended use must be completed, integrated and validated before that use of the licensing and rights fabric becomes available. This reinforces the rationale for the temporary alternative licences used by related projects. The roadmap supports that explanation and subsequent implementation; it does not mean the framework is ready for adoption now.

The licensing work is part of the human centric ecosystem being developed with **QualiaDB / Webizen**. This repository supplies licensing purposes, reviewed source interpretations, contribution and compensation requirements, rights relationships, and draft legal instruments. QualiaDB supplies a candidate semantic and computational environment in which those drafts can become inspectable, contextual and testable instruments. The next phase is to use its tools to develop and evaluate the first implementations, preserving the distinction between computational results, human review, valid authority and adopted legal effect.

The source baseline for this review is [QualiaDB commit `58117386c2167e1d713f6e07595f0c708fb45bbf`](https://github.com/mediaprophet/qualiaDB/tree/58117386c2167e1d713f6e07595f0c708fb45bbf), dated 2 November 2026. Its [README](https://github.com/mediaprophet/qualiaDB/blob/58117386c2167e1d713f6e07595f0c708fb45bbf/README.md) describes a local semantic database, query and inference environment, multiple logic families, and WellFair facilities, while explicitly identifying the software as pre-release. These are upstream descriptions, not certification by this repository. This review inspected documentation and selected source files; it did not build QualiaDB, execute its tests, or demonstrate an integration.

This roadmap does not choose a payment rail, require a blockchain, change a project's existing licence, or grant an agent access to human records. The current [license generator](GENERATOR.md) remains the executable baseline here. The new contribution, assertion and review records below are proposed integration contracts, not additional fields already accepted by its JSON schema.

## 2. CML preserves context between source and computation

**CML means Context Markup Language.** The pinned [CML documentation](https://github.com/mediaprophet/qualiaDB/blob/58117386c2167e1d713f6e07595f0c708fb45bbf/docs/manuals/standards/init-draft-standards-wip-main/cml/README.md) describes a concept graph connecting original text, concepts and selected logic. It supersedes earlier inline HTML-tag and `.ctx` proposals. This roadmap therefore targets the concept-graph design, with the actual schema and supported execution surface checked at implementation time.

The [CML vocabulary](https://github.com/mediaprophet/qualiaDB/blob/58117386c2167e1d713f6e07595f0c708fb45bbf/core-ontologies/cml.n3) provides source-span provenance, curation status and logic-application terms. Automated mappings remain proposals. Its exact-equivalence discipline requires authoritative human attestation; similarity or a model's confidence is insufficient. For this project, source text must remain recoverable separately from interpretation, amendments and executable rules.

A licensing clause may thus have several separately reviewable layers:

1. The original source, version and selected passage, with integrity evidence.
2. A proposed concept and its relationship to other concepts, including differences in jurisdiction or meaning.
3. An interpretation identifying the relevant authority, affected humans, agent roles, acts, purposes, dates, exceptions and uncertainty.
4. A proposed rule or constraint linked to a named evaluator and a declared subset of the interpretation.
5. A human review record explaining what was accepted, limited, corrected or left unresolved.

The source can remain authentic while an interpretation is disputed. A correctly evaluated rule can still express an incomplete or mistaken interpretation. Neither a matching hash nor successful evaluation supplies legal authority.

QualiaDB's CML design distinguishes the description of living humans and nature from constructed artifacts. The integration should preserve that modeling discipline explicitly: human observations and characteristics are described and validated, without treating classification as creating or owning the human. Importing an external vocabulary must not silently import all its class axioms. The existing local ontology needs a mapping audit before claims of compatibility with this discipline; this documentation update does not assert that audit has passed.

## 3. Semantic instruments and the observed implementation boundary

The upstream [semantic instruments overview](https://github.com/mediaprophet/qualiaDB/blob/58117386c2167e1d713f6e07595f0c708fb45bbf/docs/work-in-progress/SEMANTIC_INSTRUMENTS_OVERVIEW_WIP.md) describes versioned packages joining concepts, constraints, logic, dependencies, evidence and execution requirements. An icon presents an instrument; a credential asserts something about it; an execution receipt records a use; a result remains a claim. These objects must remain distinct from the human affected by their use.

The [package specification](https://github.com/mediaprophet/qualiaDB/blob/58117386c2167e1d713f6e07595f0c708fb45bbf/docs/work-in-progress/SEMANTIC_INSTRUMENT_PACKAGE_SPEC_WIP.md) is marked work in progress. It is a design reference for shapes, applicability, dependency integrity, permissions, receipts and lifecycle, not a frozen interface that this repository can assume is implemented in full.

Selected implementation evidence narrows what can responsibly be claimed:

| Evidence at the pinned commit | Observed scope | Consequence for this project |
| --- | --- | --- |
| [Semantic instrument module](https://github.com/mediaprophet/qualiaDB/blob/58117386c2167e1d713f6e07595f0c708fb45bbf/crates/qualia-core-db/src/semantic_instruments/mod.rs) | Exposes packaging, resolution, execution, attestation and other components. | Reuse and extend the existing structure after compatibility checks. |
| [Manifest implementation](https://github.com/mediaprophet/qualiaDB/blob/58117386c2167e1d713f6e07595f0c708fb45bbf/crates/qualia-core-db/src/semantic_instruments/manifest.rs) | Declares `0.1.0-demo`; fields are narrower than the WIP specification. | Freeze an explicit adapter contract; do not paste the WIP example and claim conformance. |
| [Generic runner](https://github.com/mediaprophet/qualiaDB/blob/58117386c2167e1d713f6e07595f0c708fb45bbf/crates/qualia-core-db/src/semantic_instruments/execution/runner.rs) | Labels itself a demonstration; `assess` and `recognise` perform an identity transform, with held/refused paths. | A completed demo receipt is not a completed licensing evaluation. Real rule dispatch and semantic validation require implementation and tests. |
| [Conformance test source](https://github.com/mediaprophet/qualiaDB/blob/58117386c2167e1d713f6e07595f0c708fb45bbf/crates/qualia-core-db/tests/semantic_instruments_conformance.rs) | Contains package, demo execution, dependency, credential and presentation cases. | Extend with licensing-specific cases and run the selected suite; presence of tests is not a result from this review. |

This finding concerns the inspected generic instrument runner. It does not imply that QualiaDB's separate logic evaluators are identity transforms. The implementation task is to connect suitable evaluators to a justified instrument contract and demonstrate that connection.

## 4. Candidate mappings and first instruments

The following are proposed mappings. Names in this table describe planned deliverables; they are not registered upstream APIs or new ontology identifiers.

| Licensing requirement | Candidate semantic approach | First bounded deliverable |
| --- | --- | --- |
| Source and terminology reconciliation | CML source spans, concept relations and proposed/attested status | A source-linked concept register for one reviewed draft, including rejected equivalences |
| [Contribution lifecycle](CONTRIBUTION-LIFECYCLE.md) | Separate graph records for activity, output, acceptance, valuation, obligation, settlement and release | A claim-completeness and state-consistency checker using synthetic records |
| Purpose-limited identifier use | Explicit rights statements, contextual grants, deontic conditions and temporal limits | A grant-scope checker that distinguishes authentication from profiling or onward use |
| [Contextual assertions](CONTEXTUAL-ASSERTIONS.md) | Provenance, assertion modality, issuer capacity, visibility and challenge history | An assertion validation instrument that reports missing authority or evidence without deciding truth |
| [Fairness and rights review](FAIRNESS-AND-RIGHTS-REVIEW.md) | Required evidence, impact dimensions, conflict records and review decisions | A review-completeness instrument producing questions and held conditions, without a universal human score |
| Licence-transition preparation | Dependency and authority records, full-obligation checks, readiness evidence and immutable work versions | A transition-readiness report requiring a separate authorised release decision |

The upstream [logic directory index](https://github.com/mediaprophet/qualiaDB/blob/58117386c2167e1d713f6e07595f0c708fb45bbf/crates/qualia-core-db/src/modalities/logic/DIRECTORY_INDEX.md) identifies deontic, N3 and SHACL modules among relevant implementation surfaces. The next phase must inspect their current code and supported profiles before choosing an evaluator. A modality name does not establish support for every legal interpretation or every construct in a standard. Contradictory evidence should remain explicit, with no inference of permission from missing facts.

## 5. Proposed input and output contracts

Each instrument prototype needs a versioned contract whose concrete serialization and field names are settled during implementation. Until then, the following are conceptual requirements.

| Record | Required meaning |
| --- | --- |
| Source bundle | Repository/document identity, immutable version or retrieval evidence, passage selector and digest, source status, jurisdiction and effective dates where relevant, permitted reuse and interpretation provenance |
| Actor and authority bundle | Affected human; invoking agent; agent's actual principal; capacity and authority evidence; distinct permitted acts, purpose, audience and duration; representation and guardianship limits where applicable |
| Work and dependency bundle | Identified work/version, included components, existing licences, rights holders and licensing authority, dependency digests, and accepted obligation allocation |
| Contribution bundle | Separate claim, acceptance, valuation, obligation, settlement and payout records with evidence, dispute status, corrections and access policy |
| Review bundle | Review purpose, affected humans, impact findings, uncertainty, reviewer authority/conflicts, decision reasons, challenge route and conditions for reassessment |
| Execution envelope | Instrument and dependency versions/digests, selected entry point, authorized input references, evaluation time, resource budget, permitted side effects and disclosure limits |
| Result and receipt | Evaluated subset and reasons, unresolved inputs, failed checks, policy and evaluator versions, protected evidence references, result commitment and traceable execution record |

Prototype results should distinguish **satisfied checks**, **failed checks**, **held for missing or conflicting information**, and **not applicable under the recorded scope**. These are proposed result meanings, not upstream enum values. A successful completeness check must not be displayed as a finding of legal validity, fairness, truth, payment finality or permission to release.

Separate the authority to run a check from authority to act on its result. The initial instruments are read-only and operate on synthetic or expressly authorised test inputs. Public packages contain rules and fixtures; sensitive human evidence stays in protected stores. Any public commitments require privacy review for linkability and guessing risks. Execution receipts must not leak identifiers, allegations, private financial details or mindware inferences.

## 6. Staged implementation project

| Stage | Work and deliverables | Exit evidence |
| --- | --- | --- |
| Q1: Baseline and capability verification | Select current supported QualiaDB revision and target; inspect relevant code, schemas, feature gates and build instructions; record differences from this pinned review. | Reproducible build/test record for selected surfaces, capability matrix and explicit limitations. |
| Q2: Source curation and mappings | Encode one draft and its source passages; define conceptual records and mappings; audit local ontology framing; retain human corrections separately from generated proposals. | Source recovery succeeds; automated mappings remain proposals and cannot assert `skos:exactMatch`; authoritative exact equivalence requires signed, authorised human attestation; unsupported mappings remain unresolved. |
| Q3: First semantic instrument | Implement contribution-claim completeness or assertion validation with explicit shapes, fixtures, actual evaluator dispatch, bounded execution and receipt bindings. | Positive and negative fixtures demonstrate substantive checks, not identity transformation; missing evidence returns held. |
| Q4: Rights and impact instruments | Add identifier-use scope and review-completeness checks; integrate accessible inspection, challenge and correction workflows. | Adversarial cases preserve actor/principal and purpose boundaries; protected evidence remains private. |
| Q5: Draft generation bridge | Define adapter from reviewed semantic records to the existing generator profile; report unsupported fields; retain extra records in a versioned companion artifact rather than silently discard them. | Round-trip traceability from source to rules to generated draft; existing generator tests pass; mismatches and information loss are visible. |
| Q6: Transition rehearsal | Evaluate full agreed obligations and release readiness against simulated evidence; record a separate human decision and exact work version. | No payment event alone grants rights; disputes, missing authority and unresolved drafting defects block the proposed transition. |
| Q7: Deployment proposal | Complete independent legal, privacy, accessibility, security, accounting and operational review for a selected use case. | A separately approved adoption package specifies jurisdiction, responsibilities, monitoring, remedies, rollback and real settlement interfaces. |

Q1–Q6 are development and rehearsal stages. Q7 does not become approved by completing a technical test suite. Settlement integrations, live human data, payments and consequential deployment require their own explicit implementation scope and authority.

The upstream [finite project compensation proposal](https://github.com/mediaprophet/qualiaDB/blob/58117386c2167e1d713f6e07595f0c708fb45bbf/docs/manuals/standards/qualia-decentralized-network-fabric/finite-project-compensation.md) provides additional design material: finite obligations, separation of creation recovery from operating costs, deduplicated settlement, and a distinction between funds collected and contributors actually paid. It is expressly proposed, with implementation pending. Its actor-class charging and humanitarian-access profile is an optional candidate for later review; this repository does not adopt it as a universal policy. Any selected profile must preserve existing grants and establish applicable agreements and authority.

## 7. Acceptance scenarios for the next phase

| Case | Required result |
| --- | --- |
| A model equates the project's broad “biometrics” with a narrow statutory term. | Retain the proposed relation and difference in scope; require review before an authoritative mapping. |
| An identifier grant permits authentication, while an agent for an unrelated company asks to profile the human. | Report that the profiling act is outside that grant; do not infer a different legal basis from access. |
| Two agents present conflicting guardianship authority. | Preserve both claims with restricted evidence, hold dependent action and support the human's participation and competent review. |
| A signed allegation is supplied as an adjudicated fact. | Preserve origin verification separately; reject the asserted status unless supported by appropriate decision evidence. |
| An unsolicited contribution has recorded hours but no accepted payment obligation. | Keep activity and claim records; do not create a payable debt. |
| A project has received funds but has not paid the contributor. | Show receipt, obligation discharge and beneficiary payout separately; do not claim the contributor has been paid. |
| The same settlement receipt is submitted through two services or a renamed derivative. | Apply the accepted allocation once and preserve lineage; no duplicate recovery. |
| Full obligations are met but dependency licensing authority is unresolved. | Financial checks may pass; transition readiness remains held. |
| A rule dependency is missing, changed, revoked or incompatible. | Refuse activation or hold the affected check according to the declared policy; retain historical receipts. |
| A human corrects a model's inference about their intentions. | Append a reviewable correction, reassess dependent results, and preserve access restrictions without treating the inference as the human. |
| A package collects excessive information to compute a fairness score. | Fail the declared privacy and purpose checks; require a narrower review with justified evidence. |
| QualiaDB's demo runner returns a completed identity-transform receipt. | Label it as demonstration evidence only; it cannot satisfy licensing-instrument acceptance. |

## 8. Unresolved decisions and handoff requirements

Before coding the adapter, decide and record the supported QualiaDB target, package version, concrete shape language/profile, digest and canonicalisation rules, identifier handling, private evidence references, and authentication of reviewer actions. Confirm which constraints execute on each target and which require external checks. Keep unsupported requirements visible rather than serializing them as if enforced.

Review the existing local RDFS/OWL/SHACL vocabulary against the CML framing boundary, including humans, agents and constructed artifacts. Determine how disputes, expiry and revocation propagate across cached results and delegated authority. Specify supported decision and notification processes before adverse action is allowed. None of these questions can be resolved merely by importing an ontology or signing a package.

The implementation handoff consists of this roadmap, the pinned evidence above, the [contribution specification](CONTRIBUTION-LIFECYCLE.md), [assertion specification](CONTEXTUAL-ASSERTIONS.md), [review specification](FAIRNESS-AND-RIGHTS-REVIEW.md), and reviewed legal drafts. Each work item should record its responsible maintainer, inputs, outputs, accepted semantic mappings, fixtures, review findings and execution evidence. Errors introduced during agent-assisted drafting or implementation must be corrected before the affected instruments can support a licensing transition.
