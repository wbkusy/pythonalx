class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_vectors(self, other):
        return Vector((int(self.x) + int(other.x)), (int(self.y) + int(other.y)))

    def __add__(self, other):
        return Vector(int((self.x + other.x)), int((self.y + other.y)))

    def __sub__(self, other):
        return Vector(int((other.x - self.x)), int((other.y - self.y)))


vector1 = Vector(0, 0)
vector2 = Vector(2, 3)
vector3 = vector2 + vector1
vector4 = vector2 - vector1
print(vector3.x, vector3.y)
print(vector4.x, vector4.y)
#assert (vector1 + vector2) == Vector(3, 5)
