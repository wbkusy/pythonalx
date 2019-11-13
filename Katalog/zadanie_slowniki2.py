osoba1=['a', 'b', 'c', 'd']
osoba2=['a', 'b', 'c', 'd']

import random

y=0
while True:
    random.shuffle(osoba2)
    for i in range(0, 3):
        if not osoba1[i] == osoba2[i]:
            for os1, os2 in zip(osoba1, osoba2):
                print(f"{os1} kupuje prezent {os2}")
    break
print(osoba2)