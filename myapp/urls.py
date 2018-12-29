from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(r'', views.index, name='index'),
    #path(r'signup/', views.signup, name='signup'),
    path(r'signup/', views.user_create_view, name='user_create_view'),
    path(r'login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path(r'logout/', auth_views.LogoutView.as_view(template_name='myapp/logout.html'), name='logout'),
    path(r'profile/', views.profile, name='profile'),
]