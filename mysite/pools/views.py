from django.shortcuts import render
from django.http import HttpResponse

from pools.models import Question


def funkcja_widoku(request):
    html = """<!doctype html>
    <html>
    <head></head>
    <body>
    Hello ALX!
    </body>
    </html>"""
    return HttpResponse(html)


def hello_name(request, name):
    html = f"""<!doctype html>
       <html>
       <head></head>
       <body>
       Hello {name}!
       </body>
       </html>"""
    return HttpResponse(html)

# Stwórz kalkulator

def operacje(request, op, a, b):
    if op == "sum":
        return HttpResponse(int(a)+int(b))
    elif op == "dif":
        return HttpResponse(int(a)-int(b))
    elif op == "multi":
        return HttpResponse(int(a)*int(b))
    elif op == "div" and int(b) != 0:
        return HttpResponse(int(a)/int(b))


def Question_views(request):
    pass
    #q1 = Question.objects.all()
    #text = ""
    #for q in q1:
    #    text +=
    #<br>.join(q1)


def index(request):
    return HttpResponse("Hello world! That's pools index")

# funkcja widok szczegółów
# np question/1 djangoproject.com/en/3.0/intro/tutorial03/
# python principles.com -> challanges
