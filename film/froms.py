from django import forms
from .models import Post

class addPost(forms.ModelForms):
	class Meta:
		model = Post
		fields = [
			'headline',
			'body',
			'category',
			'image',
		]