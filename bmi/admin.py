from django.contrib import admin
from .models import Bmi

# Register your models here.
class BmiAdmin(admin.ModelAdmin):
	list_display = ('user', 'bmi', 'date')

admin.site.register(Bmi, BmiAdmin)