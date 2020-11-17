from django.shortcuts import render

# Create your views here.
def home(request):
	"""images = request.FILES['name'].read()
	print(type(images))
	print(images)"""
	return render(request, 'recipes/home.html')
