from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipesView.as_view(), name='index'),

    path('recipes/', views.RecipesView.as_view(), name='recipes'),
    path('recipes/<int:pk>/', views.RecipeView.as_view(), name='recipe'),
    path('recipes/<int:pk>/edit', views.RecipeUpdate.as_view(), name='edit_recipe'),

    path('ingredients/', views.IngredientsView.as_view(), name='ingredients'),
    path('ingredients/<int:pk>/', views.IngredientView.as_view(), name='ingredient'),
    path('ingredients/<int:pk>/edit', views.IngredientUpdate.as_view(), name='edit_ingredient'),

    path('cuisines/', views.CuisinesView.as_view(), name='cuisines'),
    path('cuisines/<int:pk>/', views.CuisineView.as_view(), name='cuisine'),
    path('cuisines/<int:pk>/edit', views.CuisineUpdate.as_view(), name='edit_cuisine'),
]
