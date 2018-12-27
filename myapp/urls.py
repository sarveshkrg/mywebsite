from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'signup/', views.signup, name='signup'),
    path(r'registered=Success', views.register, name='register'),
    path(r'profile/', views.profile, name='profile'),
]