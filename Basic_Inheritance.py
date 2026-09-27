class Staff:
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id


class Teacher(Staff):
    def __init__(self, name, staff_id, subject):
        super().__init__(name, staff_id)
        self.subject = subject


teacher = Teacher("Sourav", "T-104", "English")
print(teacher.name, teacher.staff_id, teacher.subject)