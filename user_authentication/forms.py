from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Registeruser (UserCreationForm):
    email = forms.EmailField(required=True,)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email']


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
