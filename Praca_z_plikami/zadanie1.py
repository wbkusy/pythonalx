# Napisz funkcję, która otworzy podany jako argument plik (podana będzie nazwa pliku lub ścieżka)
# i wypisze go podając jego linie

# plik.txt
# Raz
# Dwa
# Trzy

# Wynik:
# 1. Raz
# 2. Dwa
# 3. Trzy

# Pozwół na uruchomienie programu z command lina

# python numerator.py test

import sys

try:
    file_name = sys.argv[1]
except IndexError:
    print("Nie podano nazwy pliku")
    exit()
def file_opener(nazwa):
    with open(nazwa, encoding='utf-8') as f:
        for i, line in enumerate(f, start=1):
            print(i, line.rstrip())

try:
    file_opener(file_name)
except FileNotFoundError:
    print("Nie ma taskiego pliku")

