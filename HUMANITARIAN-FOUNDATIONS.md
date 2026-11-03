# Humanitarian Foundations for the Licensing Framework

Status: working outline for legal, humanitarian, and technical review  
Version: 0.1-draft  
Date: 4 August 2026

This document defines the normative and semantic underpinnings of the Humanitarian Equity Licensing Framework. It is deliberately prior to licence drafting and generator implementation: generated clauses must be consequences of an explicit model, not a collection of attractive phrases.

This is not itself a licence and does not make a legal conclusion about any person, organisation, jurisdiction, or use. International instruments do not necessarily bind private parties directly. Where appropriate, a licence may incorporate selected undertakings contractually, but must accurately distinguish applicable law, binding treaty obligations, soft-law principles, project policy, and contractual promises.

## 1. Purpose

The framework exists to govern intellectual and technical works so that they:

- serve the life, dignity, agency, safety, and material needs of natural persons;
- do not facilitate exploitation, coercion, trafficking, slavery, violence, persecution, or remedy avoidance;
- preserve accountability when organisations and artificial agents act;
- recognise and fairly account for useful human work;
- make source, provenance, decisions, and claims appropriately inspectable;
- support effective remedy when harm or breach occurs; and
- permit a defensible transition from protected development to a sustainable commons or other mature ecosystem model.

“Humanitarian” therefore has a positive and a protective pole. Avoiding enumerated harms is necessary but insufficient. A humanitarian system should also support essential needs and increase people's practical ability to exercise their rights, particularly in adverse conditions.

### 1.1 The creator is not outside the humanitarian frame

A natural-person author, researcher, programmer, maintainer, or other creator is an affected person. Their life, time, health, livelihood, autonomy, reputation, property, labour, and moral and material interests cannot be treated as a free input for better-funded actors.

This follows directly from the human-rights sources the framework claims to apply. Article 27(2) of the Universal Declaration of Human Rights and article 15(1)(c) of the International Covenant on Economic, Social and Cultural Rights recognise protection of authors' moral and material interests. CESCR General Comment No. 17 connects those material interests with property, adequate remuneration, and an adequate standard of living, and describes effective administrative, judicial, and other remedies as part of meaningful protection.

Consequently:

- inspectability is not a surrender of control or an implied operational, commercial, or AI-use licence;
- the creator may refuse, condition, price, suspend, or withhold permission, subject to mandatory law and any grant already made;
- technical access, wealth, claimed public benefit, or capacity to litigate does not create permission;
- an excluded or unauthorised actor receives no licence merely because prevention is technically difficult;
- unpaid creator labour is not valued at zero;
- compute, LLM-token, hosting, infrastructure, capital, professional, safety, compliance, opportunity, and enforcement expenditure must remain visible;
- creators may seek cessation, compensation, gain-based recovery, enhanced remedies, and enforcement funding where the governing law or an accepted agreement permits; and
- procedural fairness protects accurate decision-making but must not be transformed into practical immunity for exploitation.

## 2. Semantic foundation

