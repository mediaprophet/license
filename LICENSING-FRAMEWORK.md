# Humanitarian Equity Licensing Framework

Status: working draft for legal review  
Version: 0.3-draft

Updated: 3 November 2026

This document develops a proposed incubation and release pathway within the broader framework for cooperative licensing, digital rights, contributor compensation, and humanitarian ICT. [Project purpose and ecosystem licensing transitions](PROJECT-PURPOSE.md) explains the shared direction and why other ecosystem projects currently use Creative Commons licences while the intended supporting software is developed.

The public inspection restrictions below describe a proposed licence option for expressly identified releases. They do not replace the Creative Commons or other licences already used by related projects, and they are not mandatory stages for every project using this framework.

Its normative and semantic basis is defined in `HUMANITARIAN-FOUNDATIONS.md`. It is a policy and design document, not itself a copyright licence and not legal advice. The operative terms proposed for the incubation phase are in `INCUBATION-LICENCE-DRAFT.md`. Nothing in this drafting repository applies to another work unless its authorised rights holder formally adopts identified terms for an identified release after legal review. Existing licences remain unaffected.

The generator architecture is further specified in `CREATOR-RIGHTS-AND-ECONOMIC-JUSTICE.md`, `CONTRACT-AND-IP-ARCHITECTURE.md`, `ENFORCEMENT-AND-REMEDIES.md`, and `GENERATOR-SCHEMA.md`. Those documents make the creator's autonomy and material interests primary while distinguishing accepted contractual duties from copyright and other claims against a person who never accepted the contract.

`RIGHTS-ONTOLOGY-AND-INSTRUMENTS.md` makes jural relations the framework's semantic centre. `OECD-TRANSBORDER-DATA-FRAMEWORK.md` applies that model to multi-agent information relations, transborder processing, intellectual property, confidentiality, government access, digital security, localisation, and trade-law review. Cryptographic tokens and ledger records are technical instruments linked to authority; they are not presumed to create rights, ownership, consent, or contractual assent.

## 1. Intended outcome

Under the proposed public inspection option, development source would be **publicly inspectable** so that natural persons can understand and statically review it. That proposed grant would not authorise execution, modification, deployment, redistribution, commercialisation, machine-learning training, or product development. Actual permissions depend on the licence adopted for the particular work.

The natural-person creator is an affected person. Inspectability must not transfer the creator's production and enforcement costs to them while allowing another actor to capture the value. The creator may refuse, condition, price, suspend, or withhold every permission not already granted or required by law. An excluded actor receives no licence merely because perfect technical exclusion is impossible.

The proposed public inspection licence is intentionally not an open-source licence. Open-source licences must permit derived works and cannot discriminate against persons, groups, or fields of endeavour. “Publicly inspectable source” or “source-visible” describes this particular proposal. It is distinct from the interim Creative Commons licences used by other projects and from any later ecosystem licence.

The restrictions are a defensive development posture. They are not a promise that the project will remain under these terms, nor a promise that the finished ecosystem will become permissively licensed. A later licence should be chosen only after the project has working safety, governance, attribution, and compensation systems.

## 2. What this framework can and cannot protect

Copyright can control copying, adaptation, distribution, and other protected uses of the actual code and documentation, subject to applicable statutory exceptions. It does not monopolise the ideas, methods, goals, architecture, or humanitarian concepts expressed by the project. Patent, confidentiality, trademark, access-control, and contract mechanisms address different interests and require separate decisions.

Public disclosure cannot be reversed. A person who can see source may learn from it or independently implement unprotected ideas. A public GitHub repository also carries platform-level permissions: GitHub's terms allow users to view public content and reproduce it on GitHub through features such as forking. An incubation licence must acknowledge those platform permissions rather than purport to revoke them.

If preventing disclosure to an actor or territory is materially necessary for safety, the relevant source must not be placed in a public repository. It should be kept in a private, access-controlled repository and disclosed only under an agreement that identifies the recipient. A public licence is a legal enforcement mechanism, not an access control.

## 3. Phased model

