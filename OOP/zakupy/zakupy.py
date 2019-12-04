class Product:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class Basket:

    def __init__(self):
        self.koszt = 0
        self.items = []

    def add_product(self, product, how_many):
        self.items.append(product)
        self.koszt += how_many * product.price

    def generates_report(self):
        output = "w koszyku znajdują się:"
        for i in self.items:
            output += str(self.items[i])
        output += "do zapłaty:" + str(self.koszt)
        return output



