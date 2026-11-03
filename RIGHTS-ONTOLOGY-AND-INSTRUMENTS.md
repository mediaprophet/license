# Rights Ontology and Applied Instruments

Status: implementation specification; broader integration requirements remain in development

Version: 0.2-draft

Updated: 3 November 2026

This specification makes the rights ontology the semantic centre of the licensing framework. “Data sharing” is treated as an event. The ontology represents the normative relations governing that event and every other relevant act.

The machine-readable vocabulary is in `ontology/rights-instrument-model.ttl`; its JSON-LD context is in `contexts/rights-context.jsonld`.

## 1. Foundational distinction

The framework separates five layers:

| Layer | Question | Examples |
| --- | --- | --- |
| Normative authority | Why does the position exist? | Copyright, statute, contract, valid consent, court order, binding governance rule. |
| Rights ontology | Who holds which position toward whom, over what, in which frame? | Claim/duty, privilege/no-right, power/liability, immunity/disability. |
| Legal instrument | How is the position given legally cognisable form? | IP licence, contract, data-processing terms, contributor agreement, order. |
| Technical instrument | How is the position evidenced or operationalised? | Capability token, signature, verifiable credential, access policy, ledger record. |
| Enforcement and remedy | What happens when the position is disputed or violated? | Review, revocation, restoration, injunction, compensation, appeal. |

A technical instrument does not become its own normative authority merely because it is cryptographically verifiable. A legal instrument does not become technically effective merely because it states a rule. The ontology connects the layers without collapsing them.

The equally central creator rule is:

> Inspectability is not permission; technical access is not permission; wealth is not permission; and humanitarian purpose does not require a natural-person creator to subsidise an unauthorised exploiter.

The ontology therefore represents the creator's claim over grant boundaries, privilege to withhold an ungranted permission, power to grant or condition a licence, immunity against unilateral expansion by a technical system, investments of labour and resources, and remedy pathways. The exploiter's correlative no-right is not converted into a privilege merely because enforcement is costly.

## 2. Jural positions

The framework reuses the Web Civics Hohfeldian vocabulary at `https://ns.webcivics.net/jural/`:

- **Claim / Duty:** A has a claim that B do an action; B bears the corresponding duty toward A.
- **Privilege / No-Right:** A is free, within the defined frame, to act; B has no claim that A refrain merely on that ground.
- **Power / Liability:** A can alter a legal or normative position; B is exposed to that valid alteration.
- **Immunity / Disability:** A is protected from B altering the position; B lacks the relevant power.

Every generated rights statement identifies the holder, counterparty, action, object, purpose, authority, jurisdiction, time, conditions, evidence, lifecycle, and remedy. The word “right” without this decomposition is insufficient for machine evaluation.

## 3. Multi-agent information relations

Possession, receipt, storage, access, computation, inference, and disclosure are different acts. An agent's technical capacity to perform one does not establish a privilege to do it.

For the same information resource, the ontology may express that:

- a natural person holds claims to protection, access, correction, participation, and remedy;
- a collection agent has a narrow privilege to receive defined fields for an authorised purpose and duties of minimisation and provenance;
- a storage agent has custody and security duties but no privilege to use the information for its own benefit;
- an analysis agent may derive specified results but has no privilege to identify a person or disclose source records;
- a disclosure agent has a power to transmit only to identified recipients when stated conditions hold;
- an auditor has a bounded inspection privilege and confidentiality duties;
- a principal or operator bears responsibilities arising from the agents it directs; and
- an excluded agent has no permission under the framework to obtain, process, infer from, or disclose the resource.

Accordingly:

> Technical capability is not normative permission.  
> Data transfer is not transfer of rights.  
> Delegation is not elimination of the principal's responsibility.  
> A ledger assertion is evidence, not an adjudicated fact.

## 4. Rights-statement record

### Human centric rights fabric development requirements

