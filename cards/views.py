from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from .models import *


menu = [{"title": "Главная", "url_name": "home"},
        {"title": "О сайте", "url_name": "about"},
        {"title": "Начать занятие", "url_name": "start_lesson"},
        {"title": "Обратная связь", "url_name": "contact"},
        {"title": "Войти", "url_name": "login"}
]


def index(request):
    cats = Category.objects.filter(user=request.user)

    context = {
        'cats': cats,
        'title': 'Главная страница',
        'menu': menu
    }
    return render(request, "cards/index.html", context=context)


def show_category(request, cat_id):
    words = Card.objects.filter(category=cat_id)
    cats = Category.objects.filter(user=request.user)

    context = {
        'cats': cats,
        'cards': words,
        'title': 'Отобажение слов из выбранного списка',
        'menu': menu
    }
    return render(request, "cards/show_cards.html", context=context)


def show_card(request, card_slug):
    card = get_object_or_404(Card, slug=card_slug)

    context = {
        'card': card,
        'menu': menu,
        'title': card.title_native_language,
    }
    return render(request, 'cards/card_info.html', context=context)


def about(request):
    return render(request, "cards/about.html", {'title': 'О сайте', 'menu': menu})


def start_lesson(request):
    return HttpResponse('Запуск уроков')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
