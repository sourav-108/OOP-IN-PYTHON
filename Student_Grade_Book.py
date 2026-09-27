class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0


student = Student("Mina")
student.add_grade(80)
student.add_grade(90)
print(student.average())  # 85.0