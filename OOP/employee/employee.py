class Employee:

    def __init__(self, name, surrname, rph):
        self.name = name
        self.surrname = surrname
        self.rph = rph
        self.registered_hours = 0

    def register_time(self, time):
        self.registered_hours = time

    def pay_salary(self):
        if self.registered_hours <= 8:
            to_pay = self.registered_hours * self.rph
            self.registered_hours = 0
        else:
            to_pay = self.rph * 8 + (self.registered_hours - 8) * self.rph * 2
        return to_pay


#emp = Employee("Jan", "Kowalski", 200)
#print(emp.Employee__registered_hours)
#emp._Employee__registered_hours = 10
#print(emp.pay_salary())

class PremiumEmployee(Employee):

    def __init__(self, name, surrname, rph):
        super().__init__(name, surrname, rph)
        self.bonus = 0

    def give_bonus(self, bonus):
        self.bonus = bonus

    def pay_salary(self):
        if self.registered_hours <= 8:
            to_pay = self.registered_hours * self.rph + self.bonus
            self.registered_hours = 0
        else:
            to_pay = self.rph * 8 + (self.registered_hours - 8) * self.rph * 2 + self.bonus
        return to_pay

