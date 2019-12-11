def nazwa_funkcji():
    # to jest ciało funkcji, blok instrukcji
    print("Heloo world!")


nazwa_funkcji()
# wywołanie

print(list(range(10)))


def allup(x):
    return x.upper()


z = allup(input("podaj słowow: ", ))
print(z)


def do_potegi(podstawa, wykladnik):
    return podstawa ** wykladnik


# użycie:

wynik = do_potegi(2, 12)
wynik2 = do_potegi(5, 5)
def uniqe_letters(text):
    u_letters=set(text)
    u_letters="".join(u_letters)
    return u_letters, len(text)
dane=uniqe_letters("abc d")
print(dane)

print("litery ", dane[0])


