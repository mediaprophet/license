# Contribution, compensation and settlement lifecycle

Status: proposed requirements and review cases; not an operative agreement or an implemented accounting system

Updated: 3 November 2026

This specification develops the cooperative compensation purpose described in [Project purpose](PROJECT-PURPOSE.md). It separates recognition of work from acceptance, payment obligations, settlement and authority to license. It is intended to support first drafts of semantic instruments and subsequent implementation through the [QualiaDB roadmap](QUALIADB-IMPLEMENTATION-ROADMAP.md). Its records and states are proposed concepts, not additional fields already accepted by the current generator schema.

## 1. Humans, participants and contributions

Human contributors retain their agency, dignity, privacy, rest, and access to remedy. Those protections do not depend on a project's valuation of their output. A participant can contribute, review, fund, maintain, support or be affected by a project; these are contextual roles, not rankings of human worth. An affected human need not be a project participant to have rights in relation to its operation.

Record the acting agent, its actual principal and its capacity for each activity. Distinguish a human's work from software activity and a provider's services or charges. A software agent's tool execution does not make it the human creator, oblige its operator to pay an arbitrary amount, or establish copyright or contractual authority. Record provenance and applicable provider terms separately. The principal human's biometrics, mindware and inherent rights are not contributed assets or collateral for project debts.

Classify contributions along independent dimensions. A contribution may be requested, collaborative, ongoing and interdependent at the same time; these are not mutually exclusive subclasses.

| Dimension | Record |
| --- | --- |
| Origin | Requested or commissioned work; invited proposal; unsolicited submission; voluntary contribution with clearly stated expectations |
| Purpose and scope | Requesting authority, task, intended beneficiary, necessity or usefulness assessment, acceptance criteria and version of those criteria |
| Activity | Research, design, programming, testing, documentation, translation, accessibility, review, maintenance, coordination, governance or other described work |
| Inputs | Human effort; equipment, hosting, compute, model usage, professional services or other resources; rights offered in existing material |
| Collaboration | Human and other participants, roles, shared outputs and dependencies; attribution and allocation agreements |
| Duration | Discrete task, time-limited engagement, recurring service or ongoing maintenance with review and exit terms |
| Terms | Existing licence, contribution agreement, employment or service arrangement, expense approval and any constraints on reuse |

Do not infer that an unsolicited contribution is a gift, that necessary work was commissioned, or that usefulness creates a debt. Equally, rejection of a deliverable must not erase amounts already due for authorised activity, approved expenses or other applicable obligations. Requested work should have understandable scope, rates, expenses, review and cancellation terms before it starts.

## 2. Records that must remain distinct

Each record needs a stable identifier, version, responsible actor, time, applicable authority, links to evidence and related records, access classification, and correction history. Public identifiers should not expose private financial or identity evidence. A hash can help check integrity; it does not establish truth, entitlement or lawful publication.

| Record | Minimum content and decision boundary |
| --- | --- |
| Request and agreement | Scope, actual parties and authority, agreed criteria, rates or valuation method, budget, expenses, cancellation, due dates, disputes, existing rights and assent evidence. A request is not proof that an agreement was formed. |
| Activity and resources | What was done, by whom or what tool, dates, quantities and units, evidence quality, allocations and uncertainties. Keep estimates and observations distinct. |
| Output or service | Identified artifact/version or completed service, provenance, dependency references and rights status. A service need not produce a copyright work. |
| Submission or claim | What is sought: acceptance, attribution correction, expense reimbursement, payment or another remedy; claimed amount and basis; relevant agreement and evidence. A claim is not an admitted liability. |
| Acceptance decision | Decision-maker and authority, criteria applied, accepted scope, reasons, exceptions and review route. Acceptance for integration, rights clearance and compensation approval are separate decisions. |
| Valuation | Method, quantities, rates, currency/unit, assumptions, agreed cap or adjustment, independent review where needed and disputed components. Economic valuation is not a valuation of the human. |
| Obligation | Identified obligor and beneficiary, legal or contractual basis, scope, amount/formula, trigger, due date, conditions, settlement terms and status. An investment entry is not itself an obligation. |
| Settlement allocation | Verified payment or other expressly agreed performance, date, amount/unit, recipient, fees, reversal status, receipt, and the precise obligations satisfied. A transaction identifier alone is insufficient. |
| Transition decision | Defined work/version, obligation-set version, satisfaction evidence, rights and readiness checks, authorised decision-maker, new licence and effective scope. Settlement does not issue this decision. |

