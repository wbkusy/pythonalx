# Zapytaj użytkownika o 10 liczb i wypisz ich średnią, akorzystaj z pętli for oraz funkcji range
Z=list(range(10))
print(dir(Z))



s=0
for i in range(10):
     i=int(input("podaj liczbę: "))
     s=s+i
print(s)
print(s/10)


