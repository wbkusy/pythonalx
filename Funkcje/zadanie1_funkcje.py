# naqpisz funkcje która sprawdzi czy liczba jest liczbą pierwszą

import unittest


def czy_pierwsza(x):
    #"""ten obszar nazywa się docstring i służy do dokumentcji funkcji
    #sprawdza czy x jest liczbą pierwszą
    #>>>czy_pierwsza(7)
    #True
    #>>>czy_pierwsza(10)
    #False
    #"""
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


# assert czy_pierwsza(2) is True
# assert czy_pierwsza(10) is False
# assert  czy_pierwsza(11) is True

# print(help(czy_pierwsza))

# unittesty:

# class TestCzyPierwsza(unittest.TestCase):
# def test_czy_pierwsza_dla_liczby_pierwszej(self):
# self.assertEqual(czy_pierwsza(7), True)
# self.assertEqual(czy_pierwsza(17), True)
# self.assertEqual(czy_pierwsza(11), True)
# def test_czy_pierwsza_dla_liczby_niepierwszej(self):
# self.assertIs(czy_pierwsza(10), False)
# self.assertIs(czy_pierwsza(366), False)


# class TestCzyPierwsza(unittest.TestCase):
def test_czy_pierwsza_dla_liczby_pierwszej():
    assert czy_pierwsza(7) is True
    assert czy_pierwsza(17) is True
    assert czy_pierwsza(11) is True


def test_czy_pierwsza_dla_liczby_niepierwszej():
    assert czy_pierwsza(10) is False
    assert czy_pierwsza(366) is False
