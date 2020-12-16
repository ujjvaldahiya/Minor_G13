from django.shortcuts import render,get_object_or_404
from .search_recipe_byname import search_recipe_byname as name
from .search_recipe_byingridients import search_recipe as ingredients
from .models import Recipe,RecipeHistory
from django.views.generic import DetailView
from .RecommendationSystemRecipe import find_recommendations

# Create your views here.
def home(request):
	context = {}
	if request.method=='POST':
		recipes_ingredients = request.POST.get("recipes-ingredients")
		recipes_name = request.POST.get("recipes-name")
		if recipes_ingredients:
			results =ingredients(recipes_ingredients)
			context['results'] = results
			context['case'] = 1
			images = []
			for file in request.FILES['myfiles']:
				images.append(file)

		elif recipes_name:
			results,recommendations = name(recipes_name)
			context['results'] = results
			context['recommendations'] = recommendations
			context['case'] = 2

	return render(request, 'recipes/home.html', context)

class RecipeDetailView(DetailView):
	model = Recipe
	template_name = "recipe_detail.html"

	def get(self, request, key):
		recipe = get_object_or_404(Recipe, pk = key)
		RecipeHistory.objects.create(user = request.user, recipe_id = recipe.recipe_id)
		history_obj = RecipeHistory.objects.filter(user_id = request.user.id).order_by('-id')
		
		history = []
		for i in history_obj:
			history.append(str(i.recipe_id))
		if len(history)>=4:
			history = history[:4]
		else:
			history = history
		history.append(str(recipe.recipe_id))

		context = {}
		recommendations = find_recommendations(history)
		context['results'] = recipe
		context['recommendations'] = recommendations
		return render(request, 'recipes/recipe_detail.html', context)
