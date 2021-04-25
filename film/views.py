from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'title':'Film Terbaru'
	}
	return render(request, 'film/index.html', context)