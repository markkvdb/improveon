from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

from tools.models import Tool

from .models import Student
from .forms import SignUpForm
from core.signals import create_student


# Create your views here.
def index(request):
    students = Student.objects.all()[:5]
    return render(request, 'students/index.html', context={'students': students})

class StudentDetailView(DetailView):
    model = Student

@login_required(login_url=reverse_lazy('core:login'))
def overview(request):
    student_user = None
    if request.user.is_authenticated():
        student_user = User.objects.get(username=request.user)

    student = Student.objects.get(user=student_user)
    tools = Tool.objects.filter(author=student)
    return render(request, 'students/overview.html', context={'student': student, 'tools': tools})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            create_student.send(sender=User, instance=user)
            user.refresh_from_db()  # load the profile instance created by the signal
            user.student.bio = form.cleaned_data.get('bio')
            user.student.phone_number = form.cleaned_data.get('phone_number')
            user.student.save()
            raw_password = form.clean_password2()
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('students:overview')
    else:
        form = SignUpForm()
    return render(request, 'students/signup.html', {'form': form})