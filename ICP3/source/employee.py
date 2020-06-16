class Employee :
    empCount = 0
    salarySum = 0

    def __init__(self, name, family, salary, Department):
        self.name = name
        self.family = family
        self.salary = salary
        self.Department = Department
        Employee.empCount += 1
        Employee.salarySum += salary

    def averagesalary(self):
         average = float(Employee.salarySum)/float(Employee.empCount)
         print("The Average Salary of the Employees is: ", average)

    def displayEmployee(self):
        print("Name:", self.name, "Family:", self.family, "salary:", self.salary, "Department:", self.Department)


class fullTime(Employee):
     pass


if __name__=="__main__"  :
    emp1 = Employee("Zara", "Taurs", 20000, "HR")
    "This would create second object of Employee class"
    emp2 = Employee("Manni", "William", 15000, "Developer")
    emp3 = fullTime("David", "vicky", 40000, "testing")
    Employee.averagesalary(Employee)
    emp1.displayEmployee()
    emp2.displayEmployee()
    emp3.displayEmployee()
    print("Total Employees:", Employee.empCount)
