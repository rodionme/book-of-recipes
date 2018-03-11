from django.shortcuts import render
from .models import Recipe, Ingredient


def index(request):
    return render(request, 'recipes/index.html')


def recipes(request):
    recipes = Recipe.objects.all()

    return render(request, 'recipes/recipes.html', {'recipes': recipes})


def recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)

    return render(request, 'recipes/recipe.html', {'recipe': recipe})


def ingredients(request):
    ingredients = Ingredient.objects.all()

    return render(request, 'recipes/ingredients.html', {'ingredients': ingredients})


def ingredient(request, ingredient_id):
    ingredient = Ingredient.objects.get(id=ingredient_id)

    return render(request, 'recipes/ingredient.html', {'ingredient': ingredient})
