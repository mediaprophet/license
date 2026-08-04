"""Dependency-free validator and document assembler for licence profiles.

The generator is deliberately non-adjudicative. It validates a reviewed policy
profile and assembles draft artifacts; it does not determine legal liability,
issue demands, calculate a debt, or replace qualified legal review.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


GENERATOR_VERSION = "0.2.0"
SCHEMA_VERSION = "1.1"

CORRELATIVES = {
    "claim": "duty",
    "duty": "claim",
    "privilege": "no-right",
    "no-right": "privilege",
    "power": "liability",
    "liability": "power",
    "immunity": "disability",
    "disability": "immunity",
}

JURAL_TYPES = {
    "claim": "jural:Claim",
    "duty": "jural:Duty",
    "privilege": "jural:Privilege",
    "no-right": "jural:NoRight",
    "power": "jural:Power",
    "liability": "jural:Liability",
    "immunity": "jural:Immunity",
    "disability": "jural:Disability",
}

TECHNICAL_TYPES = {
    "capability_token": "hro:CapabilityToken",
    "identity_role_credential": "hro:IdentityRoleCredential",
    "licence_entitlement_token": "hro:LicenceEntitlementToken",
    "acceptance_receipt": "hro:AcceptanceReceipt",
    "delegation_token": "hro:DelegationToken",
    "consent_token": "hro:ConsentToken",
    "obligation_token": "hro:ObligationToken",
    "provenance_attestation": "hro:ProvenanceAttestation",
    "revocation_record": "hro:RevocationRecord",
    "ledger_record": "hro:LedgerRecord",
    "smart_contract_execution": "hro:SmartContractExecution",
}

LEGAL_EFFECTS = {
    "evidence_only": "hro:EvidenceOnly",
    "access_control_effect": "hro:AccessControlEffect",
    "contractually_recognised": "hro:ContractuallyRecognised",
    "statutorily_recognised": "hro:StatutorilyRecognised",
    "adjudicated": "hro:AdjudicatedEffect",
}

OUTPUT_NAMES = (
    "CONTRACT-AND-IP-LICENCE.md",
    "CREATOR-INTERESTS-AND-INVESTMENT-SCHEDULE.md",
    "RIGHTS-ONTOLOGY-SCHEDULE.md",
    "RIGHTS-GOVERNED-INFORMATION-AGREEMENT.md",
    "TECHNICAL-INSTRUMENTS-SCHEDULE.md",
    "ENFORCEMENT-AND-REMEDIES-SCHEDULE.md",
    "RIGHTS-POLICY.jsonld",
    "VALIDATION-REPORT.md",
    "ACCEPTANCE-RECEIPT-TEMPLATE.json",
    "RELEASE-MANIFEST.json",
)


@dataclass(frozen=True)
class Issue:
    severity: str
    code: str
    path: str
    message: str

    def as_dict(self) -> dict[str, str]:
        return {
            "severity": self.severity,
            "code": self.code,
            "path": self.path,
            "message": self.message,
        }


@dataclass
class ValidationResult:
    issues: list[Issue]

    @property
    def errors(self) -> list[Issue]:
        return [issue for issue in self.issues if issue.severity == "error"]

    @property
    def warnings(self) -> list[Issue]:
        return [issue for issue in self.issues if issue.severity == "warning"]

    @property
    def valid(self) -> bool:
        return not self.errors

    def as_dict(self) -> dict[str, Any]:
        return {
            "valid": self.valid,
            "error_count": len(self.errors),
            "warning_count": len(self.warnings),
            "issues": [issue.as_dict() for issue in self.issues],
        }


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("The JSON document must have an object at its root.")
    return data


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_json(value: Any) -> str:
    return sha256_bytes(canonical_json(value).encode("utf-8"))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _schema_target(root: dict[str, Any], ref: str) -> dict[str, Any]:
    if not ref.startswith("#/"):
        raise ValueError(f"Only local JSON Schema references are supported: {ref}")
    target: Any = root
    for part in ref[2:].split("/"):
        target = target[part.replace("~1", "/").replace("~0", "~")]
    if not isinstance(target, dict):
        raise ValueError(f"Schema reference does not resolve to an object: {ref}")
    return target


def _type_matches(value: Any, expected: str) -> bool:
    if expected == "null":
        return value is None
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return True


def _validate_schema_node(
    value: Any,
    schema: dict[str, Any],
    root: dict[str, Any],
    path: str,
    issues: list[Issue],
) -> None:
    if "$ref" in schema:
        _validate_schema_node(value, _schema_target(root, schema["$ref"]), root, path, issues)
        return

    if "const" in schema and value != schema["const"]:
        issues.append(Issue("error", "schema.const", path, f"Must equal {schema['const']!r}."))
    if "enum" in schema and value not in schema["enum"]:
        issues.append(Issue("error", "schema.enum", path, f"Must be one of {schema['enum']!r}."))

    expected = schema.get("type")
    if expected is not None:
        allowed = expected if isinstance(expected, list) else [expected]
        if not any(_type_matches(value, item) for item in allowed):
            issues.append(Issue("error", "schema.type", path, f"Expected type {allowed!r}."))
            return

    if isinstance(value, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in value:
                issues.append(Issue("error", "schema.required", f"{path}.{key}", "Required property is missing."))
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in properties:
                    issues.append(Issue("error", "schema.additional", f"{path}.{key}", "Unknown property."))
        for key, child in value.items():
            if key in properties:
                _validate_schema_node(child, properties[key], root, f"{path}.{key}", issues)

    if isinstance(value, list):
        minimum = schema.get("minItems")
        if minimum is not None and len(value) < minimum:
            issues.append(Issue("error", "schema.minItems", path, f"Requires at least {minimum} item(s)."))
        if schema.get("uniqueItems"):
            serialised = [canonical_json(item) for item in value]
            if len(serialised) != len(set(serialised)):
                issues.append(Issue("error", "schema.uniqueItems", path, "Items must be unique."))
        if "items" in schema:
            for index, item in enumerate(value):
                _validate_schema_node(item, schema["items"], root, f"{path}[{index}]", issues)

    if isinstance(value, str):
        minimum = schema.get("minLength")
        if minimum is not None and len(value) < minimum:
            issues.append(Issue("error", "schema.minLength", path, f"Requires at least {minimum} character(s)."))
        pattern = schema.get("pattern")
        if pattern and re.search(pattern, value) is None:
            issues.append(Issue("error", "schema.pattern", path, f"Does not match required pattern {pattern!r}."))
        if schema.get("format") == "date-time":
            try:
                datetime.fromisoformat(value.replace("Z", "+00:00"))
            except ValueError:
                issues.append(Issue("error", "schema.format", path, "Must be an ISO 8601 date-time."))

    if isinstance(value, int) and not isinstance(value, bool):
        minimum = schema.get("minimum")
        if minimum is not None and value < minimum:
            issues.append(Issue("error", "schema.minimum", path, f"Must be at least {minimum}."))


def validate_schema(profile: dict[str, Any], schema: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []
    _validate_schema_node(profile, schema, schema, "$", issues)
    return issues


def _duplicate_ids(items: Iterable[dict[str, Any]], path: str, issues: list[Issue]) -> set[str]:
    seen: set[str] = set()
    for index, item in enumerate(items):
        identifier = item.get("id")
        if not isinstance(identifier, str):
            continue
        if identifier in seen:
            issues.append(Issue("error", "semantic.duplicate_id", f"{path}[{index}].id", f"Duplicate identifier {identifier!r}."))
        seen.add(identifier)
    return seen


def _placeholder(value: str) -> bool:
    lowered = value.lower()
    return "[" in value or "replace" in lowered or "example-only" in lowered or "pending" in lowered


def validate_semantics(profile: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []
    try:
        status = profile["profile"]["status"]
        legal_review = profile["profile"]["legal_review"]
        formation = profile["formation"]
        phase = profile["release_phase"]
        agents = profile["agents"]
        resources = profile["resources"]
        relations = profile["rights_relations"]
        technical = profile["technical_instruments"]
        data = profile["data_governance"]
        exclusions = profile["exclusions"]
        enforcement = profile["enforcement"]
        creator = profile["creator_protection"]
    except (KeyError, TypeError):
        return [Issue("error", "semantic.skipped", "$", "Semantic validation could not run until schema errors are corrected.")]

    agent_ids = _duplicate_ids(agents, "$.agents", issues)
    resource_ids = _duplicate_ids(resources, "$.resources", issues)
    relation_ids = _duplicate_ids(relations, "$.rights_relations", issues)
    technical_ids = _duplicate_ids(technical, "$.technical_instruments", issues)
    _duplicate_ids(profile.get("sources", []), "$.sources", issues)
    financial_ids = _duplicate_ids(enforcement.get("financial_remedies", []), "$.enforcement.financial_remedies", issues)
    investment_ids = _duplicate_ids(creator.get("investments", []), "$.creator_protection.investments", issues)
    transfer_ids = _duplicate_ids(data.get("transfers", []), "$.data_governance.transfers", issues)
    _ = relation_ids, financial_ids, investment_ids, transfer_ids

    if profile["rights_holder"].get("id") not in agent_ids:
        issues.append(Issue("error", "semantic.rights_holder_agent", "$.rights_holder.id", "Rights holder must also appear in agents."))
    if profile["work"].get("id") not in resource_ids:
        issues.append(Issue("error", "semantic.work_resource", "$.work.id", "Work must also appear in resources."))

    creator_agents = set(creator.get("creator_agents", []))
    for index, identifier in enumerate(creator.get("creator_agents", [])):
        if identifier not in agent_ids:
            issues.append(Issue("error", "semantic.creator_agent", f"$.creator_protection.creator_agents[{index}]", f"Unknown creator agent {identifier!r}."))
    for index, investment in enumerate(creator.get("investments", [])):
        if investment.get("contributor") not in creator_agents:
            issues.append(Issue("error", "semantic.investment_creator", f"$.creator_protection.investments[{index}].contributor", "An investment contributor must be an identified creator agent."))
    creator_safeguards = (
        "public_inspection_not_permission", "technical_access_not_permission",
        "commercial_exploitation_requires_permission", "ai_use_requires_express_permission",
        "may_refuse_or_condition_licence", "excluded_agents_receive_no_licence",
        "creator_economic_survival_is_humanitarian_interest", "provenance_required",
    )
    for field in creator_safeguards:
        if not creator.get(field):
            issues.append(Issue("error", "semantic.creator_safeguard", f"$.creator_protection.{field}", "Creator autonomy and material-interest safeguard cannot be disabled in a humanitarian profile."))
    if creator_agents and not any(relation.get("holder") in creator_agents and relation.get("resource") == profile["work"].get("id") for relation in relations):
        issues.append(Issue("error", "semantic.creator_relation", "$.rights_relations", "At least one rights relation must state a creator-held position over the Work."))
    ai_boundary_text = " ".join(profile["grant"].get("prohibited_actions", [])).lower()
    if creator.get("ai_use_requires_express_permission") and not any(term in ai_boundary_text for term in ("training", "machine", "model", "embedding", "ai ")):
        issues.append(Issue("error", "semantic.ai_boundary", "$.grant.prohibited_actions", "Express AI-use control requires an explicit AI, model-training, embedding, or machine-use boundary in the grant."))

    for index, agent in enumerate(agents):
        principal = agent.get("principal")
        if principal is not None and principal not in agent_ids:
            issues.append(Issue("error", "semantic.principal_ref", f"$.agents[{index}].principal", f"Unknown principal {principal!r}."))
        if agent.get("agent_type") == "artificial_agent" and not principal:
            issues.append(Issue("error", "semantic.orphan_agent", f"$.agents[{index}]", "Artificial agents require an identified principal."))
        if agent.get("agent_type") == "artificial_agent" and not agent.get("accountable_human_review"):
            issues.append(Issue("error", "semantic.agent_review", f"$.agents[{index}].accountable_human_review", "Artificial-agent activity requires accountable human review."))

    for index, relation in enumerate(relations):
        for field in ("holder", "counterparty"):
            if relation.get(field) not in agent_ids:
                issues.append(Issue("error", "semantic.agent_ref", f"$.rights_relations[{index}].{field}", f"Unknown agent {relation.get(field)!r}."))
        if relation.get("resource") not in resource_ids:
            issues.append(Issue("error", "semantic.resource_ref", f"$.rights_relations[{index}].resource", f"Unknown resource {relation.get('resource')!r}."))
        for token in relation.get("technical_instruments", []):
            if token not in technical_ids:
                issues.append(Issue("error", "semantic.technical_ref", f"$.rights_relations[{index}].technical_instruments", f"Unknown technical instrument {token!r}."))
        authority_text = " ".join(relation.get("authority_sources", [])).lower().replace("_", "-")
        technical_authority_terms = ("token", "credential", "ledger", "signature", "hash", "smart-contract-execution")
        if authority_text and all(any(term in source.lower().replace("_", "-") for term in technical_authority_terms) for source in relation.get("authority_sources", [])):
            issues.append(Issue("error", "semantic.capability_not_authority", f"$.rights_relations[{index}].authority_sources", "A technical instrument cannot be the sole normative authority for a rights relation."))
        if relation.get("verification_status") == "adjudicated" and status != "adopted":
            issues.append(Issue("warning", "semantic.adjudicated_claim", f"$.rights_relations[{index}].verification_status", "An adjudicated status needs the competent decision and provenance in an adopted profile."))

    for index, identifier in enumerate(profile["grant"].get("eligible_agents", [])):
        if identifier not in agent_ids:
            issues.append(Issue("error", "semantic.grant_agent", f"$.grant.eligible_agents[{index}]", f"Unknown eligible agent {identifier!r}."))

    if phase == "public_inspection":
        forbidden = {"execute", "deploy", "compile", "operate", "run", "process data"}
        permitted_text = " ".join(profile["grant"].get("permitted_actions", [])).lower()
        if any(term in permitted_text for term in forbidden):
            issues.append(Issue("error", "semantic.inspection_operation", "$.grant.permitted_actions", "Public inspection cannot include operational permission."))
        if data.get("enabled"):
            issues.append(Issue("error", "semantic.inspection_data", "$.data_governance.enabled", "Public inspection cannot enable operational information processing."))

    advance_contract_money = [item for item in enforcement.get("financial_remedies", []) if item.get("requires_assent") and item.get("formation_stage") == "pre_event_contract"]
    if formation.get("mode") == "public-notice-only" and advance_contract_money:
        issues.append(Issue("error", "semantic.nonassenter_debt", "$.enforcement.financial_remedies", "A public notice cannot create a pre-event contractual monetary obligation. Statutory claims and later voluntary settlements remain separately available."))
    if formation.get("mode") != "public-notice-only":
        checks = {
            "offer": formation.get("offer"),
            "acceptance_action": formation.get("acceptance_action"),
            "consideration": formation.get("consideration"),
            "intention": formation.get("intention"),
            "terms_version_binding": formation.get("terms_version_binding"),
            "receipt_required": formation.get("receipt_required"),
        }
        for field, value in checks.items():
            if not value:
                issues.append(Issue("error", "semantic.formation", f"$.formation.{field}", "Affirmative contract formation requires this field."))

    if status in {"adoption_candidate", "adopted"}:
        if not legal_review.get("approved"):
            issues.append(Issue("error", "semantic.legal_approval", "$.profile.legal_review.approved", "Adoption candidates and adopted profiles require recorded legal approval."))
        for field in ("reviewer", "approval_id", "expires"):
            if not legal_review.get(field):
                issues.append(Issue("error", "semantic.legal_approval_record", f"$.profile.legal_review.{field}", "A complete legal approval record is required."))
    elif not legal_review.get("approved"):
        issues.append(Issue("warning", "review.legal", "$.profile.legal_review", "Draft has not received qualified legal approval and must not be adopted."))

    if not profile["humanitarian"].get("non_monetisable_harms"):
        issues.append(Issue("error", "semantic.pay_to_harm", "$.humanitarian.non_monetisable_harms", "Payment cannot operate as permission to cause a Prohibited Harm."))
    for field in ("affected_person_priority", "human_review", "appeal"):
        if not profile["humanitarian"].get(field):
            issues.append(Issue("error", "semantic.humanitarian_safeguard", f"$.humanitarian.{field}", "Required humanitarian safeguard is disabled."))
    if not enforcement.get("human_review"):
        issues.append(Issue("error", "semantic.enforcement_review", "$.enforcement.human_review", "Final enforcement decisions require accountable human review."))

    if exclusions.get("active"):
        for field in ("criteria", "legal_basis", "evidence", "necessity", "proportionality", "exceptions", "expiry", "appeal"):
            if not exclusions.get(field):
                issues.append(Issue("error", "semantic.exclusion_basis", f"$.exclusions.{field}", "Active exclusions require this evidence and safeguard."))
        if not exclusions.get("legal_review"):
            issues.append(Issue("error", "semantic.exclusion_review", "$.exclusions.legal_review", "Active exclusions require jurisdiction-specific legal review."))
        if profile["work"].get("publicly_inspectable"):
            issues.append(Issue("warning", "risk.public_exclusion", "$.exclusions.active", "A public repository cannot reliably prevent an excluded actor from seeing source."))

    for index, item in enumerate(technical):
        for field in ("issuer", "subject"):
            if item.get(field) not in agent_ids:
                issues.append(Issue("error", "semantic.technical_agent", f"$.technical_instruments[{index}].{field}", f"Unknown agent {item.get(field)!r}."))
        principal = item.get("principal")
        if principal is not None and principal not in agent_ids:
            issues.append(Issue("error", "semantic.technical_principal", f"$.technical_instruments[{index}].principal", f"Unknown principal {principal!r}."))
        for audience in item.get("audience", []):
            if audience not in agent_ids:
                issues.append(Issue("error", "semantic.technical_audience", f"$.technical_instruments[{index}].audience", f"Unknown audience {audience!r}."))
        if item.get("resource") not in resource_ids:
            issues.append(Issue("error", "semantic.technical_resource", f"$.technical_instruments[{index}].resource", f"Unknown resource {item.get('resource')!r}."))
        if item.get("automated_adjudication"):
            issues.append(Issue("error", "semantic.automated_adjudication", f"$.technical_instruments[{index}].automated_adjudication", "Technical instruments cannot make final disputed-liability decisions."))
        if not item.get("human_review"):
            issues.append(Issue("error", "semantic.technical_review", f"$.technical_instruments[{index}].human_review", "Adverse technical effects require accountable human review."))
        if item.get("instrument_type") == "ledger_record" and item.get("stores_personal_data"):
            issues.append(Issue("error", "semantic.ledger_personal", f"$.technical_instruments[{index}].stores_personal_data", "Default ledger records must use hashes or protected references, not personal content."))
        if item.get("legal_effect") in {"contractually_recognised", "statutorily_recognised", "adjudicated"} and not item.get("authority_sources"):
            issues.append(Issue("error", "semantic.technical_authority", f"$.technical_instruments[{index}].authority_sources", "A stronger legal-effect classification requires an authority source."))
        if item.get("legal_effect") == "contractually_recognised" and formation.get("mode") == "public-notice-only":
            issues.append(Issue("error", "semantic.technical_contract", f"$.technical_instruments[{index}].legal_effect", "Public notice alone cannot give a token contractually recognised effect."))
        if item.get("legal_effect") == "adjudicated" and status != "adopted":
            issues.append(Issue("error", "semantic.technical_adjudicated", f"$.technical_instruments[{index}].legal_effect", "Adjudicated effect requires an adopted profile and competent decision provenance."))

    ledger = profile["ledger"]
    if ledger.get("stores_sensitive_data"):
        issues.append(Issue("error", "semantic.ledger_sensitive", "$.ledger.stores_sensitive_data", "Sensitive content must not be placed in the default immutable ledger design."))
    if ledger.get("enabled") and ledger.get("recording_mode") == "none":
        issues.append(Issue("error", "semantic.ledger_mode", "$.ledger.recording_mode", "Enabled ledger requires a protected recording mode."))
    if ledger.get("enabled") and not ledger.get("human_review"):
        issues.append(Issue("error", "semantic.ledger_review", "$.ledger.human_review", "Ledger disputes and corrections require human review."))

    if data.get("enabled"):
        for field in ("agreement_title", "controllers", "data_subject_agents", "categories", "purposes", "collection_limitation", "data_quality", "use_limitation", "openness", "individual_participation", "retention_and_deletion"):
            if not data.get(field):
                issues.append(Issue("error", "semantic.data_field", f"$.data_governance.{field}", "Enabled rights-governed information processing requires this field."))
        for role_field in ("controllers", "processors", "data_subject_agents"):
            for identifier in data.get(role_field, []):
                if identifier not in agent_ids:
                    issues.append(Issue("error", "semantic.data_agent", f"$.data_governance.{role_field}", f"Unknown agent {identifier!r}."))
        for index, transfer in enumerate(data.get("transfers", [])):
            for role in ("exporter", "importer"):
                if transfer.get(role) not in agent_ids:
                    issues.append(Issue("error", "semantic.transfer_agent", f"$.data_governance.transfers[{index}].{role}", f"Unknown agent {transfer.get(role)!r}."))
            assessment = transfer.get("government_access_assessment", {})
            if not assessment.get("completed"):
                issues.append(Issue("error", "semantic.government_access", f"$.data_governance.transfers[{index}].government_access_assessment", "Cross-border transfer requires a completed government-access assessment."))
            if not transfer.get("suspension_trigger"):
                issues.append(Issue("error", "semantic.transfer_suspend", f"$.data_governance.transfers[{index}].suspension_trigger", "Transfer must be suspendable when continuing protection fails."))
            if not transfer.get("legal_review"):
                severity = "error" if status in {"adoption_candidate", "adopted"} else "warning"
                issues.append(Issue(severity, "review.transfer", f"$.data_governance.transfers[{index}].legal_review", "Transfer mechanism and destination require current jurisdiction-specific legal review."))
            if any(_placeholder(str(transfer.get(field, ""))) for field in ("mechanism", "continuing_protection")):
                issues.append(Issue("warning", "review.transfer_placeholder", f"$.data_governance.transfers[{index}]", "Transfer contains example or placeholder terms."))

    deterrent_words = re.compile(r"\b(punitive|private fine|bounty|punishment|exemplary|deterrent)\b", re.IGNORECASE)
    for index, remedy in enumerate(enforcement.get("financial_remedies", [])):
        text = " ".join(str(value) for value in remedy.values())
        stage = remedy.get("formation_stage")
        if stage in {"pre_event_contract", "post_event_agreement"} and not remedy.get("requires_assent"):
            issues.append(Issue("error", "semantic.remedy_formation", f"$.enforcement.financial_remedies[{index}].requires_assent", "A contractual or settlement-stage amount requires assent."))
        if stage in {"none_statutory", "judgment_or_order", "internal_policy"} and remedy.get("requires_assent"):
            issues.append(Issue("error", "semantic.remedy_formation", f"$.enforcement.financial_remedies[{index}].requires_assent", "This formation stage must not be represented as assent-dependent."))
        if remedy.get("requires_assent") and formation.get("mode") == "public-notice-only" and stage == "pre_event_contract":
            issues.append(Issue("error", "semantic.remedy_assent", f"$.enforcement.financial_remedies[{index}]", "Pre-event contractual money has no affirmative contract-formation route."))
        if deterrent_words.search(text) and remedy.get("remedy_character") != "deterrent":
            issues.append(Issue("warning", "review.deterrent_character", f"$.enforcement.financial_remedies[{index}].remedy_character", "Potentially deterrent language must be classified accurately and reviewed in substance, not rejected merely because deterrence is intended."))
        for field in ("creator_interest_components", "evidence_basis", "proportionality_analysis"):
            if not remedy.get(field):
                issues.append(Issue("error", "semantic.remedy_support", f"$.enforcement.financial_remedies[{index}].{field}", "Financial remedies must record creator interests, evidence, and proportionality support."))
        if not remedy.get("legal_review"):
            severity = "error" if status in {"adoption_candidate", "adopted"} else "warning"
            issues.append(Issue(severity, "review.financial", f"$.enforcement.financial_remedies[{index}].legal_review", "Financial remedy requires penalty, unfair-term, causation, proportionality, and costs review."))
        if _placeholder(str(remedy.get("amount_or_range", ""))) or _placeholder(str(remedy.get("cap", ""))):
            issues.append(Issue("warning", "review.financial_placeholder", f"$.enforcement.financial_remedies[{index}]", "Financial amount or cap remains a placeholder."))

    deterrence = enforcement.get("deterrence", {})
    if deterrence.get("enabled") and not enforcement.get("financial_remedies"):
        issues.append(Issue("error", "semantic.deterrence_empty", "$.enforcement.financial_remedies", "Enabled deterrence requires at least one legally classified remedy or recovery pathway."))
    if not deterrence.get("jurisdictional_review"):
        severity = "error" if status in {"adoption_candidate", "adopted"} else "warning"
        issues.append(Issue(severity, "review.deterrence", "$.enforcement.deterrence.jurisdictional_review", "Deterrence pathways require current jurisdiction-specific review, including copyright, contract, penalty, remedies, costs, funding, consumer, and professional rules."))

    funding = enforcement.get("enforcement_funding", {})
    if funding.get("enabled"):
        for field in ("separate_agreement_required", "creator_control_preserved"):
            if not funding.get(field):
                issues.append(Issue("error", "semantic.funding_safeguard", f"$.enforcement.enforcement_funding.{field}", "Enabled enforcement funding must preserve this creator safeguard."))
        if not funding.get("professional_rules_review") or not funding.get("legal_review"):
            severity = "error" if status in {"adoption_candidate", "adopted"} else "warning"
            issues.append(Issue(severity, "review.enforcement_funding", "$.enforcement.enforcement_funding", "Funding, conditional-fee, commission, referral, control, adverse-cost, privilege, and professional-rule terms require jurisdiction-specific approval."))
    waterfall_text = " ".join(enforcement.get("recovery_waterfall", [])[:3]).lower()
    if not any(term in waterfall_text for term in ("creator", "rights holder", "rightsholder")):
        issues.append(Issue("error", "semantic.creator_recovery_priority", "$.enforcement.recovery_waterfall", "Creator or rights-holder restitution must appear among the first three recovery priorities."))

    if profile["jurisdiction"].get("trade_law_review"):
        issues.append(Issue("warning", "review.trade", "$.jurisdiction.trade_law_review", "International trade and cross-border market effects are flagged for qualified review."))

    for path, value in (
        ("$.rights_holder.legal_name", profile["rights_holder"].get("legal_name", "")),
        ("$.rights_holder.service_address", profile["rights_holder"].get("service_address", "")),
        ("$.work.title", profile["work"].get("title", "")),
        ("$.work.manifest_uri", profile["work"].get("manifest_uri", "")),
    ):
        if _placeholder(str(value)):
            issues.append(Issue("warning", "review.placeholder", path, "Placeholder must be replaced before adoption."))

    return issues


def validate_profile(profile: dict[str, Any], schema: dict[str, Any]) -> ValidationResult:
    issues = validate_schema(profile, schema)
    if not any(issue.severity == "error" for issue in issues):
        issues.extend(validate_semantics(profile))
    issues.sort(key=lambda item: (0 if item.severity == "error" else 1, item.path, item.code))
    return ValidationResult(issues)


def _escape(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def _bullets(values: Iterable[Any], empty: str = "None specified.") -> str:
    items = list(values)
    return "\n".join(f"- {_escape(value)}" for value in items) if items else empty


def _numbered(values: Iterable[Any], empty: str = "None specified.") -> str:
    items = list(values)
    return "\n".join(f"{index}. {_escape(value)}" for index, value in enumerate(items, 1)) if items else empty


def _banner(profile: dict[str, Any]) -> str:
    review = profile["profile"]["legal_review"]
    if profile["profile"]["status"] == "adopted" and review.get("approved"):
        return f"Status: generated from adopted profile; approval record `{_escape(review.get('approval_id'))}` must be independently verified"
    return "Status: DRAFT — NOT APPROVED FOR PRODUCTION USE"


def render_contract(profile: dict[str, Any]) -> str:
    p = profile["profile"]
    holder = profile["rights_holder"]
    work = profile["work"]
    formation = profile["formation"]
    grant = profile["grant"]
    humanitarian = profile["humanitarian"]
    creator = profile["creator_protection"]
    jurisdiction = profile["jurisdiction"]
    phase = profile["release_phase"].replace("_", " ")
    if formation["mode"] == "public-notice-only":
        formation_text = (
            "This release uses public notice only. Viewing or prohibited use does not create a contract. "
            "Only the stated copyright permission, hosting permissions, statutory exceptions, and other applicable law operate."
        )
    else:
        formation_text = (
            f"The complete instrument is offered through **{formation['mode']}** formation. Offer: {formation['offer']} "
            f"Acceptance: {formation['acceptance_action']} Intention to create legal relations is recorded as "
            f"{formation['intention']}. The proposed formation basis is: {formation['consideration']} "
            "The acceptance record must bind the party, authority evidence, Work release, every incorporated artifact, "
            "their hashes, the time and place of acceptance, and a durable receipt."
        )
    return f"""# Contract and Intellectual-Property Licence

