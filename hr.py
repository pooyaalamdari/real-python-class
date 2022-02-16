class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('------')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'Check Amount: {employee.calculate_payroll()}')
            print('') 


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    #is it new calculate_payroll method ???
    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name) 
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

class CommisionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commision):
        super().__init__(id, name, weekly_salary) 
        self.commision = commision

    def calculate_payroll(self):
        return self.commision + self.weekly_salary


salary_employee = SalaryEmployee(1,'john smith', 1500)
hourly_employee = HourlyEmployee(2,'john Doe', 40, 15)
commision_employee = CommisionEmployee(3, 'Kevin Bacon', 1000, 250)

payroll_system = PayrollSystem() 

payroll_system.calculate_payroll([ 
    salary_employee,
    hourly_employee,
    commision_employee
]) 