### Phase 0 — restricted development

Sensitive components, threat models, security controls, keys, datasets, and code whose disclosure would itself create unacceptable risk remain private. Access is named, logged, and contractual.

### Phase 1 — public inspection

If this option is adopted, the exact source release is published under the proposed Humanitarian Equity Public Inspection Licence. Eligible natural persons receive only the narrow permissions technically necessary to view and statically inspect an unmodified copy. No operational use or derivative work is authorised by that grant.

### Phase 2 — controlled evaluation

Selected evaluators may receive a separate written evaluation licence. That agreement may permit defined tests in an isolated environment, impose confidentiality and data-handling controls, and set an expiry date. Phase 2 permission is never implied by public access.

### Phase 3 — controlled deployment

Approved deployments use a separate agreement identifying the operator, purpose, territory, users, safety controls, audit duties, compensation, suspension rights, and remedies. Incorporated entities and their agents remain ineligible unless the Licensor deliberately changes that policy in a later framework version.

### Phase 4 — ecosystem licence

When the ecosystem is sufficiently complete, a new licence may be offered for a defined release. The licence could be open source, source-available, cooperative, commercial, public-benefit, or dual-licensed. That decision is not made by this draft.

For a transition based on contributor compensation, the intended milestone is full satisfaction of the agreed compensation and obligation fees for the identified work or derivative. The supporting systems must establish the contribution scope, resource costs, settlement evidence, outstanding disputes, and licensing authority before recording the release decision. Payment alone does not activate new terms.

Each release retains the licence under which its recipients obtained it. The Licensor may offer the same release under additional terms, or release later versions under different terms, but cannot rewrite history by withdrawing rights already validly granted. Relicensing also requires authority over every included contribution.

## 4. Incubation rules

The operative incubation licence should implement these rules:

1. **Natural persons only.** The licensee must act solely in a personal capacity and not for, at the direction of, or for the benefit of a corporation, government, NGO, partnership, association, employer, client, or other organisation.
2. **Static inspection only.** Necessary display, browser caching, and a single unmodified inspection copy may be permitted. Compilation, execution, dynamic testing, deployment, benchmarking, and data processing are withheld.
3. **No derivatives or extraction.** Modification, adaptation, translation, porting, incorporation, and reuse of protectable expression are withheld. This does not claim ownership of unprotectable ideas or prohibit independent work that does not copy protected expression.
4. **No redistribution.** The inspection copy cannot be published, mirrored, shared, sublicensed, sold, or supplied to another person, except for reproduction on the hosting platform that the platform's terms independently require.
5. **No machine-learning ingestion.** Use in training, fine-tuning, evaluation datasets, embeddings, retrieval systems, or code-generation systems is withheld. Ordinary local indexing used only to navigate an authorised inspection copy may be allowed.
6. **No circumvention.** Notices, provenance records, safeguards, rights-management information, and access controls cannot be removed or bypassed.
7. **Reserved rights.** No patent, trademark, production, commercial, or implied licence is granted.
8. **Objective termination.** Permission terminates on material breach after any legally required opportunity to cure. The Licensor may stop offering future access, but the document should not depend on an uncertain claim of arbitrary revocability.
9. **Applicable-law savings.** The licence cannot contract out of rights and exceptions that applicable law makes non-excludable.
10. **No self-executing transition.** A compensation milestone does not itself give a recipient permission to use the work. Only an express later licence or signed permission does that.

## 5. Excluded actors and territories

Exclusions should be based on legally reviewable, objectively verifiable facts. The initial policy excludes organisations and people acting for them. Any territorial rule belongs in `EXCLUSIONS-SCHEDULE-DRAFT.md`, not in the core licence, so it can be reviewed and updated without ambiguous prose.

Blanket restrictions based on birthplace, ethnicity, national origin, or similar inherent characteristics create serious human-rights, anti-discrimination, enforceability, and reputational risks. Australian federal, state, and territory laws may apply to the provision of services. A territorial schedule should therefore prefer current location, ordinary residence, intended location of use, sanctions designation, or a documented threat criterion over ancestry or ethnicity, and must be reviewed by a lawyer in every relevant jurisdiction before activation.

