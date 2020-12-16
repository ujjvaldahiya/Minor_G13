from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Exercise(models.Model):
	ID = models.IntegerField(primary_key=True)
	name = models.CharField(max_length = 100)
	body_part = models.CharField(max_length = 200)
	equipments = models.CharField(max_length = 200, null=True)
	difficulty = models.IntegerField()
	procedure = models.TextField(null=True)

	def __str__(self):
		return self.name

class ExerciseHistory(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	exercise_id = models.IntegerField()
	date = models.DateField(auto_now_add=True)
