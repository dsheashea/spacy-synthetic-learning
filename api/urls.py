from django.urls import path

from . import views

urlpatterns = [
    path('health', views.health, name='health'),
    path('check-spacy', views.check_spacy, name='check-spacy')
]