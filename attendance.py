attendance = {}

def mark_attendance():
    roll_no = input("Enter roll number: ")
    status = input("Enter attendance (Present/Absent): ")

    attendance[roll_no] = status
    print("Attendance marked successfully!")

def display_attendance():
    print("\nAttendance Records:")
    for roll, status in attendance.items():
        print(roll, ":", status)

mark_attendance()
display_attendance()