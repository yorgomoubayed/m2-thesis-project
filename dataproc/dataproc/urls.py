"""
dataproc URLs configuration
urlpatterns list routes URLs to views
"""

# Django imports
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]
