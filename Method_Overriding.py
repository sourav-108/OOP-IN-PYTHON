class Employee:
    def salary(self):
        return "salary"


class Manager(Employee):
    def salary(self):
        return "salary + bonus"


class Intern(Employee):
    def salary(self):
        return "Extra"


for person in [Manager(), Intern()]:
    print(person.salary())