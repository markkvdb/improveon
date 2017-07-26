from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.models import User

from companies.models import Company

from .models import Job
from .forms import JobCreationForm


# Create your views here.
def index(request):
    jobs = Job.objects.all()[:5]
    return render(request, 'jobs/index.html', context={'jobs': jobs})


class JobDetailView(DetailView):
    model = Job


@login_required(login_url=reverse_lazy('core:login'))
def register(request):
    if request.method == 'POST':
        form = JobCreationForm(request.POST)
        if form.is_valid():
            company_user = User.objects.get(username=request.user)
            company = Company.objects.get(user=company_user)
            job = form.save(commit=False)
            job.company = company
            job.save()
            return redirect('companies:overview')
    else:
        form = JobCreationForm()
    return render(request, 'jobs/registration.html', {'form': form})




