class Employee:
    count = 0

    def __init__(self, id, name, dept):
        self.id = id
        self.name = name
        self.dept = dept

    def display(self):
        """
        dfsdfsdfs
        :return: sdfdsfsdf
        """
        print("ID: %d\nName: %s\nDept: %s" % (self.id, self.name, self.dept))
        Employee.count = Employee.count + 1


emp1 = Employee(1, "Sid", "CS")  # here emp1 is the object of the class Employee
emp2 = Employee(2, "Aish", "EE")

emp1.display()
emp2.display()
print("Employee added = ", Employee.count)
print(emp1.__dict__)
print(emp1.__doc__)

