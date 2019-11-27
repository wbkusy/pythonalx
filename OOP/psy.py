# definicja klasy
class Pies:
    def __init__(self, imie, waga):
        self.imie = imie
        self.waga = waga

    def szczekaj(self):
        print(f"{self.imie} szczeka")


azor = Pies("Azor", 10)
rex = Pies("Rex", 25)

rex.szczekaj()


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
