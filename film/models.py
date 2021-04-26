from django.db import models
from django.utils.text import slugify


# Create your models here.
class Post(models.Model):
	headline = models.CharField(max_length=100)
	body = models.TextField()
	category = models.CharField(max_length=50, default='film favorit')
	publish = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)
	image = models.ImageField(blank=True, upload_to="image/")
	slug = models.SlugField(blank=True, editable=False)

	def save(self):
		self.slug = slugify(self.headline)
		super(Post, self).save()

	def __str__(self):
		return '{}.{}'.format(self.id, self.headline)