{_banner(profile)}  
Generated by version {GENERATOR_VERSION} from profile `{p['id']}` version `{p['version']}`.

> This generated instrument requires qualified legal review, completed party and release information, and formal adoption. It does not determine that any person has accepted it or that any term is enforceable.

## 1. Parties and instrument

**Licensor / Rights Holder:** {holder['legal_name']}  
**Service address:** {holder['service_address']}  
**Contact:** {holder['contact']}  
**Licensing capacity:** {holder['licensing_capacity']}

“Contract” means the accepted contractual terms and incorporated schedules. “Licence” means only the copyright and related permission expressly granted below. A covenant, token, ledger record, payment, or data relation does not expand the Licence.

## 2. Formation

{formation_text}

Merely possessing source, receiving information, controlling a key, or holding a technical token does not establish acceptance, capacity, authority, ownership, consent, or a broader licence.

## 3. Work and release

The “Work” is **{work['title']}**, release `{work['release_id']}`, SHA-256 `{work['sha256']}`, identified by `{work['manifest_uri']}`, only to the extent the Licensor is authorised to license it. Third-party material remains subject to its own terms.

Release phase: **{phase}**. Public inspectability: **{str(work['publicly_inspectable']).lower()}**.

## 4. Creator autonomy and material interests

The creator retains the choice to refuse, condition, price, suspend, or withhold every permission not already required by law or expressly granted in an adopted instrument. Public inspection and technical accessibility are not permission. An excluded actor receives no Licence. Commercial exploitation and AI ingestion, training, embedding, fine-tuning, evaluation, retrieval, or derivation require express permission to the extent stated by the adopted grant and applicable law.

