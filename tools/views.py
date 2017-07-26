from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.models import User

from students.models import Student

from .models import Tool
from .forms import ToolCreationForm


# Create your views here.
def index(request):
    tools = Tool.objects.all()[:5]
    return render(request, 'tools/index.html', context={'tools': tools})


class ToolDetailView(DetailView):

    model = Tool


@login_required(login_url=reverse_lazy('core:login'))
def register(request):
    if request.method == 'POST':
        form = ToolCreationForm(request.POST)
        if form.is_valid():
            student_user = User.objects.get(username=request.user)
            student = Student.objects.get(user=student_user)
            tool = form.save(commit=False)
            tool.author = student
            tool.save()
            return redirect('students:overview')
    else:
        form = ToolCreationForm()
    return render(request, 'tools/registration.html', {'form': form})