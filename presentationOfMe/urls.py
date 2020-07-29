
from django.urls import path
from . import views

urlpatterns = [
    path('', views.baseView, name='home'),
    path('home', views.homeView, name='home'),
    path('blog', views.blogView, name='blog'),
]
