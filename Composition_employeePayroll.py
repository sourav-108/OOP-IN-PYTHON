class Salary:
    def __init__(self, monthly_amount):
        self.monthly_amount = monthly_amount

    def after_tax(self, tax_rate):
        return self.monthly_amount * (1 - tax_rate)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def take_home_pay(self):
        return self.salary.after_tax(0.15)


employee = Employee("Jordan", Salary(4000))
print(employee.take_home_pay())  # 3400.0