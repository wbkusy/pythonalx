# Napisz funkcję która zwróci max z 3 podanych liczb
# max_of_three(10, 1, 17)
# 17
# max_of_three(1, 2, 3)
# 3


def ktore_wieksz(b, c):
    if b > c:
        return b
    return c


def max_of_three(x, y, z):
    return ktore_wieksz(x, ktore_wieksz(y, z))


print(max_of_three(311, -2224, 56))
