from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from polls.models import User
from polls.models import Choice
from polls.models import Question
from polls.models import Category
import json


def get_data(user, category):
    questions = Question.objects.all() if category is None else Question.objects.filter(category_id=category)
    choices = Choice.objects.all()
    calculated_choices = {}

    for question in questions:
        calculated_choices[question.id] = [0, 0, 0, 0, 0, 0]  # Option 1,Option 2,Option 3,Option 4,Total Votes,Choice

    for i in choices:
        if i.question.id not in calculated_choices.keys():
            continue
        
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

    return {
        'questions': questions,
        'choices': choices,
        'calculatedChoices': calculated_choices
    }


def new_poll(request):
    user_id = request.session['user']['id']
    user = User.objects.filter(id=user_id).first()
    category = Category.objects.filter(id=request.POST['category']).first()
    
    question = request.POST['question']
    op1 = request.POST['op1']
    op2 = request.POST['op2']
    op3 = request.POST['op3']
    op4 = request.POST['op4']

    question = Question.objects.create(author=user, category=category, question_text=question, op1=op1, op2=op2, op3=op3, op4=op4)
    question.save()

    return HttpResponse('OK')


def vote(request):
    author_id = int(request.session['user']['id'])
    poll = int(request.POST['poll'].replace('poll', ''))
    user_vote = int(request.POST['vote'].replace('op', ''))
    poll = Question.objects.get(id=poll)
    author = User.objects.get(id=author_id)

    votes = Choice.objects.filter(author_id=author, question=poll)

    if not votes.exists():
        choice = Choice.objects.create(author=author, question=poll, choice=user_vote)
        choice.save()
    else:
        old_choice = votes.first().choice
        votes.first().delete()
        
        if old_choice != user_vote:
            choice = Choice.objects.create(author=author, question=poll, choice=user_vote)
            choice.save()
    
    return HttpResponse('OK')