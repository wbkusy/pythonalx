stopnie = ["szeregowy", "plutonowy", "sierżant", "podpułkownik", "pułkownik", "major"]



class Soldier:
    def __init__(self, rank):
        self.rank = rank

    def greater(self, other):
        return stopnie.index(self.rank) > stopnie.index(other.rank)

    def __gt__(self, other):
        return self.greater(other)


s1 = Soldier('szeregowy')
s2 = Soldier('major')

print(s1.greater(s2)) # False bo ma większy stopień
print(s2.greater(s1)) # True

print(s1 < s2)

# __gt__ >