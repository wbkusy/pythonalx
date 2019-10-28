# int, str, complex, float, list, tuple,
# dict {}
 #print(dict())
x=dict()
print(type(x))
pol_ang={
    # "klucz": "wartość"
    "klucz": "key",
    "wartość": "value",
    "pies": "dog"
}
print(pol_ang)
print(pol_ang["pies"])

if "dog" in pol_ang :
    print(pol_ang["dog"])


print(dir(pol_ang))

print(pol_ang.get("dog", "Brak takiego hasła"))
print(pol_ang.get("pies", "Brak takiego hasła"))

pol_ang['kot']="cat"
print(pol_ang)
print({1:"a", 2.1:"b"})
print({(1, 2): "pierwsza"})
#print({[1, 2]: "pierwsza"}) to się nie uda bo lista nie jest hassowalna
# kluczem mogą być listy, listy tuple, napisy