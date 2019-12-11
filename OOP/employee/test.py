from employee import Employee
from employee import PremiumEmployee


class TestEmployee:

    def test_init(self):
        e = Employee("Jan", "Kowalski", 100)
        assert e.name == "Jan"
        assert e.surrname == "Kowalski"
        assert e.rph == 100

    def test_register_time(self):
        e = Employee("Jan", "Kowalski", 100)
        e.register_time(5)
        assert e.registered_hours == 5

    def test_pay_salary_normal_hours(self):
        e = Employee("Jan", "Kowalski", 100)
        e.register_time(5)
        assert e.pay_salary() == 500

    def test_pay_salary_without_registered_time(self):
        e = Employee("Jan", "Kowalski", 100)
        assert e.pay_salary() == 0

    def test_pay_salary_twice_normal_hours(self):
        e = Employee("Jan", "Kowalski", 100)
        e.register_time(5)
        assert e.pay_salary() == 500
        assert e.pay_salary() == 0

    def test_pay_salary_over_hours(self):
        e = Employee("Jan", "Kowalski", 100)
        e.register_time(10)
        assert e.pay_salary() == 1200

    def test_give_bonus(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        e.register_time(5)
        e.give_bonus(1000)
        e.give_bonus(200)
        e.give_bonus("15%")
        e.give_bonus("35%")
        assert e.pay_salary() == 1950

