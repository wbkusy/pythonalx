a= [1, 2, 3]
if 1 in a:
    print("jest")
    print(("OK"))
else:
    print("nie znalazłem")

# != oznacza znak różności


x=int(input("podaj x: "))
y=int(input("podaj y: "))
if x>=90 and x <=100:
    if y>=0 and y<=10:
        print("jeteś w dolnym prawym rogu")
    elif y>=90 and y<=100:
        print("jesteś w prawym górnym rogu")
elif   x>=0 and x <=10:
    if y>=0 and y<=10:
        print("jeteś w dolnym lewym rogu")
    elif y>=90 and y<=100:
        print("jesteś w dgórnym lewym rogu")
elif y>10 and y<90 and x>10 and x<90:
    print("jesteś w środku")
else:
    print("jesteś poza polem")
