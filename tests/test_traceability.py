import unittest
from deliveryguard.traceability import validate_requirements

class TraceabilityTests(unittest.TestCase):
    def test_valid_structure_has_no_findings(self):
        req = {"id":"FR-001","type":"functional","title":"Login","status":"approved",
               "source":{"kind":"customer_confirmed","reference":"REQ-1"},
               "acceptance_criteria":["Given a valid user, when they log in, then a session is created."],
               "code_refs":["src/auth.py"],"test_refs":["tests/test_auth.py"]}
        self.assertEqual(validate_requirements([req]), [])

    def test_missing_acceptance_and_test_are_reported(self):
        req = {"id":"FR-002","type":"functional","title":"Export","status":"draft",
               "source":{"kind":"unknown","reference":"not recorded"}}
        findings = validate_requirements([req])
        rules = {f.rule_id for f in findings}
        self.assertIn("DG-TR-003", rules)
        self.assertIn("DG-TR-004", rules)
        self.assertIn("DG-TR-005", rules)
        self.assertIn("DG-GOV-001", rules)

    def test_duplicate_id_is_reported(self):
        req = {"id":"BR-001","type":"business_rule","title":"Rule","status":"draft","source":{"kind":"contract","reference":"C1"}}
        findings = validate_requirements([req, req])
        self.assertTrue(any(f.rule_id == "DG-TR-006" for f in findings))

    def test_bad_id_is_reported(self):
        req = {"id":"LOGIN","type":"functional","title":"Login","status":"draft","source":{"kind":"unknown","reference":"?"}}
        self.assertTrue(any(f.rule_id == "DG-TR-001" for f in validate_requirements([req])))

if __name__ == "__main__":
    unittest.main()
