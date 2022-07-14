from django.urls import include, path
from rest_framework import routers
from .views import *
from .private_views import *

urlpatterns = [
    path('', QuestionList.as_view()),
    path('private/users', PrivateUserView.as_view()),
    path('private/polls', PrivateQuestionView.as_view()),
    path('private/punishments', PrivatePunishmentView.as_view()),
    path('private/reports', PrivateReportView.as_view())
]