Keep separate state dimensions rather than one misleading “approved” flag. A claim can be received, under review, awaiting evidence, partly upheld, declined or appealed. An obligation can be proposed, agreed but contingent, payable, partly satisfied, satisfied or disputed in part. An output can be accepted for integration while a valuation remains disputed. Corrections and reversals append a reasoned event; they must not silently overwrite the original assertion.

## 3. Claims, review and correction procedure

Before requesting work, publish an accessible procedure specifying a contact, acknowledgement deadline, initial assessment deadline, evidence-response period, decision deadline, appeal window and target review period. Express them in a defined calendar, with timezone and treatment of holidays where material. The operative agreement must fill these values; this specification does not invent universal deadlines. Provide extensions for accessibility or evidence constraints, give reasons and a revised date, and identify escalation when a deadline is missed. Silence is neither acceptance nor rejection nor forfeiture of a claim.

The procedure must support the following steps:

1. **Receive and protect.** Issue a receipt and claim identifier. Explain intended uses, recipients, retention and correction of supplied evidence. Permit assisted and non-public submission; do not require unnecessary biometric evidence or public disclosure of payment details.
2. **Classify.** Identify the requested decision, agreement or other asserted basis, concerned work/version, and any separate undisputed amounts. Ask for proportionate missing evidence. A missing commit hash is not grounds to disregard a service, coordination or accessibility contribution.
3. **Assign review.** Identify the reviewer and authority. Disclose relevant conflicts, provide recusal or independent review, and do not let an agent acting for another entity present itself as the claimant's representative. Tool-generated summaries must preserve access to underlying evidence and human review.
4. **Assess consistently.** Apply the recorded criteria and terms relevant to the work. Give the claimant an opportunity to address material adverse information, subject to protection of other humans and restricted evidence. Do not retroactively change the criteria to avoid payment.
5. **Decide with reasons.** State the accepted and declined elements, evidence relied upon, uncertainty, valuation and obligation effects, reviewer, date and route to correction or appeal. Protect confidential material while providing enough explanation to make a challenge practical.
6. **Correct and appeal.** Allow factual correction and review by an appropriately independent human decision-maker. Record the outcome and affected downstream decisions. Preserve external remedies and non-excludable rights; the project process is not a court and does not make legal liability final.
7. **Settle and reconcile.** Pay amounts due under the applicable terms; a dispute about one component should not be used to withhold unrelated amounts due. Record allocation, shortfalls, fees, failed transfers, reversals and beneficiary confirmation or equivalent reliable evidence.

A rejection of an unsolicited proposal does not by itself create a compensation entitlement. A reasoned review obligation is nevertheless part of the intended governance procedure. Claims arising from requested work, existing agreements or applicable law must be assessed on that basis rather than dismissed by a general “not accepted” label. Handling threats, harassment or abusive submissions can require proportionate restrictions; those decisions should preserve a usable route for legitimate claims and review.

## 4. Valuation and benefit classification

Agree the valuation method before requested work where practicable: time and rate, fixed deliverable, measured resource reimbursement, milestone, royalty or another described basis. Separate an initial estimate, a claimant's proposed value, an approved amount and actual settlement. Record changes to scope and rates with assent and effective dates. Do not silently convert voluntary work into a loan, or retrospectively impose interest, compounding, indexation or an opportunity-cost multiplier. Any such arrangement needs its own valid basis, transparent formula, cap where appropriate, and legal review.

Distinguish quantities from prices: hours, tokens, storage, equipment use and energy are measurements; the applicable rate and contractual treatment determine any agreed charge. Avoid counting the same provider invoice both as a pass-through expense and as an additional resource charge unless the agreement expressly distinguishes the services. Tax, exchange rates, transaction fees, payment finality and responsibility for shortfalls must be addressed in the relevant arrangement.

The source material's financial and non-financial examples should be represented by their actual function:

