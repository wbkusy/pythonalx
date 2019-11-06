import turtle

print(help(turtle))
turtle.speed(2)
#for i in range(360):
   # turtle.right(1) # skręca w prawo o 45 stopni
    #turtle.forward(1) # idzie do przodu ileś kroków

#for i in range(4):
   # turtle.right(90) # skręca w prawo o 45 stopni
    #turtle.forward(50) # idzie do przodu ileś kroków

#for i in range(5):
    #turtle.right(360/5) # skręca w prawo o 45 stopni
    #turtle.forward(50) # idzie do przodu ileś kroków
#for i in range(6):
    #turtle.right(60) # skręca w prawo o 45 stopni
    #turtle.forward(50) # idzie do przodu ileś kroków
#for i in range(7):
    #turtle.right(360/7) # skręca w prawo o 45 stopni
    #turtle.forward(50) # idzie do przodu ileś kroków



#for j in range(35):
    #for i in range(j+3):
        #turtle.right(360/(j+3))  # skręca w prawo o 45 stopni
        #turtle.forward(25)  # idzie do przodu ileś kroków

# setheading wskazuje kierunki w zależności o podanego kąta np 0 to east a 180 to west
turtle.speed(40)
def pusty_kwadrat(x):
    for i in range(4):
        turtle.forward(x)
        turtle.right(90)

def linijka_lewo(x):
    turtle.right(90)
    turtle.forward(2 * x)
    turtle.right(90)

def linijka_prawo(x):
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
def pelny_kwadrat(x):
    for i in range(4):
        turtle.forward(x)
        turtle.right(90)

    for j in range(x):
        turtle.right(90)
        turtle.forward(x)
        turtle.left(90)
        turtle.forward(1)
        turtle.left(90)
        turtle.forward(x)
        turtle.right(90)
x=30
for k in range(3):
    for i in range(3):
        print(pusty_kwadrat(x))
        turtle.forward(x)
        print(pelny_kwadrat(x))
    linijka_lewo(x)
    for i in range(3):
        print(pusty_kwadrat(x))
        turtle.forward(x)
        print(pelny_kwadrat(x))
    turtle.left(180)

turtle.done()