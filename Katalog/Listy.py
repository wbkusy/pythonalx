my_list = [1, "a", "ala", "kot, 121"]
print(my_list)
print(my_list[0])

my_list2 = [1, 2, 3, my_list]
print(my_list2[3][1])
print(dir(my_list2))
my_list.append(10) # doda do listy
print(my_list)
my_list.pop()
print(my_list)
print(my_list.pop()) # usunie z listy
print(my_list.index("a")) # numer pozycji szkuanej w liście
print(my_list.count("a")) # ilośc szukanych w liście

a=[1, 2, 3]
b=[4, 5, a]

print(a)
print(b)

a.append(9)
print(b)
c=a.copy()[2]
a.append(c)
print(a)
b.reverse()
print(b)

x=(1, 2, 3)
print(dir(x))
print(x[0])
y=(4, 5, 6)
x=x+y
print(x.index(2))
print(1 in x)
print("y")

