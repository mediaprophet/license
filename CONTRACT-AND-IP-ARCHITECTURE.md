# Contract and Intellectual-Property Architecture

Status: working design for legal and product review  
Version: 0.2-draft

Updated: 3 November 2026

This document defines how a generated instrument should combine copyright permission with a contract. It is not legal advice and is not an operative agreement.

## 1. Two legal pathways, not one fiction

The generator must distinguish two pathways.

### A. Accepted contract and licence

An identified eligible party is shown an identified version of the terms, affirmatively accepts them, supplies any required consideration, and receives the stated copyright permission. Contractual promises, payment duties, dispute procedures, audit duties, and agreed-remedy provisions may then operate to the extent permitted by applicable law.

### B. No licence or no proven contract

An excluded person receives no permission. A person who copies, adapts, communicates, or otherwise deals with protected material outside an applicable grant may face copyright remedies, but publication of a fee schedule does not by itself prove that person agreed to a contract or incurred a contractual debt.

This separation is mandatory. The generator must not describe an unaccepted charge as a debt, invoice an alleged infringer as though liability has been adjudicated, or imply that copyright law automatically enforces a private fee schedule.

It is equally mandatory that this separation not be used to erase the creator's interests. A non-assenter receives no contractual grant, but may remain exposed to copyright, confidentiality, technological-protection, gain-based, injunctive, regulatory, or other remedies. Public inspection and technical access do not imply operational, commercial, model-training, embedding, evaluation, fine-tuning, retrieval, or derivative-use permission. The creator may decline to offer a retroactive licence.

## 2. Instrument stack

A production release should use coordinated, versioned artifacts:

1. **IP licence:** identifies the protected Work and grants narrowly defined permissions subject to stated conditions.
2. **Contract terms:** record the parties' promises, consideration, warranties, procedures, financial duties, and remedies.
3. **Release manifest:** binds the exact work, licence version, schedules, and cryptographic hashes.
4. **Acceptance record:** proves who accepted what, when, how, with what authority and what notice.
5. **Exclusions and eligibility schedule:** determines whether a grant is available; it is not a substitute for assent.
6. **Remedies schedule:** states supported pre-estimates and recovery rules for accepted contracts.
7. **Non-licensee notice:** reserves statutory and other rights without falsely asserting a contractual debt.
8. **Creator Interests and Investment Schedule:** records retained choice, labour, compute and token costs, infrastructure, capital, opportunity, professional work, provenance, commercial value, enforcement burden, and recovery treatment.
8. **Rights-Ontology Schedule:** states each agent's Hohfeldian position, authority, action, resource, purpose, persistence, evidence, and remedy.
9. **Rights-Governed Information Agreement:** governs collection, storage, processing, inference, disclosure, transborder flow, participation, and social-relation persistence.
10. **Technical Instruments Schedule:** classifies tokens, credentials, signatures, smart-contract executions, and ledger records without treating them as self-originating legal authority.

The licence and contract may appear in one signed or click-accepted document, but their different legal functions must remain explicit.

The rights ontology is the semantic source of truth for design. The adopted legal text governs according to applicable law. Technical policy implements or evidences selected relations and must not silently override either.

## 3. Contract formation gate

When contractual enforcement matters, the generator should require a controlled acceptance flow. At minimum it records:

| Field | Requirement |
| --- | --- |
| `offeror` | Full legal identity, authority, service address, and rights-holder capacity. |
| `offeree` | Verified legal identity and, where relevant, age and contractual capacity. |
| `authority` | Personal capacity or authority to bind a named principal; no ambiguous agent account. |
| `offer` | Complete, readable terms and every incorporated schedule shown or made readily available before acceptance. |
| `acceptance` | Unambiguous signature or unticked click-to-accept control linked to a specific version. |
| `consideration` | Payment, reciprocal promise, controlled access, or another lawyer-approved basis; use a deed or other valid form if required. |
| `intention` | Express intention to create legal relations. |
| `time_and_place` | Timestamp, applicable location evidence, language, and any cooling-off or withdrawal rule. |
| `evidence` | Terms hash, release hash, acceptance receipt, notice version, account identifier, and tamper-evident audit record. |
| `mandatory_law` | Consumer, small-business, privacy, accessibility, sanctions, capacity, and unfair-terms checks. |

