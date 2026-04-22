from django.shortcuts import render
from . import models

# Create your views here.

def start(request):
    users=models.User.objects.all() 
    return render(request, 'app/index.html',context={'users':users})

def user_view(request,user_id):
    user=models.User.objects.get(pk=user_id)
    return render(request,'app/user_view.html',{'user':user})