from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import redirect
from .models import Choice
from .models import Question
from .models import User
import json


def get_profile(request, username):
    template = loader.get_template('polls/profile.html')
    user = User.objects.filter(username=username).values().first()
    
    general_context = {
    }
    user_context = {
        'user': user
    }
    is_logged = False
    
    if 'user' not in request.session.keys():
        is_logged = False
    else:
        is_logged = request.session['user']['id'] == user['id']
    
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
    username = request.POST['username']
    password = request.POST['password']
    gender = request.POST['gender']

    user = User.objects.create(username=username, gender=gender, password=password)
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
    username = request.POST['username']
    password = request.POST['password']
    photo = request.POST['photo']
    
    logged_user = request.session['user']
    user = User.objects.get(id=logged_user['id'])
    
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