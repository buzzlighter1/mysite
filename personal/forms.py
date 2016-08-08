from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)

	class Meta:
		model = User #pulls from the user table
		fields =['username', 'email', 'password']

class LoginForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)

	class Meta:
		model = User #pulls from the user table
		fields =['username', 'password']