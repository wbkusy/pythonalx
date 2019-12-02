# Utwórz klasę produkt
# która będzie działać tak

# pr= Product(1, "woda", 10.99)
# pr.id
# 1
# pr.name
# 'woda'
# pr.price
# 10.99

class Produkt:

    NEXT_ID = 1 # atrybut klasowy

    def __init__(self, name, price):

        self.name = name
        self.price = price
        self.id = Produkt.NEXT_ID
        self.incr_next_id()

    @classmethod
    def get_id(cls):
        return cls.get_id

    @classmethod
    def incr_next_id(cls):
        cls.NEXT_ID += 1

    def show(self):
        return f"{self.name} ({self.id}), cena: {self.price}"

woda = Produkt("woda nieg.", 1.50)
chleb = Produkt("chleb wiejski", 2.00)
cebula = Produkt("cebula dymka", 3.00)

#print(woda.price)

print(Produkt.id)