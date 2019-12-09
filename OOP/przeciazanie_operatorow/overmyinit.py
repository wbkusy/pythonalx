
class MyInt:
    def __init__(self, repr: str):
        self.repr = repr
        self.I = int(self.repr)

    def __add__(self, other):
        if isinstance(other, int):
            return MyInt(str(other + self.I))
        return MyInt(str(self.I + other.I))

    def __eq__(self, other):
        return self.I == other.I

    def __sub__(self, other):
        return MyInt(str(self.I - other.I))

    def __str__(self):
        return f"<MyInt: {self.repr}>"


n1 = MyInt("10")
n2 = MyInt("12")
print(n1 - n2)
print(n1 + n2)
assert n1 + n2 == MyInt("22")
assert n1 - n2 == MyInt("-2")