from django.urls import path
from . import views

urlpatterns = [
    path("", views.start, name='user_list'),
    path("user/<slug:slug>/", views.user_view, name='user_view'),
]