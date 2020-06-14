from django import forms
from django.contrib.auth.models import User

class search(forms.Form):
	name=forms.CharField(max_length=200)
	#widget=forms.TextInput(attrs={'style':'position:relative; left:200px;','id':'styling'}
	