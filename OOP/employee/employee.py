class Employee:

    def __init__(self, name, surrname, rph):
        self.name = name
        self.surrname = surrname
        self.rph = rph
        self.__registered_hours = 0

    def register_time(self, time):
        self.__registered_hours = time

    def pay_salary(self):
        if self.__registered_hours <= 8:
            to_pay = self.__registered_hours * self.rph
            self.__registered_hours = 0
        else:
            to_pay = self.rph * 8 + (self.__registered_hours - 8) * self.rph * 2
        return to_pay


emp = Employee("Jan", "Kowalski", 200)
print(emp._Employee__registered_hours)
emp._Employee__registered_hours = 10
print(emp.pay_salary())

