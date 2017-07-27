from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect

from students.models import Student
from companies.models import Company


# Create your views here.
@login_required(login_url='core/login.html')
def login_redirect(request):
    user_login = None
    student_or_company = None
    student = False
    if request.user.is_authenticated():
        user_login = User.objects.get(username=request.user)

    try:
        student_or_company = Student.objects.get(user=user_login)
        student = True
    except ObjectDoesNotExist:
        try:
            student_or_company = Company.objects.get(user=user_login)
        except:
            print('No company or student found.')

    if student_or_company is None:
        return render(request, 'core/login.html')

    if student:
        return redirect('students:overview')
    else:
        return redirect('companies:overview')

def index(request):
    return render(request, 'core/index.html')

def signup(request):
    return render(request, 'core/signup.html')