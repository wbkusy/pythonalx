osoba1=['a', 'b', 'c', 'd']
osoba2=['a', 'b', 'c', 'd']
lista=[]
import random
y=0
x=True
c=1
while y<=3:
    i=random.randint(0,3)
    j=random.randint(0,3)
    if not i==j:
        os1=osoba1[i]
        os2=osoba2[j]
        for os1, os2 in zip(osoba1, osoba2):
            print(f"{os1} kupuje prezent {os2}")
        y=y+1
        #if not ((os1, os2) or (os2,os1)) in lista:
            #lista.append((os1, os2))

            #for os1 in lista:
               # c=c+1
            #if c>2:
                   # lista.pop()
        #print(os1, os2)
        #print(i, j)
print(lista)