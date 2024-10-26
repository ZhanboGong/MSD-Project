import sys
import unittest
from io import StringIO

from patient_choose_department_doctor import show_doctors, doctors


class TestPatientChooseDepartmentDoctor(unittest.TestCase):

    def test_show_doctors_for_known_departments(self):
        # 测试已知科室的医生列表
        for department, expected_doctors in doctors.items():
            with self.subTest(department=department):
                captured_output = StringIO()
                with redirect_stdout(captured_output):
                    show_doctors(department)
                output = captured_output.getvalue().strip()
                self.assertIn(f"Doctors in {department}: {', '.join(expected_doctors)}", output)

    def test_show_doctors_for_unknown_department(self):
        # 测试未知科室的情况
        unknown_departments = ["Dermatology", "Pediatrics", "Ophthalmology"]
        for department in unknown_departments:
            with self.subTest(department=department):
                captured_output = StringIO()
                with redirect_stdout(captured_output):
                    show_doctors(department)
                output = captured_output.getvalue().strip()
                self.assertEqual(output, "")

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