The [project purpose](PROJECT-PURPOSE.md) defines a rights fabric that connects human rights, permissions, duties, relationships, provenance, and remedies across information systems. The individual human is the **principal** in relation to their own human agency and rights. Other agents may represent that human, another human, an entity, or a legal person, or have no representative authority at all. Their actual principal, role, and authority must be recorded rather than inferred from interaction with the affected human. A legal person such as a corporation must not be conflated with a human. Third-party ownership or control of the human's characteristics and properties must not invalidate their human rights.

The project's biometric scope includes **mindware**, encompassing objective and subjective foundations and formations of human experience, understanding, and agency. Representations, observations, and inferences about these characteristics must remain distinguishable from the human. The broader project vocabulary must be mapped explicitly to applicable legal categories rather than silently equated with a statutory definition of biometric data.

The intended model and supporting software need to represent:

- the principal human, each agent's role, other affected humans, and the source and limits of each asserted authority;
- each agent's actual principal or represented entity, permitted uses, legally grounded duties and limitations, and consequences of misuse with their competent decision-maker and remedy pathway;
- separate permissions and duties for collection, storage, inference, disclosure, onward use, correction, retention, and deletion or restriction where applicable;
- separate rights and restrictions concerning identification, influence, interference, profiling, manipulation, and other acts affecting a human or their informational environment, regardless of whether the agent represents that human;
- stewardship grants for specified computational representations of identifiers, recording the permitted acts, purpose, agent, actual principal, context, duration, conditions, and limits on retention, inference, disclosure, and onward use; uses outside those terms are not authorised by the grant;
- the provenance, purpose, uncertainty, and contestability of observations or inferences concerning biometrics and mindware;
- guardianship, supported decision-making, and other representation as distinct relationships, including scope, evidence, duration, review, conflicts, and changes in authority;
- accessible participation by the principal human, their expressed will and preferences, and routes to independent review and remedy; and
- WellFair considerations of welfare and fairness, including discriminatory effects, coercion, exclusion, and whether exercising rights is practical.

Possession of information or credentials is neither proof of representative authority nor a right to perform any particular act. Permission to authenticate using an identifier representation does not imply permission to identify across services, profile, influence, manipulate, disclose, or repurpose it. An agent must establish the applicable basis for each act; any independent legal authority must be recorded separately from a human's grant. Withdrawal or expiry of an agent's authority should trigger reassessment of dependent permissions without purporting to erase every downstream copy or override independently applicable duties. These are development requirements for the ontology, profiles, and runtime systems; this addition does not assert that the current schema or validator implements them.

### Existing rights statement fields

Each statement contains at least:

| Field | Meaning |
| --- | --- |
| `id` | Stable statement identifier. |
| `position` | Claim, duty, privilege, no-right, power, liability, immunity, or disability. |
| `holder` | Agent holding the position. |
| `counterparty` | Agent bearing the correlative position. |
| `action` | Inspect, collect, store, process, infer, derive, modify, disclose, delete, audit, delegate, revoke, or another defined act. |
| `resource` | Work, data element, record, derived artifact, token, service, or other object. |
| `purpose` | Purpose for which the relation operates. |
| `context` | System, release, place, jurisdiction, recipient, environment, and affected-person frame. |
| `authority_sources` | Law, contract, consent, licence, order, or policy grounding the statement. |
| `legal_instruments` | Documents expressing or recognising the statement. |
| `technical_instruments` | Credentials, tokens, policies, controls, and records supporting it. |
| `conditions` | Preconditions, constraints, exceptions, and defeaters. |
| `validity` | Commencement, expiry, termination, revocation, and survival. |
| `delegation` | Whether, to whom, for what, and to what depth authority may be delegated. |
| `evidence` | Provenance and verification required before relying on the statement. |
| `remedy` | Review, correction, restoration, protection, compensation, external relief, or appeal. |

## 5. Authority sources

An ontology statement has an `authority_kind`:

