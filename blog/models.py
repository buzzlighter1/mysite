from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
	title = models.CharField(max_length = 140)
	body = models.TextField()
	date = models.DateTimeField(auto_now=False, auto_now_add=True)
	author = models.CharField(max_length = 140, default='new user')
	cover_img = models.FileField(default='settings.MEDIA_ROOT/media/default.png')

	def get_absolute_url(self):
		return reverse('blog:posts',kwargs={'pk':self.pk}) #must give the views a name to correctly import as from urls(blog) the detailed url link

	def __str__(self):
		return self.title