from django import forms
from .models import Post

class addPost(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			'headline',
			'body',
			'category',
			'image',
		]