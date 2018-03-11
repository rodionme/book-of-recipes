from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Recipe, Ingredient


def index(request):
    return render(request, 'recipes/index.html')


def recipes(request):
    recipes = Recipe.objects.all()

    return render(request, 'recipes/recipes.html', {'recipes': recipes})


def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredients = get_list_or_404(Ingredient, recipe__id=recipe.id)

    return render(request, 'recipes/recipe.html', {'recipe': recipe, 'ingredients': ingredients})


def ingredients(request):
    ingredients = Ingredient.objects.all()

    return render(request, 'recipes/ingredients.html', {'ingredients': ingredients})


def ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)

    return render(request, 'recipes/ingredient.html', {'ingredient': ingredient})
