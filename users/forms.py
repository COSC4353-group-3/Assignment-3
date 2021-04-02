from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
#from django.contrib.localflavor.us.forms.USStateField(*, required=True, widget=None, label=None, initial=None, help_text='', error_messages=None, show_hidden_initial=False, validators=(), localize=False, disabled=False, label_suffix=None)
#from django.contrib.localflavor.us.forms.USStateSelect(attrs=None)
#from django.contrib.localflavor.us.forms.USZipCodeField(*args, **kwargs)
class UserRegisterForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
	
	class Meta:
		model = Profile
		fields = ['full_name','adress1','adress2','city','state','zipcode']
	


