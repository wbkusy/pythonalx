
# "baza danych" pracowników

import datetime, json

dane_pracownikow = list()

try:
    with open("pracownicy.dat", "rt")as fd:
        dane_pracownikow = json.load(fd)
except:
    print("odczyt plikow nie udal sie")


def wprowadz_dane():
    print("-"*40)
    print("wprowadz dane pracownika")
    imie = None
    while True:
        imie = input("podaj imie: ")
        if len(imie) <= 2:
            print("podaj imie:")
        else:
            break

    nazwisko = None
    while True:
        nazwisko = input("podaj nazwisko: ")
        if len(nazwisko) <= 2:
            print("podaj nazwisko:")
        else:
            break

    rok_urodzenia = None
    while True:
        try:
            rok_urodzenia = int(input("podaj rok urodzenia: "))
            if rok_urodzenia < 1930:
                print("idz na emeryture")
                continue
            rok_biezacy = datetime.datetime.now().year
            if rok_biezacy - rok_urodzenia >= 15:
                break

            print("za mlodys na prace")
        except Exception as exc:
            print("podaj rok urodzenia", exc)

    pensja = None

    while True:
        try:
            pensja = int(input("podaj wartosc wynagrodzenia: "))
            if pensja > 0:
                break
            print("podaj kwote wynagrodzenia:")
        except Exception as exc:
            print("podaj kwote", exc)

    return {"imie": imie, "nazwisko": nazwisko, "rok urodzenia": rok_urodzenia, "pensja": pensja}


def pokaz_rekordy():
    if len(dane_pracownikow) == 0:
        print("brak danych")
        return
    for rekord in dane_pracownikow:
        print(f"{rekord.get('imie')}\t{rekord.get('nazwisko')}/t{rekord.get('rok urodzenia')}\t{rekord.get('pensja')}")

while True:
    operacja = input("Podaj operacje [d/w/q]: ").strip().upper()
    if operacja == "Q":
        print("koniec aplikacji")
        break

    if operacja == "W":
        pokaz_rekordy()

    if operacja == "D":
        rekord = wprowadz_dane()
        dane_pracownikow.append(rekord)
        with open("pracownicy.dat", "at")as fd:
            json.dump(dane_pracownikow, fd)
