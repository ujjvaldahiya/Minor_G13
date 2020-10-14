from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Bmi(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	weight = models.FloatField(null=True)
	height = models.FloatField(null=True)
	bmi = models.FloatField(null=True)
	date = models.DateField(auto_now_add=True, null=True)

	def __str__(self):
		return self.user.username
