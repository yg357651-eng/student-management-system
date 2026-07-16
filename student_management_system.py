#=========
#IMPORTS
#=========
import json
import csv
from datetime import datetime
#=============
#FILE HANDLING
#=============
admin_username = "admin"
admin_password =""

students = []

def save_data():

    with open("students.json", "w") as file:
           json.dump(students, file)
        
def load_data():

    global students

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

    except FileNotFoundError:
        students = []
        
#=======================
#STUDENT  MANAGEMENT  
#=======================

def add_student():

    student_id = generate_student_id()

    print("Generated Student ID:", student_id) 

    name = input("Enter Student Name: ")

    if name.strip() == "":
        print("Name cannot be empty")
        return
    
    if not name.replace(" ", "").isalpha():
        print("Error: Name must contain only letters")
        return
    
    course = input("Enter Course: ")

    if course.strip() == "":
        print("Course cannot be empty")
        return

    project = input("Enter Project Name: ")

    if project.strip() == "":
        print("Project Name cannot be empty")
        return
        
    admission_date = input("Enter Admission Date (DD-MM-YYYY): ")

    try:
        date_obj = datetime.strptime(admission_date, "%d-%m-%Y")

        if date_obj > datetime.now():
            print("Admission Date cannot be in the future")
            return

    except ValueError:
        print("Invalid Date Format. Use DD-MM-YYYY")
        return

    marks = input("Enter Marks: ")

    if not marks.isdigit():
        print("Marks must be numbers")
        return

    marks = int(marks)

    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100")
        return
    
    student = {
        "id": student_id,
        "name": name,
        "course": course,
        "project": project,
        "marks": marks,
       "attendance":0,
       "admission_date": admission_date
    }

    students.append(student)
    
    save_data()

    print("Student Added Successfully")
    
def view_students():

    if len(students) == 0:
        print("No Students Found")
        return

    for student in students:

        print("=" * 30)
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Course:", student["course"])
        print("Project:", student["project"])
        print("Marks:", student["marks"])
        print("Attendance:", student.get("attendance", 0), "%")
        print("Admission Date:", student.get("admission_date", "Not Available"))
        print("=" * 30)

def search_student():

    search_id = input("Enter Student ID: ")

    if search_id == "":
        print("Student ID cannot be empty")
        return

    if not search_id.isdigit():
        print("Student ID must contain only numbers")
        return

    search_id = int(search_id)

    for student in students:
        if student["id"] == search_id:
            print("Student Found")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Project:", student["project"])
            print("Admission Date:", student.get("admission_date", "Not Available"))

            return

    print("Student Not Found")

def update_student():

    update_id = input("Enter Student ID to Update: ")

    if update_id == "":
        print("Student ID cannot be empty")
        return

    if not update_id.isdigit():
        print("Student ID must contain only numbers")
        return

    update_id = int(update_id)

    for student in students:

        if student["id"] == update_id:

            student["name"] = input("Enter New Name: ")
            student["course"] = input("Enter New Course: ")
            student["project"] = input("Enter New Project: ")

            save_data()

            print("Student Updated Successfully")
            return

    print("Student Not Found")

def delete_student():

    delete_id = input("Enter Student ID to Delete: ")

    if delete_id == "":
        print("Student ID cannot be empty")
        return

    if not delete_id.isdigit():
        print("Student ID must contain only numbers")
        return

    delete_id = int(delete_id)

    for student in students:

        if student["id"] == delete_id:

            students.remove(student)
            
            save_data()
            
            print("Student Deleted Successfully")
            return

    print("Student Not Found")
    
#===================    
#REPORTS & ANALYTICS
#===================   

def total_students():

    print("Total Students:", len(students))

def count_by_course():

    course_name = input("Enter Course Name: ")

    count = 0

    for student in students:

        if student["course"].lower() == course_name.lower():
            count += 1

    print("Total Students:", count)
    
def show_topper():

    if len(students) == 0:
        print("No Students Found")
        return

    topper = students[0]

    for student in students:

        if student["marks"] > topper["marks"]:
            topper = student

    print("Topper Student")
    print("ID:", topper["id"])
    print("Name:", topper["name"])
    print("Marks:", topper["marks"])
    
