from django.shortcuts import render
from .search_recipe_byname import search_recipe_byname as name
from .search_recipe_byingridients import search_recipe as ingredients

# Create your views here.
def home(request):
	context = {}
	if request.method=='POST':
		recipes_ingredients = request.POST.get("recipes-ingredients")
		print(recipes_ingredients)
		recipes_name = request.POST.get("recipes-name")
		print(recipes_name)
		if recipes_ingredients:
			results =ingredients(recipes_ingredients)
			context['results'] = results
			context['case'] = 1
			print(results)

		if recipes_name:
			results,recommendations = name(recipes_name)
			context['results'] = results
			context['recommendations'] = recommendations
			context['case'] = 2

	return render(request, 'recipes/home.html', context)