| Category | Examples | Required distinction |
| --- | --- | --- |
| Unit of account or settlement asset | Identified national currency, specified digital asset, agreed service unit | Record unit, issuer/network where relevant and conversion terms; a unit does not establish what is owed. |
| Basis of payment or transfer | Wages, service fees, royalties, expense reimbursement, grants, gifts, loans | Different obligations and rights may apply. A gift or funding receipt is not automatically payment of a contributor's claim. |
| Payment mechanism or schedule | Bank transfer, payment processor, micropayment, instalment | Mechanism and frequency are separate from the underlying obligation. No mandatory blockchain is assumed. |
| Financial or entitlement instrument | Loan agreement, bond, voucher, redeemable credit | Record issuer, holder, redemption rights, limits and review; do not classify every instrument as a currency. |
| Non-monetary benefit | Training, access, mutually agreed service exchange, recognition | Record agreed terms, accessibility and limits. Recognition or a badge does not silently discharge money owed. |
| Social or ecological outcome | Accessibility improvement, reduced resource use, community benefit | Record evidence, method, context and uncertainty. Outcome measurements are not automatically tradable credits or payable debts. |

A replacement of agreed monetary compensation by another form of performance requires a valid, informed agreement identifying the affected obligation and value; do not presume validity where mandatory remuneration rules or coercion concerns apply. The beneficiary's ability to decline matters. General public benefit, project exposure, prestige or a change to a licence is not compensation unless a valid arrangement specifically establishes the relevant performance. Inherent human rights and human worth are never units of settlement.

## 5. Dependencies, allocation and maintenance

Record each incorporated dependency's identity, version/hash, rights holder where known, actual licence, notices, permissions, modifications and compatibility review. Link relevant contribution and attribution records without republishing private evidence. An upstream licence condition, a voluntarily chosen support payment, and an accepted contractual funding obligation are different records. Use of a permissively licensed dependency does not create a new debt under this framework merely because the dependency had development costs.

For shared costs, identify the original cost item, total verified amount, agreed allocation basis, recipients or works, allocation version and remaining balance. Allocations against one cost item must reconcile; an allocated amount must not be treated as a new independent cost. Mark amounts paid by grants, sponsors, a project reserve or a recipient against the same obligation when those payments satisfy it under its terms. Separate management overhead or new services from reimbursement of an already paid expense.

Funds received by a project, pool, platform or intermediary are not proof that a contributor has been paid. Distinguish a funder's obligation to deposit funds from the project's obligation to deliver compensation to its beneficiary. Record custody, allocation, payout authorisation, beneficiary receipt or equivalent reliable evidence, fees and failed or reversed transfers. An intermediary's receipt may discharge a payer's separate obligation under its terms while leaving the contributor's compensation outstanding. Payment to a tool or infrastructure provider likewise does not discharge human compensation merely because both relate to the same contribution. Transition review must check the actual beneficiary obligations included in its defined set, rather than equating a funded reserve or aggregate inflow with settlement.

Define whether the transition's obligation set is collective for the work or specific to a recipient. The rule must identify the included versions, obligations, conditions and treatment of contingent or disputed items. Do not exclude an unresolved relevant obligation merely to declare completion. Record any valid resolution or amendment, who had authority, and why it affects the set; settlement status must remain auditable.

Ongoing maintenance should have a separate scope, funding arrangement, period, review and exit process. New work can generate obligations for later versions under agreed terms; it must not reopen a settled obligation or retroactively narrow an earlier valid licence. A maintenance reserve or future funding promise is not proof that an existing obligation has been fully satisfied. No contributor should be committed to indefinite unpaid support by an ambiguous “ongoing” role.

## 6. Readiness and authorised transition

The required financial condition is full satisfaction of the defined agreed obligations for the identified transition. A percentage threshold, predicted future revenue or token balance does not stand in for that condition. Non-financial conditions also remain: rights clearance, licence compatibility, human-rights and privacy safeguards, valid governance authority, reviewed wording and demonstrated system behaviour.

The transition decision must retain the obligation-set version and evidence for its conclusion, including resolved disputes, payment finality assumptions and any legally effective discharge. It must specify the work or derivative, immutable version, adopted licence, effective date and scope. Earlier valid grants remain relevant. Payment does not buy human biometrics, mindware, permission for prohibited harm or unrestricted processing of information about a human.

Review impacts with [Fairness and rights review](FAIRNESS-AND-RIGHTS-REVIEW.md). Semantic instruments may support evidence, explanation and checks, but a successful query or rule evaluation does not establish legal validity or replace authorised human review.

## 7. Worked review cases

These are hypothetical acceptance cases for later prototypes, not financial advice or executable tests of the current generator.

