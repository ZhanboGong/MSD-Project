# password_reset.py
users = {"user123": "oldpassword"}

def reset_password(username):
    if username in users:
        new_password = input("Enter your new password: ")
        users[username] = new_password
        print(f"Password reset successful for {username}.")
    else:
        print("Username not found.")

if __name__ == "__main__":
    user = input("Enter your username: ")
    reset_password(user)