The framework adopts the following concepts from the [Web Civics namespace](https://ns.webcivics.net/). The source graphs consulted are recorded in `WEB-CIVICS-SOURCE-MANIFEST.md`.

| Web Civics graph | Foundational contribution | Generator consequence |
| --- | --- | --- |
| [Selfhood](https://ns.webcivics.net/core/selfhood/) and [Values](https://ns.webcivics.net/core/values/) | A natural person is a living human and bearer of inherent dignity. A legal person or artificial agent is not interchangeable with that human-rights meaning of “person”. | Require explicit agent categories. Never infer natural-person dignity rights for a corporation or AI, and never reduce a human to an asset, account, record, consumer, or economic role. |
| [Agency](https://ns.webcivics.net/core/agency/) | Capacity, assent, representation, principals, operators, duress, responsibility, affected regions, and remedy gaps must be express. | Test authority, capacity, voluntariness, power imbalance, agency chains, and access to remedy before generating a grant or duty. |
| [Jural relations](https://ns.webcivics.net/core/jural/) | “Right” decomposes into claim/duty, privilege/no-right, power/liability, and immunity/disability. | Every operative clause must identify the holder, counterparty, content, frame, and correlative position. |
| [Policy](https://ns.webcivics.net/core/policy/) | Enforcement may log, block, seek human input, or positively prioritise. Mandatory blocking needs a legal ground and appeal path. | Generate a reason, authority, evidence threshold, mode, review path, and remedy for each enforcement rule. |
| [Humanitarian ICT](https://ns.webcivics.net/core/humanitarian-ict/) | Humanitarian ICT supports rights and humanitarian law and should be prioritised in conflict, disaster, low-bandwidth, and other adverse conditions. | Include a positive-purpose profile and essential-needs tests, not only a prohibited-use list. |
| [Agent accountability](https://ns.webcivics.net/core/agent-accountability/) | Trust is behaviourally derived. Completion and safety claims require verification provenance; self-assertion is not verification. | Generated attestations must be evidence-backed and remain unverified until a defined check passes. Artificial-agent outputs require accountable human review. |
| [Permissive Commons](https://ns.webcivics.net/core/permissive-commons/) | Actual production costs and a bounded return can form a self-extinguishing economic obligation. Attribution persists after economic discharge. | Keep permission, compensation, attribution, and discharge as separate states. Require attestable costs and prohibit perpetual rent extraction. |
| [Social Permissive Commons](https://ns.webcivics.net/core/social-permissive-commons/) | Consent is scoped and time-indexed. Capabilities, third-party obligations, co-owned records, and artifact-attached rules have different persistence on exit. | Define what terminates, survives, travels with an artifact, or requires external authority when a relationship or licence ends. |
| [Jurisdiction](https://ns.webcivics.net/core/jurisdiction/), [Sense](https://ns.webcivics.net/core/sense/), and [Tiering](https://ns.webcivics.net/core/tiering/) | Meaning and legal effect depend on place, time, ratification, reservations, legal form, binding status, and curation status. Ambiguity must be exposed rather than guessed away. | Version all sources, resolve the applicable frame, distinguish law from interpretation, and halt for review when a material term has competing meanings. |
| [CML](https://ns.webcivics.net/core/cml/) | Verbatim sources, concepts, machine-proposed mappings, human attestation, provenance, and executable logic are distinct layers. | Preserve a source-to-clause trace. A machine-generated mapping cannot silently become an authoritative legal interpretation. |

## 3. Source and authority discipline

The generator must never flatten every “human-rights source” into the same kind of rule. Each source record requires:

- canonical source and exact provision;
- original promulgating institution;
- legal form: treaty, statute, declaration, recommendation, judicial reasoning, contract, or project policy;
- binding status in the relevant jurisdiction and for the relevant actor;
- entry-into-force period, reservations, amendments, and review date;
- whether the wording is verbatim, amended, summarised, inferred, or machine-generated;
- curation status and identity of the human reviewer;
- integrity hash and retrieval date; and
- the reason the source is relevant to the proposed clause.

The Web Civics concept graphs inspected for this outline mark many mappings `cml:Proposed` and `values:HeuristicDerived`. They are valuable semantic representations and routing aids, but those labels mean that the generator must not present their deontic classification as an adjudicated legal fact. Authority continues to come from the underlying instrument, applicable law, and competent interpretation.

Where a human-rights norm does not directly bind a private party, the generator may offer one of three accurately labelled treatments:

1. a statement of purpose or interpretive principle;
2. a concrete contractual permission, prohibition, duty, power, or immunity; or
3. a compliance reference to independently applicable law.

It must not imply that citing a declaration automatically creates a universally enforceable private-law obligation.

## 4. Foundational principles

### 4.1 Natural-person dignity is the root

Human life and dignity are not merely emotional interests, preferences, economic variables, or platform metrics. The framework begins with the living natural person and their material conditions of existence.

Dignity is inherent. It is not earned through productivity, capacity, citizenship, wealth, technical skill, institutional recognition, or usefulness to another actor. Children, people with disability, people under guardianship, people in detention, displaced people, and people in crisis retain the same foundational dignity.

A corporation, government body, association, or artificial agent may hold legal powers, responsibilities, property interests, and contractual positions. Those positions must not be confused with inherent human dignity. Conversely, recognising that distinction does not erase whatever legal rights an organisation has under applicable law.

### 4.2 Human agency and self-determination

For the human centric ecosystem, the individual human is the **principal** in relation to their own human agency and rights, distinct from other agents. Those agents may act for other humans, corporations, governments, or other entities and legal persons, rather than for the affected human. Their actual principals, authority, permitted uses, limitations, and consequences of misuse must be identified through applicable law and valid legal instruments. Legal personality is not equivalent to being human. A third party must not own or control the principal human's characteristics or properties in a manner that invalidates their human rights. Agency, delegation, guardianship, and technical custody must preserve this boundary.

Enabling humans to own their own biometrics is an instrumental project objective. The project's broader use of **biometrics** includes **mindware**: the objective and subjective foundations and formations through which a human experiences and understands reality, develops meaning, forms intentions, and exercises agency, including human-rights qualities and qualia. Observations and inferred representations of those characteristics are not the human or their lived experience. This usage does not presume that all such characteristics are measurable or fall within a single legal category of biometric data.

The [project purpose](PROJECT-PURPOSE.md) connects this objective to a **rights fabric** governing information acts and relationships, and to **WellFair**, meaning welfare and fairness. Information can be copied, combined, and used to derive further claims without transferring a physical object or extinguishing the principal human's rights. Human rights protections must therefore inform collection, inference, onward use, and remedy, rather than depend solely on possession or ownership of a record.

The rights fabric must determine whether an agent has a right to act, identify, influence, interfere, profile, manipulate, or otherwise affect a human, not merely whether it can represent them. A human with stewardship over their identifiers may grant use of specified computational representations for specified purposes and terms, but that grant authorises no other use. Knowing an agent's principal or permitting a limited interaction does not establish a general right to act upon the human, their biometrics, or mindware. Each additional act needs its own applicable basis and remains subject to human rights protections and legally grounded consequences of misuse.

Humans should be able to understand, choose, refuse, condition, and end their participation. A valid permission or undertaking requires attention to:

- identity of the parties and any principal or representative;
- legal and practical capacity;
- specificity of the action, purpose, data, artifact, recipient, and duration;
- genuine notice and comprehension;
- voluntariness, including absence of deception, duress, dependency abuse, or unacceptable power imbalance;
- separate consent for materially different purposes;
- ability to withdraw future permission where the grant is defined as withdrawable; and
- consequences of refusal or exit.

Consent does not legitimate what law forbids, extinguish non-waivable rights, or erase the interests of affected third parties. Nor is consent the only possible legal basis. The generator must identify the actual basis instead of using “consent” as a universal solvent.

Guardianship and support relationships require particular attention to the principal human's continuing rights, accessible participation, the source and limits of representative authority, conflicts of interest, review, and changing circumstances. Assistance with a decision is distinct from authority to decide on another human's behalf. Neither relationship transfers ownership of the human, their biometrics, or their mindware to an agent. The international foundations include children's best interests, evolving capacities, participation, and privacy under [CRC articles 3, 5, 12, and 16](https://www.unicef.org/child-rights-convention/convention-text), and support for exercising legal capacity with safeguards respecting rights, will, and preferences under [CRPD article 12](https://www.un.org/development/desa/disabilities/convention-on-the-rights-of-persons-with-disabilities/article-12-equal-recognition-before-the-law.html). The project must identify the applicable law and authority in each context rather than infer guardianship or incapacity from disability or dependency.

### 4.3 Rights entail correlated duties and limits on power

The word “right” is too ambiguous for operative generation. Each norm must use a precise jural form:

- **claim ↔ duty:** one party may require conduct from another;
- **privilege ↔ no-right:** one party is free to act and another lacks a claim that it refrain;
- **power ↔ liability:** one party may alter a legal position and another is exposed to that alteration; or
- **immunity ↔ disability:** one party is protected from another altering its legal position.

This matters especially for licensing. A copyright permission is ordinarily a bounded privilege or licence grant; termination is a power with corresponding exposure; a non-revocable protection may operate as an immunity; attribution and payment may be duties correlated with claims.

Every generated norm must state who holds it, who bears the correlative position, what conduct or content it concerns, and the jurisdictional, temporal, release, purpose, and agent frame in which it operates.

### 4.4 Do no material harm

No generated licence may authorise conduct that applicable law makes unlawful. The humanitarian baseline should additionally provide concrete, source-linked prohibitions or restricted-use gates for at least:

- slavery, servitude, forced labour, trafficking in persons, sexual exploitation, and child exploitation;
- killing, torture, cruel treatment, enforced disappearance, unlawful detention, or facilitation of violence;
- persecution or unlawful discrimination;
- coercive manipulation, fraud, impersonation, malware, and abuse of dependency;
- unlawful surveillance, tracking, disclosure, profiling, or interference with privacy and family life;
- denial of accessibility or exclusion that prevents equal participation;
- removal, evasion, or falsification of provenance, consent, audit, accountability, and safety controls;
- use designed to conceal responsible principals or create an accountability vacuum;
- obstruction of evidence, access to justice, or effective remedy; and
- modification whose purpose or reasonably foreseeable effect is to convert a protective capability into a means of committing or concealing these harms.

A clause saying only “do not violate human rights” is inadequate. A generator should produce defined conduct, applicable sources, mental state where relevant, causal connection, evidence standard, exceptions, and enforcement process.

Law and agreement should support peaceful relations between persons through intelligible rights, duties, consent, responsibility, and effective remedy. A person who seeks gain through coercion, exploitation, concealment, or deliberate evasion of accountability must not be able to convert the resulting human cost into an externality borne by victims, contributors, or the public. The framework must therefore connect prohibited conduct to an answerable actor and provide practical means to stop the conduct, preserve proof, protect affected people, and recover lawful enforcement and remediation costs.

Some interests are not monetisable. Death, serious injury, trafficking, enslavement, torture, violence, and the destruction of a person's agency cannot be made permissible by paying a tariff. Where a later evaluation or deployment agreement grants operational permission, these matters must be outside the grant as defined **Prohibited Harms**, also supported by express contractual duties where appropriate. Payment may remedy loss or fund enforcement; it must never operate as an option price for committing or continuing the harm.

### 4.5 Protect essential needs and beneficial use

Humanitarian value is not measured solely by absence of abuse. The Humanitarian ICT graph identifies protection from violence, medical care, humanitarian assistance, protection of detainees and civilians, cultural property, the environment, freedom from torture, and fundamental rights as essential needs.

The generator should allow a project to define positive priorities such as:

- continuity or preferential access in emergencies;
- accessibility and operation under constrained infrastructure;
- safety of vulnerable or affected people over institutional convenience;
- interoperability required for relief and remedy;
- preservation of evidence and provenance;
- responsible disclosure of defects affecting human safety; and
- non-retaliatory reporting and review.

Positive priority must not become an unverified label. A claim that a system is “humanitarian”, “safe”, “anti-trafficking”, or “rights compliant” requires defined criteria and verification evidence.

### 4.6 Fair work, attribution, and material sustainability

Useful human work has material costs. A humanitarian framework must not depend on uncompensated extraction while presenting the result as public benefit.

The creator is included in this protection. A project cannot call itself humanitarian while requiring an individual creator to absorb the costs of production and enforcement so that commercial actors can capture the benefit. Economic survival, continued creative capacity, and meaningful control over exploitation are part of the protected human interest.

The contribution and compensation model should therefore ensure:

- contributors receive clear terms before undertaking requested work;
- acceptance criteria are understandable, consistently applied, and reviewable;
- authorship, provenance, labour time, direct cost, and other agreed inputs are attestable;
- valuation does not discriminate unlawfully and accounts for equal remuneration for work of equal value;
- payment status and any delayed-payment adjustment are auditable;
- economic return is bounded and does not become perpetual rent extraction;
- compensation claims, ownership, licence permissions, and governance rights remain distinct; and
- attribution survives economic discharge unless applicable law and a valid, specific arrangement provide otherwise.

The Web Civics Permissive Commons graph leaves an important design choice open: collective-pool discharge versus per-agent debt. The generator must expose that choice and its consequences; it must not silently select one.

### 4.7 Participation, development, and benefit sharing

People affected by a system should not be treated merely as data sources, test subjects, beneficiaries chosen by others, or risks to be managed. Drawing on the right-to-development and scientific-progress instruments, the framework should support:

- meaningful participation in decisions affecting people;
- fair distribution of benefits and burdens;
- access to the benefits of science and technology;
- protection of authors' moral and material interests;
- community and cultural context;
- accessibility and accommodation; and
- special protection without paternalistic removal of agency.

Participation is not satisfied by publication alone. The process must provide intelligible notice, an effective channel, adequate time, and evidence that input can affect the decision.

### 4.8 Accountability follows the actor chain

An artificial agent cannot be the endpoint of responsibility. Nor should a shell entity or opaque subcontracting chain prevent an affected person from identifying an answerable party.

For each permission or use, the framework should be able to identify:

- the natural person acting;
- any employer, client, operator, principal, controller, or beneficiary;
- the artificial agent or automated process involved;
- who configured, directed, reviewed, and could stop it;
- the affected persons and regions;
- the responsible rights holder or project decision-maker; and
- the forum capable of providing an effective remedy.

Claims made by software agents are claims, not proof. Generated compliance declarations, completion claims, safety classifications, tests, and valuations require independent provenance and a recorded result.

### 4.9 Effective remedy and procedural fairness

Rights without an effective remedy are insufficient. A humanitarian licence should not use distant governing law, forced procedure, anonymity, unaffordable fees, or institutional asymmetry to make remedy practically unavailable.

Upholding rights consumes time, expertise, investigation, preservation, protective action, representation, court access, collection, and remediation resources. An enforcement model is incomplete if it recognises a right while requiring the affected person or rights holder to absorb every reasonable cost of making that right effective. Subject to governing law, formation, proof, proportionality, and procedural fairness, the framework should place supported costs on the responsible wrongdoer and maintain lawful funding mechanisms so enforcement remains practically available.

Enforcement design should include, in proportion to risk:

- notice of the relevant rule and alleged facts;
- preservation and disclosure of appropriate evidence;
- an intelligible reason for a decision;
- opportunity to correct factual error and respond;
- impartial human review and a usable appeal path;
- urgent suspension where necessary to prevent imminent harm, followed by prompt review;
- cure where cure is compatible with safety and law;
- cessation, correction, restoration, restitution, compensation, rehabilitation, satisfaction, or guarantees of non-recurrence as applicable; and
- protection against retaliation.

The priority is protective rather than merely financial: prevent imminent harm; stop continuing harm; secure affected people and evidence; establish accountable human and organisational actors; provide remedy and non-recurrence; then determine compensation, costs, and recovery allocation. Money is a means of accountability and sustainability, not a substitute for safety or consent.

Affected third parties may have interests even when they are not a licensor or licensee. Trafficked persons, children, users, depicted people, data subjects, workers, and communities cannot be made invisible by the bilateral form of a copyright licence.

### 4.10 Context, jurisdiction, and non-discrimination

Applicable considerations may include the governing law chosen in an agreement, mandatory law, place of conduct, physical presence, domicile, place of incorporation, location of deployment, location of effects, treaty status, reservations, and availability of remedy. A routed IP address or apparent region is not conclusive proof of a person's physical presence, residence, citizenship, origin, or agency.

A framework founded on human dignity cannot coherently treat innocent natural persons as harmful merely because of race, ethnicity, ancestry, national origin, or birthplace. Territorial controls may sometimes be necessary because of sanctions, armed conflict, export controls, enforceability, infrastructure risk, or a documented threat, but should be directed to the relevant conduct, actor, deployment, transaction, or location and be necessary, proportionate, time-bounded, reviewable, and no broader than the evidence supports.

Accordingly, the generator must not offer a simple “exclude people from region X” switch. It should require the user to identify:

- the connecting fact: access location, residence, citizenship, deployment location, beneficiary, organisation, or sanctions designation;
- the concrete protective or legal basis;
- evidence and confidence;
- less discriminatory alternatives considered;
- humanitarian and innocent-person effects;
- start, review, and expiry dates;
- exceptions required by law or urgent humanitarian need; and
- correction and appeal procedures.

Excluding all incorporated entities during an incubation phase may be a deliberate project-control policy, but it is not itself a universal humanitarian principle. Organisations include abusive corporations and public authorities, but also worker cooperatives, charities, hospitals, relief organisations, and entities through which natural persons act collectively. The generator must present organisational eligibility as an explicit policy choice, disclose its consequences, and avoid equating every organisation with the same risk.

### 4.11 Persistence and lifecycle integrity

Not every rule ends when access, employment, collaboration, or a licence ends. The generator should classify each right and duty as one of:

- **grant-gated:** ends on expiry, termination, withdrawal, or exit;
- **third-party anchored:** persists until a competent external authority or defined protective condition ends it;
- **co-owned or evidentiary:** cannot be unilaterally erased and remains available to appropriate parties; or
- **artifact attached:** travels with the work or data, including attribution, purpose limitation, confidentiality, no-publication, provenance, and safety duties where valid.

Termination should stop future permission but should not rewrite past lawful events, erase evidence, destroy third-party rights, or retrospectively change the terms under which an identified release was received.

## 5. Conflict and ambiguity handling

The generator should not pretend that every norm composes cleanly. Its conflict process should:

1. establish the agent, action, object, purpose, place, time, release, and affected persons;
2. retrieve potentially applicable legal and contractual frames;
3. verify source status, version, and curation;
4. identify conflicts between permissions, duties, prohibitions, powers, and immunities;
5. protect applicable non-derogable and mandatory rules;
6. apply valid exceptions and defeaters only within their stated scope;
7. prefer a rights-preserving, necessary, and proportionate construction where interpretation is legitimately open;
8. halt and request qualified human review when a material ambiguity remains; and
9. record the decision, reason, evidence, reviewer, and review date.

“More restrictive” is not automatically “more humanitarian”. A restriction can itself cause harm, entrench control, block relief, or discriminate. Protective rules need legitimacy, evidence, proportionality, and contestability.

## 6. Generator rule model

Each generated operative rule should be derived from a structured record containing at least:

| Field | Meaning |
| --- | --- |
| `rule_id` | Stable identifier. |
| `source` | Instrument, law, project policy, rights-holder decision, or agreement provision. |
| `source_status` | Legal form, binding status, curation status, version, hash, and as-at date. |
| `modality` | Claim, duty, privilege, no-right, power, liability, immunity, disability; plus permit, obligate, or forbid for policy execution. |
| `holder` / `bearer` | Agent holding the position and agent bearing the correlative position. |
| `action` / `object` | Precisely defined conduct and material. |
| `purpose` | Permitted, required, or prohibited purpose. |
| `agent_scope` | Natural person, organisation type, public authority, artificial agent, principal, representative, or beneficiary. |
| `context` | Release, phase, environment, time, territory, jurisdiction, and affected region. |
| `preconditions` | Facts that must be established before the norm operates. |
| `duties` | Attribution, payment, notice, audit, safeguards, disclosure, deletion, preservation, or other conditions. |
| `exceptions` / `defeaters` | Applicable-law exceptions, emergency conditions, written permissions, or other narrowly defined overrides. |
| `evidence` | Required provenance, proof, confidence, reviewer, and verification result. |
| `lifecycle` | Commencement, expiry, termination, discharge, survival, and transition events. |
| `enforcement` | Log, prioritise, human review, deny, suspend, terminate, or seek external relief. |
| `remedy` | Notice, cure, appeal, restoration, compensation, and third-party protection. |
| `authority_source` | Law, copyright, accepted contract, valid consent, order, binding rule, project policy, humanitarian principle, or machine-proposed mapping, with actual binding status. |
| `legal_instrument` | Licence, contract, rights-governed information agreement, transfer schedule, consent record, order, or other legal expression. |
| `technical_instrument` | Capability, credential, signature, token, smart-contract execution, or ledger record, with legal-effect classification and revocation. |
| `information_relation` | Collection, storage, processing, inference, derivation, disclosure, transfer, correction, deletion, audit, purpose, roles, and persistence. |

The generator should compile this record into both human-readable language and a machine-readable policy representation. The natural-language licence is an output, not the source of truth for design decisions.

## 7. Non-negotiable generator invariants

The generator must reject or halt an output when any of these invariants fail:

1. Natural-person dignity is assigned to a corporation or artificial agent, or a natural person is modelled merely as an asset, resource, account, or record.
2. A clause purports to authorise unlawful conduct or waive a right that applicable law makes non-waivable.
3. An operative “right” lacks an identifiable jural meaning, holder, counterparty, content, or frame.
4. An organisation or artificial agent can act without a traceable responsible principal or review path.
5. A material compliance, safety, completion, provenance, or compensation claim is treated as verified solely because an interested actor asserted it.
6. A mandatory preventive block lacks a stated basis, evidence requirement, human review, and appeal path.
7. A materially ambiguous term is silently resolved by the system.
8. A grant is not bounded to an identified work/release and defined actions, or its lifecycle is indeterminate.
9. A contribution obligation lacks an agreed valuation basis, evidence, status, and discharge rule.
10. Termination would erase evidence, attribution, accrued claims, or protected third-party interests without a valid basis.
11. A territorial or personal exclusion relies on an imprecise proxy or protected characteristic without necessity, proportionality, legal review, expiry, and remedy.
12. The output describes itself as open source while restricting persons, groups, purposes, modification, distribution, or fields of endeavour.
13. A machine-proposed legal mapping is represented as human-attested, binding, or adjudicated when it is not.
14. Possession, receipt, technical access, a signature, token, credential, hash, smart-contract execution, or ledger record is treated as sufficient normative authority, consent, ownership, capacity, or contractual assent.
15. An artificial agent, shell entity, or subcontracting chain creates an accountability vacuum or obscures its principal, operator, controller, or affected natural persons.
16. Sensitive personal or confidential content is placed in an immutable public ledger when a hash, commitment, protected reference, or off-ledger record can serve the legitimate purpose.
17. A technical system makes a final determination of criminal guilt, disputed civil liability, personal exclusion, Prohibited Harm, or coercive enforcement without competent authority and accountable human process.
18. A rights-governed information flow lacks purpose, role, authority source, persistence, affected-person participation, security, provenance, review, or effective remedy.
19. A transborder flow lacks destination, transfer mechanism, onward-transfer terms, continuing accountability, government-access assessment, suspension trigger, or jurisdiction-specific review.
20. A restriction on information flow, access, territory, nationality, localisation, service, source code, or cryptography lacks the required transparency, legitimacy, necessity, proportionality, non-discrimination, trade-law, or public-interest analysis.
21. Public inspection, technical accessibility, or publication is treated as implied permission to operate, commercialise, train a model on, embed, fine-tune, evaluate, retrieve, redistribute, modify, or derive from the Work.
22. The creator cannot refuse or condition an ungranted use, or an excluded actor is treated as licensed merely because access cannot be perfectly prevented.
23. A creator's labour, compute, LLM-token expenditure, infrastructure, capital, professional work, opportunity, safety, compliance, or enforcement cost is erased or presumptively valued at zero.
24. A profile lacks a creator-held rights relation over the Work, creator-investment evidence architecture, and a creator-remedy pathway.
25. Deterrence, additional damages, account of profits, settlement pricing, or enforcement funding is blanket-rejected instead of being classified by its legal basis, formation route, decision-maker, evidence, legitimate interest, proportionality, and jurisdictional review.

## 8. Decisions the humanitarian foundation does not predetermine

The following are legitimate design decisions, not truths that should be hidden inside the generator:

- whether incubation source is public, access-controlled, or mixed;
- which natural persons may receive an inspection copy;
- whether any organisation type may participate and under what safeguards;
- the exact conduct-based restricted-use profile;
- sanctions, deployment, or territorial controls required for a release;
- whether compensation discharges collectively or per user;
- valuation methods, return cap, currencies, and payment rails;
- when a work transitions and what later licence applies;
- whether evaluation, research, interoperability, security testing, and humanitarian response receive separate grants;
- governing law, forum, arbitration, and urgent-relief mechanisms; and
- who has amendment, exception, suspension, and adjudicative power.

The generator's role is to make these decisions visible, show their humanitarian and legal consequences, detect contradictions, and preserve provenance—not to make contested value choices invisibly.

## 9. Minimum generated artifact set

A complete generation should produce:

1. the human-readable licence;
2. a release manifest identifying the governed material and hashes;
3. a machine-readable RDF/ODRL or equivalent policy graph;
4. a source-to-clause justification report;
5. a rights, authorship, and third-party-material register;
6. a Creator Interests and Investment Schedule plus applicable contribution and compensation terms;
7. any actor, purpose, territory, or sanctions schedule;
8. an enforcement, appeal, and remedy procedure;
9. a compatibility and contradiction report; and
10. a list of unresolved questions and mandatory legal-review flags.

The implemented generator additionally produces a Creator Interests and Investment Schedule, Rights-Ontology Schedule, Rights-Governed Information Agreement, Technical Instruments Schedule, JSON-LD policy graph, acceptance-receipt template, and SHA-256 artifact manifest.

## 10. Principal normative instrument families

The first generator profile should map at least these Web Civics instrument graphs to their authoritative source provisions:

- [Universal Declaration of Human Rights](https://ns.webcivics.net/core/concepts/udhr/);
- [International Covenant on Civil and Political Rights](https://ns.webcivics.net/core/concepts/international-covenant-civil-and-political-rights/);
- [International Covenant on Economic, Social and Cultural Rights](https://ns.webcivics.net/core/concepts/international-covenant-economic-social-and-cultural-rights/);
- [Declaration on the Right to Development](https://ns.webcivics.net/core/concepts/declaration-right-development/);
- [Basic Principles and Guidelines on the Right to a Remedy and Reparation](https://ns.webcivics.net/core/concepts/basic-principles-and-guidelines-right-remedy-and-reparation/);
- [Declaration of Basic Principles of Justice for Victims of Crime and Abuse of Power](https://ns.webcivics.net/core/concepts/declaration-basic-principles-justice-victims-crime-and-abuse/);
- [Protocol to Prevent, Suppress and Punish Trafficking in Persons](https://ns.webcivics.net/core/concepts/protocol-prevent-suppress-and-punish-trafficking-persons/);
- [Forced Labour Convention 1930](https://ns.webcivics.net/core/concepts/forced-labour-convention-1930-no-29/);
- [Equal Remuneration Convention 1951](https://ns.webcivics.net/core/concepts/equal-remuneration-convention-1951-no-100/); and
- [Declaration on the Use of Scientific and Technological Progress in the Interests of Peace and for the Benefit of Mankind](https://ns.webcivics.net/core/concepts/declaration-use-scientific-and-technological-progress-interests/).

Creator-protection mappings must also retain these authoritative external sources rather than relying only on ontology summaries:

- [OHCHR — International Covenant on Economic, Social and Cultural Rights, article 15](https://2covenants.ohchr.org/About-ICESCR.html); and
- [CESCR General Comment No. 17, E/C.12/GC/17](https://docstore.ohchr.org/SelfServices/FilesHandler.ashx?enc=rqNdEMxtlOYr9fSDXiMU0krS4leZY2Rj4s%2FZdozfPaYUIKjkQ5tx1%2BQ5WMNcfkU82X4w5YqIgNztVW2R4FCzKg%3D%3D).

This list is a starting profile, not an exhaustive or automatically applicable bill of terms. Applicability and legal effect must be resolved for the chosen actors, place, time, and conduct.
