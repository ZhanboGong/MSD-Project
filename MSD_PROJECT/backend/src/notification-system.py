# notification_system.py
notifications = {}

def add_notification(patient_id, message):
    notifications[patient_id] = message
    print(f"Notification added for Patient {patient_id}.")

def view_notification(patient_id):
    message = notifications.get(patient_id, "No new notifications.")
    print(f"Patient {patient_id} Notification: {message}")

if __name__ == "__main__":
    patient_id = input("Enter Patient ID: ")
    action = input("Enter 'add' to send a notification or 'view' to see notifications: ").strip().lower()
    if action == "add":
        message = input("Enter notification message: ")
        add_notification(patient_id, message)
    elif action == "view":
        view_notification(patient_id)