- `statute_or_mandatory_law`;
- `copyright_or_other_ip`;
- `accepted_contract`;
- `valid_consent`;
- `court_or_regulatory_order`;
- `binding_organisational_rule`;
- `project_policy`;
- `humanitarian_principle`; or
- `machine_proposed`.

The last three do not silently acquire the status of binding law. A humanitarian principle may guide construction or be incorporated as a contractual undertaking. A machine proposal remains proposed until an authorised human attests or adopts it.

## 6. Legal instruments

The generator can associate a statement with one or more:

- public inspection licence;
- contract and IP licence;
- controlled evaluation or deployment agreement;
- rights-governed information agreement;
- data-processing or transborder-transfer schedule;
- contributor and assignment instrument;
- consent or participation record;
- confidentiality or trade-secret agreement;
- governance constitution or participation compact;
- settlement, release, judgment, or order; and
- enforcement, appeal, and remedy procedure.

International recommendations and trade instruments may supply source material and legal-review considerations, but do not become private contractual duties without an applicable legal or incorporation route.

## 7. Technical instruments

### 7.1 Token and credential types

| Type | Permitted semantic function |
| --- | --- |
| Capability token | Enables a narrowly scoped technical action. It is not, by itself, proof of a legal privilege. |
| Identity or role credential | Supports an identity, capacity, role, or authority claim. Key control alone does not prove all of these facts. |
| Licence-entitlement token | References an identified licence grant and release. It does not expand that grant. |
| Acceptance receipt | Records assent to identified terms and schedules; formation still depends on applicable law and facts. |
| Delegation token | Records bounded derived authority, including principal, scope, expiry, and depth. |
| Consent token | Records a specific consent assertion, scope, provenance, validity, and withdrawal mechanism. It does not replace other lawful-basis analysis. |
| Obligation token | Records an asserted obligation or discharge state. It is not an adjudicated debt merely because it exists. |
| Provenance attestation | Supports origin, authorship, processing, verification, or custody claims. |
| Revocation record | Records that a capability or asserted authority is no longer usable after the effective event. |

Every technical instrument identifies issuer, subject, principal, audience, resource, action, purpose, jurisdictional frame, issue and expiry time, delegation rules, revocation method, authority source, verification status, and legal-effect classification.

### 7.2 Legal-effect classifications

- `evidence_only` — supports a fact or claim but creates no automatic legal effect;
- `access_control_effect` — changes what the system technically permits;
- `contractually_recognised` — an accepted agreement assigns an effect to the instrument;
- `statutorily_recognised` — applicable law assigns an effect;
- `adjudicated` — a competent body has determined the effect.

The generator defaults every token and ledger record to `evidence_only`. A stronger classification requires an identified authority source and legal review.

### 7.3 Smart-contract execution

Executable code can perform a transaction or access-control transition. It is not presumed to be the whole legal contract. Each deployment must define:

- the governing natural-language instrument;
- the encoded subset and exact program hash;
- oracle and external-data dependencies;
- priority when code and legal text conflict;
- error, exploit, coercion, incapacity, key-loss, and compromise procedures;
- pause, reversal, correction, and human-review mechanisms; and
- whether the operation is evidence, performance, formation, discharge, or another legally reviewed event.

No smart contract may autonomously determine criminal guilt, final civil liability, a Prohibited Harm, personal exclusion, or coercive enforcement.

## 8. Ledger records

A ledger may record release hashes, offer and acceptance, issuance, delegation, exercise, onward disclosure, consent and withdrawal, contribution, attribution, obligations, payments, discharge, suspension, incident, appeal, and remedy events.

The default privacy architecture is:

- store hashes, commitments, pseudonymous references, and protected external pointers rather than personal or sensitive content;
- minimise linkability and public metadata;
- encrypt protected off-ledger records and apply access and retention controls;
- append a correction or superseding status rather than pretending an immutable false statement disappeared;
- support key rotation, compromise marking, revocation, contested status, and provenance;
- never treat consensus or timestamping as proof that an assertion was voluntary, lawful, accurate, or authorised; and
- perform privacy, financial-regulation, sanctions, consumer, evidence, and jurisdiction review before production use.

