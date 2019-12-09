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

    def test_get_money(self):
        b = CashMachine()
        assert b.get_money(100) == []
        b.put_money([100])
        assert b.get_money(100) == [100]
        cm.put_money([50,50])
        assert b.get_money(100) == [50,50]