Sanctions compliance is a separate floor, not a substitute for the project policy. Sanctions lists and country measures change; they should be referenced dynamically rather than copied into a licence that will become stale.

## 6. Human-rights and anti-harm controls

“Any breach of human rights” is too indeterminate to be the sole trigger of a copyright licence. During Phase 1, all execution is already prohibited. Later evaluation or deployment agreements should specify prohibited conduct in objectively assessable terms, including:

- trafficking in persons, forced labour, slavery, or sexual exploitation;
- unlawful discrimination, persecution, detention, or violence;
- surveillance, identification, profiling, or targeting that unlawfully endangers a person or protected group;
- evasion of legal responsibility, audit, safety controls, or victim remedies;
- removal or weakening of anti-trafficking, consent, provenance, accountability, or other safety mechanisms; and
- use contrary to applicable sanctions, criminal, privacy, data-protection, or human-rights law.

The relevant agreement should identify controlling instruments, evidence standards, audit rights, suspension procedure, urgent protective action, and a fair dispute process. Human-rights principles should guide governance and interpretation, but they do not replace a chosen governing law.

For any later operational grant, defined conduct involving trafficking, forced labour, exploitation, violence, serious injury, coercion, or deliberate accountability evasion must remain outside the grant and be supported by enforceable contractual duties where appropriate. The agreement should prioritise cessation, affected-person safety, evidence, responsibility, remedy, and non-recurrence. A payment, damages clause, settlement, or retroactive licence must never operate as a price for permission to commit or continue such conduct.

## 7. Contributions, compensation, and future authority

Creator investment is recorded even where no separate contributor requested the work. Human labour, LLM tokens, compute, storage, hosting, capital, professional services, opportunity, safety, compliance, investigation, preservation, and enforcement costs must remain visible in licence pricing, legitimate-interest analysis, settlement, loss, gain-based relief, and funding decisions. Unpaid work is not presumptively valueless.

Public suggestions, issues, pull requests, and code submissions create ownership and expectation risks. The proposed contribution process requires an approved agreement before acceptance. `CONTRIBUTOR-TERMS-DRAFT.md` is a drafting checklist, not an active agreement.

To preserve a single decision-maker's ability to offer future licences, the preferred inbound model is assignment of transferable economic rights to the Licensor, with an alternative broad licence only where assignment is legally unavailable. Moral rights require jurisdiction-specific treatment; in Australia they cannot simply be assigned or licensed away.

The contribution ledger should record authorship, provenance, accepted scope, creation date, governing agreement, value method, payment status, and any third-party dependencies. Recording an “obligation cost” expresses a project accounting claim only when the contribution agreement says how and when it becomes legally payable. An RDF entry alone should not unintentionally create debt.

Compensation and licence permission are separate state machines:

- paying or recording an obligation does not grant use rights;
- receiving inspection permission does not create a right to compensation;
- submitting work does not guarantee acceptance or payment; and
- transition milestones guide the Licensor but do not automatically relicense a release.

The [contribution lifecycle](CONTRIBUTION-LIFECYCLE.md) supplies the detailed procedural design: requested versus unsolicited work, accepted outputs, accrued obligations, valuation evidence, reasoned review, settlement allocation, disputes and maintenance across versions. Its proposed records are not implemented by the current generator. Contributions, benefits and payment mechanisms must remain distinguishable; nonfinancial recognition cannot silently replace agreed money. Upstream licence conditions, separately accepted upstream payment obligations and voluntary support must also remain distinct.

Participation and affected-human interests extend beyond contribution accounting. The [fairness and rights review](FAIRNESS-AND-RIGHTS-REVIEW.md) covers sustainable participation, access and ecological burdens, information rights and practical remedy. The [contextual assertions specification](CONTEXTUAL-ASSERTIONS.md) governs evidence and claims used in those decisions without converting allegations into authoritative facts or general reputation scores.

## 8. Rights and provenance records

