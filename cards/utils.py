from .models import *

menu = [{"title": "Главная", "url_name": "home"},
        {"title": "О сайте", "url_name": "about"},
        {"title": "Начать занятие", "url_name": "start_lesson"},
        {"title": "Обратная связь", "url_name": "contact"},
        {"title": "Войти", "url_name": "login"}
        ]


class DataMixin:
     def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.filter(user=self.request.user)
        context['menu'] = menu
        context['cats'] = cats
        return context
