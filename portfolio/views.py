from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Portfolio


class Index(generic.ListView):
	template_name = 'portfolio/portfolio.html'
	context_object_name = 'portfolio_list'

	def get_queryset(self):
		return Portfolio.objects.all().order_by("-date")[:25]
