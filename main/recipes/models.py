from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    # type

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    # image(s?)
    # cousine

    def __str__(self):
        return self.name