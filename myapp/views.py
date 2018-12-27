from django.shortcuts import render
from . models import User
from . forms import UserForm

def index(request):
    return render(request, 'myapp/index.html', {})

def profile(request):
    all_users = User.objects.all()
    return render(request, 'myapp/profile.html', {'all_users':all_users})
'''
def signup(request):
    return render(request, 'myapp/signup.html', {})
'''

def user_create_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserForm()

    return render(request, 'myapp/user_create.html', {'form':form})