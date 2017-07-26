from django.conf.urls import url

from . import views
from .views import ToolDetailView


app_name = 'tools'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', ToolDetailView.as_view(), name='detail'),
    url(r'^register/', views.register, name='register'),
]