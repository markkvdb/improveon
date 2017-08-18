from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.core.files.images import ImageFile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from tools.models import Tool

from .models import Student
from .forms import SignUpForm, ChangeForm
from core.signals import create_student


# Create your views here.
def index(request):
    student_list = Student.objects.all().order_by('-id')
    paginator = Paginator(student_list, 6)

    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)


    return render(request, 'students/index.html', context={'students': students})

class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        context['tools'] = Tool.objects.filter(author=context['student'])
        return context

@permission_required('students.change_student', login_url=reverse_lazy('core:login'))
@login_required(login_url=reverse_lazy('core:login'))
def overview(request):
    student_user = None
    if request.user.is_authenticated():
        student_user = User.objects.get(username=request.user)

    try:
        student = Student.objects.get(user=student_user)
    except ObjectDoesNotExist:
        return render(request, 'core/index.html')

    tools = Tool.objects.filter(author=student)
    return render(request, 'students/overview.html', context={'student': student, 'tools': tools})

@permission_required('students.change_student', login_url=reverse_lazy('core:login'))
@login_required(login_url=reverse_lazy('core:login'))
def change_info(request):
    student_user = None
    if request.user.is_authenticated():
        student_user = User.objects.get(username=request.user)

    try:
        student = Student.objects.get(user=student_user)
    except ObjectDoesNotExist:
        return render(request, 'core/index.html')

    if request.method == 'POST':
        form = ChangeForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            student_user.email = form.cleaned_data['email']
            form.save()
            return redirect('students:overview')
    else:
        form = ChangeForm(instance=student)

    return render(request, 'students/signup.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            create_student.send(sender=User, instance=user)
            user.refresh_from_db()  # load the profile instance created by the signal
            user.student.bio = form.cleaned_data.get('bio')
            user.student.phone_number = form.cleaned_data.get('phone_number')
            user.student.resume = File(request.FILES['resume'])
            user.student.photo = ImageFile(request.FILES['photo'])

            # Add user to group
            students_group = Group.objects.get(name='students')
            user.groups.set([students_group])
            user.student.save()
            raw_password = form.clean_password2()
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('students:overview')
    else:
        form = SignUpForm()
    return render(request, 'students/signup.html', {'form': form})