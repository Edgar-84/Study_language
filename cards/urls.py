from django.urls import path

from .views import *

urlpatterns = [
    path('', CardsHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('card_info/<slug:card_slug>', ShowCard.as_view(), name='card'),
    path('start_lesson/', start_lesson, name='start_lesson'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('category/<slug:cat_slug>/', ShowCategory.as_view(), name='category'),
    path('addcard/<slug:cat_id>/', AddCard.as_view(), name='add_card'),
    path('addcategory/', AddCategory.as_view(), name='add_category'),
]
