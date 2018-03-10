from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, {'app': {'name': 'Book of Recipes'}}, name='index'),
]
