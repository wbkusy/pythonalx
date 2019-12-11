class Animal:

    def __init__(self, name, ):
        self.energy = 100
        self.name = name

    @property
    def is_alive(self):
        return self.energy > 0

    def move(self, distance):
        self.energy -= 0.1 * distance
        if self.is_alive:
            return distance
        else:
            return self.is_alive

    def eat(self, calories):
        self.energy +=0.2 * calories


class Dog(Animal):

    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def bark(self):
        print("How How")
        self.energy -= 0.01



a= Animal("Zenek")
print(a.move(50))
print(a.move(5000))
azor = Dog("Azor", "Owczarek Niemiecki")
print(azor.move(100))
azor.bark()
#a.bark()
print(azor.energy, azor.species)

