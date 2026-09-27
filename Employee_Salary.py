class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def total_pay(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def total_pay(self):
        return self.salary + self.bonus


manager = Manager("Arif", 50000, 10000)
print(manager.total_pay())  # 60000