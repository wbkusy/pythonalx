napis = "Ala ma kota"

for znak in napis:
    znak = znak.upper()
    print(znak)

print("wartość na końcu pętli", znak)
elementy = (1, 'a', 2, 'c')

for element in elementy:
    print(element)
lista = [4, 12, 11, 1]

for l in lista:
    print(l)

slownik = {1: "a", "Ala": "kot", "Albert": "Einstein"}

for k in slownik.items():
    print(k)

zbior = {1, 2, 3, "a"}

for z in zbior:
    print(z)



liczby=[1,2,3,4,5,0,12,13,16,76]
for liczba in liczby:
    if liczba==0:
        break
    print(10/liczba)
else:
    print("wykonałem się")
print("jestem po pętli")

for liczba in liczby:
    if liczba==0:
        continue
    print(10/liczba)
else:
    print("wykonałem się")
print("jestem po pętli")


print(range(10))
print(list(range(10)))

for i in range(5):
    print(i, end="")
print()
print(1,  2,  3,  4, sep="-" )