## 9. Decision and enforcement boundary

Technical enforcement can log, notify, request human input, deny an action outside an active capability, suspend a compromised credential, or preserve evidence. It cannot finally adjudicate disputed rights, impose private criminal sanctions, create contractual assent from prohibited conduct, or make an unaccepted fee an enforceable debt.

Every adverse technical action requires an accountable principal, reason code, evidence reference, proportionality check, notification rule, human review, appeal, correction, and restoration path, except where a short urgent protective action is necessary and prompt review follows.

## 10. Generator output

The generator compiles one reviewed profile into:

1. human-readable legal instruments;
2. a rights-ontology schedule showing every agent's position;
3. JSON-LD rights statements;
4. a technical-instrument and ledger schedule;
5. an acceptance-receipt template;
6. a transborder and rights-governed information schedule where enabled;
7. enforcement and remedy procedures; and
8. a hash manifest and source-to-output report.

The ontology is the design source of truth. The adopted legal text governs the parties according to applicable law; executable policy must never silently override it.

## 11. Contextual assertions, compensation and review

The rights fabric needs to distinguish an observation, inference, allegation, attestation and competent decision. Each has an issuer, context, evidence, permitted audience, validity and challenge history; a signed claim is not thereby true. The [contextual assertion specification](CONTEXTUAL-ASSERTIONS.md) develops these requirements without reducing humans to global reputation scores or treating inferred mindware as the human's own account.

The [contribution lifecycle](CONTRIBUTION-LIFECYCLE.md) separates recorded work and resources from acceptance, valuation, payable obligations, settlement, payout and licensing authority. Each relation can be connected to a legal or governance instrument, but its graph representation does not create the underlying debt or grant. Dependency attribution, historical cost allocation and ongoing maintenance must preserve version and obligation lineage rather than charge recovered costs again.

The [fairness and rights review](FAIRNESS-AND-RIGHTS-REVIEW.md) supplies a contextual review procedure for proposed clauses, processing acts and decisions. Its findings remain distinct from enforceable rights and from computational shape validation. A missing review, uncertain authority or contested material fact must be visible to downstream decisions rather than treated as a favourable default.

These records extend the intended semantic model. They are not additional fields already supported by the current profile schema or generator. Schema changes, migration rules and substantive validation require a separately tested implementation.

## 12. QualiaDB, CML and semantic instruments

The next implementation phase will use QualiaDB's logic systems and semantic tooling to develop the first instruments from these drafts. The [QualiaDB implementation roadmap](QUALIADB-IMPLEMENTATION-ROADMAP.md) records a pinned source review, candidate mappings, staged deliverables and acceptance cases.

CML, **Context Markup Language**, connects original source passages to contextual concepts and selected logic. The intended integration preserves that chain, separates automated proposals from authoritative human review, and retains contradictions and uncertainty. The ontology framing must also be audited against QualiaDB's distinction between descriptions of living humans and constructed artifacts; compatibility is not established by shared vocabulary names.

A semantic instrument packages a specific, versioned method with its dependencies, constraints, evidence and execution contract. It is distinct from a legal instrument, a credential, its visible icon and any result it produces. An execution receipt proves neither legal correctness nor an entitlement to act on the result. Inspection, acquisition, installation, execution permission and legal authority remain separate decisions.

The upstream tooling is in active development. In particular, the inspected generic instrument runner is a labelled identity-transform demonstration, while broader logic evaluators are separate surfaces. The roadmap requires a real, tested connection before claiming that a licensing rule has executed. No current profile, package or receipt is sufficient by itself to establish compensation, adjudicate rights, authorise processing of human biometrics or mindware, or change a licence.