The parties recognise the creator's moral and material interests, invested labour, compute and token expenditure, infrastructure, capital, professional work, opportunity cost, safety work, and enforcement burden. Those interests are detailed in `CREATOR-INTERESTS-AND-INVESTMENT-SCHEDULE.md`; unpaid work is not valued at zero merely because the creator initially bore its cost.

Creator protection basis: {creator['ownership_and_authority']}

## 5. Grant

Subject to formation, eligibility, the Rights-Ontology Schedule, and this instrument, the Licensor grants the eligible agents a non-transferable, non-sublicensable permission to perform only:

{_bullets(grant['permitted_actions'])}

Purpose: **{grant['purpose']}**  
Duration: **{grant['duration']}**

No other copyright, patent, trademark, database, trade-secret, privacy, data, operational, production, commercial, or other permission is granted by implication.

## 6. Grant boundaries and contractual duties

The following acts are outside the grant or contractually prohibited as classified in the Rights-Ontology Schedule:

{_bullets(grant['prohibited_actions'])}

Every implementation must distinguish an IP grant boundary from a contractual covenant, representation, warranty, statutory notice, or procedure. Labelling a promise does not determine its legal construction.

## 7. Prohibited Harms

No permission is granted to cause, facilitate, conceal, profit from, or evade accountability for:

