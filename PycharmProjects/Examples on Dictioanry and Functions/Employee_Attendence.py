import datetime

def display_menu():
    print("\n***** Employee Attendance System *****")
    print("1. Mark Attendance")
    print("2. View Attendance Records")
    print("3. Exit")

def mark_attendance(attendance_records):
    emp_id = input("\nEnter Employee ID to mark attendance: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if emp_id not in attendance_records:
        attendance_records[emp_id] = []
    attendance_records[emp_id].append(timestamp)
    print(f"\nAttendance marked for Employee ID {emp_id} at {timestamp}\n")

def view_attendance(attendance_records):
    emp_id = input("\nEnter Employee ID to view attendance: ")
    if emp_id in attendance_records:
        print(f"\nAttendance records for Employee ID {emp_id}:")
        for record in attendance_records[emp_id]:
            print(record)
    else:
        print("\nNo attendance records found!")

attendance_records = {}

while True:
    display_menu()
    choice = input("Select an option between 1-3: ")

    if choice == '1':
        mark_attendance(attendance_records)
    elif choice == '2':
        view_attendance(attendance_records)
    elif choice == '3':
        print("\nExiting Employee Attendance System...!")
        break
    else:
        print("\nInvalid choice! Please select a valid option.\n")
