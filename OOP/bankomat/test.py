from bankomat import CashMachine


class TestCashMachine:


    def test_cash_machine_init(self):
        b = CashMachine()
        assert True

    def test_is_available(self):
        b = CashMachine()
        assert b.is_available() is False

    def test_put_money(self):
        b = CashMachine()
        b.put_money([200, 100, 100, 50])
        assert b.is_available() is True
