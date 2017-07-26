from django.conf.urls import url

from . import views
from .views import StudentDetailView


app_name = 'students'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', StudentDetailView.as_view(), name='detail'),
    url(r'^overview/', views.overview, name='overview'),
    url(r'^signup/', views.signup, name='signup'),
]