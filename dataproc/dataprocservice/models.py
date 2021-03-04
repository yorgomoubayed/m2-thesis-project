from django.db import models
from django.utils.text import slugify
from django.conf import settings

class Construct(models.Model):
	title 				= models.CharField(max_length=50, null=False, blank=True)
	created_at	 		= models.DateTimeField(auto_now_add=True, verbose_name="created at")
	updated_at	 		= models.DateTimeField(auto_now=True, verbose_name="updated at")
	slug 				= models.SlugField(blank=True, unique=True, default=uuid.uuid1)

	def __str__(self):
		return self.title