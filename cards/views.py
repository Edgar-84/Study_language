from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *


menu = ["О сайте", "Мои карточки", "Начать занятие", "Обратная связь", "Войти"]


def index(request):
    posts = Category.objects.all()
    return render(request, "cards/index.html", {'posts': posts, 'title': 'Главная страница', 'menu': menu})


def about(request):
    return render(request, "cards/about.html", {'title': 'О сайте', 'menu': menu})


def cards(request, card):
    return HttpResponse(f"<h1>Cards number</h1><p>{card}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
