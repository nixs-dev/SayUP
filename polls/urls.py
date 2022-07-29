from django.urls import path
from .views import web, user, poll, friendrequest


urlpatterns = [
    path('', web.index, name='index'),
    path('home', web.home, name='home'),
    path('vote', poll.vote, name='vote'),
    path('save_poll', poll.new_poll, name='save_poll'),
    path('polls', web.update_polls, name='polls'),
    path('profiles/<str:username>', web.get_profile, name='user_profile'),
    path('profiles/actions/sendfriendrequest', friendrequest.send, name='send_friendrequest'),
    path('profiles/actions/acceptfriendrequest', friendrequest.accept, name='accept_friendrequest'),
    path('auth/login', web.login, name='login'),
    path('auth/register', web.register, name='register'),
    path('auth/login/check', user.login, name='loginCheck'),
    path('auth/register/check', user.register, name='registerCheck'),
    path('auth/profile/update', user.update, name="updateProfile"),
    path('logout', user.logout),
]