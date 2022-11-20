import random

from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import *
from .utils import *


class CardsHome(LoginRequiredMixin, DataMixin, ListView):
    model = Category
    template_name = "cards/index.html"
    context_object_name = 'cats'
    login_url = reverse_lazy('login')

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
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        common_date = self.get_user_context(title="Слова из списка",
                                            category_object=Category.objects.get(slug=self.kwargs["cat_slug"]))

        return dict(list(context.items()) + list(common_date.items()))

    def get_queryset(self):
        return Card.objects.filter(category__slug=self.kwargs["cat_slug"]).order_by('-time_create')


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
        common_date = self.get_user_context(title="Добавление карточки",
                                            cat_id=int(self.request.path.split('/')[-2]))
        return dict(list(context.items()) + list(common_date.items()))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        kwargs.update({'cat_id': int(self.request.path.split('/')[-2])})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.category = Category.objects.get(id=int(self.request.path.split('/')[-2]))
        print('form valid')
        return super().form_valid(form)


class CardUpdateView(DataMixin, LoginRequiredMixin, UpdateView):
    model = Card
    form_class = EditCardForm
    template_name = "cards/card_edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        common_date = self.get_user_context(title="Редактирование карточки")
        return dict(list(context.items()) + list(common_date.items()))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        kwargs.update({'card_id': int(self.request.path.split('/')[-3])})
        return kwargs


class CardDeleteView(DataMixin, LoginRequiredMixin, DeleteView):
    model = Card
    template_name = 'cards/delete_card.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        common_date = self.get_user_context(title="Удаление карточки",
                                            card_name=Card.objects.get(id=int(self.request.path.split('/')[-3])))
        return dict(list(context.items()) + list(common_date.items()))


class AddCategory(DataMixin, LoginRequiredMixin, CreateView):
    form_class = AddCategoryForm
    template_name = "cards/addcategory.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        common_date = self.get_user_context(title="Создание списка")
        return dict(list(context.items()) + list(common_date.items()))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class CategoryUpdateView(DataMixin, LoginRequiredMixin, UpdateView):
    model = Category
    form_class = AddCategoryForm
    template_name = "cards/update_category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        common_date = self.get_user_context(title="Редактирование карточки")
        return dict(list(context.items()) + list(common_date.items()))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class CategoryDeleteView(DataMixin, LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'cards/delete_category.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        common_date = self.get_user_context(title="Удаление категории",
                                            category_name=Category.objects.get(
                                                id=int(self.request.path.split('/')[-2])))
        return dict(list(context.items()) + list(common_date.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'cards/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        common_date = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(common_date.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = "cards/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        common_date = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(common_date.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class ShowSelectCategoryView(DataMixin, LoginRequiredMixin, ListView):
    model = Category
    template_name = "cards/select_category_lesson.html"
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        common_date = self.get_user_context(title="Выбор списка для занятия")
        return dict(list(context.items()) + list(common_date.items()))

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class FirstLessonView(DataMixin, ListView, LoginRequiredMixin):
    model = Card
    template_name = "cards/first_lesson.html"
    context_object_name = 'cards'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        common_date = self.get_user_context(title='Занятие №1',
                                            type_translate=int(self.request.path.split('/')[-2]))

        return dict(list(context.items()) + list(common_date.items()))

    def get_queryset(self):
        return Card.objects.filter(category_id=int(self.request.path.split('/')[-3])).order_by('?')


def show_menu_lesson_view(request):
    return render(request, "cards/show_menu_lesson.html",
                  {'title': 'Выбор занятия',
                   'menu': menu})


def select_language_review_lesson(request, pk):
    return render(request, "cards/show_menu_review_cards.html",
                  {'title': 'Выбор отображения карточек',
                   'cat_id': int(request.path.split('/')[-2]),
                   'menu': menu})


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'cards/upload_xlsx_file.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')


def about(request):
    return render(request, "cards/about.html", {'title': 'О сайте', 'menu': menu})


def contact(request):
    return HttpResponse('Обратная связь')


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
