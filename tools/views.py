from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Tool


# Create your views here.
def index(request):
    tools = Tool.objects.all()[:5]
    return render(request, 'tools/index.html', context={'tools': tools})


class ToolDetailView(DetailView):

    model = Tool
