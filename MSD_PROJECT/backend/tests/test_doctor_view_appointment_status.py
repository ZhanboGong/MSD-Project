import doctor_view_appointment_status

def test_view_appointment_status(capsys):

    doctor_view_appointment_status.view_appointment_status()
    captured = capsys.readouterr()


    assert "Patient: John Doe, Department: Cardiology, Time: 2024-10-30 09:00, Status: Confirmed" in captured.out
    assert "Patient: Jane Smith, Department: Neurology, Time: 2024-10-31 10:00, Status: Pending" in captured.out

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "test_doctor_view_appointment_status.py"])
