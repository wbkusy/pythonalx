import random

# w zależności od zmiennej DEBUG printuje położenie skarbu
x1 = random.randint(0, 9)
x2 = random.randint(0, 9)
y1 = random.randint(0, 9)
y2 = random.randint(0, 9)

odleglosc_po_wylosowaniu = abs(x2 - x1) + abs(y2 - y1)
z2 = x2
c2 = y2

b1 = x1
n1 = y1
print("""
Witaj!

Twoim zadaniem będzie odnaleźenie skarbu!
Możesz się poruczać wpisując komendy:
w-góra
s-dół
a-lewo
d-prawo

Uważaj! możesz wypaść poza planszę.
po każdym ruchu możesz dostać informację o położeniu!""")
s = 0
while True:
    print("Mapa:")
    for i in range(10):
        print()
        for j in range(10):
            if i == y1 and j == x1:
                print("G", end="  ")
            else:
                print("Y", end="  ")
    print()
    R = random.randint(1, 5)
    if R == 1:
        DEBUG = True
    else:
        DEBUG = False
        if DEBUG:
            print(f"położenie gracza (x={x1}, y={y1})")
            print(f"położenie skarbu (x={x2}, y={y2})")
            print("odległość od skarbu:", abs(x2 - x1) + abs(y2 - y1))

    ruch = input("podaj komendę: ")  # pyta gracza o ruch inputem
    if ruch == 's':  # zmieniamy pozycję gracza - zgodnie z komendą
        y1 = y1 + 1
    elif ruch == 'w':
        y1 = y1 - 1
    elif ruch == 'a':
        x1 = x1 - 1
    elif ruch == 'd':
        x1 = x1 + 1
    else:
        print("nie właściwy klawisz")

    if DEBUG:
        print(f"położenie gracza po ruchu: (x={x1}, y={y1})")
    if not (0 <= x1 <= 9 and 0 <= y1 <= 9):
        print("wypadłeś poza planszę")
        break
    odleglosc_po_ruchu = abs(x2 - x1) + abs(y2 - y1)

    if x1 == z2 and y1 == c2:
        print("wygrałeś")
        print("odleglosc_po_wylosowaniu:", z2, c2)
        break
    elif odleglosc_po_ruchu > odleglosc_po_wylosowaniu:
        print("zimno")
        # print(odleglosc_po_wylosowaniu)
        # print(odleglosc_po_ruchu)
    elif odleglosc_po_ruchu < odleglosc_po_wylosowaniu:
        print("ciepło")
        # print(odleglosc_po_wylosowaniu)
        # print(odleglosc_po_ruchu)
    odleglosc_po_wylosowaniu = odleglosc_po_ruchu
    s = s + 1

    if s > 2 * abs(z2 - b1) + abs(c2 - n1):
        print("wykorzystałeś max liczbę ruchów")
        print(2 * (abs(z2 - b1) + abs(c2 - n1)))
        y1 = random.randint(0, 9)
        y2 = random.randint(0, 9)
        print("zmiana położenia sparbu")
        n1 = y1
        c2 = y2
        s = 0

# Postaraj się zwizualizowac położeneie gracza na planszy (AlA tabliczka mnożenia)
