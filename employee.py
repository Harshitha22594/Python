
# Q6. Employee Payroll System (Corporate Domain)
# Design an Employee class.
# Methods to think about:
# • calculate salary (object method)
# • apply leave deduction (object method)
# • display payslip (object method)
# • update hra percentage (class method)


class employee:
    company_name = "Tech Solutions"
    hra_percentage = 20

    def __init__(self, emp_id, name, basic_salary, leaves_taken):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
        self.leaves_taken = leaves_taken
        self.total_salary = 0

    def calculate_salary(self):
        hra = (self.basic_salary * self.hra_percentage) / 100
        self.total_salary = self.basic_salary + hra - (self.leaves_taken * 100)
        print(f"Total salary for {self.name} is {self.total_salary}")

    def apply_leave_deduction(self, leave_days):
        deduction = leave_days * 100
        self.total_salary -= deduction
        print(f"Leave deduction for {leave_days} days. Total salary: {self.total_salary}")

    def display_payslip(self):
        print(f"Payslip for {self.name} (Employee ID: {self.emp_id})")
        print(f"Basic Salary: {self.basic_salary}")
        print(f"HRA Percentage: {self.hra_percentage}%")
        print(f"Leaves Taken: {self.leaves_taken}")
        print(f"Total Salary: {self.total_salary}")

    @classmethod
    def update_hra_percentage(cls, new_hra):
        cls.hra_percentage = new_hra
        print("Updated HRA percentage to", cls.hra_percentage)

e1 = employee(1, "Harshitha", 50000, 2)
e1.calculate_salary()
e1.apply_leave_deduction(1)
e1.display_payslip()
e1.update_hra_percentage(25)
e2 = employee(2, "Pragna", 60000, 3)
e2.calculate_salary()
e2.apply_leave_deduction(2)
e2.display_payslip()