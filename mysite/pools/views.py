from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

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


def question_list(request):
    lista = Question.objects.all()
    return render(
        request,
        "list.html",
        {"questions": lista}
    )


def question_details(request, id):
    quest = Question.objects.get(pk=id)
    return render(
        request,
        "details.html",
        {"question": quest}
    )


def index(request):
    return HttpResponse("Hello world! That's pools index")


def vote(request, id):
    question = Question.object.get(pk=id)
    choice_id = request.POST.get("choice")
    if choice_id:
        choice = question.choices.get(id=choice_id)
        choice.votes += 1
        choice.save()
    else:
        return render(request, "details.html", {"question": question,
                                                "error": "nie wybrales odpowiedzi"})
    print("odbylo sie glosowanie")
    return HttpResponseRedirect(reverse("pools:list"))
# funkcja widok szczegółów
# np question/1 djangoproject.com/en/3.0/intro/tutorial03/
# python principles.com -> challanges
