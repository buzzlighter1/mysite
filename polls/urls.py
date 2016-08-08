from django.conf.urls import url
from . import views

app_name ='polls' #easy ref to this app urls only
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    #regex calling on the pk (primary key from the database)
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),

    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name = 'results'),

    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name = 'vote'),


    ]
