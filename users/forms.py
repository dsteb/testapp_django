from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
	username = forms.EmailField()