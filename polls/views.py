from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from .models import User
from .models import Choice
from .models import Question
import json


def new_poll(request):
    user_id = request.session['user']['id']
    user = User.objects.filter(id=user_id)[0]

    question = request.POST['question']
    op1 = request.POST['op1']
    op2 = request.POST['op2']
    op3 = request.POST['op3']
    op4 = request.POST['op4']

    question = Question.objects.create(author=user, question_text=question, op1=op1, op2=op2, op3=op3, op4=op4)
    question.save()

    return HttpResponse('OK')

def getData(user):
    questions = Question.objects.all()
    choices = Choice.objects.all()
    calculated_choices = {}

    for question in questions:
        calculated_choices[question.id] = [0, 0, 0, 0, 0, 0]  # Option 1,Option 2,Option 3,Option 4,Total Votes,Choice

    for i in choices:
        calculated_choices[i.question.id][i.choice-1] += 1
        calculated_choices[i.question.id][-2] += 1

        if i.author_id == user['id']:
            calculated_choices[i.question.id][-1] = i.choice

    for question in calculated_choices:
        options = calculated_choices[question]
        total_votes = options[-2]

        for j in range(0, len(options)-2):
            if total_votes != 0:
                options[j] = round((options[j]/total_votes) * 100)
            else:
                options[j] = 0

    list_questions = []
    for i in questions.values():
        queryset_modified = i
        
        queryset_modified['author_username'] = User.objects.get(id=queryset_modified['author_id']).username
        list_questions.append(queryset_modified)
    list_choices = [i for i in choices.values()]
    
    return {
        'questions': list_questions,
        'choices': list_choices,
        'calculatedChoices': calculated_choices
        }


def get_polls(request):
    template = loader.get_template('polls/pollsList.html')
    data = getData(request.session['user'])

    context = {
        'questions': data['questions'],
        'choices': data['calculatedChoices']
    }
    
    print(context['questions'])
    return template.render(context, request)


def update_polls(request):
    data = get_polls(request)

    return HttpResponse(data)


def index(request):
    template = loader.get_template('polls/index.html')
    
    polls = get_polls(request)

    context = {
        'user': request.session['user'],
        'polls': polls
    }

    return HttpResponse(template.render(context, request))


def vote(request):
    author_id = int(request.session['user']['id'])
    poll = int(request.POST['poll'].replace('poll', ''))
    user_vote = int(request.POST['vote'].replace('op', ''))
    poll = Question.objects.filter(id=poll)
    author_id = User.objects.filter(id=author_id)

    votes = Choice.objects.filter(author_id=author_id[0], question=poll[0])

    if not votes.exists():
        choice = Choice.objects.create(author=author_id[0], question=poll[0], choice=user_vote)
        choice.save()
    else:
        votes[0].delete()
    
    return HttpResponse('OK')
