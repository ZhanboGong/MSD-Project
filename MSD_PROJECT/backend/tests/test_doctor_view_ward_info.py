import doctor_view_ward_info
from io import StringIO
import sys

def test_view_ward_info_existing_patient(capfd):
    # Test for an existing patient (patient_123)
    doctor_view_ward_info.view_ward_info("patient_123")
    captured = capfd.readouterr()
    assert "Patient patient_123 is in Ward A1, Bed 12." in captured.out

def test_view_ward_info_non_existing_patient(capfd):
    # Test for a non-existing patient (patient_999)
    doctor_view_ward_info.view_ward_info("patient_999")
    captured = capfd.readouterr()
    assert "No information available for this patient." in captured.out

def test_main_existing_patient(monkeypatch, capfd):
    # Test the main input flow with existing patient ID
    monkeypatch.setattr('builtins.input', lambda: 'patient_456')
    doctor_view_ward_info.main()
    captured = capfd.readouterr()
    assert "Patient patient_456 is in Ward B2, Bed 8." in captured.out

def test_main_non_existing_patient(monkeypatch, capfd):
    # Test the main input flow with non-existing patient ID
    monkeypatch.setattr('builtins.input', lambda: 'patient_999')
    doctor_view_ward_info.main()
    captured = capfd.readouterr()
    assert "No information available for this patient." in captured.out
