from django.shortcuts import render, redirect
from .models import Post
from .forms import addPost

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

def createPost(request):
	addform = addPost(request.POST)
	if request.method == 'POST':
		if addform.is_valid():
			addform.save()
			return redirect('film:index')
	context = {
		'title':'Add Post',
		'addform':addform,
	}
	return render(request, 'film/add_post.html', context)