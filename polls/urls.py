from django.urls import path
from . import views
from . import views_user

urlpatterns = [
    path('', views.index, name='index'),
    path('vote', views.vote, name='vote'),
    path('save_poll', views.new_poll, name='save_poll'),
    path('polls', views.update_polls, name='polls'),
    path('profiles/<str:username>', views_user.get_profile, name='user_profile'),
    path('auth/login', views_user.loginPage, name='login'),
    path('auth/register', views_user.registerPage, name='register'),
    path('auth/login/check', views_user.login, name='loginCheck'),
    path('auth/register/check', views_user.register, name='registerCheck'),
    path('auth/profile/update', views_user.update, name="updateProfile"),
    path('logout', views_user.logout),
]