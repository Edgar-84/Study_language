from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('card_info/<slug:card_slug>', show_card, name='card'),
    path('start_lesson/', start_lesson, name='start_lesson'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('category/<int:cat_id>/', show_category, name='category'),
]
