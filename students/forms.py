from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    bio = forms.CharField(max_length=2000)
    phone_number = forms.IntegerField(max_value=999999999999)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'bio', 'phone_number', 'password1', 'password2', )