# Funkcje anonimowe


x = lambda a,b : a*b

print(x(10, 6))
def fun_sort(x):
    return x[1]


lista=[('jabłko', 2.99), ('banan', 4.99), ('winogrona', 7.99)]
print(sorted(lista, key=lambda x:x[1]))