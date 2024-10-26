# patient_check_expenses.py
expenses = {
    "patient_123": [
        {"date": "2024-10-20", "description": "Room Charge", "amount": 100},
        {"date": "2024-10-21", "description": "Medication", "amount": 50}
    ],
    "patient_456": [
        {"date": "2024-10-20", "description": "Consultation Fee", "amount": 200}
    ]
}

def view_expenses(patient_id):
    patient_expenses = expenses.get(patient_id, [])
    if patient_expenses:
        print(f"Expenses for Patient {patient_id}:")
        for expense in patient_expenses:
            print(f"{expense['date']}: {expense['description']} - ${expense['amount']}")
    else:
        print("No expenses available.")

if __name__ == "__main__":
    patient_id = input("Enter your Patient ID: ")
    view_expenses(patient_id)
