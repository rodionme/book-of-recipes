from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Ingredient


def create_recipe(name, description, ingredients):
    """
    Create an recipe with the given name, description and list of ingredients
    """
    return Recipe.objects.create(name=name, description=description, ingredients=ingredients)


def create_ingredient(name):
    """
    Create an ingredient with the given name
    """
    return Ingredient.objects.create(name=name)


class RecipesViewTest(TestCase):
    def test_no_recipes(self):
        """
        If no recipes exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('recipes'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No recipes are available.')
        self.assertQuerysetEqual(response.context['recipes'], [])

    def test_recipe(self):
        """
        The recipes page may display recipe
        """
        pass

    def test_two_recipes(self):
        """
        The recipes page may display multiple recipes
        """
        pass


class IngredientsViewTest(TestCase):
    def test_no_ingredients(self):
        """
        If no ingredients exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('ingredients'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No ingredients are available.')
        self.assertQuerysetEqual(response.context['ingredients'], [])

    def test_two_ingredients(self):
        """
        The ingredients page may display multiple ingredients
        """
        create_ingredient(name='Ingredient 1')
        create_ingredient(name='Ingredient 2')
        response = self.client.get(reverse('ingredients'))

        self.assertQuerysetEqual(response.context['ingredients'],
                                 ['<Ingredient: Ingredient 1>', '<Ingredient: Ingredient 2>'], ordered=False)
