from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .utils import *


class CardsHome(DataMixin, ListView):
    model = Category
    template_name = "cards/index.html"
    context_object_name = 'cats'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        common_date = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(common_date.items()))

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class ShowCategory(DataMixin, ListView):
    model = Card
    template_name = "cards/show_cards.html"
    context_object_name = "cards"
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        common_date = self.get_user_context(title="Слова из списка",
                                            name=(Category.objects.filter(slug=self.kwargs["cat_slug"]))[0].title)
        return dict(list(context.items()) + list(common_date.items()))

    def get_queryset(self):
        return Card.objects.filter(category__slug=self.kwargs["cat_slug"])


class ShowCard(DataMixin, DetailView):
    model = Card
    template_name = "cards/card_info.html"
    slug_url_kwarg = "card_slug"
    context_object_name = "card"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        common_date = self.get_user_context(title="Карточка")
        return dict(list(context.items()) + list(common_date.items()))


class AddCard(DataMixin, LoginRequiredMixin, CreateView):
    form_class = AddCardForm
    template_name = "cards/addcard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        common_date = self.get_user_context(title="Добавление карточки")
        return dict(list(context.items()) + list(common_date.items()))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'cards/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        common_date = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(common_date.items()))


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
