import update_diagnoses
from io import StringIO
import sys


def test_update_diagnosis():
    # Test updating the diagnosis for a patient
    update_diagnoses.update_diagnosis("patient_789", "Flu", "Rest and hydration")

    # Verify that the medical record was updated correctly
    assert update_diagnoses.medical_records["patient_789"] == {
        "diagnosis": "Flu",
        "treatment": "Rest and hydration"
    }


def test_main(monkeypatch, capfd):
    # Simulate user input for patient_id, diagnosis, and treatment
    inputs = iter(["patient_123", "Cold", "Rest and fluids"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Run the main function to verify the input handling
    update_diagnoses.main()

    # Verify the printed output
    captured = capfd.readouterr()
    assert "Updated record for Patient patient_123." in captured.out

    # Verify that the medical record was updated correctly
    assert update_diagnoses.medical_records["patient_123"] == {
        "diagnosis": "Cold",
        "treatment": "Rest and fluids"
    }
