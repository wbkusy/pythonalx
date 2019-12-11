class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_vectors(self, other):
        return Vector((int(self.x) + int(other.x)), (int(self.y) + int(other.y)))

    def __add__(self, other):
        return Vector(int((self.x + other.x)), int((self.y + other.y)))


vector1 = Vector(1, 2)
vector2 = Vector(2, 3)
print(Vector.add_vectors(vector1, vector2))
#assert (vector1 + vector2) == Vector(3, 5)
