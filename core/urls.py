from django.urls import include, path
from rest_framework import routers

urlpatterns = [
    path('', include('polls.urls')),
]
