# zapytaj usera o tekst, zapytaj użytkownika o szerokość, wyświetl tekst, który będzie miał same duże litery
# tekst powinnien być wycentrowany zgodnie z wartością szerokości

x=input("podaj napis: ")
z= int(input("podaj szerokość :"))
x=x.upper()
y="!"
print(f"{y}{x.center(z)}{y}")
