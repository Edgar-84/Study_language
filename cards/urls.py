from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='cards'),
    path('about/', about, name='about'),
]
