from django.db import models

# Create your models here.
class Blog(models.Model):
	blogTitle = models.CharField(max_length=200)
	datePosted = models.DateField(auto_now=False, auto_now_add=False)
	blogContent = models.TextField()
	
	def __str_(self):
		return self.title