{_bullets(humanitarian['prohibited_harms'])}

These interests are non-monetisable. Payment, damages, settlement, a token, or a retroactive licence cannot purchase permission to commit or continue a Prohibited Harm. Urgent safety, cessation, evidence, affected-person remedy, accountability, and non-recurrence take priority over revenue.

## 8. Rights ontology

`RIGHTS-ONTOLOGY-SCHEDULE.md` is incorporated only when identified in the accepted artifact record. It specifies the holder, counterparty, jural position, action, resource, purpose, authority, evidence, technical instruments, validity, delegation, and remedy for each relation.

Technical capability is not normative permission. Data transfer is not transfer of rights. Delegation does not remove the principal's responsibility. A machine-generated or ledger-recorded assertion is not an adjudicated fact.

## 9. Rights-governed information

Any authorised collection, storage, processing, derivation, inference, disclosure, or cross-border access is governed separately by `RIGHTS-GOVERNED-INFORMATION-AGREEMENT.md`. Permission to operate the Work does not grant ownership of or unrestricted rights over information processed through it.

## 10. Technical instruments

Tokens, credentials, signatures, smart-contract executions, and ledger records are governed by `TECHNICAL-INSTRUMENTS-SCHEDULE.md`. Their default legal effect is evidentiary or technical. A stronger legal effect exists only through an identified, valid authority source.

