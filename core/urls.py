from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


app_name = 'core'

urlpatterns = [
    url(r'^login/success/', views.login_redirect, name='login_redirect'),
    url(r'^login/', auth_views.LoginView.as_view(template_name='core/login.html', extra_context={'next': 'success/'}), name='login'),
    url(r'^$', views.index, name='index'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^search/', views.search, name='search'),
]