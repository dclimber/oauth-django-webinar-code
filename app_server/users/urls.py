from django.urls import path

from . import views

urlpatterns = [
    path('token/', views.token, name='get-token'),
    path('token/revoke/', views.revoke_token, name='revoke-token'),
]
