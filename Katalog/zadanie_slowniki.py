

# marchgew: 2.35, zimeniaki: 2.2, cebula: 1.8, ogorki: 4.0

# co chcesz kupić? marchew
# Ile chcesz kupić [marchew]? 3
# Za [marchew] płacisz 7.05 PLN

"""
asortyment:
 marchgew: 2.35, zimeniaki: 2.2, cebula: 1.8, ogorki: 4.0
"""

cennik={"marchew": 2.35, "ziemniaki": 2.2, "cebula": 1.8, "ogorki": 4.0}
magazyn={"marchew_ilosc": 100, "ziemniaki_ilosc": 200, "cebula_ilosc": 150, "ogorki_ilosc": 50}
#print(help(magazyn.update))
z=True
s=0
while z:
    print("co chcesz kupić?")
    x = input()
    if x in cennik:
        print("ile?")
        c = int(input())
        while True:
            if c > int(magazyn.get(x+"_ilosc")):
                print("nie ma tyle towaru, mamy tylko", magazyn.get(x+"_ilosc"), "podaj ilość:")
                c=int(input())
            else: break
        g=float(cennik.get(x))
        s = s+c*g
        magazyn[x+"_ilosc"]=magazyn[x+"_ilosc"]-c
        print("coś jeszcze? (tak/nie)")
        y=input()
        if y == "tak":
            z=True
        else:
            print("cena do zapłaty: ", s)
            z = False
    elif x == "dodaj":
        q = input("produkt", )
        p = input("cena", )
    else:
        print("nie ma takiego towaru")




def update_magazynu(x, c):
    magazyn[x + "_ilosc"] = magazyn[x + "_ilosc"] - c

def czy_jest_w_magazynie(x, c):
    c = int(input())
    while True:
        if c > int(magazyn.get(x + "_ilosc")):
            print("nie ma tyle towaru, mamy tylko", magazyn.get(x + "_ilosc"), "podaj ilość:")
            c = int(input())
        else:
            break











