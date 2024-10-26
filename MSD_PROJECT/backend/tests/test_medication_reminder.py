import unittest
from io import StringIO
from unittest.mock import patch
import medication_reminder

class TestMedicationReminder(unittest.TestCase):

    def setUp(self):
        self.today = medication_reminder.TODAY
        self.reminders = medication_reminder.reminders

    def test_no_reminders(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            medication_reminder.check_reminders("nonexistent_patient", today=self.today)
        self.assertIn("No reminders available for this patient.", fake_out.getvalue().strip())

    def test_medication_reminder_today(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            medication_reminder.check_reminders("patient_123", today="2024-10-28")
        self.assertIn("Reminder: Medication for Patient patient_123 is scheduled for today.", fake_out.getvalue().strip())
        self.assertIn("No reminders due today for Patient patient_123", fake_out.getvalue().strip())

    def test_test_reminder_today(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            medication_reminder.check_reminders("patient_123", today="2024-10-30")
        self.assertIn("Reminder: Test for Patient patient_123 is scheduled for today.", fake_out.getvalue().strip())
        self.assertIn("No reminders due today for Patient patient_123", fake_out.getvalue().strip())

    def test_both_reminders_today(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            medication_reminder.check_reminders("patient_456", today="2024-10-29")
        self.assertIn("Reminder: Medication for Patient patient_456 is scheduled for today.", fake_out.getvalue().strip())
        self.assertIn("Reminder: Test for Patient patient_456 is scheduled for today.", fake_out.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
