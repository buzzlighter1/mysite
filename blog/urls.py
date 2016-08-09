from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
from . import views
"""
	url(r'^$', ListView.as_view(
		queryset = Post.objects.all().order_by("-date")[:25],
		 template_name ="blog/blog.html")), 
"""
app_name ='blog'

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name ='blog_list'), 

	url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='posts'),

	url(r'^add/$',views.BlogCreate.as_view(), name='add-blog'),

	url(r'^update/(?P<pk>[0-9]+)/$',views.BlogUpdate.as_view(), name='update-blog'),

	url(r'^delete/(?P<pk>[0-9]+)$',views.BlogDelete.as_view(), name='delete-blog'),	

	]