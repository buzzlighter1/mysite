from django.conf.urls import url, include
from django.views.generic import ListView, DeleteView, DetailView
from . import views

#patterns to link to poll/views.py

app_name = 'portfolio'

urlpatterns = [
	url(r'^$', views.Index.as_view(), name='index'),

    ]
