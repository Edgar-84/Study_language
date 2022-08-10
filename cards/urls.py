from django.urls import path

from .views import *

urlpatterns = [
    path('', CardsHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('card_info/<int:pk>/edit/', CardUpdateView.as_view(), name='update_card'),
    path('card_info/<int:pk>/delete/', CardDeleteView.as_view(), name='delete_card'),
    path('card_info/<slug:card_slug>', ShowCard.as_view(), name='card'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='update_category'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),
    path('category/<slug:cat_slug>/', ShowCategory.as_view(), name='category'),
    path('addcard/<slug:cat_id>/', AddCard.as_view(), name='add_card'),
    path('addcategory/', AddCategory.as_view(), name='add_category'),
    path('start_lesson/', show_menu_lesson_view, name='start_lesson'),
    path('start_lesson/show_menu_review_cards/', show_menu_review_cards, name='show_menu_review_cards'),
]
