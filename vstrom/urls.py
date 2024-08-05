from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'vstrom'
urlpatterns = [
    path('', views.index, name='index'),
    path('load_participants/', views.load_participants, name='load_participants'),
    #path('post_contact/', views.post_contact, name='post_contact')
]