## 11. Termination and persistence

{grant['termination']}

Termination does not erase accrued claims, protected evidence, attribution, third-party-anchored obligations, co-owned records, valid statutory retention, artifact-attached safeguards, or remedies that properly survive.

## 12. Enforcement

`ENFORCEMENT-AND-REMEDIES-SCHEDULE.md` applies only when validly incorporated. Unauthorised conduct is not contractual acceptance. A non-assenter does not owe a contractual debt merely because a notice or schedule states an amount. Statutory remedies and settlement offers retain their distinct legal character.

## 13. Mandatory law and interpretation

Nothing excludes an exception, guarantee, remedy, privacy position, data-subject position, human-rights protection, or other rule that applicable law does not permit the parties to exclude. The Rights-Ontology Schedule aids precise interpretation but does not override the adopted legal text or competent law.

## 14. Governing law and forum

Proposed governing law: **{jurisdiction['governing_law']}**  
Proposed forum: **{jurisdiction['forum']}**

Mandatory law, jurisdiction where conduct or effects occur, affected-person remedies, privacy enforcement, trade rules, and enforceability require separate review. Urgent protective relief remains available where law permits.
"""


def render_creator_schedule(profile: dict[str, Any]) -> str:
    creator = profile["creator_protection"]
    rows = []
    for item in creator["investments"]:
        rows.append(
            "| " + " | ".join(
                _escape(value)
                for value in (
                    item["id"], item["contributor"], item["category"], item["description"],
                    item["valuation_method"], "; ".join(item["evidence"]), item["recovery_treatment"],
                )
            ) + " |"
        )
    return f"""# Creator Interests and Investment Schedule

{_banner(profile)}

The creator is an affected natural person and rights-bearing participant in this humanitarian framework. The creator is not required to donate labour, compute, token expenditure, capital, opportunity, safety work, intellectual production, or enforcement effort to an unauthorised exploiter.

## 1. Creator-control rules

- Identified creator agents: {', '.join(creator['creator_agents'])}
- Ownership and authority basis: {creator['ownership_and_authority']}
- Public inspection is not operational or commercial permission: {str(creator['public_inspection_not_permission']).lower()}
- Technical access or possession is not permission: {str(creator['technical_access_not_permission']).lower()}
- Commercial exploitation requires permission: {str(creator['commercial_exploitation_requires_permission']).lower()}
- AI use requires express permission: {str(creator['ai_use_requires_express_permission']).lower()}
- The creator may refuse or condition a licence: {str(creator['may_refuse_or_condition_licence']).lower()}
- Excluded agents receive no licence: {str(creator['excluded_agents_receive_no_licence']).lower()}
- Creator economic survival is a humanitarian interest: {str(creator['creator_economic_survival_is_humanitarian_interest']).lower()}

Subject to mandatory law and verified title, the creator holds the privilege to withhold permission, the power to grant permission on selected conditions, a claim that assenting licensees remain within the grant, and an immunity against a technical system unilaterally enlarging another agent's rights. The absence of permission is not cured by the exploiter's wealth, technical capability, claimed utility, or willingness to litigate.

## 2. Investment register

| ID | Contributor | Category | Description | Valuation method | Evidence | Recovery treatment |
| --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(rows)}

The register is evidence architecture, not an automatic damages calculation. It prevents creator-supplied resources from disappearing from pricing, loss, settlement, proportionality, legitimate-interest, profit-recovery, and enforcement-funding analysis.

## 3. AI-assisted production and provenance

{creator['ai_contribution_policy']}

Provider terms, copyright subsistence, authorship, confidentiality, privacy, trade-secret treatment, patent consequences, and third-party inputs require separate review. The framework records human and machine contributions rather than presuming that payment for an AI service either destroys or proves the creator's rights.

## 4. Exploitation boundary

No implied permission arises for commercial operation, hosted service, resale, redistribution, model training, fine-tuning, embedding, retrieval ingestion, benchmark or safety evaluation, synthetic-data generation, extraction of protected expression, removal of safeguards, or the creation of a competing derivative product. The precise reach of copyright, contract, confidentiality, technological-protection, database, passing-off, consumer, competition, privacy, or other law remains jurisdiction- and fact-specific.
"""


def render_rights_schedule(profile: dict[str, Any]) -> str:
    rows = []
    for relation in profile["rights_relations"]:
        rows.append(
            "| " + " | ".join(
                _escape(value)
                for value in (
                    relation["id"], relation["position"], CORRELATIVES[relation["position"]],
                    relation["holder"], relation["counterparty"], relation["action"], relation["resource"],
                    relation["purpose"], "; ".join(relation["authority_sources"]), relation["verification_status"],
                )
            ) + " |"
        )
    details = []
    for relation in profile["rights_relations"]:
        details.append(f"""### `{relation['id']}`

- Context: {relation['context']}
- Legal instruments: {', '.join(relation['legal_instruments']) or 'None identified'}
- Technical instruments: {', '.join(relation['technical_instruments']) or 'None identified'}
- Conditions: {'; '.join(relation['conditions']) or 'None stated'}
- Validity: {relation['validity']}
- Delegation depth: {relation['delegation_depth']}
- Evidence: {'; '.join(relation['evidence'])}
- Remedy: {'; '.join(relation['remedy'])}
""")
    return f"""# Rights-Ontology Schedule

{_banner(profile)}

This schedule is the human-readable rendering of the profile's normative relations. The correlative column is derived from the Web Civics Hohfeldian jural vocabulary; it does not invent a new authority source.

| ID | Position | Correlative | Holder | Counterparty | Action | Resource | Purpose | Authority | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(rows)}

## Interpretation rules

1. A rights statement operates only within its stated frame and authority.
2. Receipt or possession of a resource does not transfer every relation concerning it.
3. A capability token enables an action only technically; it is not the authority source.
4. A principal remains visible when an artificial agent acts.
5. Natural-person-only dignity positions are not assigned to corporations or artificial agents.
6. Machine-proposed and disputed statements are not represented as verified or adjudicated.
7. Every adverse decision requires evidence, accountable human review, correction, and remedy.

## Relation details

{chr(10).join(details)}
"""


def render_data_agreement(profile: dict[str, Any]) -> str:
    data = profile["data_governance"]
    if not data["enabled"]:
        body = """## No operational information permission

This profile does not authorise the Work to collect, store, process, infer from, derive from, disclose, or transfer personal, confidential, sensitive, or other operational information. A separate reviewed profile and agreement are required before any such activity.
"""
    else:
        transfer_sections = []
        for transfer in data["transfers"]:
            assessment = transfer["government_access_assessment"]
            transfer_sections.append(f"""### Transfer `{transfer['id']}`

