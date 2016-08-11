from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import pre_save #allows models to be altered before being saved
from django.utils.text import slugify

class PostManager(models.Manager):
	def active(self, *args, **kwargs):
		return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())

class Post(models.Model):
	title = models.CharField(max_length = 140)
	body = models.TextField()
	slug = models.SlugField(unique=True)
	date = models.DateTimeField(default=timezone.now)
	draft = models.BooleanField(default = True)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	last_modified = models.DateTimeField(blank=True, auto_now = True, null=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	cover_img = models.FileField(default='settings.MEDIA_ROOT/media/default.png')

	objects = PostManager()

	def get_absolute_url(self):
		return reverse('posts:posts',kwargs={'slug':self.slug}) #must give the views a name to correctly import as from urls(blog) the detailed url link

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-date', '-last_modified']

#method that will occur before the post is saved to generate the slug title
def pre_save_post_receiver(sender, instance, *args, **kwargs):
	slug = slugify(instance.title)
	exists = Post.objects.filter(slug=slug).exists()
	if exists:
		slug = "%s-%s" %(slug, instance.id)
	instance.slug = slug


pre_save.connect(pre_save_post_receiver, sender=Post)