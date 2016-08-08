from django.db import models

class Portfolio(models.Model):
	title = models.CharField(max_length=150)
	code = models.TextField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=150)
	tags = models.TextField()
	gitLink = models.URLField()
	image = models.FileField()

	def __str__(self):
		return self.title

