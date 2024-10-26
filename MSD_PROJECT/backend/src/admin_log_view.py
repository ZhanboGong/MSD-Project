
log = [
    {"user": "staff1", "action": "login", "status": "success"},
    {"user": "user123", "action": "reset password", "status": "failed"}
]

def view_logs():
    print("User Logs:")
    for entry in log:
        print(f"User: {entry['user']}, Action: {entry['action']}, Status: {entry['status']}")

if __name__ == "__main__":
    view_logs()
