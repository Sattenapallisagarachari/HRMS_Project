salaries = {}

def add_salary(name, salary):
    salaries[name] = salary
    print("Added", name, "with salary of", salary)

def update_salary(name, new_salary):
    if name in salaries:
        salaries[name] = new_salary
        print("Updated", name, "'s salary to", new_salary)
    else:
        print("Employee not found!")

def display_salaries():
    if not salaries:
        print("No salaries found!")
    else:
        for name, salary in salaries.items():
            print(name, ":", salary)
