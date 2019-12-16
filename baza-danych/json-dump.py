
# Serializacja zmiennych do formatu json

import json

pracownik = {"imie": "Jan",
             "nazwisko": "Kowalski",
             "wiek": 42,
             "dostepy": ['sala01', 'sala02', 'sala03'],
             "wynagrodzeneie": 12345.67,
             "manager": False,
             "auto": None
             }

with open("pracownik.dat", "wt") as fd:
    json.dump(pracownik, fd)
