from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
	posts = Post.objects.all()
	context = {
		'title':'Film Terbaru',
		'posts':posts,
	}
	return render(request, 'film/index.html', context)