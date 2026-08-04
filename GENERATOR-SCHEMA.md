# Licence Generator Input Schema and Decision Process

Status: implemented specification  
Version: 0.1-draft  
Date: 4 August 2026

This document defines the implementation contract for the humanitarian licence generator. The normative JSON Schema is `schemas/license-profile.schema.json`; the dependency-free implementation is `src/license_generator.py`; and usage is documented in `GENERATOR.md`. Validation and generation do not approve legal terms.

## 1. Design rule

The generator is a constrained compiler, not an autonomous lawyer. It transforms a reviewed policy profile into a coordinated artifact set, preserves source-to-clause provenance, and halts when a requested outcome lacks authority, evidence, proportionality, or a reliable legal mechanism.

## 2. Required profile groups

| Group | Core fields | Output consequence |
| --- | --- | --- |
| `profile` | identifier, schema version, status, owner, reviewers, timestamps | Version and audit metadata. |
| `rights_holder` | legal identity, address, authority, title evidence, service channel | Party, standing, notices, signature block. |
| `creator_protection` | creator agents, retained control, refusal and exclusion, AI-use boundary, investments, provenance | Creator Interests and Investment Schedule plus validation of creator autonomy and material interests. |
| `work` | title, type, paths, release ID, hashes, authors, third-party material | Defined Work and release manifest. |
| `jurisdiction` | governing law, forum, relevant conduct/effect locations, mandatory-law checks | Choice-of-law language and legal-review flags. |
| `release_phase` | restricted, public inspection, evaluation, deployment, ecosystem | Available grants and mandatory controls. |
| `formation` | mode, offeree identity, authority, acceptance event, consideration, receipt | Contract status and enforceability evidence. |
| `agents` | natural person, legal entity, artificial agent, principal, operator, beneficiary | Eligibility, attribution, and accountability chain. |
| `resources` | work, information, derived artifact, sensitivity, authority, persistence class | Objects governed by rights relations. |
| `rights_relations` | jural position, holder, counterparty, action, resource, purpose, authority, evidence, remedy | Human-readable and JSON-LD rights schedules. |
| `grant` | protected acts, permitted acts, purpose, system, territory, duration, transferability | IP permission and boundaries. |
| `exclusions` | legal/protective basis, connecting facts, evidence, exceptions, expiry, review | Schedule or mandatory halt. |
| `humanitarian` | positive purposes, affected persons, essential needs, prohibited harms, safeguards, non-monetisable interests | Purpose, priority, safety, and remedy clauses. |
| `data_governance` | controllers, processors, affected agents, categories, purposes, OECD principles, transfers | Rights-Governed Information Agreement. |
| `technical_instruments` | type, issuer, subject, principal, authority, effect, crypto, expiry, revocation | Token, credential, acceptance, and execution schedule. |
| `ledger` | recording mode, privacy, correction, revocation, key compromise, review | Ledger safeguards and evidence policy. |
| `enforcement` | event classes, evidence thresholds, reviewer, urgent measures, appeal | Enforcement and review procedure. |
| `sources` | authority, URL, version, hash, legal status, mapping status | Source manifest and justification report. |

## 3. Formation schema

`formation.mode` must be one of:

- `public-notice-only`;
- `click-accepted`;
- `signed-standard-form`;
- `negotiated`; or
- `deed-or-jurisdictional-equivalent`.

If `formation.mode` is not `public-notice-only`, the profile must identify offer, acceptance, intention, consideration or formal substitute, party identity, capacity, authority, terms hash, release hash, timestamp, receipt, and incorporated schedules.

If `formation.mode` is `public-notice-only`, the generator must not represent a pre-event contractual amount as a debt against a non-assenter. It must still generate creator-control language, statutory-remedies reservations, profit-recovery and additional-damages pathways, evidence and investment schedules, enforcement funding, and non-binding settlement or retroactive-licence offers. A later settlement may create obligations when separately accepted.

## 4. Rights-relation record

Each operative rule is stored as:

| Field | Meaning |
| --- | --- |
| `id` | Stable identifier. |
| `position` | Claim, duty, privilege, no-right, power, liability, immunity, or disability. |
| `holder` | Agent holding the position. |
| `counterparty` | Agent bearing the correlative position. |
| `action` | Defined conduct. |
| `resource` | Work, information, system, copy, derived artifact, benefit, or other subject. |
| `purpose` | Permitted, restricted, or prohibited purpose. |
| `context` | Release, phase, time, place, system, agent, and affected-person frame. |
| `authority_sources` | Law, copyright, accepted contract, valid consent, order, binding rule, or identified policy. |
| `legal_instruments` | Documents expressing or recognising the position. |
| `technical_instruments` | Tokens, credentials, controls, or evidence linked to—but not creating—the authority. |
| `conditions` | Preconditions, constraints, exceptions, and defeaters. |
| `evidence` | Facts and provenance needed to establish application or breach. |
| `validity` | Start, end, termination, revocation, discharge, survival, and transition. |
| `delegation_depth` | Maximum permitted derived-authority depth. |
| `verification_status` | Proposed, attested, verified, disputed, or adjudicated. |
| `remedy` | Cessation, restoration, compensation, affected-person protection, appeal, or external relief. |

## 5. Financial-remedy schema

Every component must have:

- `basis`: statutory, contractual, settlement, judgment, avoided-licence, profit-recovery, additional-damages, creator-investment, enforcement-cost, funding, or policy basis;
- `formation_stage`: statute without assent, pre-event contract, post-event agreement, judgment/order, or internal policy;
- `requires_assent`: boolean;
- `remedy_character`: compensatory, restitutionary, deterrent, protective, cost recovery, settlement price, or funding allocation;
- `trigger`: precisely defined event;
- `legitimate_interest`: creator and other protected interests;
- `creator_interest_components`: labour, compute, capital, opportunity, control, attribution, pricing, response, and other supported interests;
- `valuation_method`: formula and evidence source;
- `evidence_basis`: contemporaneous records supporting the component;
- `proportionality_analysis`: relationship between the amount and protected interests;
- `amount_or_range`: currency and date;
- `causal_link`: connection to the trigger;
- `cap_and_floor`: with justification;
- `duplication_group`: prevents double recovery;
- `becomes_payable_when`: acceptance, due date, settlement, judgment, or other lawful event;
- `review_and_dispute`: reviewer, response time, appeal, correction;
- `legal_review`: jurisdiction, reviewer, date, expiry; and
- `recovery_allocation`: affected-person, costs, contributor, reserve, or project pool.

Deterrent intent is not excluded. Words such as `punitive`, `fine`, `bounty`, `additional`, `enhanced`, or `exemplary` trigger accurate characterisation and jurisdictional review; they are not treated as legal bases by themselves. Recovery-contingent enforcement rewards are represented under a separate funding agreement and may be used where lawful.

## 6. Decision sequence

```text
1. Identify creator, rights holder, exact Work, retained control, and invested resources
   -> halt if title or incorporated-material authority is incomplete
2. Determine release phase and disclosure risk
   -> require access control if disclosure itself creates unacceptable harm
3. Resolve parties, principals, capacity, authority, and affected people
4. Select formation mode
   -> if monetary contract remedies requested without affirmative assent, halt
5. Define the copyright grant and classify every term
   -> distinguish grant boundaries, conditions, covenants, notices, and procedures
6. Apply mandatory-law, humanitarian, jurisdiction, and exclusion checks
   -> put defined Prohibited Harms outside any operational grant; payment cannot authorise them
7. Build creator-investment, economic-survival, lifecycle, evidence, notice, cure, urgent-protection, and appeal rules
8. Compile rights relations and ensure technical capability is not treated as normative authority
9. Validate rights-governed information, transborder, government-access, trade, token, and ledger records
10. Classify each proposed enforcement event
   -> contract breach / outside grant / non-licensee / exception / third-party harm
11. Validate every financial and enforcement-funding component
   -> creator interests, basis, formation stage, character, evidence, proportionality, valuation, cap, non-duplication, payable event, funding control
12. Generate artifacts, JSON-LD policy, receipt template, validation report, and hash manifest
13. Run contradiction, compatibility, unfair-term, penalty, privacy, trade, security, and accessibility checks
14. Require recorded human and legal approval before adoption
```

## 7. Generated artifacts

A successful run produces the exact bundle documented in `GENERATOR.md`: Contract and IP Licence; Creator Interests and Investment Schedule; Rights-Ontology Schedule; Rights-Governed Information Agreement; Technical Instruments Schedule; Enforcement and Remedies Schedule; JSON-LD policy; Validation Report; Acceptance Receipt Template; and SHA-256 Release Manifest.

## 8. Hard failures

In addition to the invariants in `HUMANITARIAN-FOUNDATIONS.md`, generation fails when:

- a contract is asserted without offer-and-acceptance evidence;
- prohibited conduct is treated as acceptance;
- an excluded person is simultaneously granted permission for the excluded act;
- a contractual charge is asserted against a non-assenter;
- copyright remedies are described as a privately fixed statutory tariff;
- a monetary component lacks a legal basis, valuation record, payable event, or dispute path;
- recovery would be duplicated;
- enforcement costs are unlimited or recoverable regardless of reasonableness;
- a deterrent or multiplier lacks a classified legal basis, formation stage, supported creator interest, evidence, proportionality analysis, competent decision-maker, and review;
- a fee, damages clause, or settlement would operate as an option to cause or continue a Prohibited Harm;
- enforcement funding conflicts with professional rules;
- a settlement price is labelled an existing debt; or
- a machine is the final decision-maker for liability, exclusion, or coercive enforcement.
- a technical token, credential, signature, hash, smart-contract execution, or ledger assertion is the sole asserted source of normative authority;
- a ledger stores sensitive content in the default immutable-record model;
- an artificial agent has no traceable principal or accountable human review;
- a cross-border information flow lacks an accountable role, mechanism, government-access assessment, continuing protection, onward-transfer terms, suspension trigger, or remedy; or
- an adopted profile lacks a complete, current legal approval record.
- creator refusal, conditional licensing, exclusion, economic survival, investment provenance, AI-use control, or creator recovery is disabled or omitted;
- public inspection or technical access is treated as permission; or
- creator/rightsholder restitution is absent from the leading recovery priorities.

## 9. Implemented first-version boundary

The first software version is a validator and document assembler. It does not calculate legal liability, scrape alleged infringers, issue invoices, send demands, initiate debt collection, select lawyers, or make autonomous enforcement decisions.

The implementation supports public inspection and controlled-deployment examples, creator protection and investment records, multiple agents and resources, rights relations, rights-governed information, transborder transfer records, technical instruments, ledgers, exclusions, statutory and contractual remedies, deterrence, profit and cost recovery, and enforcement-funding records. Every expanded use remains subject to the relevant legal and professional review gates.
