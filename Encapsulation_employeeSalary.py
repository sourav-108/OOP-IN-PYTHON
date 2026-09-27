class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, amount):
        if amount <= 0:
            raise ValueError("Salary must be positive")
        self.__salary = amount


employee = Employee("Sourav", 3500)
employee.salary = 3800
print(employee.salary)  # 3800