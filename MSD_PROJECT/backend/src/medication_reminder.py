from datetime import datetime

TODAY = datetime(2024, 10, 26).strftime("%Y-%m-%d")

reminders = {
    "patient_123": {"medication": "2024-10-28", "test": "2024-10-30"},
    "patient_456": {"medication": "2024-10-29", "test": "2024-11-01"}
}

def check_reminders(patient_id, today=TODAY):
    reminder = reminders.get(patient_id)
    if not reminder:
        print("No reminders available for this patient.")
        return
    
    medication_due = reminder["medication"] == today
    test_due = reminder["test"] == today
    
    if medication_due:
        print(f"Reminder: Medication for Patient {patient_id} is scheduled for today.")
    
    if test_due:
        print(f"Reminder: Test for Patient {patient_id} is scheduled for today.")
    
    if not (medication_due or test_due):
        print(f"No reminders due today for Patient {patient_id}.")

if __name__ == "__main__":
    patient_id = input("Enter Patient ID: ")
    check_reminders(patient_id)
