# Rights and Provenance Register

Status: initial template  
Updated: 3 November 2026

This register separates project history from legal ownership of particular material. It is not proof by itself and does not replace source records, contracts, assignments, or legal review.

## Project lineage

The Licensor reports that the architectures, methodologies, and foundational work leading to this project have been developed since 1999. This is a historical provenance statement, not a claim that every current file was created in 1999 and not a claim of copyright over ideas or methods as such.

## Historical source repository record

The available Git history for the Humanitarian Equity Framework source repository begins on 19 July 2025. Before adopting a repository-wide notice for that work, confirm whether every included file was created by the proposed Licensor, imported from earlier work, created in employment or contracting circumstances, or supplied by another contributor.

## Material register

| Path / artifact | Release hash | Author(s) | Rights holder(s) | Created | First published | Provenance / agreement | Third-party material | Outbound licence | Review status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **[path]** | **[hash]** | **[name]** | **[name]** | **[year/date]** | **[year/date]** | **[source/agreement]** | **[none or details]** | **[licence/version]** | **[pending/verified]** |

## Rights-statement register

This table records the semantic assertion separately from the legal or technical instrument that gives it operational significance. A token, credential, ledger entry, or access-control rule is evidence or implementation only to the extent stated in its governing legal instrument.

| Statement ID | Subject agent | Jural relation | Action | Resource | Correlative agent / relation | Normative authority | Legal instrument | Technical instrument | Persistence | Human review / appeal | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **[ID]** | **[agent ID]** | **[claim/duty/privilege/no-right/power/liability/immunity/disability]** | **[action]** | **[resource ID]** | **[agent/relation]** | **[law/contract/policy/other]** | **[instrument ID]** | **[token/credential/ledger/policy ID or none]** | **[ephemeral/session/transactional/durable/archival]** | **[route]** | **[proposed/approved/suspended/revoked/expired]** |

## Authority and instrument register

| Instrument ID | Kind | Issuer / parties | Scope | Source of authority | Legal-effect classification | Effective / expiry | Integrity reference | Personal or sensitive data stored | Revocation / suspension | Review status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **[ID]** | **[legal/technical]** | **[agent IDs]** | **[actions/resources/territory]** | **[statute/contract/policy/authority ID]** | **[evidence/access_control/contractual/mixed/none]** | **[dates]** | **[hash/signature/ledger reference]** | **[no, or protected-data record]** | **[method]** | **[pending/verified]** |

The register must never infer ownership, consent, contractual assent, legal validity, or adjudicated liability from possession of a technical capability alone.

## Creator investment and material-interest register

Unpaid work is not recorded as having zero value. This register preserves the evidence needed for licence pricing, creator compensation, legitimate-interest analysis, settlement, loss, gain-based relief, enforcement funding, and any recoverable-cost claim.

| Investment ID | Creator / contributor | Category | Period | Quantity or method | Direct expenditure | Replacement / opportunity value | Evidence | Related Work/release | Recovery treatment | Verified by |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **[ID]** | **[agent ID]** | **[labour/LLM tokens/compute/infrastructure/capital/professional/opportunity/safety/enforcement/other]** | **[dates]** | **[hours, units, allocation method]** | **[currency, amount, date]** | **[method and value]** | **[timesheet/invoice/log/repository/comparable]** | **[release/hash]** | **[pricing/loss/settlement/cost/profit/funding]** | **[reviewer/date/status]** |

For AI-assisted work, record the human plan, prompts, supplied materials, selections, corrections, integration, testing, editorial judgment, provider and model terms, token and compute use, machine outputs, and final authorship decisions separately. Expenditure is relevant evidence but does not by itself prove copyright subsistence or ownership in every output.

## Contribution, settlement and assertion references

The investment register records effort and resources; it does not establish that an amount is payable, settled or sufficient to authorise a licence transition. Supplement it with the distinct records in the [contribution lifecycle](CONTRIBUTION-LIFECYCLE.md). The following is a manual review template for the next implementation phase, not an additional generator schema:

| Material / immutable version | Agreement and accepted scope | Claim and decision | Obligation and liable party | Allocation and settlement evidence | Dispute / correction | Dependency and existing licence | Release authority / decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **[artifact/version]** | **[record IDs]** | **[IDs/status/reviewer]** | **[ID/basis/amount/currency or none]** | **[IDs/amount allocated/outstanding]** | **[ID/status/impact]** | **[version/terms/authority]** | **[ID or pending]** |

Keep dependency attribution, dependency licence duties, accepted upstream funding obligations and voluntary support separately identified. Use allocation references to prevent double charging of shared costs or double recovery of an already satisfied obligation. New maintenance obligations must identify their own scope and affected version; they must not silently reopen a completed release decision.

Claims about authorship, contribution, authority or conduct should link to [contextual assertion records](CONTEXTUAL-ASSERTIONS.md), including issuer, evidence, permitted uses, uncertainty and challenge history. A disputed authorship statement must remain distinguishable from a verified assignment or an adjudicated finding. Public provenance should expose only the information justified for that purpose; private identity, financial, biometric and guardian records need protected storage and access review. Hashes and stable identifiers also require privacy review where they can expose or link humans.

## Proposed notice method

For a release that expressly adopts the public inspection option after verification, a notice may take this form:

> Copyright © **[actual year or year range for the material] [verified rights holder]**.  
> Publicly inspectable only; no permission to run, modify, redistribute, or deploy. See the root licence for the identified release.

Use a year range only when protected material in the relevant item was created across that range. Older imported material should retain its own accurate notice. The statement “project lineage since 1999” belongs in provenance documentation, not as a substitute for the copyright year of newly written code.

## Chain-of-title checks

- **[ ]** Proposed Licensor's full legal name and service address confirmed.
- **[ ]** Employment and contractor contexts reviewed for each historical period.
- **[ ]** Earlier licences, standards contributions, assignments, and institutional policies checked.
- **[ ]** Joint authors and external contributors identified.
- **[ ]** Third-party and generated material identified and compatible.
- **[ ]** Moral-rights treatment reviewed.
- **[ ]** Authority to enforce and to offer future licences confirmed.
