from django.urls import reverse
from django.views import generic
from django.db.models import Count
from .models import Recipe, Ingredient, Cuisine


class RecipesView(generic.ListView):
    template_name = 'recipes/recipes.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        recipes = Recipe.objects.all()
        query = self.request.GET.get('q')
        ingredients = self.request.GET.getlist('i')

        if query:
            recipes = recipes.filter(name__contains=query)

        if ingredients:
            recipes = recipes\
                .filter(ingredients__pk__in=ingredients)\
                .annotate(ingredients_count=Count('ingredients'))\
                .order_by('-ingredients_count')

        return recipes

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        context['ingredients'] = Ingredient.objects.all()
        context['selected_ingredients'] = [int(ingredient_id) for ingredient_id in self.request.GET.getlist('i')]

        return context


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
