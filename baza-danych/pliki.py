
# Powtórka z obsługi plików

fd = open("dane.txt", "rt")
for index, line in enumerate(fd, 1):
    print("krok", index, "i", line, end="")
fd.close()
print()
with open("dane.txt", "rt") as fd:
    for index, line in enumerate(fd, 1):
        print("krok", index, "i", line, end="")

print("czy plik zamknięty:", fd.closed)
