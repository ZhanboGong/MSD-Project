# patient_view_modify_appointments.py
appointments = {"John Doe": {"department": "Cardiology", "doctor": "Dr. Smith", "time": "2024-10-30 09:00"}}

def view_appointments(patient_name):
    if patient_name in appointments:
        print(f"Appointment for {patient_name}: {appointments[patient_name]}")
    else:
        print("No appointment found.")

def modify_appointment(patient_name):
    if patient_name in appointments:
        new_time = input("Enter new time (YYYY-MM-DD HH:MM): ")
        appointments[patient_name]["time"] = new_time
        print(f"Appointment updated for {patient_name}.")
    else:
        print("No appointment found.")

if __name__ == "__main__":
    name = input("Enter your name: ")
    action = input("View or Modify appointment? (view/modify): ").strip().lower()
    if action == "view":
        view_appointments(name)
    elif action == "modify":
        modify_appointment(name)
