import datetime


employees = {}
salaries = {}
attendance_records = {}


def display_menu():
    print("\n***** Employee Management + Attendance System *****")
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Activate/Inactivate Employee")
    print("4. View Employees")
    print("5. Delete Employee")
    print("6. Add/Update Salary")
    print("7. Display Salaries")
    print("8. Mark Attendance")
    print("9. View Attendance Records")
    print("10. Exit")


def add_employee(employees):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    email = input("Enter Employee Email: ")
    phone = input("Enter Employee Phone Number: ")
    department = input("Enter Employee Department: ")
    designation = input("Enter Employee Designation: ")
    status = "Active"

    employees[emp_id] = {
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Department": department,
        "Designation": designation,
        "Status": status
    }
    print(f"\nEmployee {name} (ID: {emp_id}) added successfully!\n")

def search_employee(employees):
    emp_id = input("\nEnter Employee ID to search: ")
    if emp_id in employees:
        print("\nEmployee Found:")
        for key, value in employees[emp_id].items():
            print(f"{key}: {value}")
    else:
        print("\nEmployee Not Found!")

def update_employee_status(employees):
    emp_id = input("\nEnter Employee ID: ")
    if emp_id in employees:
        status = input("Enter Employee Status (Active/Inactive): ")
        if status not in ["Active", "Inactive"]:
            print("\nInvalid Status! Choose either 'Active' or 'Inactive'.\n")
            return
        employees[emp_id]["Status"] = status
        print(f"\nEmployee {emp_id} status updated to {status}\n")
    else:
        print("\nEmployee Not Found!")

def view_employees(employees):
    if employees:
        print("\nEmployee List:")
        for emp_id, details in employees.items():
            print(f"\nID: {emp_id}")
            for key, value in details.items():
                print(f"{key}: {value}")
    else:
        print("\nNo employees found!\n")

def delete_employee(employees):
    emp_id = input("\nEnter Employee ID to delete: ")
    if emp_id in employees:
        name = employees[emp_id]["Name"]
        del employees[emp_id]
        salaries.pop(emp_id, None)
        attendance_records.pop(emp_id, None)
        print(f"\nEmployee ID {emp_id} deleted successfully!\n")
    else:
        print("\nEmployee Not Found!")

def add_or_update_salary(employees, salaries):
    emp_id = input("\nEnter Employee ID for salary update: ")
    if emp_id in employees:
        try:
            salary = float(input(f"Enter new salary for {employees[emp_id]['Name']}: "))
            salaries[emp_id] = salary
            print(f"Salary for {employees[emp_id]['Name']} set to {salary}\n")
        except ValueError:
            print("Invalid salary input! Please enter a numeric value.\n")
    else:
        print("Employee ID not found!")

def display_salaries(employees, salaries):
    if not salaries:
        print("\nNo salaries found!\n")
    else:
        print("\nEmployee Salaries:")
        for emp_id, salary in salaries.items():
            name = employees.get(emp_id, {}).get("Name", "Unknown")
            print(f"{name} (ID: {emp_id}): {salary}")


def mark_attendance(attendance_records, employees):
    emp_id = input("\nEnter Employee ID to mark attendance: ")
    if emp_id in employees:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if emp_id not in attendance_records:
            attendance_records[emp_id] = []
        attendance_records[emp_id].append(timestamp)
        print(f"\nAttendance marked for Employee ID {emp_id} at {timestamp}\n")
    else:
        print("\nEmployee ID not found!")

def view_attendance(attendance_records, employees):
    emp_id = input("\nEnter Employee ID to view attendance: ")
    if emp_id in attendance_records:
        print(f"\nAttendance records for Employee ID {emp_id} ({employees.get(emp_id, {}).get('Name', 'Unknown')}):")
        for record in attendance_records[emp_id]:
            print(record)
    else:
        print("\nNo attendance records found!")


while True:
    display_menu()
    choice = input("Select an option between 1-10: ")

    if choice == '1':
        add_employee(employees)
    elif choice == '2':
        search_employee(employees)
    elif choice == '3':
        update_employee_status(employees)
    elif choice == '4':
        view_employees(employees)
    elif choice == '5':
        delete_employee(employees)
    elif choice == '6':
        add_or_update_salary(employees, salaries)
    elif choice == '7':
        display_salaries(employees, salaries)
    elif choice == '8':
        mark_attendance(attendance_records, employees)
    elif choice == '9':
        view_attendance(attendance_records, employees)
    elif choice == '10':
        print("\nExiting System... Goodbye!\n")
        break
    else:
        print("\nInvalid choice! Please select a valid option.\n")
