
from django.contrib.auth import authenticate, login
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path,include
from . import views
app_name = 'users'
urlpatterns = [
# Страница входа
path(r'^login/$', auth_views.LoginView.as_view(template_name= 'users/login.html'),name='login'),
path(r'^logout/$', views.logout_view, name='logout'),
    path(r'^register/$', views.register, name='register'),
]