def average_marks():

    if len(students) == 0:
        print("No Students Found")
        return

    total = 0

    for student in students:

        total += student["marks"]

    average = total / len(students)

    print("Average Marks:", round(average, 2))
    
def pass_fail_report():

    if len(students) == 0:
        print("No Students Found")
        return

    for student in students:

        print("Name:", student["name"])

        if student["marks"] >= 40:
            print("Status: PASS")

        else:
            print("Status: FAIL")

        print("-" * 20)
        
def grade_report():

    if len(students) == 0:
        print("No Students Found")
        return

    for student in students:

        marks = student["marks"]

        if marks >= 90:
            grade = "A"

        elif marks >= 80:
            grade = "B"

        elif marks >= 70:
            grade = "C"

        elif marks >= 60:
            grade = "D"

        else:
            grade = "F"

        print("Name:", student["name"])
        print("Marks:", marks)
        print("Grade:", grade)
        print("-" * 20)
        
def student_ranking():

    if len(students) == 0:
        print("No Students Found")
        return

    ranked_students = sorted(
        students,
        key=lambda student: student["marks"],
        reverse=True
    )

    rank = 1

    for student in ranked_students:

        print("Rank:", rank)
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("-" * 20)

        rank += 1
        
def search_by_name():

    name = input("Enter Student Name: ")

    if name.strip() == "":
        print("Name cannot be empty")
        return

    found = False

    for student in students:

        if student["name"].lower() == name.lower():

            print("Student Found")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Project:", student["project"])
            print("Marks:", student["marks"])

            found = True

    if not found:
        print("Student Not Found")
        
def report_card():

    student_id = input("Enter Student ID: ")

    if not student_id.isdigit():
        print("Invalid ID")
        return

    student_id = int(student_id)

    for student in students:

        if student["id"] == student_id:

            marks = student["marks"]

            if marks >= 90:
                grade = "A"
            elif marks >= 80:
                grade = "B"
            elif marks >= 70:
                grade = "C"
            elif marks >= 60:
                grade = "D"
            else:
                grade = "F"

            if marks >= 40:
                status = "PASS"
            else:
                status = "FAIL"

            print("=" * 30)
            print("      REPORT CARD")
            print("=" * 30)
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Project:", student["project"])
            print("Marks:", marks)
            print("Grade:", grade)
            print("Status:", status)
            print("Attendance:", student.get("attendance", 0), "%")
            print("Admission Date:", student.get("admission_date", "Not Available"))
            print("=" * 30)

            return

    print("Student Not Found")
    
    
def update_attendance():

    student_id = input("Enter Student ID: ")

    if not student_id.isdigit():
        print("Invalid ID")
        return

    student_id = int(student_id)

    for student in students:

        if student["id"] == student_id:

            attendance = input("Enter Attendance Percentage: ")

            if not attendance.isdigit():
                print("Attendance must be a number")
                return

            attendance = int(attendance)

            if attendance < 0 or attendance > 100:
                print("Attendance must be between 0 and 100")
                return

            student["attendance"] = attendance

            save_data()

            print("Attendance Updated Successfully")
            return

    print("Student Not Found")
    
def update_marks():

    student_id = input("Enter Student ID: ")

    if not student_id.isdigit():
        print("Invalid ID")
        return

    student_id = int(student_id)

    for student in students:

        if student["id"] == student_id:

            marks = input("Enter New Marks: ")

            if not marks.isdigit():
                print("Marks must be numbers")
                return

            marks = int(marks)

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100")
                return

            student["marks"] = marks

            save_data()

            print("Marks Updated Successfully")
            return

    print("Student Not Found")
      
def attendance_report():

    if len(students) == 0:
        print("No Students Found")
        return

    for student in students:

        attendance = student.get("attendance", 0)

        print("Name:", student["name"])
        print("Attendance:", attendance, "%")

        if attendance < 75:
            print("Warning: Low Attendance")

        print("-" * 20)