- Exporter: `{transfer['exporter']}`
- Importer: `{transfer['importer']}`
- Origin / destination: {transfer['origin']} → {transfer['destination']}
- Categories: {', '.join(transfer['data_categories'])}
- Purpose: {transfer['purpose']}
- Mechanism: {transfer['mechanism']}
- Remote access: {str(transfer['remote_access']).lower()}
- Onward transfer: {transfer['onward_transfer']}
- Continuing protection: {transfer['continuing_protection']}
- Localisation review recorded: {str(transfer['localisation_review']).lower()}
- Suspension trigger: {transfer['suspension_trigger']}
- Legal review complete: {str(transfer['legal_review']).lower()}

Government-access assessment:

- Completed: {str(assessment['completed']).lower()}
- Legal basis: {assessment['legal_basis']}
- Necessity and proportionality: {assessment['necessity_and_proportionality']}
- Oversight: {assessment['oversight']}
- Transparency: {assessment['transparency']}
- Redress: {assessment['redress']}
""")
        body = f"""## 1. Parties and roles

Agreement title: **{data['agreement_title']}**

- Controllers or functionally equivalent decision-makers: {', '.join(data['controllers'])}
- Processors, custodians, or directed agents: {', '.join(data['processors']) or 'None specified'}
- Data-subject or affected-person agents: {', '.join(data['data_subject_agents'])}

Roles are determined by applicable law and facts, not solely by contractual labels.

## 2. Resources and purposes

Categories:

{_bullets(data['categories'])}

Purposes:

{_bullets(data['purposes'])}

No possession, technical access, token, transfer, or processing event creates undifferentiated “ownership of data”. Rights and duties are those identified in the Rights-Ontology Schedule and applicable authority sources.

## 3. OECD-aligned protections

- Collection limitation: {data['collection_limitation']}
- Data quality: {data['data_quality']}
- Use limitation: {data['use_limitation']}
- Openness: {data['openness']}
- Individual participation: {data['individual_participation']}
- Retention and deletion: {data['retention_and_deletion']}

Security safeguards:

{_bullets(data['security_safeguards'])}

Accountability continues regardless of location. Any restriction or transfer must be transparent, risk-based, necessary, and proportionate, and must preserve applicable intellectual-property, privacy, confidentiality, human-rights, security, participation, and remedy positions.

## 4. Social and multi-agent relations

Consent is scoped, time-indexed, and only one possible authority source. Relation-gated capabilities revoke on exit. Third-party-anchored obligations, co-owned records, valid statutory retention, and artifact-attached safeguards follow their own persistence rules. Artificial agents act through identified principals and cannot be the endpoint of accountability.

## 5. Transborder flows

{chr(10).join(transfer_sections) if transfer_sections else 'No transborder transfer is authorised.'}

## 6. Government demands

To the extent lawful, a recipient must scrutinise and minimise a demand, verify authority, challenge a disproportionate demand, notify the appropriate party or affected person, preserve evidence, report permitted transparency information, and suspend transfers when continuing protection cannot be maintained. Nothing requires obstruction of lawful process.

## 7. Exit and remedy

Exit must revoke relation-gated access promptly while preserving each valid persistence class. The procedure must provide notice, access, correction, challenge, restriction, portability where applicable, complaint, representation, restoration, and effective external remedy without exposing protected third-party information.
"""
    return f"""# Rights-Governed Information Agreement

{_banner(profile)}

This instrument governs normative relations concerning information. “Sharing” is one possible action; it is not a transfer of every right. OECD instruments guide the design but do not automatically become private contractual law.

{body}
"""


def render_technical_schedule(profile: dict[str, Any]) -> str:
    rows = []
    details = []
    for item in profile["technical_instruments"]:
        rows.append(
            "| " + " | ".join(
                _escape(value)
                for value in (
                    item["id"], item["instrument_type"], item["issuer"], item["subject"], item["resource"],
                    ", ".join(item["actions"]), item["legal_effect"], item["delegation_depth"],
                )
            ) + " |"
        )
        details.append(f"""### `{item['id']}`

- Principal: {item['principal'] or 'None stated'}
- Audience: {', '.join(item['audience'])}
- Purpose: {item['purpose']}
- Authority sources: {', '.join(item['authority_sources'])}
- Cryptographic suite: {item['cryptographic_suite']}
- Validity: {item['validity']}
- Revocation: {item['revocation']}
- Stores personal data: {str(item['stores_personal_data']).lower()}
- Human review: {str(item['human_review']).lower()}
- Automated adjudication: {str(item['automated_adjudication']).lower()}
""")
    ledger = profile["ledger"]
    return f"""# Technical Instruments and Ledger Schedule

{_banner(profile)}

Technical instruments operationalise or evidence rights statements. They are not independent sources of normative authority.

| ID | Type | Issuer | Subject | Resource | Actions | Legal effect | Delegation depth |
| --- | --- | --- | --- | --- | --- | --- | ---: |
{chr(10).join(rows) if rows else '| — | — | — | — | — | — | — | — |'}

## Instrument details

{chr(10).join(details) if details else 'No technical instruments are enabled.'}

## Ledger policy

- Enabled: {str(ledger['enabled']).lower()}
- Technology: {ledger['technology'] or 'None'}
- Recording mode: {ledger['recording_mode']}
- Stores sensitive data: {str(ledger['stores_sensitive_data']).lower()}
- Correction: {ledger['correction_strategy']}
- Revocation: {ledger['revocation_strategy']}
- Key compromise: {ledger['key_compromise_process']}
- Human review: {str(ledger['human_review']).lower()}

The default record stores hashes, commitments, pseudonymous references, or protected pointers—not sensitive content. A timestamp or signature proves neither voluntariness nor legal authority by itself. Incorrect immutable assertions receive signed dispute, correction, or superseding records.

## Executable-instrument boundary

A smart-contract execution is performance evidence for an encoded subset. The adopted legal text, governing law, program hash, oracle assumptions, conflict rule, pause, correction, key-loss, coercion, exploit, and appeal processes must be recorded. Code cannot autonomously determine criminal guilt, final civil liability, personal exclusion, Prohibited Harm, or coercive enforcement.
"""


def render_enforcement(profile: dict[str, Any]) -> str:
    enforcement = profile["enforcement"]
    deterrence = enforcement["deterrence"]
    funding = enforcement["enforcement_funding"]
    remedy_rows = []
    remedy_details = []
    for item in enforcement["financial_remedies"]:
        remedy_rows.append(
            "| " + " | ".join(
                _escape(value)
                for value in (
                    item["id"], item["basis"], item["formation_stage"], item["remedy_character"],
                    item["trigger"], item["amount_or_range"], item["becomes_payable_when"],
                )
            ) + " |"
        )
        remedy_details.append(f"""### `{item['id']}`

- Legitimate interests: {item['legitimate_interest']}
- Creator-interest components: {'; '.join(item['creator_interest_components'])}
- Valuation: {item['valuation_method']}
- Evidence: {'; '.join(item['evidence_basis'])}
- Proportionality: {item['proportionality_analysis']}
- Causal link: {item['causal_link']}
- Cap or limit: {item['cap']}
- Duplication group: {item['duplication_group']}
- Review and dispute: {item['review_and_dispute']}
- Jurisdictional legal review completed: {str(item['legal_review']).lower()}
""")
    return f"""# Enforcement and Remedies Schedule

{_banner(profile)}

This schedule distinguishes accepted contractual duties, copyright or other statutory claims, settlements, judgments, and project allocation policy. It does not create a debt against a non-assenter.

## 1. Procedure

- Notice: {enforcement['notice']}
- Cure: {enforcement['cure']}
- Urgent protection: {enforcement['urgent_protection']}
- Appeal: {enforcement['appeal']}
- Evidence preservation: {enforcement['evidence_preservation']}
- Affected-person remedy: {enforcement['affected_person_remedy']}
- Creator remedy: {enforcement['creator_remedy']}
- Non-licensee notice: {enforcement['non_licensee_notice']}

