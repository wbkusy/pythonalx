import sys

# input_file = sys.argv[1]


input_file = "logs.txt"
with open("dane/" + input_file) as in_file:
    data = in_file.read().splitlines()




loginy = []
logouty = []
for logi in data:
    y = ""
    if logi.count("LOGIN") == 1:
        for i in range(len(logi)):
            if logi[i].isdecimal() is True:
                y = y + str(logi[i])
            else:
                if y != "":
                    loginy.append(int(y))
                y = ""
        if y != "":
            loginy.append(int(y))
            # print(wynik)
    elif logi.count("LOGOUT") == 1:
        for i in range(len(logi)):
            if logi[i].isdecimal() is True:
                y = y + str(logi[i])
            else:
                if y != "":
                    logouty.append(int(y))
                y = ""
        if y != "":
            logouty.append(int(y))
            # print(wynik)



times = []
times2 = []
for i in range(1, 10):
    r = 0
    s = 0
    for j in range(0, len(loginy), 2):
        if loginy[j] == i:
            r = r + loginy[j + 1]
    for m in range(0, len(logouty), 2):
        if logouty[m] == i:
            s = s + logouty[m + 1]
    times.append(r)
    times2.append(s)
#print(times)
#print(times2)



hgw=[]
for y in range(0, 9):
    h=times2[y]-times[y]
    hgw.append(h)
#print(hgw)
i = 0
for wy in hgw:
    i = i + 1
    print("użytkownik " + str(i) + " był zalogowany przez: " + str(wy))

