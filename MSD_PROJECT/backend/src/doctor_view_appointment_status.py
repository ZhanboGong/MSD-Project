# doctor_view_appointment_status.py
appointments = [
    {"patient": "John Doe", "department": "Cardiology", "time": "2024-10-30 09:00", "status": "Confirmed"},
    {"patient": "Jane Smith", "department": "Neurology", "time": "2024-10-31 10:00", "status": "Pending"}
]

def view_appointment_status():
    print("Appointment Status:")
    for appointment in appointments:
        print(f"Patient: {appointment['patient']}, Department: {appointment['department']}, "
              f"Time: {appointment['time']}, Status: {appointment['status']}")

if __name__ == "__main__":
    view_appointment_status()
