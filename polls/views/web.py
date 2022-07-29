from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.template import loader
from polls.models import User
from polls.models import Choice
from polls.models import Question
from polls.models import Category
from polls.models import FriendRequest
from . import poll, friendrequest
import json


def index(request):
    template = loader.get_template('polls/index.html')
    
    context = {
        'user': request.session['user'] if 'user' in request.session else None
    }

    return HttpResponse(template.render(context, request))


def home(request):
    template = loader.get_template('polls/home.html')
    
    polls = get_polls(request)
    categories = get_categories(request)
    add_poll_modal = get_add_poll_modal(request)
    friend_requests_modal = get_friendrequests(request)
    
    context = {
        'user': request.session['user'],
        'polls': polls,
        'categories': categories,
        'add_poll_modal': add_poll_modal,
        'friend_requests_modal': friend_requests_modal
    }

    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('polls/login.html')

    return HttpResponse(template.render(None, request))


def register(request):
    template = loader.get_template('polls/register.html')

    return HttpResponse(template.render(None, request))


def get_profile(request, username):
    template = loader.get_template('polls/profile.html')
    user = get_object_or_404(User, username=username)
    
    general_context = {
    }
    user_context = {
        'user': user
    }
    
    someone_is_logged = False
    is_logged = False
    pendent_friend_request = None
    is_friend = None
    
    if 'user' not in request.session.keys():
        is_logged = False
        someone_is_logged = False
    else:
        someone_is_logged = True
        
        if request.session['user']['id'] == user.id:
            is_logged = True
        else:
            is_logged = False
    
    if someone_is_logged:
        friendrequest_from_this = FriendRequest.objects.filter(sender=User.objects.get(id=request.session['user']['id']), recipient=user).first()
        friendrequest_from_another = FriendRequest.objects.filter(sender=user, recipient=User.objects.get(id=request.session['user']['id'])).first()
        
        if friendrequest_from_this is not None:
            is_friend = friendrequest_from_this.accepted
        elif friendrequest_from_another is not None:
            pendent_friend_request = friendrequest_from_another if not friendrequest_from_another.accepted else None
            
            if pendent_friend_request is None:
                is_friend = True
        else:
            is_friend = None
            pendent_friend_request = None
    
    user_context['someone_is_logged'] = someone_is_logged
    user_context['is_logged'] = is_logged
    user_context['pendent_friend_request'] = pendent_friend_request
    user_context['is_friend'] = is_friend
    
    if is_logged:
        user_info_template = loader.get_template('polls/logged_user_info.html')
        general_context['user_info_template'] = user_info_template.render(user_context, request)
    else:
        user_info_template = loader.get_template('polls/non_logged_user_info.html')
        general_context['user_info_template'] = user_info_template.render(user_context, request)
        
    return HttpResponse(template.render(general_context, request))


def get_friendrequests(request):
    template = loader.get_template('polls/friend_requests_modal.html')
    
    requests_sent = FriendRequest.objects.filter(sender_id=request.session['user']['id'], accepted=False)
    requests_received = FriendRequest.objects.filter(recipient_id=request.session['user']['id'], accepted=False)
 
    context = {
        'requests_sent': requests_sent,
        'requests_received': requests_received
    }
    
    return template.render(context, request)


def get_polls(request):
    template = loader.get_template('polls/polls_list.html')
    category = request.GET['category'] if 'category' in request.GET.keys() else None
    data = poll.get_data(request.session['user'], category)
    
    context = {
        'questions': data['questions'],
        'choices': data['calculatedChoices']
    }
    
    return template.render(context, request)


def get_categories(request):
    categories = Category.objects.all()
    template = loader.get_template('polls/categories_list.html')
    
    context = {
        'categories': categories
    }
    
    return template.render(context, request)


def get_add_poll_modal(request):
    categories = Category.objects.all()
    template = loader.get_template('polls/add_poll_modal.html')
    
    context = {
        'categories': categories
    }
    
    return template.render(context, request)

    
def update_polls(request):
    data = get_polls(request)

    return HttpResponse(data)


def error_404(request, exception):
    template = loader.get_template('polls/errors/404.html')
    
    return HttpResponse(template.render(None, request))