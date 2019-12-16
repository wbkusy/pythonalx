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




class PremiumEmployee(Employee):

    def __init__(self, name, surrname, rph):
        super().__init__(name, surrname, rph)
        self.bonus = []

    def give_bonus(self, bonus):
        self.bonus.append(bonus)

    def pay_salary(self):
        to_pay = super().pay_salary()
        for b in self.bonus:
            to_pay += b
        return to_pay

