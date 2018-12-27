from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    #path(r'signup/', views.signup, name='signup'),
    path(r'signup/', views.user_create_view, name='user_create_view'),
    path(r'profile/', views.profile, name='profile'),
]