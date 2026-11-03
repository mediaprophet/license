# Fairness and rights review

Status: proposed review specification and implementation acceptance cases; not an operational evaluator or adopted legal instrument.

This specification makes **WellFair**—welfare and fairness—reviewable across contribution agreements, licensing decisions, information processing and agent activity. It complements the [humanitarian foundations](HUMANITARIAN-FOUNDATIONS.md), [contribution lifecycle](CONTRIBUTION-LIFECYCLE.md) and [contextual assertions](CONTEXTUAL-ASSERTIONS.md). Its records are design requirements for the [QualiaDB implementation phase](QUALIADB-IMPLEMENTATION-ROADMAP.md); they are not additional fields currently accepted by the licence-profile schema.

The review asks what a proposed act would do to affected humans, whether there is an applicable basis for it, how benefits and burdens are distributed, and how errors or misuse can be corrected. It can recommend changes and identify missing evidence. It cannot itself establish legal validity, determine disputed liability or authorise an act. An authorised decision-maker must separately record a decision within their actual powers.

## 1. Review unit and evidence record

Review a specific clause, transaction, information act, workflow or release decision. Broad labels such as “humanitarian”, “fair” or “compliant” are insufficient. A review of one version or purpose does not approve every future use.

| Record element | Required content |
| --- | --- |
| Scope | Stable review ID, document or system version, exact clause or proposed act, affected resources, purpose, time and deployment context. |
| Humans and agents | Affected humans, acting agents, actual principals, operators, beneficiaries and accountable decision-makers; distinguish representation from other activity affecting a human. |
| Authority | Claimed basis for each act, exact instrument or provision, jurisdiction and applicability analysis; distinguish law, contract, human permission, project policy and an unverified assertion. |
| Evidence | Source, issuer, acquisition basis, date, provenance, access conditions, integrity reference, limitations and conflicting evidence. Use protected references for sensitive material. |
| Participation | Notice, accessible explanation, affected-human input, support needs, disagreements and how input changed or failed to change the proposal. |
| Findings | Separate findings for each review dimension, facts relied upon, interpretations, unknowns, alternatives and proposed mitigation. |
| Process | Reviewer competence, independence and conflicts, responsible owner, response deadline, review date, escalation and correction or appeal route. |
| Decision linkage | Recommendation, subsequent authorised decision, its scope and conditions, implementation evidence, monitoring and re-review triggers. |

Record “unknown” when evidence is missing. A model's confidence is not proof, a probability of legal enforceability or permission to proceed. Any quantitative estimate must identify its method, units, assumptions, evidence and limits. Do not collapse these dimensions into one fairness score or infer that a favourable total can offset an unlawful act.

## 2. Review dimensions

| Dimension | Questions to answer | Evidence or result |
| --- | --- | --- |
| Legal and authority | Who has a right or power to perform this exact act? Which mandatory protections, existing grants, contracts and jurisdictional questions apply? Is representation actually relevant, or is this an independent act by an agent for another entity? | Source-specific analysis; unresolved legal questions routed to qualified review. No universal conclusion drawn from clause similarity. |
| Ethical and human agency | Can the affected human understand, refuse, condition or challenge the act? Does it exploit dependency, constrain dignity or seek inappropriate control over biometrics or mindware? | Power-imbalance analysis, scoped permission record and practical alternatives. |
| Economic and material | Who supplies labour, time, equipment, connectivity, money and risk? What was requested and agreed? Could delay or a disputed demand make participation or remedy unaffordable? | Separate contribution, expense, obligation and impact records; supported ranges for uncertain costs. |
| Social and participation | Who is excluded, exposed or burdened, including humans outside the agreement? Are language, disability, care responsibilities and community context addressed? | Accessible participation plan and distribution of benefits and burdens; avoid unnecessary collection of sensitive characteristics. |
| Resolution and remedy | Can an affected human obtain reasons, correct information, stop harmful activity and reach an independent reviewer? Who funds necessary support and preservation? | Named route, timeframe, safe communication, protection from retaliation and escalation beyond a conflicted actor. |
| Temporal and lifecycle | What changes at expiry, withdrawal where applicable, correction, settlement, transfer, dependency update or release? What must survive, and on what basis? | Review triggers, retention limits, correction propagation, pending disputes and release-specific decisions. |

