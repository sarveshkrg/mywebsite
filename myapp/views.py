from django.shortcuts import render
from . models import User

def index(request):
    all_users = User.objects.all()
    context = {'all_users':all_users}
    return render(request, 'myapp/index.html', context)