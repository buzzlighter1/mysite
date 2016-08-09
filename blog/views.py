from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .models import Post
#create the view that will return the blog list
class IndexView(generic.ListView):
	template_name = 'blog/blog.html'
	context_object_name ='blog_list' #the list name

	def get_queryset(self):
		return Post.objects.all().order_by("-date")[:25] #what the database returns

	# def listing(request):
	# 	post_list = Post.objects.all()
	# 	paginator = Paginator(post_list, 25) # Show 25 contacts per page
	# 	page = request.GET.get('page')
	# 	try:
	# 		queryset = paginator.page(page)
	# 	except PageNotAnInteger:
 #        # If page is not an integer, deliver first page.
	# 		queryset = paginator.page(1)
	# 	except EmptyPage:
 #        # If page is out of range (e.g. 9999), deliver last page of results.
 #        	queryset = paginator.page(paginator.num_pages)
 #        return render(request, 'blog/blog.html', {'blog': blog_list})


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