An accountable human must classify the event as compliant use, covenant breach, act outside the IP grant, post-termination act, non-assenter conduct, statutory exception, mistaken allegation, or affected-person harm before selecting a response.

## 2. Deterrence and creator restoration

Deterrence enabled: **{str(deterrence['enabled']).lower()}**  
Objective: {deterrence['objective']}

Protected interests:

{_bullets(deterrence['protected_interests'])}

Required evidence:

{_bullets(deterrence['evidence_required'])}

- Accepted-contract path: {deterrence['contract_path']}
- Non-assenter path: {deterrence['non_assenter_path']}
- Profit recovery: {deterrence['profit_recovery']}
- Creator cost recovery: {deterrence['creator_cost_recovery']}
- Additional or enhanced damages: {deterrence['additional_damages_reservation']}
- Jurisdictional review completed: {str(deterrence['jurisdictional_review']).lower()}

Deterrence is a legitimate design objective. The schedule does not erase it merely because a remedy may be described as punitive, exemplary, enhanced, additional, or recovery-contingent. Instead, it classifies the legal basis, decision-maker, formation route, evidence, legitimate interests, proportionality, and payment event. A private agreement cannot itself impose a criminal fine, while a court-controlled or statutory deterrent remedy remains fully reserved where applicable.

## 3. Financial components

| ID | Basis | Formation stage | Character | Trigger | Amount/range | Payable event |
| --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(remedy_rows) if remedy_rows else '| — | No remedy configured | — | — | — | — | — |'}

{chr(10).join(remedy_details)}

Every component requires its stated legal or contractual basis, formation where applicable, evidence, proportionality, non-duplication, and a legally sufficient event making the amount due. A settlement or retroactive-licence price is an offer until accepted. A creator need not offer a retroactive licence for harmful, unsafe, excluded, or strategically unacceptable use.

## 4. Enforcement funding

- Enabled: {str(funding['enabled']).lower()}
- Mechanisms: {', '.join(funding['mechanisms'])}
- Separate agreement required: {str(funding['separate_agreement_required']).lower()}
- Creator control preserved: {str(funding['creator_control_preserved']).lower()}
- Professional-rules review completed: {str(funding['professional_rules_review']).lower()}
- Legal review completed: {str(funding['legal_review']).lower()}
- Allocation: {funding['allocation']}

Safeguards:

{_bullets(funding['safeguards'])}

The framework permits a recovery-contingent enforcement reward, conditional fee, litigation funding, rights-management mandate, collective mechanism, or creator reserve where a separate lawful agreement establishes it. This makes enforcement economically possible without converting an accusation into a debt or transferring final control to an unaccountable funder.

## 5. Prohibited Harms

Money cannot authorise a Prohibited Harm. Priorities are immediate safety, cessation, evidence, identification of principals and operators, affected-person participation and remedy, restoration, accountability, and non-recurrence. Deliberate gain, concealment, recurrence, evidence destruction, vulnerability targeting, and post-notice conduct are recorded only as potential facts for competent review.

## 6. Recovery allocation

{_numbered(enforcement['recovery_waterfall'])}

The creator is expressly an affected person. The waterfall must not erase the creator's lost use value, invested resources, opportunity, attributable gain, or cost of enforcing the right. It operates subject to binding law, court orders, affected-person rights, funding agreements, insurance, insolvency priorities, and professional rules.
"""


def render_jsonld(profile: dict[str, Any]) -> dict[str, Any]:
    base = f"urn:hro-profile:{profile['profile']['id']}:"
    graph: list[dict[str, Any]] = []
    for agent in profile["agents"]:
        graph.append({
            "id": f"{base}agent:{agent['id']}",
            "type": "values:Agent",
            "name": agent["name"],
            "agentType": agent["agent_type"],
            "roles": agent["roles"],
            "principal": f"{base}agent:{agent['principal']}" if agent["principal"] else None,
            "requiresHumanReview": agent["accountable_human_review"],
        })
    for resource in profile["resources"]:
        graph.append({
            "id": f"{base}resource:{resource['id']}",
            "type": "hro:InformationResource",
            "name": resource["name"],
            "categories": resource["categories"],
            "sensitivity": resource["sensitivity"],
            "persistenceClass": resource["persistence_class"],
        })
    for relation in profile["rights_relations"]:
        graph.append({
            "id": f"{base}relation:{relation['id']}",
            "type": ["hro:RightsStatement", JURAL_TYPES[relation["position"]]],
            "position": JURAL_TYPES[relation["position"]],
            "correlativePosition": JURAL_TYPES[CORRELATIVES[relation["position"]]],
            "holder": f"{base}agent:{relation['holder']}",
            "counterparty": f"{base}agent:{relation['counterparty']}",
            "action": relation["action"],
            "resource": f"{base}resource:{relation['resource']}",
            "purpose": relation["purpose"],
            "context": relation["context"],
            "authoritySource": [f"urn:authority:{_slug(item)}" for item in relation["authority_sources"]],
            "legalInstrument": [f"urn:legal-instrument:{_slug(item)}" for item in relation["legal_instruments"]],
            "technicalInstrument": [f"{base}technical:{item}" for item in relation["technical_instruments"]],
            "condition": relation["conditions"],
            "validity": relation["validity"],
            "delegationDepth": relation["delegation_depth"],
            "evidenceDescription": relation["evidence"],
            "verificationStatus": f"hro:{relation['verification_status'].title()}",
            "remedyDescription": relation["remedy"],
        })
    creator = profile["creator_protection"]
    creator_policy_id = f"{base}creator-protection"
    graph.append({
        "id": creator_policy_id,
        "type": "hro:CreatorProtectionPolicy",
        "creator": [f"{base}agent:{value}" for value in creator["creator_agents"]],
        "ownershipAndAuthority": creator["ownership_and_authority"],
        "publicInspectionNotPermission": creator["public_inspection_not_permission"],
        "technicalAccessNotPermission": creator["technical_access_not_permission"],
        "commercialExploitationRequiresPermission": creator["commercial_exploitation_requires_permission"],
        "aiUseRequiresExpressPermission": creator["ai_use_requires_express_permission"],
        "mayRefuseOrConditionLicence": creator["may_refuse_or_condition_licence"],
        "excludedAgentsReceiveNoLicence": creator["excluded_agents_receive_no_licence"],
        "creatorEconomicSurvivalIsHumanitarianInterest": creator["creator_economic_survival_is_humanitarian_interest"],
        "aiContributionPolicy": creator["ai_contribution_policy"],
        "investment": [f"{base}investment:{item['id']}" for item in creator["investments"]],
    })
    for item in creator["investments"]:
        graph.append({
            "id": f"{base}investment:{item['id']}",
            "type": "hro:CreatorInvestment",
            "contributor": f"{base}agent:{item['contributor']}",
            "investmentCategory": item["category"],
            "description": item["description"],
            "valuationMethod": item["valuation_method"],
            "evidenceDescription": item["evidence"],
            "recoveryTreatment": item["recovery_treatment"],
        })
    for item in profile["technical_instruments"]:
        graph.append({
            "id": f"{base}technical:{item['id']}",
            "type": TECHNICAL_TYPES[item["instrument_type"]],
            "issuer": f"{base}agent:{item['issuer']}",
            "subject": f"{base}agent:{item['subject']}",
            "principal": f"{base}agent:{item['principal']}" if item["principal"] else None,
            "audience": [f"{base}agent:{value}" for value in item["audience"]],
            "resource": f"{base}resource:{item['resource']}",
            "action": item["actions"],
            "purpose": item["purpose"],
            "authoritySource": [f"urn:authority:{_slug(value)}" for value in item["authority_sources"]],
            "legalEffect": LEGAL_EFFECTS[item["legal_effect"]],
            "cryptographicSuite": item["cryptographic_suite"],
            "validity": item["validity"],
            "delegationDepth": item["delegation_depth"],
            "revocationMechanism": item["revocation"],
            "storesPersonalData": item["stores_personal_data"],
            "requiresHumanReview": item["human_review"],
            "automatedAdjudication": item["automated_adjudication"],
        })
    return {
        "@context": {
            "hro": "https://ns.webcivics.net/license-rights/",
            "jural": "https://ns.webcivics.net/jural/",
            "values": "https://ns.webcivics.net/values/",
            "prov": "http://www.w3.org/ns/prov#",
            "odrl": "http://www.w3.org/ns/odrl/2/",
            "id": "@id", "type": "@type",
            "position": {"@id": "hro:position", "@type": "@id"},
            "holder": {"@id": "hro:holder", "@type": "@id"},
            "counterparty": {"@id": "hro:counterparty", "@type": "@id"},
            "resource": {"@id": "hro:resource", "@type": "@id"},
            "authoritySource": {"@id": "hro:authoritySource", "@type": "@id"},
            "legalInstrument": {"@id": "hro:legalInstrument", "@type": "@id"},
            "technicalInstrument": {"@id": "hro:technicalInstrument", "@type": "@id"},
            "issuer": {"@id": "hro:issuer", "@type": "@id"},
            "subject": {"@id": "hro:subject", "@type": "@id"},
            "principal": {"@id": "hro:principal", "@type": "@id"},
            "audience": {"@id": "hro:audience", "@type": "@id"},
            "legalEffect": {"@id": "hro:legalEffect", "@type": "@id"},
            "creator": {"@id": "hro:creator", "@type": "@id"},
            "contributor": {"@id": "hro:contributor", "@type": "@id"},
            "investment": {"@id": "hro:investment", "@type": "@id"},
        },
        "id": f"{base}policy",
        "type": "odrl:Policy",
        "profileId": profile["profile"]["id"],
        "profileVersion": profile["profile"]["version"],
        "generatorVersion": GENERATOR_VERSION,
        "@graph": graph,
    }


def _slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "unspecified"


def render_validation_report(profile: dict[str, Any], result: ValidationResult) -> str:
    rows = []
    for issue in result.issues:
        rows.append(f"| {issue.severity.upper()} | `{issue.code}` | `{_escape(issue.path)}` | {_escape(issue.message)} |")
    return f"""# Validation Report

