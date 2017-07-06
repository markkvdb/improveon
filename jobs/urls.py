from django.conf.urls import url

from . import views
from .views import JobDetailView


app_name = 'jobs'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', JobDetailView.as_view(), name='detail'),
]