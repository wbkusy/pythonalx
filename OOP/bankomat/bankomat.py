class CashMachine:

    def __init__(self):
        self.money = []

    def is_available(self):
        if self.money == []:
            return False
        return True

    def put_money(self, cash):
        self.money = cash


    def get_money(self, amount):
        if self.is_available:
            to_withdraw = []
            for money in self.money:
                if money + sum(to_withdraw) <= amount:
                    to_withdraw.append(money)
            return to_withdraw
        return []


