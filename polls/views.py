from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from .models import Choice
from .models import Question
import json

def getData():
    questions = Question.objects.all()
    choices = Choice.objects.all()
    calculatedChoices = {}

    for i in choices:
        if i.question.id not in calculatedChoices:
            calculatedChoices[i.question.id] = [0, 0, 0, 0, 0]

        calculatedChoices[i.question.id][i.choice-1] += 1
        calculatedChoices[i.question.id][len(calculatedChoices[i.question.id])-1] += 1

    for i in calculatedChoices:
        a = calculatedChoices[i]
        total = a[len(a)-1]

        for j in range(0, len(a)-2):
            a[j] = round((a[j]/total) * 100)

    list_questions = [i for i in questions.values()]
    list_choices = [i for i in choices.values()]
    return {
        'questions': list_questions,
        'choices': list_choices,
        'calculatedChoices': calculatedChoices
        }

def getPolls(request):
    template = loader.get_template('polls/pollsList.html')

    data = getData()

    context = {
        'questions': data['questions'],
        'choices': data['calculatedChoices']
    }

    return template.render(context, request)

def updatePolls(request):
    data = getData()

    return JsonResponse(data)


def index(request):
    template = loader.get_template('polls/index.html')
    
    polls = getPolls(request)

    context = {
        'polls': polls
    }


    return HttpResponse(template.render(context, request))

def vote(request):
    poll = int(request.POST['poll'].replace('poll', ''))
    vote = int(request.POST['vote'].replace('op', ''))
    obj = Question.objects.filter(id=poll)

    choice = Choice.objects.create(question=obj[0], choice=vote)
    choice.save()

    return HttpResponse('OK')
