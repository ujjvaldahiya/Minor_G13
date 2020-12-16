from django.shortcuts import get_object_or_404, render
from .search_exer import search_exer as searchexer
from .search_exer_byname import search_exer_byname as searchexerbyname
from .RecommendationSystemExercise import find_recommendations
from .workout_plans import find_plan
from .models import Exercise,ExerciseHistory
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
		
	context['plans'] = find_plan()
	print(context['plans'])
 
	return render(request, 'exercises/home.html', context)

class ExerciseDetailView(DetailView):
	model = Exercise
	template_name = "exercise_detail.html"

	def get(self, request, key):
		exercise = get_object_or_404(Exercise, pk = key)
		ExerciseHistory.objects.create(user = request.user, exercise_id = exercise.ID)
		history_obj = ExerciseHistory.objects.filter(user_id = request.user.id).order_by('-id')
		
		history = []
		for i in history_obj:
			history.append(str(i.exercise_id))
		if len(history)>=4:
			history = history[:4]
		else:
			history = history
		history.append(str(exercise.ID))

		context = {}
		context['result'] = exercise
		context['recommendations'] = find_recommendations(history)

		return render(request, 'exercises/exercise_detail.html', context)
