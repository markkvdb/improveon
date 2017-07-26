from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    bio = forms.CharField(max_length=2000)
    anonymous = forms.BooleanField(required=False)
    name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'bio', 'anonymous', 'password1', 'password2', )