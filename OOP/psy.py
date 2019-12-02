# definicja klasy
class Pies:

    gatunek = "camis familiaris"
    ile = 0
    def __init__(self, imie, waga):
        self.imie = imie
        self.waga = waga
        Pies.ile += 1


    def szczekaj(self):
        print(f"{self.imie} szczeka")

    @classmethod
    def incr(cls):
        cls.ile += 1


azor = Pies("Azor", 10)
print(Pies.ile)

rex = Pies("Rex", 25)
print(Pies.ile)

rex.szczekaj()

print(azor.gatunek)

Pies.gatunek="Camis Lupus"

print(rex.gatunek)
# Tworzę instancję klasy Pies, jest przypisana do zmienna azor
# azor=Pies()
# rex=Pies()
# print(azor)
# print((isinstance(azor, Pies)))
# print((isinstance(azor, object)))
# print(dir(azor))

# azor=Pies("Azor", 10)
# rex=Pies("Rex", 25)

# azor.waga=10
# print(azor.waga)
# print(azor==rex)
