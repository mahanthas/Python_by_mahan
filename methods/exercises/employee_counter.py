"""
Create an Employee class that tracks how many employees have been created using a class-level variable. 
Add a @classmethod named get_total_employees() that returns this count.
"""

class Employee:
    count = 0
    def __init__(self, name):
        self.name=name
        Employee.count += 1

    @classmethod
    def get_total_employees(cls):
        return f"the total employee count is {cls.count}"
    
employee1 = Employee("mahan")
employee2 = Employee("swamy")    
print(Employee.get_total_employees())