# Napisz funkcję która wymnoży przez siebie elementy podane w liście wejściowej

l=[1, 14, 10]

def pomnoz(lista):
    a=1
    for i in lista:
        a=a*i
    return a

def iloczyn(start, *args):
    wynik = start
    for nr, arg in enumerate(args, 1):
        # print(f"Pozycja {nr} = {arg}")
        wynik = wynik * arg
    return wynik

print(iloczyn(1, 2, 3, 6))
print(pomnoz(l))


# napisz funkcje która zwróci liczby z podanego napisu


def tylko_liczby(x):
    wynik=[]
    for i in range(len(x)):
        if x[i].isdecimal() is True:
            wynik.append(int(x[i]))
    return wynik


print(tylko_liczby("zad149n92l59"))


# w domu ogarnąć liczby a nie tylko cyfry np v230ty76 odda [230, 76]