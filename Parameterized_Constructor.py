class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


student = Student("Durjoy", 13)
print(student.name, student.roll)