from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def rendering(request):
    users=[
        {'ism':'Saidansaf','familiya':'Afzalxonov','yosh':'11'},
    ]
    return render(request,'app/index.html',context={"users":users})