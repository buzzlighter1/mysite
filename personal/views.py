from django.shortcuts import render, HttpResponse
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View

from .forms import UserForm, LoginForm

from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse


def index(request):
	return render(request, 'personal/index.html')

def aboutView(request):
	return render(request, 'personal/about.html')

def contact(request):
	return render(request, 'personal/basic.html', {'content':['You can contact me directly at: ','alexwilkinson@gmail.com']})

#this is for new users to add their information to the database and authenticate and login
class UserFormView(View):
	form_class = UserForm
	templete_name = 'personal/registration_form.html'

	#display a blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request,self.templete_name,{'form':form})

	#process form data
	def post(self,request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False) #creates a new object from the form doesn't save yet

			#clean the data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.is_active = False
			user.save()

			#return user object if credentials are correct
			user = authenticate(username = username, password = password)

			if user is not None:
				if user.is_active:
					login(request,user) #request.user.username to call username
					return redirect('personal:index')



#class IndexView(generic.DetailView):
#	templete_name = 'personal/index.html'



