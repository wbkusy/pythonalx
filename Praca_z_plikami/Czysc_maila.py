import sys

input_file = sys.argv[1]
output_file = sys.argv[2]


#def czyszczenie_maili(x):
    #y=[]
    #with open("dane/"+x) as f:
       # for i in f:
           # for j in range(0, 9):
           #     if str(i) == str("user-"+str(j)+"@email.com"):
            #        y.append(str(i))
           #     else:
              #      pass
   # return y

#print(czyszczenie_maili("emails.txt"))


try:
    input_file = sys.argv[1]
except IndexError:
    input_file = None
try:
    output_file = sys.argv[1]
except IndexError:
    output_file = None

with open("dane/" + input_file) as in_file:
    data=in_file.read().splitlines()

cleaned_emails = set()
for email in data:
    if email.count("@")==1:
        cleaned_emails.add(email.strip().lower())
cleaned_emails=list(cleaned_emails)
cleaned_emails.sort()
with open("wyniki/"+output_file, "w") as f:
    for email in cleaned_emails:
        f.write(email + "\n")



