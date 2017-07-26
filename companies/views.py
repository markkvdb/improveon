from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

from jobs.models import Job

from .models import Company
from .forms import SignUpForm
from core.signals import create_company


# Create your views here.
def index(request):
    companies = Company.objects.all()[:5]
    return render(request, 'companies/index.html', context={'companies': companies})


class CompanyDetailView(DetailView):
    model = Company


@login_required(login_url=reverse_lazy('core:login'))
def overview(request):
    company_user = None
    if request.user.is_authenticated():
        company_user = User.objects.get(username=request.user)

    company = Company.objects.get(user=company_user)
    jobs = Job.objects.filter(company=company)
    return render(request, 'companies/overview.html', context={'company': company, 'jobs': jobs})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            create_company.send(sender=User, instance=user)
            user.refresh_from_db()  # load the profile instance created by the signal
            user.company.name = form.cleaned_data.get('name')
            user.company.bio = form.cleaned_data.get('bio')
            user.company.anonymous = form.cleaned_data.get('anonymous')
            user.company.save()
            raw_password = form.clean_password2()
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('companies:overview')
    else:
        form = SignUpForm()
    return render(request, 'companies/signup.html', {'form': form})