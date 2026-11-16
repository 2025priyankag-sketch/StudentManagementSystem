students = []

def register_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    course = input("Enter course: ")

    student = {
        "Name": name,
        "Roll No": roll_no,
        "Course": course
    }

    students.append(student)
    print("Student registered successfully!")

def display_students():
    print("\nRegistered Students:")
    for student in students:
        print(student)

register_student()
display_students()