The accepting control should say substantially: “I have read and agree to the identified Contract and IP Licence and incorporated schedules.” The system should issue a durable receipt and allow the person to retain the accepted text.

Merely visiting a page, receiving a repository URL, or having notice that terms exist is not the framework's preferred evidence of a contract. If a release remains publicly accessible without affirmative acceptance, the generator must classify it as `public-notice-only` and must not rely on contractual fees against a viewer.

## 4. Copyright grant structure

The licence should identify:

- the copyright owner or authorised licensor and chain of title;
- the Work by manifest, version, path, and hash;
- third-party and public-domain material that is outside the grant;
- the relevant protected acts, such as reproduction, adaptation, communication, publication, and distribution;
- the acts affirmatively permitted, the purposes, people, places, systems, and period covered;
- conditions that must be satisfied for the permission to arise or continue;
- contractual covenants that remain promises even when their breach does not place an act outside the copyright grant;
- statutory exceptions and rights that cannot lawfully be excluded; and
- termination, cure, survival, and the treatment of copies made while permission was valid.

The generator must label each operative term as one or more of:

- `grant_boundary` — an act was never licensed;
- `condition` — permission depends on the term, subject to legal construction;
- `covenant` — a contractual promise with contractual remedies;
- `representation_or_warranty` — a statement on which acceptance relies;
- `statutory_notice` — a reservation or explanation of rights under law; or
- `procedure` — notice, evidence, review, cure, dispute, or enforcement machinery.

Calling every promise a “condition” does not make it one. The source-to-clause report must explain why a term limits the grant, creates a contractual duty, or does both, and legal review must consider how the chosen law characterises it.

## 5. Eligibility and excluded actors

Eligibility is a precondition to the IP grant. The contract should require the acceptor to state whether they act personally or for a principal and to identify any principal. A false eligibility statement may be a contractual representation or misrepresentation if a valid agreement exists, but it does not justify an arbitrary punitive invoice.

For an excluded actor:

- no IP permission is granted;
- the system should refuse controlled access where lawful and technically possible;
- any infringement claim proceeds under applicable copyright and other law;
- the rights holder may make a separately identified settlement or retroactive-licence offer; and
- money becomes payable only through a valid agreement, an applicable law, or an order of a competent body.

If exclusion is safety-critical, access control is required. A public repository cannot reliably keep the source from an excluded actor.

## 5A. Prohibited harms in operational agreements

An evaluation or deployment agreement that permits operation must define a category of **Prohibited Harms** using specific conduct, causal connection, mental state where relevant, evidence, exceptions, and controlling legal or policy sources. It should include at least the applicable forms of trafficking, forced labour, slavery, exploitation, violence, serious injury, unlawful surveillance, persecution, coercion, and deliberate evasion of accountability identified in `HUMANITARIAN-FOUNDATIONS.md`.

The architecture should treat a Prohibited Harm as:

- outside the IP grant for the relevant act, purpose, system, actor, or deployment;
- an express contractual prohibition and duty to prevent, stop, report, preserve evidence of, and remediate the event where valid and proportionate;
- grounds for urgent suspension or termination subject to prompt accountable review;
- incapable of authorisation merely through payment of damages, a fee, or a retroactive licence price; and
- connected to statutory, regulatory, criminal, tort, privacy, victim-support, or other pathways where the bilateral licence is insufficient.

The agreement should identify the responsible natural person, operator, principal, controller, and beneficiary; require disclosure of material agency chains; and prevent subcontracting, automation, or a shell entity from creating a remedy gap. If affected persons are intended to have directly enforceable contractual rights, the instrument must expressly establish that result using a mechanism recognised by the governing law; otherwise it must not falsely imply that they are parties or beneficiaries.

## 6. Breach classification

The enforcement engine must first classify the event:

1. **Licensed and compliant:** no enforcement.
2. **Contract breach inside the copyright grant:** contractual cure and remedies; do not automatically call it infringement.
3. **Act outside a grant boundary:** potential copyright infringement plus any contractual claim.
4. **Post-termination act:** assess whether the act requires permission and whether termination was valid.
5. **Excluded or non-assenting actor:** statutory or other non-contractual claim; no assumed contractual debt.
6. **Mandatory exception or defence:** preserve the legally protected act.
7. **Third-party harm or illegality:** protective, regulatory, criminal, tort, privacy, or victim-remedy pathways may be more important than the bilateral licence.

