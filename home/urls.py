from django.urls import path
from . import views


urlpatterns = [
    path('', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name = 'contact'),
    path('signup', views.handleSignUp, name = 'singup'),
    path('login', views.handleLogIn, name='login'),
    path('logout', views.handleLogOut, name='logout'),
    path('home/<str:slug>/', views.homepost, name = 'homepost'),
]

