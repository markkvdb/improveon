from django.forms import ModelForm
from .models import Job


class JobCreationForm(ModelForm):
    class Meta:
        model = Job
        fields = ['name', 'description']
