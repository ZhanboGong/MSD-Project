# patient_choose_visit_time.py
from datetime import datetime, timedelta

available_slots = [(datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d %H:%M") for i in range(1, 6)]

def choose_time():
    print("Available Time Slots:")
    for i, slot in enumerate(available_slots):
        print(f"{i + 1}. {slot}")
    choice = int(input("Select a slot (1-5): ")) - 1
    print(f"You have chosen: {available_slots[choice]}")

if __name__ == "__main__":
    choose_time()
