# medication_reminder.py
from datetime import datetime, timedelta

reminders = {
    "patient_123": {"medication": "2024-10-28", "test": "2024-10-30"},
    "patient_456": {"medication": "2024-10-29", "test": "2024-11-01"}
}

def check_reminders(patient_id):
    today = datetime.now().strftime("%Y-%m-%d")
    reminder = reminders.get(patient_id)

