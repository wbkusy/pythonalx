import re


daty = "\d{2} \w{3} \d{4}"
emaile = "user-\d\d@email\.edu\.pl"
kod_pocztowy = "\d{2}-\d{3}"


with open('input.txt') as f:
    text = f.read()

pattern1 = re.compile(daty)
pattern2 = re.compile(emaile)
pattern3 = re.compile(kod_pocztowy)
match1 = pattern1.findall(text)
match2 = pattern2.findall(text)
match3 = pattern3.findall(text)
print(match1)
print(match2)
print(match3)
