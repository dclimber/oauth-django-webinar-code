from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('callback/', views.callback, name='callback'),
    path('workhorse/', views.workhorse, name='workhorse'),
]
