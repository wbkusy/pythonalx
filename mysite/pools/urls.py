from django.urls import path
from pools.views import funkcja_widoku, hello_name, operacje, index, Question_views

urlpatterns = [
    path('question/', Question_views),
    #path("", index, name="index"),
    path('hello/', funkcja_widoku),
    path('hello/<name>', hello_name),
    path('<op>/<a>/<b>', operacje, name="question-list"),
    path('q/<nr>', Question_views)
]