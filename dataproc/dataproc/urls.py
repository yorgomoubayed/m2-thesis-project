"""
dataproc URL configuration
urlpatterns list routes URLs to views
"""

# Import django libraries
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]
