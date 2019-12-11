# Lososwanie

import random
print(dir(random))
print(help(random.randint))

print(random.randint(1, 5))

x1=random.randint(1,10)
y1=random.randint(1,10)

x2=random.randint(1,10)
y2=random.randint(1,10)

print("położenie skarbu", x2, y2)
print("położenie gracza", x1, y1)
print(abs(100))
print(abs(-100))
odleglosc=abs(x2-x1)+abs(y2-y1)
print(odleglosc)

x=1
warunek=x>7

while x>7:
    print("jestem w pętli")

x=10
while x>0:
    print(x)
    x=x-1

while True:
    intrukcaj=input("wciśnij literkę k aby zakończyć: ")
    if intrukcaj=='k':
        break
