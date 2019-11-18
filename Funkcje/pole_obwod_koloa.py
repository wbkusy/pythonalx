# napisać funkcję do obliczenia pola i obwodu koła (2 funkcje a potem jedna wspólna)

from math import pi, sin


def oblicz_pole_kola(r):
    return pi*r**2

def oblicz_obwod_kola(r):
    return 2*r*pi

def oblicz_poli_i_obwod_kola(r):
    return oblicz_pole_kola(r), oblicz_obwod_kola(r)


print(oblicz_poli_i_obwod_kola(4))