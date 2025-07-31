class Employee:
    def __init__(self, emp_id, name, department, salary):
        """Initialize an employee record."""
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display_info(self):
        """Returns a formatted string with employee details."""
        return f"ID: {self.emp_id} | Name: {self.name} | Department: {self.department} | Salary: ${self.salary}"


class HRDashboard:
    def __init__(self):
        """Initialize the HR Dashboard with an empty employee list."""
        self.employees = []

    def add_employee(self):
        """Adds a new employee to the system."""
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        department = input("Enter Employee Department: ")
        salary = float(input("Enter Employee Salary: "))
        self.employees.append(Employee(emp_id, name, department, salary))
        print("Employee added successfully!")

    def display_employees(self):
        """Displays all employees in the system."""
        if not self.employees:
            print("\nNo employees found.")
        else:
            print("\nEmployee Records:")
            for employee in self.employees:
                print(employee.display_info())

    def remove_employee(self):
        """Removes an employee based on Employee ID."""
        emp_id = input("Enter Employee ID to remove: ")
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                print("Employee removed successfully!")
                return
        print("Employee not found.")

    def calculate_total_salary(self):
        """Calculates and displays the total salary expenditure."""
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"\nTotal Salary Expenditure: ${total_salary:.2f}")


def main():
    """Main function to run the HR Dashboard."""
    dashboard = HRDashboard()
    while True:
        print("\nHR Dashboard Menu:")
        print("1) Display Employees")
        print("2) Add Employee")
        print("3) Remove Employee")
        print("4) Total Salary Expenditure")
        print("5) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            dashboard.display_employees()
        elif choice == "2":
            dashboard.add_employee()
        elif choice == "3":
            dashboard.remove_employee()
        elif choice == "4":
            dashboard.calculate_total_salary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()