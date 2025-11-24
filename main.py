import csv
import json
import os


DATA_FILE = 'student_data.csv'
STUDENTS = []



def get_input_validated(prompt, validator, error_msg):
    """Reusable function to handle user input and validation loops."""
    while True:
        try:
            value = validator(input(prompt))
            return value
        except ValueError:
            print(error_msg)
        except Exception as e:
            
            print(e)

def find_student(student_id):
    """Finds a student by ID or returns None."""
    return next((s for s in STUDENTS if s['id'] == student_id), None)

def get_attendance_pct(student):
    """Calculates attendance percentage, handling division by zero."""
    a = student['attendance']
    return (a['attended'] / a['total'] * 100) if a['total'] else 0.0

#Dataaaaa

def load_data():
    """Loads student data, deserializing grades/attendance from JSON."""
    global STUDENTS
    STUDENTS = []
    if not os.path.exists(DATA_FILE):
        print("No data file found. Starting empty.")
        return

    try:
        with open(DATA_FILE, 'r', newline='') as f:
            reader = csv.DictReader(f)
            
            STUDENTS = [
                {
                    **row,
                    'grades': json.loads(row['grades']),
                    'attendance': json.loads(row['attendance'])
                }
                for row in reader
            ]
    except Exception as e:
        print(f"Error loading data: {e}. Starting empty.")

def save_data():
    """Saves the current STUDENTS list, serializing grades/attendance to JSON."""
    if not STUDENTS: return 

    try:
        with open(DATA_FILE, 'w', newline='') as f:
            headers = ['id', 'name', 'grades', 'attendance']
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()

            
            writer.writerows([
                {
                    **s,
                    'grades': json.dumps(s['grades']),
                    'attendance': json.dumps(s['attendance'])
                }
                for s in STUDENTS
            ])
        print("Data saved successfully.")
    except IOError as e:
        print(f"Error saving data: {e}")

#  core featuressss

def add_student():
    """Adds a new student after validating ID uniqueness."""
    student_id = input("Enter new student ID: ")
    if find_student(student_id):
        print("Error: ID already exists.")
        return

    STUDENTS.append({
        'id': student_id,
        'name': input("Enter new student name: "),
        'grades': {},
        'attendance': {'attended': 0, 'total': 0}
    })
    print(f"Student added successfully.")
    save_data()

def update_grade():
    """Updates a student's grade with input validation."""
    student = find_student(input("Enter student ID to update grade: "))
    if not student:
        print("Student ID not found.")
        return

    assignment = input("Enter assignment name: ")
    
    # reusable validation of scoree
    score = get_input_validated(
        "Enter score (0-100): ",
        lambda x: (float(x), (x for x in []).throw(Exception("Score must be between 0 and 100.")) if not (0 <= float(x) <= 100) else float(x))[0],
        "Invalid input. Please enter a number for the score."
    )
    
    # Reusable validation of weightt
    weight = get_input_validated(
        "Enter weight (0-1): ",
        lambda x: (float(x), (x for x in []).throw(Exception("Weight must be between 0 and 1.")) if not (0 <= float(x) <= 1) else float(x))[0],
        "Invalid input. Please enter a number for the weight."
    )

    student['grades'][assignment] = {'score': score, 'weight': weight}
    print(f"Grade for {student['name']} updated.")
    save_data()

def update_attendance():
    """Updates a student's attendance with input validation."""
    student = find_student(input("Enter student ID to update attendance: "))
    if not student:
        print("Student ID not found.")
        return

    current = student['attendance']['attended']
    attended = get_input_validated(
        f"Enter new attended classes (current: {current}): ",
        lambda x: (int(x), (x for x in []).throw(Exception("Attended classes cannot be negative.")) if int(x) < 0 else int(x))[0],
        "Invalid input. Please enter a whole number."
    )

    total = get_input_validated(
        f"Enter new total classes (current: {student['attendance']['total']}): ",
        lambda x: (int(x), (x for x in []).throw(Exception("Total classes cannot be less than attended.")) if int(x) < attended else int(x))[0],
        "Invalid input. Please enter a whole number."
    )

    student['attendance'].update({'attended': attended, 'total': total})
    print(f"Attendance for {student['name']} updated.")
    save_data()

def calculate_gpa(student):
    """Calculates the weighted GPA (0-100) for a student."""
    grades = student['grades'].values()
    if not grades:
        return 0.0

    total_weighted_score = sum(g['score'] * g['weight'] for g in grades)
    total_weight = sum(g['weight'] for g in grades)

    return total_weighted_score / total_weight if total_weight else 0.0

def display_report():
    """Displays a formatted table of all students with GPA and attendance."""
    if not STUDENTS:
        print("No student data to display.")
        return

    print("\n--- Full Student Report ---")
    header = f"{'ID':<10} | {'Name':<20} | {'Weighted GPA (%)':<20} | {'Attendance (%)':<20}"
    print(header)
    print("-" * len(header))

    for s in sorted(STUDENTS, key=lambda s: s['id']):
        gpa = calculate_gpa(s)
        attendance_pct = get_attendance_pct(s)
        print(f"{s['id']:<10} | {s['name']:<20} | {gpa:<20.2f} | {attendance_pct:<20.2f}")
    print("-" * len(header))

def flag_at_risk_students():
    """Filters and displays students whose attendance is below 75%."""
    at_risk = [
        s for s in STUDENTS 
        if get_attendance_pct(s) < 75
    ]

    print("\n--- At-Risk Students (Attendance < 75%) ---")
    header = f"{'ID':<10} | {'Name':<20} | {'Attendance (%)':<20}"
    print(header)
    print("-" * len(header))
    
    if at_risk:
        for s in sorted(at_risk, key=lambda s: s['id']):
            print(f"{s['id']:<10} | {s['name']:<20} | {get_attendance_pct(s):<20.2f}")
    else:
        print("No students are currently at-risk.")
    print("-" * len(header))

# main app loopsyyy

def main():
    """CLI application loop."""
    load_data()
    menu = {
        '1': add_student, '2': update_grade, '3': update_attendance,
        '4': display_report, '5': flag_at_risk_students
    }

    while True:
        print("\n--- Student Manager ---")
        for key, func in menu.items():
            print(f"{key}. {func.__name__.replace('_', ' ').title()}")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '6':
            print("Exiting program.")
            break
        
        action = menu.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()