Ecological and access effects are assessed within the economic, social and temporal dimensions. Record device requirements, bandwidth, energy use, hosting location, maintenance, equipment replacement and waste where relevant. Separate measured values from estimates and record the boundary of each estimate. Compare feasible alternatives, including lower-bandwidth, local, assisted and asynchronous participation. Local processing is not automatically private or low impact; remote processing is not automatically prohibited. Assess the actual design, applicable terms and effects.

An ecological measure, attention estimate or computation threshold does not create a compensation debt. An agreed payable expense requires its own basis in the contribution lifecycle or applicable law. Public-benefit and environmental outcomes also cannot silently discharge agreed monetary obligations.

## 3. Sustainable human participation

Human welfare includes rest, sleep, recreation, health, care relationships and the practical means to live. The distinction between useful work and other human activity must not become a requirement to monitor a contributor's entire life. Article 24 of the [Universal Declaration of Human Rights](https://www.un.org/en/about-us/universal-declaration-of-human-rights/) recognises rest and leisure, including reasonable limits on working hours. It informs this project's design alongside applicable labour law; this specification does not turn that declaration into a universal private contract or invent an eight-hour compensation trigger.

Projects should agree expected effort, availability, response windows, payment conditions and escalation before requested work. They should permit accessible and asynchronous participation, realistic breaks and voluntary cessation of future contributions. Silence during rest or care is not evidence of misconduct, loss of dignity or consent to new terms. Ending participation does not erase already accrued obligations, valid surviving duties or earlier grants.

Valuation must recognise agreed research, integration, translation, accessibility, coordination and review work as well as visible output. Continuous biometric, behavioural or productivity surveillance is not the default evidence mechanism. Use proportionate evidence of the agreed contribution and offer a review route when a contributor cannot provide a particular form of measurement. A contribution record must not be repurposed into a general assessment of the human.

## 4. Human biometrics, mindware and identifiers

The individual human remains the principal in relation to their human agency and rights. Other agents may act for unrelated humans, corporations, governments or other entities. Record those actual relationships rather than assuming the agent serves the affected human.

The project's broad meaning of biometrics includes mindware and associated qualities and qualia, as explained in [Project purpose](PROJECT-PURPOSE.md). It does not assert that every characteristic is measurable or has the same legal classification. A computational representation, inferred intention or emotional label is distinct from the human and their lived experience. An adverse decision must not acquire authority merely because an inference is precise-looking or signed.

For each proposed use of an identifier representation, review the representation, act, actor and principal, purpose, context, duration, recipients, inference limits, retention, onward use and correction or withdrawal mechanisms. A grant for one use authorises only that use within its terms. Additional acts—including identification across services, profiling, influence, interference or manipulation—require their own applicable basis. An independent legal authority must be recorded separately; it must not be attributed to the human's permission.

Guardianship or assistance requires a separate review of source, scope, duration, conflicts and changes in authority. The human remains the rights holder. Support with understanding or communication is distinct from power to decide. Neither credentials nor a shared account establish guardianship. Preserve the human's participation, will and preferences within the applicable framework; do not infer incapacity from disability. Where authority is disputed, refer the specific decision for competent review and consider safe interim arrangements without granting the disputed agent wider control or unnecessarily cutting off essential support.

## 5. Review procedure and outputs

