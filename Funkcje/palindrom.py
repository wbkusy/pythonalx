# Napisz funkcję która zprawdzi czy dany tekst jest palindromem
# to trzeba w pyteście odpalić przez koniguracje

def is_palindrom(x):
    x = x.lower().replace(" ", "").replace(".", "").replace(",", "") # albo signs_to_remove = " .,;!?"
    return x == x[::-1] #jeśli coś jest sobie równe to i tak zwraca true bez if


def test_palindrom():
    assert is_palindrom("kajak") is True
    assert is_palindrom("A to idiota") is True
    assert is_palindrom("A to idiota.") is True
    assert is_palindrom("Ada, gmina za nim gada") is True


print(is_palindrom("kajak"))
