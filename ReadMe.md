README.md

# ----------Project Title--------------
Academic Record & Attendance Tracking System

Name: Eshita Parihar

Registration Number: 25BAI10698

Course: B.Tech(Artificial Intellegence and Machine Learning)

Institution: VIT Bhopal

Supervisor: Dr. Vinesh Kumar

# ----------Key Contents--------------
Introduction

Features

Installation

Usage

Workflow & Flowchart

PseudoCode

# ----------Introduction--------------

This project is a Student Performance & Attendance Management System designed to efficiently store, update, and analyze student records. It allows the user to add students, record their grades, calculate weighted GPA, track attendance, and automatically identify students who are at academic risk due to low attendance.

In the realm of Computer Science, the project solves the problem of manual data handling, which is often time-consuming, error-prone, and difficult to organize. By using Python and structured data storage, the system provides a reliable and automated way to manage student information, making academic record-keeping faster, more accurate, and easier to maintain.

# ---------Features--------------

1. Add New Students
    Allows easy creation of new student records with unique IDs, names, and initial data fields.

2. Update Grades
    Lets the user enter assignment scores and their weights, and stores them securely.

3. Weighted GPA Calculation
    Automatically calculates each student’s GPA based on weighted grades for accurate performance assessment.

4. Attendance Management
    Enables updating of attended and total classes, and calculates attendance percentage.

5. Full Student Report
    Generates a neatly formatted table displaying each student's GPA and attendance percentage.

6. At-Risk Student Detection
    Automatically identifies students whose attendance is below 75% and flags them for attention.

7. CSV-Based Data Storage
    Saves all student information in a CSV file with JSON-encoded fields for grades and attendance, ensuring data persistence.

8. User-Friendly Menu Interface
    Offers a simple command-line menu for navigating all features easily.

Installation
Provide step-by-step instructions for setting up the project.


# ------------Installation-------------------

Follow the steps below to install and set up the Student Performance & Attendance Management System:

1. Install Python

Ensure that Python (version 3.x) is installed on your system.
You can download it from the official Python website.

2. Download the Project Files

Place the following files in a single folder:

project.py (your main Python script)

student_data.csv (optional; created automatically if not present)

3. Install Required Libraries

This project only uses built-in Python modules:

csv

json

os

No extra installation is required.

4. Run the Program

Open a terminal/command prompt, navigate to the project folder, and run:

python project.py

The program will start and automatically create the CSV file if it does not already exist
Enjoy the program!


# ----------Usage--------------

To run and use the Student Performance & Attendance Management System, follow these steps:

1. Running the Program

Make sure Python is installed on your computer.

Place the project file (.py) and the data file (student_data.csv, if it exists) in the same folder.

Open a terminal/command prompt and run:

python project.py


(No authentication or login is required.)

2. Main Menu Navigation

When the program starts, it loads existing data (if any) and displays the main menu:

1. Add Student
2. Update Grade
3. Update Attendance
4. Display Report
5. At-risk Students
6. Exit


You simply enter the number of the option you want to use.

3. Using Each Feature
a) Add Student

Enter a unique Student ID.

Enter the student’s name.

The system creates an empty record and saves it.
Expected Output:

Student added successfully.

b) Update Grade

Enter Student ID.

Enter the assignment name (e.g., “Math Test 1”).

Enter score (0–100).

Enter weight (0–1).
The updated grades are saved automatically.

c) Update Attendance

Enter Student ID.

Enter number of attended classes.

Enter total classes.
The updated attendance is saved.

d) Display Report

Shows a table like:

ID        Name                Weighted GPA (%)     Attendance (%)
101       Rahul Sharma        84.50                92.00
102       Priya Singh         78.25                68.00

e) At-Risk Students

Lists students whose attendance is below 75%.

Example:

ID        Name                Attendance (%)
102       Priya Singh         68.00

4. Exiting the Program

Choose option 6 to exit.
All data is automatically saved to the CSV file.




# ----------Workflow & Flowchart--------------
```text
+----------------------+
|        START         |
+----------+-----------+
           |
           v
+----------------------+
|     load_data()      |
|  - read CSV if exists|
+----------+-----------+
           |
           v
+----------------------+
|      MAIN MENU       |
| 1 Add Student        |
| 2 Update Grade       |
| 3 Update Attendance  |
| 4 Display Report     |
| 5 Flag At-Risk       |
| 6 Exit               |
+----------+-----------+
           |
           v
+----------------------+
|   USER CHOICE 1–6    |
+--+----+----+----+----+
   |    |    |    |    |
   v    v    v    v    v

+----------+   +-----------+   +------------+
| Add      |   | Update    |   | Update     |
| Student  |   | Grade     |   | Attendance |
+----------+   +-----------+   +------------+
   |             |               |
   v             v               v

   ADD:          GRADE:         ATTEND:
 - check ID     - find student - find student
 - create entry - validate     - validate
 - save_data()    score/weight   attended/total
                 - update dict  - update dict
                 - save_data()  - save_data()

   |             |               |
   +-------------+-------+-------+
                         |
                         v
+-------------------------------+
|          OTHER OPS           |
|  Display Report (GPA + %)    |
|  Flag At-Risk (<75%)         |
+---------------+---------------+
                |
                v
+-------------------------------+
|        RETURN TO MENU         |
+---------------+---------------+
                |
         If choice == 6
                |
                v
+-------------------------------+
|             EXIT              |
+-------------------------------+

```


# ---------PseudoCcode--------------
START

LOAD student data from CSV

REPEAT
    DISPLAY menu:
        1. Add Student
        2. Update Grade
        3. Update Attendance
        4. Display Report
        5. At-Risk Students
        6. Exit

    INPUT choice

    IF choice == 1 THEN
        INPUT student ID
        IF ID exists THEN show error
        ELSE
            INPUT name
            CREATE empty grades and attendance
            SAVE data
        ENDIF

    ELSE IF choice == 2 THEN
        INPUT student ID
        IF not found THEN show error
        ELSE
            INPUT assignment name
            INPUT score (0–100)
            INPUT weight (0–1)
            UPDATE grades
            SAVE data
        ENDIF

    ELSE IF choice == 3 THEN
        INPUT student ID
        IF not found THEN show error
        ELSE
            INPUT attended classes
            INPUT total classes
            UPDATE attendance
            SAVE data
        ENDIF

    ELSE IF choice == 4 THEN
        FOR each student
            CALCULATE GPA using weighted formula
            CALCULATE attendance %
            DISPLAY all in table
        END FOR

    ELSE IF choice == 5 THEN
        FOR each student
            IF attendance < 75% THEN
                DISPLAY as at-risk
            ENDIF
        END FOR

    ELSE IF choice == 6 THEN
        EXIT LOOP
    ELSE
        DISPLAY "Invalid option"
    ENDIF

UNTIL choice == 6

SAVE data
END