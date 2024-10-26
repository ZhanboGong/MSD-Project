# update_diagnoses.py
medical_records = {}

def update_diagnosis(patient_id, diagnosis, treatment):
    medical_records[patient_id] = {
        "diagnosis": diagnosis,
        "treatment": treatment
    }
    print(f"Updated record for Patient {patient_id}.")

if __name__ == "__main__":
    patient_id = input("Enter Patient ID: ")
    diagnosis = input("Enter diagnosis: ")
    treatment = input("Enter treatment plan: ")
    update_diagnosis(patient_id, diagnosis, treatment)
