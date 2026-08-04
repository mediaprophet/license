from __future__ import annotations

import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from src.license_generator import OUTPUT_NAMES, generate, load_json, validate_profile


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = load_json(ROOT / "schemas" / "license-profile.schema.json")


class GeneratorValidationTests(unittest.TestCase):
    def load_profile(self, name: str = "public-inspection-profile.json") -> dict:
        return load_json(ROOT / "examples" / name)

    def test_example_profiles_pass(self) -> None:
        for name in ("public-inspection-profile.json", "controlled-deployment-profile.json"):
            with self.subTest(name=name):
                result = validate_profile(self.load_profile(name), SCHEMA)
                self.assertTrue(result.valid, [issue.as_dict() for issue in result.errors])

    def test_schema_rejects_unknown_property(self) -> None:
        profile = self.load_profile()
        profile["unexpected"] = True
        result = validate_profile(profile, SCHEMA)
        self.assertTrue(any(issue.code == "schema.additional" for issue in result.errors))

    def test_unknown_agent_reference_is_rejected(self) -> None:
        profile = self.load_profile()
        profile["rights_relations"][0]["holder"] = "missing-agent"
        result = validate_profile(profile, SCHEMA)
        self.assertTrue(any(issue.code == "semantic.agent_ref" for issue in result.errors))

    def test_public_notice_cannot_create_contractual_money(self) -> None:
        profile = self.load_profile()
        profile["formation"]["mode"] = "public-notice-only"
        remedy = copy.deepcopy(profile["enforcement"]["financial_remedies"][-1])
        remedy["id"] = "invalid-public-charge"
        remedy["formation_stage"] = "pre_event_contract"
        remedy["becomes_payable_when"] = "Public notice is viewed"
        profile["enforcement"]["financial_remedies"] = [remedy]
        result = validate_profile(profile, SCHEMA)
        self.assertTrue(any(issue.code == "semantic.nonassenter_debt" for issue in result.errors))

    def test_public_notice_preserves_later_voluntary_settlement(self) -> None:
        profile = self.load_profile()
        profile["formation"]["mode"] = "public-notice-only"
        settlement = copy.deepcopy(profile["enforcement"]["financial_remedies"][-1])
        self.assertEqual(settlement["formation_stage"], "post_event_agreement")
        profile["enforcement"]["financial_remedies"] = [settlement]
        result = validate_profile(profile, SCHEMA)
        self.assertFalse(any(issue.code in {"semantic.nonassenter_debt", "semantic.remedy_assent"} for issue in result.errors))

    def test_creator_autonomy_safeguards_are_mandatory(self) -> None:
        profile = self.load_profile()
        profile["creator_protection"]["may_refuse_or_condition_licence"] = False
        result = validate_profile(profile, SCHEMA)
        self.assertTrue(any(issue.code == "semantic.creator_safeguard" for issue in result.errors))

    def test_creator_investment_requires_creator_contributor(self) -> None:
        profile = self.load_profile()
        profile["creator_protection"]["investments"][0]["contributor"] = "eligible-inspector"
        result = validate_profile(profile, SCHEMA)
        self.assertTrue(any(issue.code == "semantic.investment_creator" for issue in result.errors))

    def test_creator_held_relation_over_work_is_required(self) -> None:
        profile = self.load_profile()
        profile["rights_relations"] = [profile["rights_relations"][0]]
        result = validate_profile(profile, SCHEMA)
        self.assertTrue(any(issue.code == "semantic.creator_relation" for issue in result.errors))

    def test_ai_use_boundary_is_required(self) -> None:
        profile = self.load_profile()
        profile["grant"]["prohibited_actions"] = ["commercial operation", "redistribution"]
        result = validate_profile(profile, SCHEMA)
        self.assertTrue(any(issue.code == "semantic.ai_boundary" for issue in result.errors))

    def test_creator_recovery_has_leading_priority(self) -> None:
        profile = self.load_profile()
        profile["enforcement"]["recovery_waterfall"] = ["Lawyer fees", "Funder return", "Project treasury", "Creator last"]
        result = validate_profile(profile, SCHEMA)
        self.assertTrue(any(issue.code == "semantic.creator_recovery_priority" for issue in result.errors))

    def test_deterrent_character_is_reviewed_not_blanket_rejected(self) -> None:
        profile = self.load_profile()
        remedy = profile["enforcement"]["financial_remedies"][2]
        remedy["trigger"] += " This pathway is punitive and deterrent where the governing statute permits."
        self.assertEqual(remedy["remedy_character"], "deterrent")
        result = validate_profile(profile, SCHEMA)
        self.assertFalse(any(issue.code == "semantic.punitive_money" for issue in result.errors))
        self.assertTrue(result.valid, [issue.as_dict() for issue in result.errors])

    def test_enabled_funding_preserves_creator_control(self) -> None:
        profile = self.load_profile()
        profile["enforcement"]["enforcement_funding"]["creator_control_preserved"] = False
        result = validate_profile(profile, SCHEMA)
        self.assertTrue(any(issue.code == "semantic.funding_safeguard" for issue in result.errors))

    def test_automated_adjudication_is_rejected(self) -> None:
        profile = self.load_profile()
        profile["technical_instruments"][0]["automated_adjudication"] = True
        result = validate_profile(profile, SCHEMA)
        self.assertTrue(any(issue.code == "semantic.automated_adjudication" for issue in result.errors))

    def test_technical_capability_is_not_normative_authority(self) -> None:
        profile = self.load_profile()
        profile["rights_relations"][0]["authority_sources"] = ["capability-token", "ledger-record"]
        result = validate_profile(profile, SCHEMA)
        self.assertTrue(any(issue.code == "semantic.capability_not_authority" for issue in result.errors))

    def test_public_notice_cannot_give_token_contractual_effect(self) -> None:
        profile = self.load_profile()
        profile["formation"]["mode"] = "public-notice-only"
        profile["technical_instruments"][0]["legal_effect"] = "contractually_recognised"
        result = validate_profile(profile, SCHEMA)
        self.assertTrue(any(issue.code == "semantic.technical_contract" for issue in result.errors))

    def test_sensitive_immutable_ledger_is_rejected(self) -> None:
        profile = self.load_profile()
        profile["ledger"]["stores_sensitive_data"] = True
        result = validate_profile(profile, SCHEMA)
        self.assertTrue(any(issue.code == "semantic.ledger_sensitive" for issue in result.errors))

    def test_orphan_artificial_agent_is_rejected(self) -> None:
        profile = self.load_profile("controlled-deployment-profile.json")
        artificial = next(agent for agent in profile["agents"] if agent["agent_type"] == "artificial_agent")
        artificial["principal"] = None
        result = validate_profile(profile, SCHEMA)
        self.assertTrue(any(issue.code == "semantic.orphan_agent" for issue in result.errors))

    def test_adoption_requires_legal_approval_record(self) -> None:
        profile = self.load_profile()
        profile["profile"]["status"] = "adopted"
        result = validate_profile(profile, SCHEMA)
        self.assertTrue(any(issue.code == "semantic.legal_approval" for issue in result.errors))

    def test_generation_writes_complete_hashed_bundle(self) -> None:
        profile = self.load_profile()
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "generated"
            manifest = generate(profile, SCHEMA, output)
            self.assertEqual(set(path.name for path in output.iterdir()), set(OUTPUT_NAMES))
            for artifact in manifest["artifacts"]:
                path = output / artifact["name"]
                digest = hashlib.sha256(path.read_bytes()).hexdigest()
                self.assertEqual(digest, artifact["sha256"])
            receipt = json.loads((output / "ACCEPTANCE-RECEIPT-TEMPLATE.json").read_text(encoding="utf-8"))
            self.assertEqual(receipt["status"], "template-not-accepted")
            policy = json.loads((output / "RIGHTS-POLICY.jsonld").read_text(encoding="utf-8"))
            self.assertGreater(len(policy["@graph"]), 0)
            self.assertTrue(any("hro:CreatorInvestment" == node.get("type") for node in policy["@graph"]))
            creator_schedule = (output / "CREATOR-INTERESTS-AND-INVESTMENT-SCHEDULE.md").read_text(encoding="utf-8")
            self.assertIn("The creator is not required to donate labour", creator_schedule)

    def test_generation_refuses_nonempty_directory(self) -> None:
        profile = self.load_profile()
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir)
            (output / "existing.txt").write_text("user content", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                generate(copy.deepcopy(profile), SCHEMA, output)


if __name__ == "__main__":
    unittest.main()
