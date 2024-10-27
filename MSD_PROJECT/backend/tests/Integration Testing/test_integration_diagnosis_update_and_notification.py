
import update_diagnoses
import notification_system

def test_integration_diagnosis_update_and_notification():

    patient_id = "patient_002"
    new_diagnosis = "Cold"
    notification_message = "Your diagnosis has been updated."
    
    update_diagnoses.update_diagnosis(patient_id, new_diagnosis)
    
    notification_system.add_notification(patient_id, notification_message)
    
    notification = notification_system.notifications.get(patient_id)
    
    assert notification == notification_message, "通知未正确发送。"

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "test_integration_diagnosis_update_and_notification.py"])
