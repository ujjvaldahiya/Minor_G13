from django.urls import path
from .views import home,RecipeDetailView

urlpatterns = [
	path('', home, name='recipes-home'),
	path('recipes/<int:key>/', RecipeDetailView.as_view(), name='recipes-detail'),
]