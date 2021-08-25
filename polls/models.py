from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    op1 = models.CharField(max_length=15)
    op2 = models.CharField(max_length=15)
    op3 = models.CharField(max_length=15)
    op4 = models.CharField(max_length=15)


class Choice(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.IntegerField(max_length=1)