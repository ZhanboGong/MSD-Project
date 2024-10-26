# doctor_view_ward_info.py
patient_ward_info = {
    "patient_123": {"ward": "A1", "bed": "12"},
    "patient_456": {"ward": "B2", "bed": "8"}
}

def view_ward_info(patient_id):
    info = patient_ward_info.get(patient_id)
    if info:
        print(f"Patient {patient_id} is in Ward {info['ward']}, Bed {info['bed']}.")
    else:
        print("No information available for this patient.")

if __name__ == "__main__":
    patient_id = input("Enter Patient ID: ")
    view_ward_info(patient_id)
