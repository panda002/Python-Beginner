class Employee:  # here Employee is a class adn we can create as many employees we want

    id = 1
    name = 'Sid'
    dept = "CS"

    def display_prof(self):
        print("ID: %d\nName: %s" % (self.id, self.name))

    def display_dept(self):
        dept = self.dept
        print("Dept: ", dept)


emp = Employee()
emp.display_prof()
emp.display_dept()
