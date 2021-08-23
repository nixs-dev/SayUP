from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    op1 = models.CharField(max_length=15)
    op2 = models.CharField(max_length=15)
    op3 = models.CharField(max_length=15)
    op4 = models.CharField(max_length=15)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.IntegerField(max_length=1)