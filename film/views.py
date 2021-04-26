from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
	posts = Post.objects.all()
	print(posts)
	context = {
		'title':'Film Terbaru',
		'posts':posts,
	}
	return render(request, 'film/index.html', context)

def detailPost(request, slugInput):
	posts = Post.objects.get(slug=slugInput)
	context = {
		'title':'Film Terbaru',
		'posts':posts,
	}
	return render(request, 'film/detail_post.html', context)