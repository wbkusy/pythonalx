lista = [1, 0, 10, "a"]
# noqa <-- zmusza do ignorowania danej linii
for i in lista:
    try:
        print(10 / i)
    except ZeroDivisionError:
        print("dzielisz przez 0")
    except TypeError:
        print("dzielisz przez coś co nie jest liczbą")
    except NameError:
        print("nie zdefiniowana zmienna")
    finally:
        print("wykonałem się")