Profile: `{profile.get('profile', {}).get('id', 'unknown')}`  
Generator: `{GENERATOR_VERSION}`  
Result: **{'PASS' if result.valid else 'FAIL'}**  
Errors: **{len(result.errors)}**  
Warnings: **{len(result.warnings)}**

Passing validation means the profile satisfies this generator's structural and semantic safeguards. It is not legal advice, legal approval, a factual verification, or an adoption record.

| Severity | Code | Path | Message |
| --- | --- | --- | --- |
{chr(10).join(rows) if rows else '| INFO | `validation.clean` | `$` | No issues found. |'}
"""


def _write_text(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def _write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def generate(profile: dict[str, Any], schema: dict[str, Any], output: Path) -> dict[str, Any]:
    result = validate_profile(profile, schema)
    if not result.valid:
        raise ValueError(f"Profile has {len(result.errors)} validation error(s).")
    if output.exists() and any(output.iterdir()):
        raise FileExistsError(f"Output directory is not empty: {output}")
    output.mkdir(parents=True, exist_ok=True)

    rendered_text = {
        "CONTRACT-AND-IP-LICENCE.md": render_contract(profile),
        "CREATOR-INTERESTS-AND-INVESTMENT-SCHEDULE.md": render_creator_schedule(profile),
        "RIGHTS-ONTOLOGY-SCHEDULE.md": render_rights_schedule(profile),
        "RIGHTS-GOVERNED-INFORMATION-AGREEMENT.md": render_data_agreement(profile),
        "TECHNICAL-INSTRUMENTS-SCHEDULE.md": render_technical_schedule(profile),
        "ENFORCEMENT-AND-REMEDIES-SCHEDULE.md": render_enforcement(profile),
        "VALIDATION-REPORT.md": render_validation_report(profile, result),
    }
    for name, text in rendered_text.items():
        _write_text(output / name, text)
    _write_json(output / "RIGHTS-POLICY.jsonld", render_jsonld(profile))

    terms_files = sorted([*rendered_text.keys(), "RIGHTS-POLICY.jsonld"])
    terms_hashes = {name: sha256_file(output / name) for name in terms_files}
    receipt = {
        "template": True,
        "profile_id": profile["profile"]["id"],
        "profile_version": profile["profile"]["version"],
        "profile_sha256": sha256_json(profile),
        "work": {
            "id": profile["work"]["id"],
            "release_id": profile["work"]["release_id"],
            "sha256": profile["work"]["sha256"],
        },
        "formation_mode": profile["formation"]["mode"],
        "artifacts": [{"name": name, "sha256": terms_hashes[name]} for name in terms_files],
        "offeror": profile["rights_holder"]["id"],
        "offeree": "[record verified identity]",
        "offeree_capacity": "[record capacity]",
        "principal_and_authority": "[record personal capacity or identified principal and authority]",
        "acceptance_action": "[record affirmative action or signature]",
        "accepted_at": "[ISO 8601 date-time]",
        "accepted_in": "[relevant place and jurisdiction evidence]",
        "consideration_or_formal_basis": profile["formation"]["consideration"],
        "signature_or_proof": "[implementation-specific proof]",
        "status": "template-not-accepted",
        "notice": "This record is evidence only. Formation, identity, capacity, authority, voluntariness, and legal effect depend on applicable law and facts.",
    }
    _write_json(output / "ACCEPTANCE-RECEIPT-TEMPLATE.json", receipt)

    all_without_manifest = [name for name in OUTPUT_NAMES if name != "RELEASE-MANIFEST.json"]
    manifest = {
        "manifest_version": "1.0",
        "generator_version": GENERATOR_VERSION,
        "profile_id": profile["profile"]["id"],
        "profile_version": profile["profile"]["version"],
        "profile_sha256": sha256_json(profile),
        "work_release_id": profile["work"]["release_id"],
        "work_sha256": profile["work"]["sha256"],
        "legal_review_approved": profile["profile"]["legal_review"]["approved"],
        "adoption_status": profile["profile"]["status"],
        "artifacts": [{"name": name, "sha256": sha256_file(output / name)} for name in all_without_manifest],
        "sources": profile["sources"],
        "notice": "Hashes identify generated drafts. This manifest is not an adoption, acceptance, or legal-validity determination.",
    }
    _write_json(output / "RELEASE-MANIFEST.json", manifest)
    return manifest


def _print_result(result: ValidationResult, as_json: bool) -> None:
    if as_json:
        print(json.dumps(result.as_dict(), ensure_ascii=False, indent=2))
        return
    print(f"Validation: {'PASS' if result.valid else 'FAIL'} ({len(result.errors)} error(s), {len(result.warnings)} warning(s))")
    for issue in result.issues:
        print(f"{issue.severity.upper():7} {issue.code:32} {issue.path}: {issue.message}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate a rights-ontology licence profile and assemble draft instruments.")
    parser.add_argument("--schema", type=Path, help="JSON Schema path. Defaults to schemas/license-profile.schema.json beside the project.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_command = subparsers.add_parser("validate", help="Validate without writing output artifacts.")
    validate_command.add_argument("profile", type=Path)
    validate_command.add_argument("--json", action="store_true", help="Print machine-readable validation result.")

    generate_command = subparsers.add_parser("generate", help="Validate and generate into a new or empty directory.")
    generate_command.add_argument("profile", type=Path)
    generate_command.add_argument("--out", type=Path, required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    project_root = Path(__file__).resolve().parents[1]
    schema_path = args.schema or project_root / "schemas" / "license-profile.schema.json"
    try:
        schema = load_json(schema_path)
        profile = load_json(args.profile)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Input error: {exc}", file=sys.stderr)
        return 2

    result = validate_profile(profile, schema)
    if args.command == "validate":
        _print_result(result, args.json)
        return 0 if result.valid else 1

    _print_result(result, False)
    if not result.valid:
        return 1
    try:
        manifest = generate(profile, schema, args.out)
    except (OSError, ValueError) as exc:
        print(f"Generation error: {exc}", file=sys.stderr)
        return 2
    print(f"Generated {len(manifest['artifacts']) + 1} artifacts in {args.out.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
