# funkcja z dowolną liczbą parametrów


# Funkcja mnoży wartości podane do jej środka, możliwe podanie nieznanej liczby parametrów

def iloczyn(start, *args):
    wynik = start
    for nr, arg in enumerate(args, 1):
        # print(f"Pozycja {nr} = {arg}")
        wynik = wynik * arg
        print(f"{nr} {arg}")
    return wynik


print(iloczyn(1, 2, 3, 4, 5))
# iloczyn(1,2)

print(help(enumerate))
