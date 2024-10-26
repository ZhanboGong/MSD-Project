# hospital_staff_login.py
users = {"staff1@example.com": "password123", "doctor1": "securepass"}

def login(username, password):
    if username in users and users[username] == password:
        print(f"Welcome, {username}! You are successfully logged in.")
    else:
        print("Invalid username or password. Please try again.")

if __name__ == "__main__":
    user = input("Enter your email/username: ")
    passwd = input("Enter your password: ")
    login(user, passwd)
