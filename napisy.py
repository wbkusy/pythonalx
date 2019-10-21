#
# Typ danych: napisy (albo string)
#
napis1 = "Ala ma kota"
napis2 = 'Ala ma kota'
napis3 = 'a to jest "cudzysłów" '
napis4 = "a to jest \"cudzysłów\" "
napis5 = "znaki specjalne \t \n \r "

dlugosc = len(napis1)
print("Długość zmiennej napis to ",dlugosc,"znaków")
# wiek = input("podaj wiek:")
# print("twój wiek to: ",wiek.strip())

s = "Ruda tańczy jak szalona"
print(s.capitalize()) # kapitalki
print(s.upper())      # góra
print(s.lower())      # dół
print(s.title())      # formatowanie jako tytuł
print(s.swapcase())   # duże w małe, małe w duże
print(s.center(100))  # centrowanie
print(s.replace("R","D")) # zamina znaków
print("czy liczba:",s.isdecimal()) # sprawdzenie czy string jest liczbą

litera = s[3] # pobierz czwartą literę napisu
print("4-ta litera:", s[3])
print("litera przedostatnia", s[-2])

