import patient_view_records
from io import StringIO
import sys

def test_view_patient_record_existing_patient(capfd):
    # Test for an existing patient record
    patient_view_records.view_patient_record("patient_123")
    captured = capfd.readouterr()
    assert "Patient patient_123 Record: {'diagnosis': 'Flu', 'test_result': 'Negative'}" in captured.out

def test_view_patient_record_non_existing_patient(capfd):
    # Test for a non-existing patient record
    patient_view_records.view_patient_record("patient_999")
    captured = capfd.readouterr()
    assert "No record found for the given patient ID." in captured.out

def test_main_existing_patient(monkeypatch, capfd):
    # Simulate user input for existing patient ID
    monkeypatch.setattr('builtins.input', lambda: 'patient_123')
    patient_view_records.main()
    captured = capfd.readouterr()
    assert "Patient patient_123 Record: {'diagnosis': 'Flu', 'test_result': 'Negative'}" in captured.out

def test_main_non_existing_patient(monkeypatch, capfd):
    # Simulate user input for non-existing patient ID
    monkeypatch.setattr('builtins.input', lambda: 'patient_999')
    patient_view_records.main()
    captured = capfd.readouterr()
    assert "No record found for the given patient ID." in captured.out
