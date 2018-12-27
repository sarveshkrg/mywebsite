from django.shortcuts import render
from . models import User
from django.http import HttpResponse

def index(request):
    return render(request, 'myapp/index.html', {})

def profile(request):
    all_users = User.objects.all()
    return render(request, 'myapp/profile.html', {'all_users':all_users})

def signup(request):
    return render(request, 'myapp/signup.html', {})

def register(request):
    if request.method == 'POST':
        user = User()
        user.name = request.POST.get('name')
        user.mobileno = request.POST.get('mobileno')
        user.gender = request.POST.get('gender')
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        user.save()
        return render(request, 'myapp/signup.html')
