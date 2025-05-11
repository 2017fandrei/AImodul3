from datetime import datetime


class Employee:
    raise_amount = 1.04

    def __init__(self):
        self.pay = 0

    def apply_raise(self):
        self.pay += self.raise_amount

    @classmethod
    def set_raise_amount(cls, new_raise_amount):
        cls.raise_amount = new_raise_amount

    @staticmethod
    def is_workday(day):
        return day.weekday() not in (5, 6)


# print(Employee.is_workday(datetime.now()))
print(Employee.raise_amount)
Employee.set_raise_amount(0.17)
print(Employee.raise_amount)
