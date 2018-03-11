from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', views.recipes, name='recipes'),
    path('recipes/<int:recipe_id>', views.recipe, name='recipe'),
    path('ingredients/', views.ingredients, name='ingredients'),
    path('ingredients/<int:ingredient_id>', views.ingredient, name='ingredient'),
]
