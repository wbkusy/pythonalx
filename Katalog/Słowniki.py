# int, str, complex, float, list, tuple,
# dict {}
print(dict())
x = dict()
print(type(x))
pol_ang = {
    # "klucz": "wartość"
    "klucz": "key",
    "wartość": "value",
    "pies": "dog"
}
print(pol_ang)
print(pol_ang["pies"])

if "dog" in pol_ang:
    print(pol_ang["dog"])
else:
    print("nie ma")

print(dir(pol_ang))

print(pol_ang.get("dog", "Brak takiego hasła"))
print(pol_ang.get("pies", "Brak takiego hasła"))

pol_ang['kot'] = "cat"
print(pol_ang)
print({1: "a", 2.1: "b"})
print({(1, 2): "pierwsza"})
# print({[1, 2]: "pierwsza"}) to się nie uda bo lista nie jest hassowalna
# kluczem mogą być listy, listy tuple, napisy

print(pol_ang.values())
print(pol_ang.keys())
print(pol_ang.items())

print(dict(krowa="cow", dom="house"))
print(pol_ang.pop("pies"))
print(pol_ang)
print(pol_ang.popitem())

# set {}
# zbiór, kolekcja unikalnych i nieuporządkowanych wartości
zbior = {1, 2, 3, 4}
print(zbior, type(zbior))
print(dir(zbior))

zbior2 = {1, "a", 2, "b", "c", "z", 3}
print(zbior2)

zbior2.add("a")
print(zbior2)

lista = [1, 2, 3, 1, 1, 1, 4, 2, 2, 1, ]
print(set(lista))

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {1, 2}
print("suma xbiorów: ", A | B, A.union(B))
print("różnica zbiorów ", A - B, A.difference(B))
print("część wspólna, przecięcie", A & B, A.intersection(B))
print("różnica symetryczna", A ^ B, A.symmetric_difference(B))
print("podziel", A.issubset(C))
print("podziel", C.issubset(A))
