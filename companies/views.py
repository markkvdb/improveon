from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Company

# Create your views here.
def index(request):
    companies = Company.objects.all()[:5]
    return render(request, 'companies/index.html', context={'companies': companies})

class CompanyDetailView(DetailView):

    model = Company
