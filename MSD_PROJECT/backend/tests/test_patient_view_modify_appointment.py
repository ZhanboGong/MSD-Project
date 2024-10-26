import patient_view_modify_appointments
from io import StringIO
import sys


def test_view_appointments_existing_patient(capfd):
    # Test viewing an appointment for an existing patient
    patient_view_modify_appointments.view_appointments("John Doe")
    captured = capfd.readouterr()
    assert "Appointment for John Doe: {'department': 'Cardiology', 'doctor': 'Dr. Smith', 'time': '2024-10-30 09:00'}" in captured.out


def test_view_appointments_non_existing_patient(capfd):
    # Test viewing an appointment for a non-existing patient
    patient_view_modify_appointments.view_appointments("Jane Doe")
    captured = capfd.readouterr()
    assert "No appointment found." in captured.out


def test_modify_appointment_existing_patient(monkeypatch, capfd):
    # Simulate modifying an existing appointment
    inputs = iter(["2024-11-01 10:00"])  # New time input
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    patient_view_modify_appointments.modify_appointment("John Doe")

    # Capture the output
    captured = capfd.readouterr()
    assert "Appointment updated for John Doe." in captured.out

    # Verify the updated appointment time
    assert patient_view_modify_appointments.appointments["John Doe"]["time"] == "2024-11-01 10:00"


def test_modify_appointment_non_existing_patient(monkeypatch, capfd):
    # Test modifying an appointment for a non-existing patient
    inputs = iter(["2024-11-01 10:00"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    patient_view_modify_appointments.modify_appointment("Jane Doe")
    captured = capfd.readouterr()
    assert "No appointment found." in captured.out


def test_main_view_existing_patient(monkeypatch, capfd):
    # Simulate user input to view an existing appointment
    inputs = iter(["John Doe", "view"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    patient_view_modify_appointments.main()
    captured = capfd.readouterr()
    assert "Appointment for John Doe: {'department': 'Cardiology', 'doctor': 'Dr. Smith', 'time': '2024-10-30 09:00'}" in captured.out


def test_main_modify_existing_patient(monkeypatch, capfd):
    # Simulate user input to modify an existing appointment
    inputs = iter(["John Doe", "modify", "2024-11-01 10:00"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    patient_view_modify_appointments.main()
    captured = capfd.readouterr()
    assert "Appointment updated for John Doe." in captured.out
    assert patient_view_modify_appointments.appointments["John Doe"]["time"] == "2024-11-01 10:00"


def test_main_non_existing_patient(monkeypatch, capfd):
    # Simulate user input for a non-existing patient
    inputs = iter(["Jane Doe", "view"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    patient_view_modify_appointments.main()
    captured = capfd.readouterr()
    assert "No appointment found." in captured.out
