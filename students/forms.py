from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student


class SignUpForm(UserCreationForm):
    bio = forms.CharField(max_length=2000)
    phone_number = forms.IntegerField(max_value=999999999999)
    resume = forms.FileField(required=False)
    photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'bio', 'phone_number', 'password1', 'password2', 'resume', 'photo')


class ChangeForm(forms.ModelForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = Student
        fields = ['email', 'bio', 'phone_number', 'resume', 'photo']