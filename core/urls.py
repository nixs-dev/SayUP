from django.urls import include, path
from rest_framework import routers

urlpatterns = [
    path('', include('polls.urls')),
    path('api', include('api.urls'))
]

handler404 = 'polls.views.error_404'