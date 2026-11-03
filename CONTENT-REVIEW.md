# Content revision review and validation

Date: 3 November 2026

Scope: the documentation update on `codex/humanitarian-equity-content-update`, compared with baseline `ff97c25409d2f43097aeb3aa7f8fe14198649dde`.

## Review method

Three parallel workstreams developed the contribution, human-rights and QualiaDB specifications with separate file ownership. Integration reviewed their language, source interpretation, cross-references and relationship to existing instruments. A separate reviewer examined the integrated changes. This is a documentation and design review, not legal approval, financial audit or certification of the proposed software.

## Integration decisions

- Replaced the contributor terms' rejection-without-explanation approach with reasoned decisions, accessible correction and appeal. Rejection of an output does not erase accrued obligations for requested activity or expenses.
- Separated funding received by an intermediary from compensation delivered to the beneficiary. A sponsor's funding obligation can be discharged while contributor obligations remain outstanding.
- Kept the full defined-obligation transition condition, independent rights and readiness checks, and an authorised release decision. Existing valid grants remain relevant.
- Added source dispositions rather than importing the historical licence, generated legal conclusions or provisional ontology syntax. No mandatory payment rail, DAO, universal score or automatic ecological debt was adopted.
- Grounded the QualiaDB handoff in a pinned source review. CML is Context Markup Language; the inspected generic semantic-instrument runner is a demonstration implementation. Actual evaluator integration and conformance tests are next-phase work.
- Distinguished every new proposed record from fields supported by the existing generator. Clarified that automated validation cannot establish evidence truth, legal validity, settlement or runtime compliance.
- Scoped the sample public-inspection notice to releases that expressly adopt that option, rather than implying it is mandatory for all ecosystem projects.

## Independent review

The independent review found one actionable wording inconsistency in roadmap stage Q2: “machine exact-equivalence proposals cannot become attested” could be read as barring subsequent valid human ratification. The gate now keeps automated mappings as proposals, prohibits automated assertion of `skos:exactMatch`, and requires signed, authorised human attestation for authoritative exact equivalence. This preserves the intended review pathway and the pinned CML distinction.

The reviewer independently checked the pinned CML README and vocabulary, semantic-instrument runner and manifest, and the dated W3C credential Recommendation. The principal technical descriptions were supported. No other substantive publication blocker was identified in the reviewed changes. Review conclusions apply to this documentation revision and do not certify unimplemented behaviour or eliminate the possibility of drafting errors.

## Verification

- The existing generator suite passed all 20 tests using Python 3.12.14: `python -m unittest discover -s tests -v`.
- All 133 local Markdown file links resolved; no duplicate headings were found. New files also passed a trailing-whitespace check.
- `git diff --check` passed for the integrated tracked changes. No runtime code, executable schema or ontology changes are included in this revision.
- The existing [reference Page](https://chatgpt.com/space/page_14f228d735c08191ad993e7ea8e51f22) was refreshed and read back successfully: all additions were present, with links to the development branch. It remains a personal reference Page with its existing access settings.
- The archive branch was pushed at the exact baseline commit. The completed documentation is prepared for publication on the separate update branch; the Git commit and remote branch records identify the published version.

The new documents contain 35 synthetic review scenarios: 11 contribution cases, 5 fairness cases, 7 assertion cases and 12 QualiaDB acceptance cases. These specify expected future behaviour; they are not 35 executed software tests.

## Remaining implementation and adoption work

Following clarification of the project's intended emphasis, the purpose, status descriptions, interim-licensing explanation and reusable reference text were revised to state the dependency directly: constituent ecosystem work, including the related QualiaDB and semantic tooling, must be sufficiently developed, integrated and validated before the intended licensing and rights fabric can be used. This is the rationale for temporary alternative licences in related projects. Framework readiness is distinct from satisfaction of a particular work's compensation obligations and its authorised licence transition. The documentation work package is complete; the broader framework remains in development. This follow-up wording revision passed diff and local-link checks (134 links), and the corresponding reference Page changes were verified by readback. Runtime code was unchanged; the earlier generator test results remain the recorded regression baseline.

Follow stages Q1–Q7 in the [QualiaDB roadmap](QUALIADB-IMPLEMENTATION-ROADMAP.md). This review did not build or run QualiaDB, validate a live cross-repository adapter, implement payments, or exercise real human records. Source versions, supported logic profiles, schema mappings, evaluator dispatch, protected evidence, authenticated decisions, correction propagation and release authority require implementation evidence. The current local ontology still needs the framing and mapping audit identified in the roadmap.

Jurisdiction-specific legal review, contribution agreements, accounting and settlement policies, privacy and accessibility review, and adoption of identified release instruments remain separate tasks. Drafting errors, including agent-introduced errors, must be remediated before the affected components support a licensing transition. See the [project plan](PROJECT-PLAN.md) and [source adoption record](HUMANITARIAN-EQUITY-SOURCE-MANIFEST.md).
