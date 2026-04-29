from django.shortcuts import render, redirect,get_object_or_404
from django.urls.base import reverse_lazy
from . import models
from . import forms
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView

# Create your views here.

class UserListView(ListView):
    model=models.User
    template_name='app/index.html'
    context_object_name='users'

class UserCreateView(CreateView):
    model=models.User
    template_name='app/user_create.html'
    form_class=forms.UserForm
    success_url=reverse_lazy('user_list')

class UserDetailView(DetailView):
    model=models.User
    template_name='app/user_view.html'
    context_object_name='user'
    slug_field='slug'
    slug_url_kwarg='slug'

class UserUpdateView(UpdateView):
    model=models.User
    template_name='app/user_update.html'
    form_class=forms.UserForm
    context_object_name='form'
    slug_field='slug'
    slug_url_kwarg='slug'
    success_url=reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model=models.User
    template_name='app/user_delete.html'
    context_object_name='user'
    slug_field='slug'
    slug_url_kwarg='slug'
    success_url=reverse_lazy('user_list')







#---------------------------------------------------------------------------------------------------
# def start(request):
#     users=models.User.objects.all() 
#     return render(request, 'app/index.html',context={'users':users})

# def user_view(request,slug):
#     user=models.User.objects.get(slug=slug)
#     return render(request,'app/user_view.html',{'user':user})

# def user_create(request):
#     form=forms.UserForm(request.POST,request.FILES)
#     if request.method=="POST":
#         if form.is_valid():
#             form.save()
#         return redirect('user_list') 
#     return render(request,'app/user_create.html',{'form':form})

# def user_update(request, slug):
#     user = get_object_or_404(models.User, slug=slug)
#     form=forms.UserForm(request.POST,request.FILES,instance=user)
#     if request.POST:
#         if form.is_valid():
#             form.save()
#         return redirect(f'/app/user/{user.slug}')
    
#     return render(request, 'app/user_update.html', {'user': user,'form':form})

# def user_delete(request,slug):
#     user = get_object_or_404(models.User, slug=slug)
#     if request.POST:
#         user.delete()
#         return redirect('user_list')
#     return render(request,'app/user_delete.html',{'user':user})