# Tworzenie rekordu pracownika: 2 parametry obowiązkowe, 2 opcjonalne, oddać zmienną typu słownik


def utworz_urzytkownika(imie, nazwisko, email = "info@firma.pl", nr_tel = None):
    pracownik = dict()
    pracownik["imie"] = imie
    pracownik["nazwisko"] = nazwisko
    pracownik["email"] = email
    pracownik["nr_tel"] = nr_tel
    return [pracownik]



print(utworz_urzytkownika("Jan", "Kowalski"))
print(utworz_urzytkownika("Adam", "Nowak", "anowak@firma.pl", "123456789"))
print(utworz_urzytkownika("Jan", "Zieliński", nr_tel="987654321"))
print(utworz_urzytkownika("Jan", "Zieliński", email="zielinskij@firma.pl"))
print(utworz_urzytkownika("Jan", "Zieliński", "zielinskij@firma.pl"))
print(utworz_urzytkownika("Jan", "Zieliński", nr_tel="783438268", email="zielinskij@firma.pl"))