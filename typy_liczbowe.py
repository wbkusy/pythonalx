# w pythonie mamy:
# liczby całkowite - integer
print(type(10))
print(int())
print(int("10"))
print(int("10", base=3))
print(int(2.7))
# liczba zmienno przecinkowa float
print(float())
print(float(1/3))
print(0.1 + 0.1 + 0.1)
print(0.1 + 0.1 + 0.1 == 0.3)
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1") == Decimal("0.3"))

# liczby naukowe
print(1e12)

# liczby zespolonne complex
print(complex())
print(10 +11j)

# wartości boolwskie bool
print(bool())

print(10+True)

# Prześledzić działanie operatorów logicznych or and not
print(True and False)

