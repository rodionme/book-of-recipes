from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import Recipe, Ingredient, Cuisine


def index(request):
    return render(request, 'recipes/index.html')


class RecipesView(generic.ListView):
    template_name = 'recipes/recipes.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipe.objects.all()


class RecipeView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/recipe.html'


class RecipeUpdate(generic.UpdateView):
    model = Recipe
    fields = ['name', 'cuisine', 'description', 'ingredients']
    template_name = 'recipes/edit-recipe.html'

    def get_success_url(self):
        return reverse('recipe', args=(self.object.id,))


class IngredientsView(generic.ListView):
    template_name = 'recipes/ingredients.html'
    context_object_name = 'ingredients'

    def get_queryset(self):
        return Ingredient.objects.all()


class IngredientView(generic.DetailView):
    model = Ingredient
    template_name = 'recipes/ingredient.html'


class IngredientUpdate(generic.UpdateView):
    model = Ingredient
    fields = ['name']
    template_name = 'recipes/edit-ingredient.html'

    def get_success_url(self):
        return reverse('ingredient', args=(self.object.id,))


class CuisinesView(generic.ListView):
    template_name = 'recipes/cuisines.html'
    context_object_name = 'cuisines'

    def get_queryset(self):
        return Cuisine.objects.all()


class CuisineView(generic.DetailView):
    model = Cuisine
    template_name = 'recipes/cuisine.html'


class CuisineUpdate(generic.UpdateView):
    model = Cuisine
    fields = ['name']
    template_name = 'recipes/edit-cuisine.html'

    def get_success_url(self):
        return reverse('cuisine', args=(self.object.id,))