Use `RIGHTS-REGISTER.md` as the human-readable source of truth and map it into RDF after the legal model is stable. Each material item should identify:

- title or path and immutable release identifier;
- author or rights holder;
- year of creation and, if different, first publication;
- employment, contracting, assignment, or prior-licence context;
- incorporated third-party material and its licence;
- contributor agreement and compensation record; and
- the outbound licence applied to that release.

The project may accurately say “project lineage and foundational work date to 1999.” A copyright notice should use the creation/publication years of the protected material, not the date on which an underlying idea first arose. The historical Humanitarian Equity Framework repository's available Git history begins in July 2025; older material should be identified item by item rather than giving every new file a 1999 notice.

## 9. Release gates

The Licensor should record a signed release decision before moving a component between phases. At minimum, it should confirm:

- chain of title and third-party licence compatibility;
- review and remediation of wording, terminology, specific details, and drafting errors, including those introduced during agent-assisted development, with the relevant documents, legal instruments, and system behaviour reconciled and validated before a related functional component transitions to use these systems;
- safety and abuse testing appropriate to the component;
- protection of secrets and vulnerable-person data;
- contribution and obligation-cost records;
- governance, audit, incident, and dispute processes;
- the exact release hash and licence text;
- sanctions and anti-discrimination review;
- the jurisdictions, actors, purposes, and environments permitted; and
- whether the change applies only to a new version or also offers an additional licence for an old version.

The historic 80% obligation-fulfilment threshold is not the completion criterion for the compensation-based transition described here. That transition requires full satisfaction of the defined agreed obligations, together with the independent safety, title, sustainability, and governance gates and an authorised licence decision.

## 10. Implementation order

1. Confirm the Licensor's exact legal name, service address, and ownership chain.
2. Obtain advice on governing law, forum, anti-discrimination exposure, sanctions, enforceability, and contributor terms.
3. Decide whether GitHub's public-repository permissions are compatible with the threat model. Move sensitive source private if they are not.
4. Choose a contract-formation mode and implement versioned affirmative acceptance if contractual remedies are required.
5. Finalise the public inspection licence, exclusions schedule, and evidence-backed remedies schedule.
6. Put contributor terms in place before accepting more contributions.
7. Populate the rights register and reconcile it with the RDF ontologies.
8. Apply new licence notices only through an explicit, versioned release decision that identifies existing grants and the rights available for the affected material.
9. Add short file headers that identify the governing root licence without making inaccurate historical copyright claims.

These adoption tasks must be adapted to the chosen release model; public inspection is an option, not a prerequisite for every related project. The next technical phase follows the [QualiaDB implementation roadmap](QUALIADB-IMPLEMENTATION-ROADMAP.md): reconcile the contribution and rights specifications with verified CML and semantic-instrument contracts, implement bounded prototypes, test counterexamples and produce reviewable first drafts before deployment. The [source adoption record](HUMANITARIAN-EQUITY-SOURCE-MANIFEST.md) records why historical compensation, governance and standards proposals were retained or revised.

## 11. Authoritative reference points

- [Australian Attorney-General's Department — Copyright basics](https://www.ag.gov.au/rights-and-protections/copyright/copyright-basics)
- [IP Australia — Computer-related inventions and copyright](https://www.ipaustralia.gov.au/patents/what-are-patents/what-computer-related-inventions-can-be-patented)
- [IP Australia — Who owns intellectual property?](https://www.ipaustralia.gov.au/understanding-ip/who-owns-ip)
- [GitHub Terms of Service — user-generated content](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service#d-user-generated-content)
- [Open Source Initiative — Open Source Definition](https://opensource.org/osd)
- [Creative Commons FAQ — software licensing](https://creativecommons.org/faq/#can-i-apply-a-creative-commons-license-to-software)
- [Australian Human Rights Commission — Racial discrimination](https://www.humanrights.gov.au/employers/good-practice-good-business-factsheets/racial-discrimination)
- [Australian Sanctions Office — Compliance Policy](https://www.dfat.gov.au/international-relations/security/sanctions/compliance-policy)
