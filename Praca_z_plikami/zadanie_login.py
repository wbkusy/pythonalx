import sys

# input_file = sys.argv[1]
input_file = "logs.txt"

with open("dane/" + input_file) as in_file:
    data = in_file.read().splitlines()
loginy = []
logouty = []

time_counted = []
time_counted2 = []
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
r = 0
s=0
times = []
times2 = []
for i in range(1, 10):
    for j in range(0, len(loginy), 2):
        if loginy[j] == i:
            r = r + loginy[j + 1]
    for m in range(0, len(logouty), 2):
        if logouty[m] == i:
            s = s + logouty[m + 1]
    times.append(r)
    times2.append(s)
print(times)
print(times2)
hgw=[]
for y in range(0, 9):
    h=times2[y]-times[y]
    hgw.append(h)

print(hgw)
#print(loginy)
#print(logouty)
#hgw = dict()
#for d in range(0, len(loginy), 2):
    #hgw = {loginy[d]: loginy[d + 1]}
  #  time_counted.append(hgw)
#print(time_counted)
#hgw = dict()
#for u in range(0, len(logouty), 2):
  #  hgw = {logouty[u]: logouty[u + 1]}
 #   time_counted2.append(hgw)
#print(time_counted2)
