from django.conf.urls import url

from . import views
from .views import CompanyDetailView

app_name = 'companies'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', CompanyDetailView.as_view(), name='detail'),
]
