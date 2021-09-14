from django.contrib import admin
from django.urls import path,include
from short_url import views

urlpatterns = [
    path('', views.short_url, name='short_url'),
    
]