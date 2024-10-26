# patient_choose_department_doctor.py
departments = ["Cardiology", "Neurology", "Orthopedics"]
doctors = {"Cardiology": ["Dr. Smith", "Dr. Lee"],
           "Neurology": ["Dr. Brown", "Dr. Taylor"],
           "Orthopedics": ["Dr. Green", "Dr. Miller"]}

def show_doctors(department):
    if department in doctors:
        print(f"Doctors in {department}: {', '.join(doctors[department])}")

if __name__ == "__main__":
    print("Available Departments: ", ", ".join(departments))
    chosen_department = input("Choose a department: ")
    show_doctors(chosen_department)
