class FullTimeEmployee:
    def calculate_pay(self):
        return 4000


class HourlyEmployee:
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_pay(self):
        return self.hours * self.rate


employees = [
    FullTimeEmployee(),
    HourlyEmployee(80, 25)
]

for employee in employees:
    print(employee.calculate_pay())