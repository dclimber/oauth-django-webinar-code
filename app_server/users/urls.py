from django.urls import path

from . import views

urlpatterns = [
    path('token/', views.token),
    path('token/refresh/', views.refresh_token),
    path('token/revoke/', views.revoke_token),
]
