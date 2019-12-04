from zakupy import Product, Basket
from collections import namedtuple

item = namedtuple("item", ["product", "how_many"])

class Test_zakupy:


    def test_init_basket(self):
        basket = Basket()
        assert True

    def test_add_product_to_basket(self):
        basket = Basket()
        product1 = Product(1, "woda", 10.00)
        basket.add_product(product1, 5)
        product2 = Product(2, "cukier", 5.00)
        basket.add_product(product2, 3)
        assert len(basket.items) == 2
        assert basket.koszt == 65

    def test_generate_report(self):
        basket = Basket()
        product1 = Product(1, "woda", 10.00)
        basket.add_product(product1, 5)
        product2 = Product(2, "cukier", 5.00)
        basket.add_product(product2, 3)
        #expected = """w koszyku znajdują się:
#woda
#cukier
#do zapłaty: 65"""
 #       assert basket.generates_report == expected