| Case | Facts | Required result |
| --- | --- | --- |
| Requested work and approved expense | Agreement pays 10 authorised hours at AUD 60 and reimburses AUD 40. Records support both; AUD 500 is allocated and verified as received. | Agreed total AUD 640; AUD 140 remains outstanding. The output's integration status is separate. Transition cannot be declared financially complete. |
| Unsolicited useful patch | A human submits a patch and claims AUD 300 without a prior payment agreement. The project wants to use the patch. | Record the claim and give a reasoned decision; clear rights and compensation terms before adoption. Neither usefulness nor submission alone proves a payable AUD 300 obligation. Preserve any independent applicable basis. |
| Requested output declined | An engagement pays authorised time regardless of whether an experiment succeeds. Its output is unsuitable. | Decline integration with reasons while assessing authorised time and expenses under the agreement. “Rejected” does not cancel amounts due. |
| Disputed valuation | Claim is AUD 800; review accepts AUD 600 and identifies AUD 200 as disputed. | Maintain separate admitted and disputed components, review rights and evidence. Do not report the claim as wholly approved, wholly paid or extinguished by paying AUD 600. |
| Shared hosting cost | A verified AUD 100 invoice is allocated AUD 60 to version A and AUD 40 to version B; a sponsor pays the full invoice on their behalf. | Reconcile the single cost and allocations. If the payment satisfies those obligations under their terms, both are satisfied; recipients are not charged the same outstanding invoice again. |
| Badge offered instead of money | AUD 200 is due; the project issues an achievement badge and publishes thanks. | Attribution may be recorded appropriately. AUD 200 remains due unless a separate valid agreement changes its discharge. The badge is not a payment event. |
| Pool funded but payout incomplete | A sponsor deposits AUD 1,000 into the project pool, satisfying its funding commitment. The project owes a contributor AUD 1,000 but only AUD 700 has reached the beneficiary. | Record the sponsor's discharged funding obligation separately from the contributor obligation. AUD 300 remains outstanding to the contributor; a funded pool cannot establish full compensation or transition readiness. |
| Upstream component | A third-party component is used under an existing licence; the project elects to support its maintainer. | Preserve licence conditions and provenance. Record voluntary support separately; no invented compulsory upstream debt or amendment of the existing licence. |
| Tool-assisted contribution | A human researches and corrects generated code; a provider invoice covers model use. | Record human activity, tool output, provider expense and actual rights separately. Payment of the invoice does not prove human authorship of every output or transfer all necessary rights. |
| Later maintenance | Version A's defined obligations are fully satisfied. Version B includes new agreed maintenance. | A's settled costs stay settled; B has its own identified obligations. Existing valid grants for A continue according to their terms. |
| Payment reversed before decision | A payment initially appears complete but is reversed before transition approval. | Reconcile evidence and reopen the unpaid balance as appropriate; do not issue a transition based on stale status. A later reversal after a valid grant requires legal review and does not automatically revoke that grant. |

## 8. Source and implementation boundary

This specification draws on the contribution classifications and financial/non-financial examples in [contributionsCosts/outline.md](https://github.com/mediaprophet/humanitarian-equity-framework/blob/f91bb7c1aa3896d83143c333cece711e851dd363/ontology/contributionsCosts/outline.md), the evidence/timeline/dispute concepts in [projectClaims.ttl](https://github.com/mediaprophet/humanitarian-equity-framework/blob/f91bb7c1aa3896d83143c333cece711e851dd363/ontology/projectClaims.ttl), collaborative roles and processes in [work/dev.md](https://github.com/mediaprophet/humanitarian-equity-framework/blob/f91bb7c1aa3896d83143c333cece711e851dd363/work/dev.md), and upstream attribution and maintenance intentions in the historical [LICENSE](https://github.com/mediaprophet/humanitarian-equity-framework/blob/f91bb7c1aa3896d83143c333cece711e851dd363/LICENSE). The source contains generated proposals and provisional ontology syntax; it is conceptual input, not imported legal authority or a production vocabulary.

The historical 80% release threshold, predetermined permissive licence, compulsory blockchain route and conflation of currencies with payments or outcomes are not adopted here. The current profile's creator-investment records remain useful background evidence, but do not implement these claim states, payable balances or transition decisions. Subsequent work must define reviewed schemas, authority checks, privacy controls, reconciliation rules and test fixtures before any operational integration or adoption.
