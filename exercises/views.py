from django.shortcuts import get_object_or_404, render
from .RecommendationSystemExercise import find_recommendations
from .search_exer import search_exer as searchexer
from .search_exer_byname import search_exer_byname as searchexerbyname
from .models import Exercise
from django.views.generic import DetailView

# Create your views here.
def home(request):
	context = {}
	if request.method=='POST':
		exercise_equipment = request.POST.get("exercise-equipment")
		exercise_name = request.POST.get("exercise-name")
		if exercise_equipment:
			beg = request.POST.get("beginner")
			inter = request.POST.get("intermediate")
			adv = request.POST.get("advanced")
			beginner = False
			intermediate = False
			advanced = False
			if beg=='on':
				beginner = True
			if inter=='on':
				intermediate = True
			if adv=='on':
				advanced = True
			 
			results = searchexer(exercise_equipment, beginner, intermediate, advanced)
			context['results'] = results
			context['case'] = 1

		if exercise_name:
			results,recommendations = searchexerbyname(exercise_name)
			context['results'] = results
			context['recommendations'] = recommendations
			context['case'] = 2
 
	return render(request, 'exercises/home.html', context)

class ExerciseDetailView(DetailView):
	model = Exercise
	template_name = "exercise_detail.html"

	def get(self, request, key):
		name = get_object_or_404(Exercise, pk = key)
		context = {}
		exercise_name = name.name
		results,recommendations = searchexerbyname(exercise_name)
		context['results'] = results
		context['recommendations'] = recommendations
		print(context)
		return render(request, 'exercises/exercise_detail.html', context)
