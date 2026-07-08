class Person:
    def __init__(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
class Employee(Person):
    def __init__(self,name,annual_salary,work_start_year,national_insurance_number):
        super().__init__(name)
        self.annual_salary=annual_salary
        self.work_start_year=work_start_year
        self.national_insurance_number=national_insurance_number
    def get_annual_salary(self):
        return self.annual_salary
    def set_annual_salary(self,annual_salary):
        self.annual_salary=annual_salary
    def get_work_start_year(self):
        return self.work_start_year
    def set_work_start_year(self,work_start_year):
        self.work_start_year=work_start_year
    def get_national_insurance_number(self):
        return self.national_insurance_number
    def set_national_insurance_number(self,national_insurance_number):
        self.national_insurance_number=national_insurance_number
class TestEmployee:
    def run_tests(self):
        emp=Employee("Alice",75000.0,2022,"AB123456C")
        print("Employee Name:",emp.get_name())
        print("Annual Salary:",emp.get_annual_salary())
        print("Start Year:",emp.get_work_start_year())
        print("Insurance Number:",emp.get_national_insurance_number())
        emp.set_name("Bob")
        emp.set_annual_salary(82000.0)
        print("\nUpdated Name:",emp.get_name())
        print("Updated Salary:",emp.get_annual_salary())
tester=TestEmployee()
tester.run_tests()