from django.views import generic
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import Post
from .forms import PostForm
from pagedown.widgets import PagedownWidget
from django import forms

from django.contrib.auth.models import User

# def BlogCreate(request):
# 	form = PostForm()
# 	context = {
# 		"form":form,
# 	}
# 	return render(request, "post_form.html", context)


#create the view that will return the blog list
class IndexView(generic.ListView):
	template_name = 'blog/blog.html'
	context_object_name ='blog_list' #the list name

	paginate_by = 10

	def get_queryset(self):
		query = self.request.GET.get('q')
		if query:
			return Post.objects.active().filter(
				Q(title__icontains = query) |
				Q(body__icontains = query)
				).distinct()

		if self.request.user.is_active or self.request.user.is_superuser: #if the user is logged in an active can view
			return Post.objects.all()
		else:
			return Post.objects.active() #what the database returns


#the indavidual blog view
class DetailView(generic.DetailView):
	model = Post #what database table
	template_name ='blog/post.html'

#template defaults to <model name>-form.html in lowercase so here post_form.html
class BlogCreate(CreateView):
	model = Post
	fields =['title', 'publish','body', 'draft', 'cover_img']

	def get_form(self, form_class):
		form = super(BlogCreate, self).get_form(form_class)
		form.fields['publish'] = forms.DateField(widget=forms.SelectDateWidget)
		form.fields['body'] = forms.CharField(widget=PagedownWidget)
		return form



# class BlogCreate(View):
# 	template_name = 'blog/post_form.html'

# 	def post(self,request):
# 		form = PostForm(request.POST or None)
# 		if form.is_valid():
# 			instance = form.save(commit=False)
# 			instance.save()
# 			return redirect('blog:blog_list')

# 		return render(request, 'blog/post_form.html',{'form:form'})

#template defaults to <model name>-form.html in lowercase so here post_form.html
class BlogUpdate(UpdateView):
	model = Post
	fields =['title', 'publish','body', 'draft', 'cover_img']

	def get_form(self, form_class):
		form = super(BlogUpdate, self).get_form(form_class)
		form.fields['publish'] = forms.DateField(widget=forms.SelectDateWidget)
		form.fields['body'] = forms.CharField(widget=PagedownWidget)
		return form

#template defaults to <model name>-form.html in lowercase so here post_form.html
class BlogDelete(DeleteView):
	model = Post
	success_url = reverse_lazy('blog:blog_list')




