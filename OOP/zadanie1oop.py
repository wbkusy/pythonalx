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
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


woda = Produkt(1, "woda nieg.", 1.50)
chleb = Produkt(2, "chleb wiejski", 2.00)
cebula = Produkt(3, "cebula dymka", 3.00)

print(woda.price)

def test_product():
    woda=Produkt(1, "woda nieg.", 1.50)
    assert