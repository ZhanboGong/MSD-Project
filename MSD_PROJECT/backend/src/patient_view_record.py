# patient_view_records.py
medical_records = {
    "patient_123": {"diagnosis": "Flu", "test_result": "Negative"}
}

def view_patient_record(patient_id):
    record = medical_records.get(patient_id)
    if record:
        print(f"Patient {patient_id} Record: {record}")
    else:
        print("No record found for the given patient ID.")

if __name__ == "__main__":
    patient_id = input("Enter your Patient ID: ")
    view_patient_record(patient_id)
