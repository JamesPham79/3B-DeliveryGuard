import unittest
from deliveryguard.drift import analyze_changed_paths

class DriftTests(unittest.TestCase):
    def test_api_contract_flags_docs_and_contract_tests(self):
        findings = analyze_changed_paths(["api/openapi.yaml"])
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].rule_id, "DG-DRIFT-API-001")
        self.assertEqual(findings[0].status, "UNKNOWN")

    def test_database_migration_flags_data_docs(self):
        findings = analyze_changed_paths(["db/migrations/001_add_user.sql"])
        self.assertTrue(any(f.rule_id == "DG-DRIFT-DB-001" for f in findings))

    def test_code_change_is_unknown_not_pass(self):
        findings = analyze_changed_paths(["src/auth/login.py"])
        self.assertTrue(any(f.status == "UNKNOWN" for f in findings))

    def test_documentation_change_does_not_flag_itself(self):
        self.assertEqual(analyze_changed_paths(["docs/architecture.md"]), [])

    def test_empty_input(self):
        self.assertEqual(analyze_changed_paths([]), [])

if __name__ == "__main__":
    unittest.main()
