from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from . import models
from . import forms

class UserListView(ListView):
    model=models.Student
    template_name='app/index.html'
    context_object_name='users'

def user_create(request):
    form=forms.UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'app/user_create.html', {'form': form})

class UserDetailView(DetailView):
    model=models.Student
    template_name='app/user_view.html'
    context_object_name='user'
    slug_field='slug'
    slug_url_kwarg='slug'

def user_update(request, slug):
    user = get_object_or_404(models.Student, slug=slug)
    if request.method=='POST':
        user.name = request.POST.get('name')
        user.surename = request.POST.get('surename')
        user.age = request.POST.get('age')
        if request.FILES.get('picture'):
            user.picture = request.FILES.get('picture')
        user.save()
        return redirect('user_view', slug=user.slug)
    return render(request, 'app/user_update.html', {'user': user})

def user_delete(request, id):
    user = get_object_or_404(models.Student, id=id)
    if request.method=='POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'app/user_delete.html', {'user': user})