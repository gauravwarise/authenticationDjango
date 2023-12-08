from django.contrib import admin
from django.urls import path
from .views import IndexView,RegistrationView, AuthView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register', RegistrationView.as_view(), name='register'),
    path('authuser', AuthView.as_view(), name='authuser'),

]