1. Fix the review scope and identify affected humans, actual principals and decision powers.
2. Collect only evidence the reviewers have a basis to obtain and use; separate allegations, observations and inferences.
3. Check source currency, legal status and applicability, then invite affected-human input through accessible, safe routes.
4. Assess every relevant dimension and alternatives. Record disagreements and uncertainty rather than forcing consensus.
5. Recommend one of: proceed within specified conditions; revise and re-review; hold the specified act pending evidence or authority; or refer for competent determination. “No issue identified within scope” is not a guarantee.
6. Obtain a separate authorised decision and record reasons, scope, conditions and the affected human's challenge route. A reviewer cannot confer powers they do not possess.
7. Verify the adopted safeguards in practice and re-open the review on relevant changes, complaints, expiry or new evidence.

A hold must identify what is paused, why, who can resolve it and when it will be reviewed. Protective action must itself be necessary, proportionate and reviewable; a restrictive outcome is not automatically humanitarian. Urgent protective action requires its own authority and prompt subsequent review. A dispute must not be labelled resolved simply because a software workflow is closed.

The review report should link each finding to evidence, an owner and a disposition. Agent-assisted drafting must retain a proposed status until appropriately reviewed. Remediation of erroneous wording, mappings and system behaviour is part of readiness for licensing transitions. See [Enforcement and remedies](ENFORCEMENT-AND-REMEDIES.md) for the separate classification of legal remedies and recovery arrangements.

## 6. Worked acceptance cases

These are synthetic design cases, not findings about real humans or declarations of law. Passing them requires observable implementation evidence in the next phase.

| Case | Review finding and required behaviour | Failure to detect |
| --- | --- | --- |
| Identifier comparison | A human permits a service to compare one representation for account authentication. An analytics agent for a different company proposes cross-service profiling. The second act has no basis in the authentication grant; prevent reliance on that grant, record the proposed act and require its own applicable basis before it proceeds. | Treating possession of the representation or a successful match as general profiling permission. |
| Conflicting guardianship | Two agents claim authority over disclosure of a supported human's record, and the human objects. Record the competing sources, scope and objection; obtain accessible input and competent review. Limit interim disclosure to any separately established basis and preserve essential support where possible. | Selecting whichever agent logged in first, assuming disability proves incapacity, or treating an agent's credential as ownership. |
| Contribution dispute | A contributor claims agreed review work was rejected without explanation. Preserve the agreement and acceptance evidence; provide a reasoned decision and independent challenge route under the adopted procedure. Keep disputed and undisputed amounts distinguishable. | Converting a disputed claim into established debt, erasing it, or denying review because the claimant has a low reputation score. |
| Resource burden | A proposed workflow demands constant connectivity and expensive hardware. Assess who bears those costs, whether alternatives enable participation, and what expenses were agreed. Record estimated energy separately from contractual obligations. | Imposing automatic compensation because an energy threshold was crossed, or excluding a human without considering feasible access alternatives. |
| Rest and ongoing work | A maintainer declines new work during care responsibilities while an earlier accepted payment remains outstanding. Respect future participation choices, preserve the earlier claim and arrange continuity with separately agreed contributors. | Conflating a pause with forfeiture, imposing further unpaid work or assuming a claim grants rights in the maintainer's mindware. |

## 7. Source disposition

The six review dimensions adapt the useful structure in the [historical evaluator draft, sections 1 and 4](https://github.com/mediaprophet/humanitarian-equity-framework/blob/f91bb7c1aa3896d83143c333cece711e851dd363/software-agents/evaluator.md). Its numeric legal-risk scores, generated legal conclusions and unresolved citation tokens are not adopted as authority. This document replaces them with contextual evidence, uncertainty and competent decision processes.

The emphasis on humans, fair work and room for rest follows the [human correction in rights-work/dev.md](https://github.com/mediaprophet/humanitarian-equity-framework/blob/f91bb7c1aa3896d83143c333cece711e851dd363/rights-work/dev.md#L66-L107). Resource and access considerations develop the [software-agent resource discussion](https://github.com/mediaprophet/humanitarian-equity-framework/blob/f91bb7c1aa3896d83143c333cece711e851dd363/software-agents/thoughts.md#L1-L33), without adopting its proposed energy-to-compensation inference. These are design sources; applicable legal authority must be established separately.
