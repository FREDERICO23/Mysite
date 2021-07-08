from django.db import models
from datetime import datetime


# Create your models here.
class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length=200, default ='DEFAULT VALUE')
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField("Published: ", default = datetime.now())
	tutorial_venue = models.CharField(max_length=200, null = True, blank =False)

	"""docstring for Tutorial"""
	def __str__(self):
		return self.tutorial_title 