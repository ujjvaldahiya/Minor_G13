from django.contrib import admin
from .models import Exercise,ExerciseHistory

# Register your models here.
admin.site.register(Exercise)
admin.site.register(ExerciseHistory)