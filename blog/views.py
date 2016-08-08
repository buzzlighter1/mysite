from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Post
#create the view that will return the blog list
class IndexView(generic.ListView):
	template_name = 'blog/blog.html'
	context_object_name ='blog_list' #the list name

	def get_queryset(self):
		return Post.objects.all().order_by("-date")[:25] #what the database returns

#the indavidual blog view
class DetailView(generic.DetailView):
	model = Post #what database table
	template_name ='blog/post.html'

#template defaults to <model name>-form.html in lowercase so here post_form.html
class BlogCreate(CreateView):
	model = Post
	fields =['title', 'body', 'date']

#template defaults to <model name>-form.html in lowercase so here post_form.html
class BlogUpdate(UpdateView):
	model = Post
	fields =['title', 'body', 'date']

#template defaults to <model name>-form.html in lowercase so here post_form.html
class BlogDelete(DeleteView):
	model = Post
	success_url = reverse_lazy('blog:index')