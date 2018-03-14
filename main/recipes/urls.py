from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', views.RecipesView.as_view(), name='recipes'),
    path('recipes/<int:pk>/', views.RecipeView.as_view(), name='recipe'),
    path('recipes/<int:pk>/edit', views.RecipeUpdate.as_view(), name='edit_recipe'),
    path('ingredients/', views.IngredientsView.as_view(), name='ingredients'),
    path('ingredients/<int:pk>/', views.IngredientView.as_view(), name='ingredient'),
    path('ingredients/<int:pk>/edit', views.IngredientUpdate.as_view(), name='edit_ingredient'),
]
