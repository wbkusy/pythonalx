# zdefiniuj funkcje zawierajacych liste lat przestepnych na podstawie zadanego zakresu
# lata_przestepne(1990, 2020)
# [1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
# rok przestepny nie dzieli sie przez 100 ale jest wyjatek ze jak dzieli sie przez 400 to jest przestepny

lata = []



def lata_przestepne(x, y):
    while not x == y:
        if x % 400 == 0:
            lata.append(x)
            x = x + 1
        elif x % 100 == 0:
            pass
        elif x % 4 == 0:
            lata.append(x)
            x = x + 1
        else:
            x = x + 1
    return lata

c=int(input())
z=int(input())
print(lata_przestepne(c, z))


def test_lata_przestepne():
    assert lata_przestepne(2020, 2030) == [2020, 2024, 2028]
