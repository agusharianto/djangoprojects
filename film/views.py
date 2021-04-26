from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
	posts = Post.objects.all()
	categorys = Post.objects.values('category').distinct()
	context = {
		'title':'Film Terbaru',
		'categorys':categorys,
		'posts':posts,
	}
	return render(request, 'film/index.html', context)

def detailPost(request, slugInput):
	posts = Post.objects.get(slug=slugInput)
	categorys = Post.objects.values('category').distinct()
	context = {
		'title':'Film Terbaru',
		'categorys':categorys,
		'posts':posts,
	}
	return render(request, 'film/detail_post.html', context)

def categoryPost(request, categoryInput):
	posts = Post.objects.filter(category=categoryInput)
	categorys = Post.objects.values('category').distinct()
	context = {
		'title':'Category Film',
		'posts':posts,
		'categorys':categorys,
	}
	return render(request,'film/category_post.html', context)