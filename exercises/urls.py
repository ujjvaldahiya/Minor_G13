from django.urls import path
from .views import home,ExerciseDetailView

urlpatterns = [
	path('', home, name='exercises-home'),
	path('exercise/<int:key>/', ExerciseDetailView.as_view(), name='exercises-detail'),
]