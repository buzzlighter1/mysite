from django.conf.urls import url, include
from django.http import HttpResponse
from . import views

#patterns to link to poll/views.py

app_name = 'resume'

urlpatterns = [
	url(r'^(?P<pk>[a-z]+)/$', views.ResumeView.as_view(), name='index'),

	url(r'^$', views.Basic_cv, name='basic_cv'),




    ]
