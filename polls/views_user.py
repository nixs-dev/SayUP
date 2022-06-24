from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import redirect, get_object_or_404
from .models import Choice
from .models import Question
from .models import User
from .models import FriendRequest
import json


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
    is_friend = False
    
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
        friendrequest = FriendRequest.objects.filter(sender=User.objects.get(id=request.session['user']['id']), recipient=user).values().first()
        
        if friendrequest is None:
            friendrequest = FriendRequest.objects.filter(sender=user, recipient=User.objects.get(id=request.session['user']['id'])).values().first()
        
        if friendrequest is not None:
            friendrequest = friendrequest['accepted']
        is_friend = friendrequest
    
    user_context['someone_is_logged'] = someone_is_logged
    user_context['is_logged'] = is_logged
    user_context['is_friend'] = is_friend
    
    if is_logged:
        user_info_template = loader.get_template('polls/logged_user_info.html')
        general_context['user_info_template'] = user_info_template.render(user_context, request)
    else:
        user_info_template = loader.get_template('polls/non_logged_user_info.html')
        general_context['user_info_template'] = user_info_template.render(user_context, request)
        
    return HttpResponse(template.render(general_context, request))

def registerPage(request):
    template = loader.get_template('polls/register.html')

    return HttpResponse(template.render(None, request))

def register(request):
    photo = None
    photo_data = None
    
    if len(request.FILES) > 0:
        photo = request.FILES['photo']
        photo_data = photo.read()
    else:
        photo = None
        photo_data = None
        
    username = request.POST['username']
    password = request.POST['password']
    gender = request.POST['gender']

    user = User.objects.create(photo=photo_data, username=username, gender=gender, password=password)
    user.save()

    return redirect('login')

def loginPage(request):
    template = loader.get_template('polls/login.html')

    return HttpResponse(template.render(None, request))

def login(request):
    username = request.POST['username']
    password = request.POST['password']

    users = [u for u in User.objects.filter(username=username).values()]

    if users == []:
        return JsonResponse([False, 'Usuário não encontrado'], safe=False)

    user = users[0]

    if user['password'] == password:
        request.session['user'] = user
        return JsonResponse([True, ''], safe=False)
    else:
        return JsonResponse([False, 'Senha incorreta'], safe=False)
        
def update(request):
    photo = None
    photo_data = None
    
    if len(request.FILES) > 0:
        photo = request.FILES['photo']
        photo_data = photo.read()
    else:
        photo = None
        photo_data = None
        
    username = request.POST['username']
    password = request.POST['password']
    
    logged_user = request.session['user']
    user = User.objects.get(id=logged_user['id'])
    
    user.photo = photo_data
    user.username = username
    user.password = password
    user.save()
    
    request.session['user'] = User.objects.filter(id=logged_user['id']).values().first()
    
    return JsonResponse(True, safe=False)

def logout(request):
    try:
        del request.session['user']
    except:
        pass
    finally:
        return redirect('auth/login')