def dashboard():

    if len(students) == 0:
        print("No Students Found")
        return

    total_students = len(students)

    total_marks = 0

    topper = students[0]

    pass_count = 0
    fail_count = 0

    for student in students:

        total_marks += student["marks"]

        if student["marks"] > topper["marks"]:
            topper = student

        if student["marks"] >= 40:
            pass_count += 1
        else:
            fail_count += 1

    average_marks = total_marks / total_students

    print("=" * 30)
    print("      DASHBOARD")
    print("=" * 30)
    print("Total Students:", total_students)
    print("Average Marks:", round(average_marks, 2))
    print("Topper:", topper["name"])
    print("Topper Marks:", topper["marks"])
    print("Pass Students:", pass_count)
    print("Fail Students:", fail_count)
    print("=" * 30)
    
def course_statistics():

    if len(students) == 0:
        print("No Students Found")
        return

    courses = {}

    for student in students:

        course = student["course"]

        if course not in courses:
            courses[course] = {
                "count": 0,
                "total_marks": 0
            }

        courses[course]["count"] += 1
        courses[course]["total_marks"] += student["marks"]

    print("=" * 30)
    print("COURSE STATISTICS")
    print("=" * 30)

    for course, data in courses.items():

        average = data["total_marks"] / data["count"]

        print("Course:", course)
        print("Students:", data["count"])
        print("Average Marks:", round(average, 2))
        print("-" * 20)
    
#===============
#AUTHENTICATION
#===============

def save_settings():

    settings = {
        "username": admin_username,
        "password": admin_password
    }

    with open("settings.json", "w") as file:
        json.dump(settings, file)

    
def login():

    attempts = 3

    while attempts > 0:

        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username == admin_username and password == admin_password:
            print("Login Successful")
            return True

        attempts -= 1

        print("Invalid Username or Password")
        print("Attempts Left:", attempts)

    print("Too Many Failed Attempts")
    return False
        
def change_password():

    global admin_password

    old_password = input("Enter Old Password: ")

    if old_password != admin_password:
        print("Wrong Password")
        return

    new_password = input("Enter New Password: ")

    if len(new_password) < 4:
        print("Password must be at least 4 characters")
        return

    admin_password = new_password
    save_settings()
    print("Password Changed Successfully")
    
def students_by_course():

    course_name = input("Enter Course Name: ")

    if course_name.strip() == "":
        print("Course Name cannot be empty")
        return

    found = False

    for student in students:

        if student["course"].lower() == course_name.lower():

            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("-" * 20)

            found = True

    if not found:
        print("No Students Found In This Course")

def scholarship_students():

    if len(students) == 0:
        print("No Students Found")
        return

    found = False

    print("=" * 30)
    print("SCHOLARSHIP ELIGIBLE STUDENTS")
    print("=" * 30)

    for student in students:

        marks = student["marks"]
        attendance = student.get("attendance", 0)

        if marks >= 80 and attendance >= 75:

            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Marks:", marks)
            print("Attendance:", attendance, "%")
            print("-" * 20)

            found = True

    if not found:
        print("No Eligible Students Found")
        
def course_wise_topper():

    if len(students) == 0:
        print("No Students Found")
        return

    toppers = {}

    for student in students:

        course = student["course"]

        if course not in toppers:
            toppers[course] = student

        elif student["marks"] > toppers[course]["marks"]:
            toppers[course] = student

    print("=" * 30)
    print("COURSE-WISE TOPPERS")
    print("=" * 30)

    for course, topper in toppers.items():

        print("Course:", course)
        print("Topper:", topper["name"])
        print("Marks:", topper["marks"])
        print("-" * 20)
        
def top_3_students():

    if len(students) == 0:
        print("No Students Found")
        return

    ranked_students = sorted(
        students,
        key=lambda student: student["marks"],
        reverse=True
    )

    print("=" * 30)
    print("TOP 3 STUDENTS")
    print("=" * 30)

    limit = min(3, len(ranked_students))

    for i in range(limit):

        print("Rank", i + 1)
        print("Name:", ranked_students[i]["name"])
        print("Marks:", ranked_students[i]["marks"])
        print("Course:", ranked_students[i]["course"])
        print("-" * 20)
        
