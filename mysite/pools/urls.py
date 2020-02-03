from django.urls import path
from pools.views import funkcja_widoku, hello_name, operacje, index, question_details, question_list, vote


app_name = "pools"
urlpatterns = [
    path("", index, name="index"),
    path('hello/', funkcja_widoku),
    path('hello/<name>', hello_name),
    path('<op>/<a>/<b>', operacje),
    path('questions/', question_list, name="list"),
    path('questions/<id>', question_details, name="details"),
    path('pytnaie/<id>/vote', vote, name="vote"),
]
