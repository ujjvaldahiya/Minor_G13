from django.contrib import admin
from .models import Recipe,RecipeHistory

# Register your models here.
admin.site.register(Recipe)
admin.site.register(RecipeHistory)