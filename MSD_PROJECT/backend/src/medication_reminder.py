# medication_reminder.py
from datetime import datetime, timedelta

reminders = {
    "patient_123": {"medication": "2024-10-28", "test": "2024-10-30"},
    "patient_456": {"medication": "2024-10-29", "test": "2024-11-01"}
}

def check_reminders(patient_id):
    today = datetime.now().strftime("%Y-%m-%d")
    reminder = reminders.get(patient_id)
    if reminder:
        if reminder["medication"] == today:
            print(f"Reminder: Medication for Patient {patient_id} is scheduled for today.")
        if reminder["test"] == today:
            print(f"Reminder: Test for Patient {patient_id} is scheduled for today.")
    else:
        print("No reminders available for this patient.")

if __name__ == "__main__":
    patient_id = input("Enter Patient ID: ")
    check_reminders(patient_id)
