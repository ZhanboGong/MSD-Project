# patient_check_ward.py
patient_ward_info = {
    "patient_123": "Ward A1",
    "patient_456": "Ward B2"
}

def check_ward(patient_id):
    ward = patient_ward_info.get(patient_id)
    if ward:
        print(f"You are in {ward}.")
    else:
        print("No ward information available.")

if __name__ == "__main__":
    patient_id = input("Enter your Patient ID: ")
    check_ward(patient_id)
