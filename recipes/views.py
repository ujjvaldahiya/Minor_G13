from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .search_recipe_byname import search_recipe_byname as name
from .search_recipe_byingridients import search_recipe as ingredients
from .find_available import search_available
from .models import Recipe,RecipeHistory
from django.views.generic import DetailView
from .RecommendationSystemRecipe import find_recommendations
from .detection import pred
import PIL.Image as Image
import base64

# Create your views here.
def home(request):
	context = {}
	if request.method=='POST':
		recipes_ingredients = request.POST.get("recipes-ingredients")
		recipes_name = request.POST.get("recipes-name")
		check_img = request.POST.get("check-img")
		if recipes_ingredients or check_img=="on":
			available = []

			if check_img == "on":
				files = request.FILES.getlist('myfiles')
				for f in files:
					with open("C:\\Users\\Ujjval Dahiya\\Desktop\\minor\\media\\temp_pics\\image.jpg", "wb") as img:
						img.write(f.read())
					available.append(pred())		

			ing = search_available(recipes_ingredients)
			available.extend(ing)

			results = ingredients(available)
			context['results'] = results
			context['case'] = 1
			context['available'] = available

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
