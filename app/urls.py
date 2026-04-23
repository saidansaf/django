from django.urls import path
from . import views

<<<<<<< HEAD
urlpatterns = [
    path('',views.user_view)
=======
urlpatterns=[
    path("",views.start,name='user_list'),
    path("user/<int:user_id>/", views.user_view, name='user_view')
>>>>>>> 83fabe0 (eng oxirgisi)
]