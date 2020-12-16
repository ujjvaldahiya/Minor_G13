from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    necessary_ing = models.CharField(max_length=500)
    major_ing = models.CharField(max_length=500)
    ingredients = models.TextField()
    procedure = models.TextField()
    time = models.IntegerField(null=True)
    servings = models.IntegerField(null=True)

class RecipeHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_id = models.IntegerField()
    date = models.DateField(auto_now_add=True)
