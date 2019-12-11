# Funkcje anonimowe


#x = lambda a, b: a * b

#print(x(10, 6))


#def fun_sort(x):
 #   return x[1]


#lista = [('jabłko', 2.99), ('banan', 4.99), ('winogrona', 7.99)]
#print(sorted(lista, key=lambda x: x[1]))

# Napisz funkcję która z zadanej listy liczb wybierze elementy określone przez funkcję kluczy
# lista= [1, 2, 3, 4, 5, 6]
# wybierz(lista, key = lambda x: x%2 == 0)
# [2, 4, 6]
# wybierz(lista, key = lambda x: x > 5)
# [6]

a = [1, 2, 3, 4, 5, 6, 7]


#def wybierz(lista, c):

    #return sorted(lista, c=lambda x: x % 2 == 0)


#print(wybierz(a, c=lambda x: x % 2 == 0))


def wybierz(lista, funkcja):
    wynik=[]
    for el in lista:
        if funkcja(el) is True:
            wynik.append(el)
    return wynik


print(wybierz(a, lambda x: x%3 ==0))


def wieksze_niz_4(x):
    return x>4