def performance_analysis():

    if len(students) == 0:
        print("No Students Found")
        return

    print("=" * 30)
    print("PERFORMANCE ANALYSIS")
    print("=" * 30)

    for student in students:

        marks = student["marks"]

        if marks >= 90:
            performance = "Excellent"

        elif marks >= 75:
            performance = "Good"

        elif marks >= 50:
            performance = "Average"

        else:
            performance = "Poor"

        print("Name:", student["name"])
        print("Marks:", marks)
        print("Performance:", performance)
        print("-" * 20)

#=================
#EXPORT FUNCTIONS
#=================

def export_to_csv():

    if len(students) == 0:
        print("No Students Found")
        return

    with open("students_report.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            ["ID", "Name", "Course", "Project", "Marks", "Attendance"]
        )

        for student in students:

            writer.writerow([
                student["id"],
                student["name"],
                student["course"],
                student["project"],
                student["marks"],
                student.get("attendance", 0)
            ])

    print("CSV File Created Successfully")
    
#==================
#SETTINGS & HELPERS
#==================
    
def load_settings():

    global admin_username
    global admin_password

    try:
        with open("settings.json", "r") as file:

            settings = json.load(file)

            admin_username = settings["username"]
            admin_password = settings["password"]

    except FileNotFoundError:

        admin_username = "admin"
        admin_password = ""
        
def generate_student_id():

    if len(students) == 0:
        return 101

    last_id = max(student["id"] for student in students)

    return last_id + 1
        
#==============
#MAIN PROGRAM
#==============

load_data()
load_settings()

if login ():

# 3. Main Program
            while True:
            
                print("1. Add Student")
                print("2. View Students")
                print("3. Search Student")
                print("4. Update Student")
                print("5. Delete Student")
                print("6. Total Student")
                print("7. Count student by course")
                print("8. Show topper")
                print("9. Average marks")
                print("10.Pass/Fail report")
                print('11.Grade report')
                print("12.Student ranking")
                print("13.Search by name")
                print("14.Report card")
                print("15.Update Attendance")
                print("16.Update marks")
                print("17.Attendance report")
                print("18.Dashboard statistics")
                print("19.Change password")
                print("20.Student by course")
                print("21.Scholarship Student")
                print("22.Course-wise Topper")
                print("23.Course Statistics")
                print("24.Top 3 Students")
                print("25.Performance Analysis")
                print("26.Export To CSV")
                print("27.Exit")
                
                choice = input("Enter Choice: ")
            
                if choice == "1":
                    add_student()
            
                elif choice == "2":
                    view_students()
            
                elif choice == "3":
                    search_student()
            
                elif choice == "4":
                    update_student()
            
                elif choice == "5":
                    delete_student()
            
                elif choice =="6":
                    total_students()
                    
                elif choice =="7":
                       count_by_course()
                       
                elif choice =="8":
                       show_topper()
                       
                elif choice =="9":
                       average_marks()
                       
                elif choice =="10":
                       pass_fail_report()
                       
                elif choice =="11":
                       grade_report()
                       
                elif choice =="12":
                       student_ranking()
                       
                elif choice =="13":
                       search_by_name()
                       
                elif choice =="14":
                       report_card()
                       
                elif choice == "15":
                    update_attendance()
                    
                elif choice =="16":
                    update_marks()
            
                elif choice == "17":
                     attendance_report()
                     
                elif choice =="18":
                    dashboard()
                    
                elif choice =="19":
                    change_password()
                    
                elif choice =="20":
                    students_by_course()
                    
                elif choice =="21":
                    scholarship_students()
                    
                elif choice =="22":
                    course_wise_topper()
                    
                elif choice =="23":
                    course_statistics()  
                    
                elif choice =="24":
                    top_3_students() 
                    
                elif choice =="25":
                    performance_analysis()
                    
                elif choice =="26":
                    export_to_csv()
            
                elif choice == "27":
                    print("Program Closed")
                    break
                    
            else:
                print("Invalid Choice")
            