The generator must prevent double recovery for the same loss and must not use contract drafting to erase non-excludable rights.

## 7. Adoption modes

| Mode | Formation evidence | Suitable use | Contractual monetary terms |
| --- | --- | --- | --- |
| `public-notice-only` | Notice and release records only | Publicly inspectable source | Do not rely on them against non-assenters. |
| `click-accepted` | Identity, complete terms, affirmative click, receipt | Controlled inspection or evaluation | Possible after jurisdiction and fairness review. |
| `signed-standard-form` | Electronic or wet signature and schedules | Higher-risk access or deployment | Possible, with consumer/small-business unfair-term review. |
| `negotiated` | Signed agreement and negotiation record | Organisational or high-risk deployment | Tailored remedies, security, insurance, and audit terms. |
| `deed_or_equivalent` | Formal execution satisfying chosen law | Where consideration is doubtful | Counsel must confirm form and effect. |

The generator should default to `click-accepted` for a natural-person inspection licence if contractual remedies are required. It should halt if the requested monetary enforcement depends on `public-notice-only` formation.

## 8. Australian reference points

Under the current Australian Copyright Act, doing or authorising a protected act without the owner's licence can infringe copyright, subject to the Act. Section 115 permits a court to grant an injunction and either damages or an account of profits; the court may award additional damages after considering matters including flagrancy, deterrence, post-infringement conduct, benefit, and other relevant circumstances. Those are court-controlled remedies, not amounts created merely by publishing a tariff.

The ACCC explains that a contract generally forms through offer and acceptance, including signature or an affirmative “I agree” action. It also warns that standard-form consumer and small-business terms may be unlawful if unfair. Applicable law and other jurisdictions must be reviewed for each release.

## 9. Mandatory generator checks

The generator must halt for legal review when:

- the rights holder or chain of title is incomplete;
- the Work or accepted terms cannot be tied to immutable versions;
- the requested contract mode has no reliable acceptance evidence;
- consideration, capacity, identity, or authority is materially uncertain;
- an excluded actor is treated as having accepted merely by prohibited use;
- a contractual fee is described as a statutory copyright remedy;
- a term attempts to override a mandatory exception or non-excludable protection;
- a one-sided standard-form term may be unfair or a remedy may be penal; or
- the system cannot distinguish a contract claim, copyright claim, settlement offer, and adjudicated debt.

## 10. Optional standards and interoperability permission

A project may propose a separate permission for a defined standards contribution or interoperability activity. It must identify the exact material and version, permitted acts, purpose, recipients and any agency capacity, duration, publication and redistribution terms, attribution, incorporated material, applicable standards-body process and approval evidence. Determine separately whether any patent commitment is intended and whether the rights holder can make it. A copyright permission must not be presented as patent clearance.

No standards exemption is active merely because this document describes the option. Membership of, contribution to, or implementation of a standard associated with W3C, IETF, IEEE or another body is not treated here as a general permission to use the Work. The historical framework's broad standards exemption is replaced with this requirement for a bounded, reviewed instrument. Mandatory legal exceptions and earlier valid grants remain independently applicable.

An implementation profile would need an approved adapter or schema extension for this option; the current generator does not expose a dedicated standards-permission workflow. The [source adoption record](HUMANITARIAN-EQUITY-SOURCE-MANIFEST.md) records the lineage, and the [QualiaDB roadmap](QUALIADB-IMPLEMENTATION-ROADMAP.md) describes later semantic implementation.

## 11. Primary references

- [Copyright Act 1968 (Cth), ss 36 and 115](https://www.legislation.gov.au/C1968A00063/latest/text)
- [ACCC — Contracts](https://www.accc.gov.au/business/selling-products-and-services/contracts)
- [ACCC — Unfair contract terms](https://www.accc.gov.au/business/selling-products-and-services/contracts/unfair-contract-terms)
- [High Court of Australia — *Paciocco v Australia and New Zealand Banking Group Limited* [2016] HCA 28](https://www.hcourt.gov.au/cases-and-judgments/judgments/judgments-1998-current/paciocco-v-australia-and-new-zealand-banking-group-limited)
