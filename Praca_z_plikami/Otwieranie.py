

#f = open("napisy2")
#print(f)

#f.close()


# ASCII
# a-z A-Z 0-9
# 7 bit - 128
# unicode
# UTF-8

f = open("napisy2")
for line in f:
    print()

f.close()

f = open("napisy2")
print(f.read())

f.close()



try:
    f = open('napisy2')
except Exception:
    print("wyjątek")
finally:
    f.close()

with open('napisy2', encoding='utf-8') as f:
    for i in f:
        print(i.upper())