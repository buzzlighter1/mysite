from django.db import models
from django.core.urlresolvers import reverse

class resume(models.Model):
	title = models.CharField(max_length=150, primary_key="true", default="New Resume")
	name = models.CharField(max_length = 140)
	education = models.TextField()
	work = models.TextField()
	contact = models.CharField(max_length = 500)
	statement = models.TextField()
	author = models.CharField(max_length = 140, default='new user')
	profile_pic = models.FileField(default='settings.MEDIA_ROOT/media/default.png')
	portfolio = models.TextField()

	def get_absolute_url(self):
		return reverse('resume:index',kwargs={'pk':self.pk}) #must give the views a name to correctly import as from urls(blog) the detailed url link

	def __str__(self):
		return self.title

	def contact_list(self):
		return self.contact.split(',')