from django.forms import ModelForm
from .models import Post, CommentPost

class addPost(ModelForm):
	class Meta:
		model = Post
		fields = '__all__'


class addComment(ModelForm):
	class Meta:
		model = CommentPost
		fields = [
			'comment'
		]