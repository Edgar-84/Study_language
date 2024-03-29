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
    path('show_menu/', show_menu_lesson_view, name='show_menu'),
    path('show_menu/select_category/', ShowSelectCategoryView.as_view(), name='select_category_lesson'),
    path('show_menu/review_cards_language/<int:pk>/', select_language_review_lesson, name='select_language_review'),
    path('first_lesson/<int:cat_pk>/<int:type_pk>/', FirstLessonView.as_view(), name='first_lesson'),
    path('uploads/form/<int:cat_id>/', model_form_upload, name='model_form_upload'),
]
