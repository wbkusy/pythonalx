class CashMachine:

    def __init__(self):
        self.money = []

    def is_available(self):
        if self.money == []:
            return False
        return True

    def put_money(self, cash):
        self.put_money = cash
        for i in cash:
            self.money.append(cash[i])
