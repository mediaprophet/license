# Contextual assertions and contestable evidence

Status: proposed information and review model; not an implemented credential service, reputation system or extension to the current generator schema.

Cooperative projects need to record what was contributed, who reviewed it and what evidence supports a decision. A human must remain distinguishable from every assertion about them. Neither a contribution history nor a model's inference is a complete account of a human's character, mindware or worth.

This specification develops contextual assertions for the [rights fabric](PROJECT-PURPOSE.md), [contribution lifecycle](CONTRIBUTION-LIFECYCLE.md) and [fairness review](FAIRNESS-AND-RIGHTS-REVIEW.md). It rejects a universal reputation or trust score. A decision should use relevant, authorised evidence for its defined purpose, with reasons and a challenge route. Absence of a credential is not evidence of incompetence or misconduct.

## 1. Keep statement types distinct

| Type | Meaning and limits |
| --- | --- |
| Observation | A report of something observed by an identified source using a described method. It can be mistaken, incomplete or affected by measurement limits. |
| Inference | A conclusion derived from stated inputs and a method or model. Preserve those dependencies and uncertainty. An inferred intention or emotion must not silently become an observed fact. |
| Allegation | A report that conduct occurred or a rule was breached, without treating the report as an established finding. Protect reporting, response and review processes. |
| Attestation | An identified issuer vouches for a precisely scoped statement under stated criteria and authority. Signature verification concerns authenticity and integrity; it does not by itself establish truth. |
| Adjudicated finding | A finding by a body or decision-maker with identified competence and authority, within a specified proceeding and scope. Preserve its jurisdiction, date, finality and appeal or correction status. |

These types are not an automatic ladder. Repetition does not promote an allegation into fact. Several inferences from one underlying source are not independent corroboration. An internal project reviewer cannot label their view a court finding. If an observation later supports an adjudicated finding, create and link a separate finding record rather than rewriting the original observation.

## 2. Minimum assertion record

The following conceptual fields define requirements for future schema and semantic mapping work. They are not production property names.

| Field group | Required information |
| --- | --- |
| Identity and version | Stable assertion ID, version, issued time, status and previous or superseding record. Do not require a globally correlatable human identifier. |
| Statement | Subject, predicate and object or value; type from section 1; precise language and any translation provenance. Separate the assertion from its evidence. |
| Issuer and agency | Issuer, actual principal, role, authority claimed, relevant competence and conflicts. Identify tool/model involvement without substituting software for the accountable issuer. |
| Context | Project, work/version, task, observation period, location or jurisdiction where material, purpose and conditions. Avoid generalising beyond this scope. |
| Evidence | Protected source references, acquisition basis, integrity information, method, provenance, contrary evidence and dependence on other assertions. |
| Uncertainty | What is known, unknown, disputed or estimated; confidence only with an intelligible method and limitations. A precise number must not mask uncertainty. |
| Permitted processing | Basis and terms for collection, creation, storage, verification, inference, use, disclosure and onward use; permitted recipients and actual principals. |
| Lifecycle | Validity interval, review date, expiry, retention, restriction, correction, withdrawal, supersession and deletion rules where applicable. |
| Contest and disposition | Notice, accessible response channel, reviewer, timeline, challenge status, reasons and linkage to any resulting decision or remedy. |

Each processing act needs its own applicable basis. Authority to issue a credential does not confer unrestricted authority to gather information about the subject. Receipt of an assertion does not permit general publication, cross-service identification, profiling, influence or manipulation. The human's stewardship over specified identifier representations and the limits of any grant continue to apply.

Records about several humans require consideration of each affected human's rights. One participant's permission cannot silently authorise disclosure of another's confidential information. Where consent is not the relied-upon basis, identify the independent authority and its limits rather than inventing consent.

## 3. Privacy, allegations and human agency

Access should follow the purpose and terms of the specific review. Keep sensitive evidence outside public immutable records. Even a hash or status endpoint can expose information or permit correlation; assess whether it is needed, who can query it and what it reveals. Public attribution of a work does not require publication of private payment, disability, guardianship or allegation records.

An allegation record needs a defined intake and protection process, access limits and a qualified review path. The affected human should have a meaningful opportunity to respond with sufficient particulars, subject to justified protections for reporters, third parties, safety and lawful process. Record the reason, scope and review date of any restriction on disclosure. A safety measure based on an unresolved allegation must remain distinct from a finding of wrongdoing and must be proportionate, bounded and reviewable.

