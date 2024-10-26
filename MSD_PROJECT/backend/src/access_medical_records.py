# access_medical_records.py
medical_records = {}

def create_record(patient_id, data):
    medical_records[patient_id] = data
    print(f"Medical record created for Patient {patient_id}.")

def view_record(patient_id):
    record = medical_records.get(patient_id)
    if record:
        print(f"Patient {patient_id} Record: {record}")
    else:
        print("No record found for the given patient ID.")

if __name__ == "__main__":
    patient_id = input("Enter Patient ID: ")
    action = input("Enter 'create' to add a record or 'view' to access: ").strip().lower()
    if action == "create":
        data = input("Enter patient medical data: ")
        create_record(patient_id, data)
    elif action == "view":
        view_record(patient_id)
