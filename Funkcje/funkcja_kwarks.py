# Przekazywanie listy parametrów nazywanych

def funkcja_parametry(nr, **kwargs):
    print(kwargs["imie"])
    print("nr pracownika=",nr)
funkcja_parametry(102, imie="Jan", nazwisko="Kowalski", email="jk@firma.pl", wiek=44)