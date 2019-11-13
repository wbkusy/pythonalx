

#lista=[-2, 10, 0, 5, 1, 16, 9]

#wybierz_z_przedziału(lista, 5, 10)
#[10, 5, 9]



#lista = [7, 8, 9, 1, 11]
#lista2 = []


#def wybierz_z_przedzialu(x, y, z):
    #for i in x:
        #print(x[i])
        #if y < i < z:
            #lista2.append(lista[i])


    #return


#print(wybierz_z_przedzialu(lista, 5, 10))

lista=[-2, 10, 0, 5, 1, 16, 9]
def wybierz_z_listy(lista, a, b):
    wynik=[]
    for i in lista:
        if i >= a and i <= b:
            wynik.append(i)
    return wynik

def test_wybierz_z_listy_pusta_lita():
    assert wybierz_z_listy([], 10, 20) == []

def test_wybierz_z_przedzialu():
    assert wybierz_z_listy([1,10, 11, 20, 30], 10, 20) == [10, 11, 20]