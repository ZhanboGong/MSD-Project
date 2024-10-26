import sys
import unittest
from io import StringIO
from patient_check_ward import check_ward, patient_ward_info

class TestPatientCheckWard(unittest.TestCase):

    def test_known_patient_id(self):
        # 测试已知的患者ID
        for patient_id, expected_ward in patient_ward_info.items():
            with self.subTest(patient_id=patient_id):
                captured_output = StringIO()
                with redirect_stdout(captured_output):
                    check_ward(patient_id)
                output = captured_output.getvalue().strip()
                self.assertIn(f"You are in {expected_ward}.", output)

    def test_unknown_patient_id(self):
        # 测试未知的患者ID
        unknown_patient_ids = ["unknown_patient", "patient_999", "patient_789"]
        for patient_id in unknown_patient_ids:
            with self.subTest(patient_id=patient_id):
                captured_output = StringIO()
                with redirect_stdout(captured_output):
                    check_ward(patient_id)
                output = captured_output.getvalue().strip()
                self.assertIn("No ward information available.", output)

# 用于上下文管理器的重定向stdout
try:
    from unittest.mock import redirect_stdout
except ImportError:
    import contextlib

    @contextlib.contextmanager
    def redirect_stdout(target):
        original = sys.stdout
        sys.stdout = target
        yield
        sys.stdout = original

if __name__ == '__main__':
    unittest.main()