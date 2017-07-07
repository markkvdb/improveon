from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()[:5]
    return render(request, 'students/index.html', context={'students': students})

class StudentDetailView(DetailView):

    model = Student