The project must not infer moral worth, credibility in every context, emotional state or capacity from activity metrics. Human biometrics and mindware include interests beyond conventional identification, as described in [Project purpose](PROJECT-PURPOSE.md). A human's account of their lived experience and another agent's model of that experience must remain separately attributed. The system must be able to represent disagreement without overwriting the human's account.

Assistance with reading, presenting or challenging an assertion does not make the assistant the human's principal or owner. Guardians and representatives require verified scope for the particular act, not a generic ability to control all information. Offer accessible notice and support, and protect a route to challenge a representative's conflict or misuse.

## 4. Corrections and consequential decisions

Assertions may be active, challenged, restricted, expired, withdrawn or superseded. Those are record states, not verdicts about the human. Keep lifecycle state, statement type, evidence verification and decision outcome separate.

When an assertion is challenged or corrected:

1. Acknowledge the challenge, record its scope, and identify the reviewer and expected response time.
2. Consider whether further use or disclosure should be restricted while the issue is reviewed; record the authority and effect of that restriction.
3. Preserve necessary evidence with appropriate access and retention limits. Do not silently destroy an accrued claim or protected third-party record.
4. Record the result and reasons. Link a correction or replacement to the earlier version without continuing to present the earlier content as current.
5. Identify decisions and derived assertions that relied on the changed record. Notify authorised recipients where appropriate and re-evaluate affected decisions.
6. Record what could and could not be corrected downstream. A technical revocation or update cannot guarantee that every copy has disappeared.

A licence transition, exclusion or payment decision must cite the exact assertion versions relied upon and any unresolved challenge. A system must not silently treat missing, expired or inaccessible evidence as proof against a human. Specify the review action for those states, including proportionate alternative evidence. A lack of machine-readable evidence is not the same as a lack of rights.

## 5. Credentials and semantic instruments

Use existing credential standards where they fit. The [W3C Verifiable Credentials Data Model 2.0, Recommendation of 15 May 2025](https://www.w3.org/TR/2025/REC-vc-data-model-2.0-20250515/) models claims by issuers, validity, status and related verification processes, and addresses privacy and correlation risks. Its verification process does not itself establish the truth of every claim or whether a verifier should rely on it. A profile must separately define issuer trust, permitted use and decision criteria.

Open Badges may be a candidate format for particular achievement records. The implementation phase must verify the selected specification version and exact vocabulary rather than copying property names from historical generated notes. Neither a credential nor a badge is mandatory public attribution, payment, a grant of intellectual-property rights or a universal reputation measure.

The [QualiaDB roadmap](QUALIADB-IMPLEMENTATION-ROADMAP.md) should preserve source text, proposed mappings, reviewed meaning and executable conditions as distinct layers. Semantic instruments may connect assertions to permissions, duties and evidence. Their existence does not supply missing legal authority. A successful signature check, graph validation or reasoning run is evidence of that technical check only.

## 6. Synthetic cases for implementation review

| Input and proposed decision | Required result |
| --- | --- |
| A reviewer attests that a contributor completed accessibility testing for release R1. A hiring service wants a general character rating. | Preserve the task and release context. Do not derive a universal rating or authorise the new use from the original attestation. Check any separate basis for sharing. |
| Three models repeat an allegation derived from the same forum post. | Record the common source and dependent inferences. Do not count them as three independent witnesses or promote the allegation into a finding. |
| A credential signature is valid, but the issuer's authority for the asserted role is disputed. | Record the successful cryptographic check and unresolved authority separately; route the consequential decision for review. |
| A contribution claim is corrected from twelve hours to ten. | Link the replacement to the earlier claim, review affected valuation and payment records, and retain necessary protected evidence without creating a public misconduct label. |
| A human disputes an agent's inference about their intentions. | Preserve separately attributed accounts and the challenge. Do not treat model confidence as authority over the human's mindware. |
| A guardian requests disclosure of an allegation beyond their recorded authority. | Do not infer permission from the relationship label. Review the actual authority and affected rights, with accessible support for the principal human. |
| A qualified contributor has no public credential and declines cross-service identity linking. | Offer relevant alternative evidence where feasible. Do not infer lack of capability, create a global identifier or punish the refusal through an unrelated score. |

## 7. Historical source and adoption boundary

The [contextual assertion discussion in work/dev.md](https://github.com/mediaprophet/humanitarian-equity-framework/blob/f91bb7c1aa3896d83143c333cece711e851dd363/work/dev.md#L346-L465) provides the design direction: context, evidence, issuer, visibility and links to existing credentials. This specification adopts that direction and expands its human-rights and review requirements. It does not adopt the earlier global reputation scores, unverified vocabulary mappings or the inference that credential verification establishes substantive truth. New mappings require specification checks, fixtures and human review before implementation.
