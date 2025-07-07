import csv
import os

class Employee:
    def __init__(self, empid, name, address, contact_number, spouse_name, number_of_child, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.spouse_name = spouse_name
        self.number_of_child = number_of_child
        self.salary = salary

    def to_dict(self):
        """Convert employee details to a dictionary for CSV writing."""
        return {
            'Employee ID': self.empid,
            'Name': self.name,
            'Address': self.address,
            'Contact Number': self.contact_number,
            'Spouse Name': self.spouse_name,
            'Number of Children': self.number_of_child,
            'Salary': self.salary
        }

def write_employees_to_csv(employees, filename='employees.csv'):
    """Write employee data to a CSV file."""
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=employees[0].to_dict().keys())
            writer.writeheader()
            for employee in employees:
                writer.writerow(employee.to_dict())
        print(f"Employee data written to {filename} successfully.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def display_employees(employees):
    """Display the list of employees."""
    if not employees:
        print("No employee records found.")
        return
    
    print("\nEmployee Details:")
    for employee in employees:
        print(f"ID: {employee.empid}, Name: {employee.name}, Address: {employee.address}, "
              f"Contact Number: {employee.contact_number}, Spouse Name: {employee.spouse_name}, "
              f"Number of Children: {employee.number_of_child}, Salary: {employee.salary}")

def get_employee_input():
    """Get employee details from user input."""
    empid = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    contact_number = input("Enter Contact Number: ")
    spouse_name = input("Enter Spouse Name: ")
    number_of_child = input("Enter Number of Children: ")
    salary = input("Enter Salary: ")
    
    return Employee(empid, name, address, contact_number, spouse_name, number_of_child, salary)

def main():
    employees = []
    
    while True:
        print("\nMenu:")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            employee = get_employee_input()
            employees.append(employee)
            write_employees_to_csv(employees)
        elif choice == '2':
            display_employees(employees)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
