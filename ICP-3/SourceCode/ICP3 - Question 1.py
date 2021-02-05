class Employee:
    count = 0
    Total_Salary = 0

    def __init__(self, name, family, salary, dept):
        self.name = name
        self.family = family
        self.salary = salary
        self.dept = dept
        Employee.count += 1
        Employee.Total_Salary += salary

    def emp_count(self):

        print("total number of employees", Employee.count)

    def avg_salary(self):

        avg_sal = Employee.Total_Salary / Employee.count
        print("average salary:", avg_sal)

    def sample_func(self):
        print('calling base class member function')


class Full_time_employee(Employee):
    def __init__(self):
        print('Full time employee(sub class)')

if __name__ == '__main__':
    number_of_employees = int(input("No of employees:"))
    for i in range(number_of_employees):
        nam= input("name:")
        fam = input("family:")
        sal = float(input("salary:"))
        dep = input("dept:")
        BaseClass = Employee(nam,fam,sal,dep)
    Employee_Details = Full_time_employee() 
    Employee_Details.emp_count()
    Employee_Details.avg_salary()
    BaseClass.sample_func()
