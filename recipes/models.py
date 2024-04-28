# models.py
from django.db import models

class FoodRecipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
