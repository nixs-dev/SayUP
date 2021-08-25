from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import redirect
from .models import Choice
from .models import Question
from .models import User
import json


def registerPage(request):
    template = loader.get_template('polls/register.html')

    return HttpResponse(template.render(None, request))

def register(request):
    username = request.POST['username']
    password = request.POST['password']

    user = User.objects.create(username=username, password=password)
    user.save()

    return HttpResponse('OK')


def loginPage(request):
    template = loader.get_template('polls/login.html')

    return HttpResponse(template.render(None, request))

def login(request):
    username = request.POST['username']
    password = request.POST['password']

    users = [u for u in User.objects.filter(username=username).values()]

    if users == []:
        return HttpResponse('Usuário não encontrado')

    user = users[0]

    if user['password'] == password:

        request.session['user'] = user
        return redirect('/')
    else:
        return HttpResponse('Senha incorreta')