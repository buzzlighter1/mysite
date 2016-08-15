from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
from . import views

app_name ='blog'

urlpatterns = [
#order is important to prevent issues
	url(r'^$', views.IndexView.as_view(), name ='blog_list'), 

	url(r'^delete/(?P<pk>[\d]+)/$',views.BlogDelete.as_view(), name='delete-blog'),

	url(r'^add/$',views.BlogCreate.as_view(), name='add-blog'),

	url(r'^(?P<slug>[\w-]+)/$',views.DetailView.as_view(), name='posts'),

	url(r'^update/(?P<slug>[\w-]+)/$',views.BlogUpdate.as_view(), name='update-blog'),

	#url(r'^delete/(?P<slug>[\w-]+)/$',views.BlogDelete.as_view(), name='delete-blog'),
	

	]
