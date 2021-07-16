from django.urls import path
from . import views


urlpatterns = [
    path('', views.search, name='search'),
    path('<str:slug>/', views.searchpost, name = 'searchpost')
]
