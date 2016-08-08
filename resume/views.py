from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

from .models import resume
#create the view that will return the blog list

def Basic_cv(request):
	with open("{% static 'resume/Resume.pdf' %}", 'rb') as pdf:
		response = HttpResponse(pdf.read(), content_type='application/pdf')
		response['Content_Disposition'] = 'filename=resume.pdf'
		return response
	pdf.closed


class ResumeView(generic.DetailView):
	model = resume
	template_name ='resume/resume.html'


#template defaults to <model name>-form.html in lowercase so here post_form.html
class ResumeCreate(CreateView):
	model = resume
	fields =['title', 'name', 'education', 'work','contact','statement','portfolio','profile_pic','author']

#template defaults to <model name>-form.html in lowercase so here post_form.html
class ResumeUpdate(UpdateView):
	model = resume
	fields =['name', 'education', 'work','contact','statement','portfolio','profile_pic','author']

#template defaults to <model name>-form.html in lowercase so here post_form.html
class ResumeDelete(DeleteView):
	model = resume
	success_url = reverse_lazy('/')