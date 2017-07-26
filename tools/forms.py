from django.forms import ModelForm
from .models import Tool


class ToolCreationForm(ModelForm):
    class Meta:
        model = Tool
        fields = ['name', 'description']
