from django.urls import include, path
from rest_framework import routers
from api import views

urlpatterns = [
    path('', include('polls.urls')),
    path('api', include('api.urls')),
]
