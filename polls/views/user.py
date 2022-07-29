from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from polls.models import Choice
from polls.models import Question
from polls.models import User
from polls.models import FriendRequest
from datetime import timedelta
import json


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
    gender = json.loads(request.POST['gender'])

    user = User.objects.create(photo=photo_data, username=username, gender=gender, password=password)
    user.save()

    return redirect('login')


def login(request):
    username = request.POST['username']
    password = request.POST['password']

    users = [u for u in User.objects.filter(username=username).values()]

    if users == []:
        return JsonResponse([False, 'Usuário não encontrado'], safe=False)

    user = users[0]

    if user['password'] == password:
        request.session['user'] = user
        
        if 'remember' not in request.POST or request.POST['remember'] != 'on':
            request.session.set_expiry(0)
        else:
            expiry = int(timedelta(days=30).total_seconds())
            
            request.session.set_expiry(expiry)
        
        return JsonResponse([True, ''], safe=False)
    else:
        return JsonResponse([False, 'Senha incorreta'], safe=False)

      
def update(request):
    reset_photo = json.loads(request.POST["reset_photo"])
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
    
    if reset_photo:
        user.photo = None
    else:
        if photo_data is not None:
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
        return redirect('/')