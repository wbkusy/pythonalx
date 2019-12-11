a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
b=[-2,3,-5,11,99,8, 100, 101, 134]

def przytnij(lista, start, stop):
    wynik = []
    dodawac=False
    for i in lista:
        if start(i) is True and stop(i) is False:
            #wynik.append(i)
            dodawac=True
        if dodawac:
            wynik.append(i)
            if stop(i) is True:
                break
    return wynik


print(przytnij(b, lambda x: x > 1, lambda y: y == 101))
