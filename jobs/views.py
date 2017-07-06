from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Job


# Create your views here.
def index(request):
    jobs = Job.objects.all()[:5]
    return render(request, 'jobs/index.html', context={'jobs': jobs})


class JobDetailView(DetailView):

    model = Job
