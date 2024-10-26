# patient_account_creation.py
patients = {}

def create_account(medical_record_number, patient_id):
    username = f"user_{medical_record_number}_{patient_id}"
    patients[username] = "default_password"
    print(f"Account created! Username: {username}")

if __name__ == "__main__":
    record_number = input("Enter medical record number: ")
    patient_id = input("Enter patient ID: ")
    create_account(record_number, patient_id)

