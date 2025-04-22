class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7-rest_days)*8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment

    def salary(self):
        return self.hours * self.hourly_payment

employee = EmployeeSalary.get_hours('Иван', 4, 'Ivan@ya.ru')
print(employee.rest_days)
print(employee.hours)
print(employee.salary())

employee = EmployeeSalary.get_email('Иван', 20,4)
print(employee.name)
print(employee.email)
print(employee.salary())
employee.set_hourly_payment(200)
print(employee.salary())