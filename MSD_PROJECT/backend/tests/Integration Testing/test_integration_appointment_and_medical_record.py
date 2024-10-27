import doctor_register_patient
import access_medical_records

def test_integration_appointment_and_medical_record():
    patient_id = "patient_001"
    department = "Cardiology"
    doctor = "Dr. Smith"
    diagnosis = "Needs follow-up"    
    doctor_register_patient.register_appointment(patient_id, department, doctor)    
    access_medical_records.create_record(patient_id, diagnosis)    
    record = access_medical_records.medical_records.get(patient_id)    
    assert record == diagnosis, "病历记录未正确创建。"

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "test_integration_appointment_and_medical_record.py"])
