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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage


class MediaFileSystemStorage(FileSystemStorage):
	def get_available_name(self,name):
		return name

	def _save(self, name, content):
		if self.exists(name):
			return name
		return super(MediaFileSystemStorage,self)._save(name,content)

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

class BlogCreate(LoginRequiredMixin, CreateView):
	login_url = 'personal:login'
	form_class = PostForm
	model = Post

	def get_form(self, form_class):
		form = super(BlogCreate, self).get_form(form_class)
		form.fields['publish'] = forms.DateField(widget=forms.SelectDateWidget)
		form.fields['body'] = forms.CharField(widget=PagedownWidget)
		return form



class BlogUpdate(LoginRequiredMixin, UpdateView):
	login_url = 'personal:login'
	form_class = PostForm
	model = Post

	def get_form(self, form_class):
		form = super(BlogUpdate, self).get_form(form_class)
		form.fields['publish'] = forms.DateField(widget=forms.SelectDateWidget)
		form.fields['body'] = forms.CharField(widget=PagedownWidget)
		return form



# #template defaults to <model name>-form.html in lowercase so here post_form.html
class BlogDelete(LoginRequiredMixin, DeleteView):
	login_url = 'personal:login'
	model = Post
	success_url = reverse_lazy('blog:blog_list')




#Redundent code will be trashed-------------------------------------------------------------------------------

# def BlogCreate(request):
# 	form = PostForm()
# 	context = {
# 		"form":form,
# 	}
# 	return render(request, "post_form.html", context)



# class BlogCreate(LoginRequiredMixin, View):
# 	login_url = 'personal:login'
# 	form_class = PostForm
# 	template_name = 'blog/post_form.html'

# 	def get(self, request):
# 		form = self.form_class(None)
# 		return render(request, self.template_name,{'form':form})

# 	def post(self, request):
# 		args ={}
# 		form = self.form_class(request.POST,request.FILES)

# 		if form.is_valid():
# 			newpost = form.save(commit=False)
# 			newpost = Post(cover_img = request.FILES['cover_img'])
# 			newpost.author = request.user
# 			newpost = Post(form.cleaned_data.get('publish'))
# 			newpost.save()
# 			return redirect('blog:blog_list')
# 		else:
# 			form = self.form_class(None)
# 		args['form'] = form
# 		return render(request, 'blog/post_form.html', args)




# class BlogUpdate(LoginRequiredMixin, View):
# 	login_url = 'personal:login'
# 	form_class = PostForm
# 	template_name = 'blog/post_form.html'

# 	def get(self, request, slug):
# 		postUpdated = get_object_or_404(Post, slug=slug)
# 		form = self.form_class(request.POST or None, instance=postUpdated)
# 		return render(request, self.template_name,{'form':form})

# 	def post(self, request, slug):
# 		postUpdated = get_object_or_404(Post, slug=slug)
# 		args ={}
# 		form = self.form_class(request.POST, request.FILES, instance=postUpdated)

# 		if form.is_valid():
# 			postUpdated = form.save(commit = False)
# 			postUpdated.author = request.user
# 			Post.cover_img = Post(cover_img = request.FILES['cover_img'])
# 			postUpdated.publish = form.cleaned_data.get('publish')
# 			postUpdated.save()
# 			return redirect('blog:blog_list')
# 		else:
# 			form = self.form_class(None)
# 		args['form'] = form
# 		return render(request, 'blog/post_form.html', args)