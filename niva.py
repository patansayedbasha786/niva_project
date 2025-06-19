
import time

def sci_fi_print(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
    time.sleep(delay)
    print()

print("========== USER DATABASE ==========")

# ========== USER DATA ==========
users = {
    "12345": {
        "password": "123",
        "name": "sayed",
        "address": "Madanapalle",
        "college": "Sree Vidyanikethan College",
        "age": 19,
        "email": "sayed@niva.edu.in",
        "cgpa": 8.7,
        "attendance": "95%",
        "ai_rank": "Top 10%",
        "goal": "Build Smart IoT System",
        "fee_report": {
            "total": 30000,
            "reimbursement": 24000,
            "building_fee": 6000
        },
        "achievements": [
            "Secured 1st Place in IoT Hackathon",
            "Completed 3-month AI Internship",
            "Presented paper at State TechFest"
        ],
        "marks": {
            "Semester 1": [("Python Programming", 89), ("Mathematics", 82), ("Digital Logic", 85)],
            "Semester 2": [("C Programming", 91), ("Data Structures", 87), ("Web Tech", 88)],
            "Semester 3": [("OOP with Java", 85), ("DBMS", 89), ("Computer Networks", 90)],
            "Semester 4": [("Operating Systems", 92), ("Software Engineering", 86), ("AI Basics", 91)],
            "Semester 5": [("Cloud Computing", 88), ("Cyber Security", 90), ("ML Models", 93)]
        }
    },
    "1234": {
        "password": "123",
        "name": "hussen",
        "address": "TechCity, India",
        "college": "Sree Vidyanikethan College",
        "age": 19,
        "email": "hussen.tech@protonmail.com",
        "cgpa": 9.7,
        "attendance": "98%",
        "ai_rank": "Top 1%",
        "goal": "Invent a Sentient AI Kernel",
        "fee_report": {
            "total": 31000,
            "reimbursement": 25000,
            "building_fee": 7000
        },
        "achievements": [
            "Won National OS Kernel Design Hackathon",
            "Top 1% in AI Challenge 2024 – IIT TechFest",
            "Led 6-member team in building real-time Sentient Core"
        ],
        "marks": {
            "semester 1": [("Python Programming", 95), ("Mathematics", 90), ("Digital Logic", 93)],
            "semester 2": [("C Programming", 94), ("Data Structures", 96), ("Web Tech", 92)],
            "semester 3": [("OOP with Java", 97), ("DBMS", 95), ("Computer Networks", 98)],
            "semester 4": [("Operating Systems", 96), ("Software Engineering", 94), ("AI Basics", 97)],
            "semester 5": [("Cloud Computing", 99), ("Cyber Security", 98), ("ML Models", 99)]
        }
    }
}

# ========== DISPLAY FUNCTIONS ==========

def display_profile(u):
    print("\n═════════ BASIC PROFILE ═════════")
    print(f" Name        : {u['name']}")
    print(f" Age         : {u['age']}")
    print(f" Email       : {u['email']}")
    print(f" Address     : {u['address']}")
    print(f" CGPA        : {u['cgpa']}")
    print(f" Attendance  : {u['attendance']}")
    print(f" AI Rank     : {u['ai_rank']}")
    print(f" Goal        : {u['goal']}")
    print("═════════════════════════════════")

def display_fee_report(u):
    fee = u['fee_report']
    print(f"\n═══════════  FEE REPORT – USER: {u['name'].upper()} ═════════════")
    print(f" Total Fee         : ₹{fee['total']}")
    print(f" Reimbursement     : ₹{fee['reimbursement']}")
    print(f" Building Fee      : ₹{fee['building_fee']}")
    print(f" Final Fee Status  :  Cleared")
    print("══════════════════════════════════════════════════════")

def display_achievements(u):
    print(f"\n═══════════  ACHIEVEMENTS – USER: {u['name'].upper()} ═════════════")
    for i, ach in enumerate(u['achievements'], 1):
        print(f" {i}. {ach}")
    print("══════════════════════════════════════════════════════")

def display_marks(u):
    print("\n MARKS REPORT")
    if "marks" not in u:
        print(" Marks data not available.")
        return
    semesters = u["marks"]
    print("Available Semesters:")
    for sem in semesters:
        print(f"• {sem}")
    sem_choice = input("Enter semester (e.g., Semester 1): ").strip()
    if sem_choice in semesters:
        print(f"\n═════════  {sem_choice.upper()} REPORT ═════════")
        total = 0
        for subject, mark in semesters[sem_choice]:
            if mark >= 90:
                grade = "A"
            elif mark >= 80:
                grade = "B"
            else:
                grade = "C"
            total += mark
            print(f" {subject:<20} - {mark} Marks - Grade: {grade}")
        sgpa = round(total / len(semesters[sem_choice]) / 10, 2)
        print(f" SGPA: {sgpa}")
        print("══════════════════════════════════════════")
    else:
        print(" Invalid semester.")

# ========== MAIN SYSTEM ==========

def run_niva():
    print("\n ACCESSING NIVA INTELLIGENCE SYSTEM...")
    uid = input(" Enter User ID: ").strip()
    if uid in users:
        pwd = input(" Enter Password: ").strip()
        if pwd == users[uid]['password']:
            u = users[uid]
            print(f"\n ACCESS GRANTED: Welcome to NIVA Terminal.")
            display_profile(u)
            while True:
                print("\n Enter a section to view more data (type exit to quit):")
                print(" 1.Marks Report | 2.Achievements | 3.Fee Report | 4. exit")
                choice = input("\n Your choice: ").strip().lower()

                if choice == '4':
                    print("\n Logging out... Goodbye!")
                    break
                elif choice == '2':
                    display_achievements(u)
                elif choice == '3':
                    display_fee_report(u)
                elif choice == '1':
                    display_marks(u)
                else:
                    print(" Invalid section or not yet implemented.")
        else:
            print(" Incorrect password.")
    else:
        print(" User not found.")

run_niva()