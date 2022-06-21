from django.db import models


class User(models.Model):
    photo = models.BinaryField(null=True)
    username = models.CharField(max_length=30, unique=True)
    gender = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    

class Category(models.Model):
    name = models.CharField(max_length=60)
    classname_fontawesome = models.CharField(max_length=40)
    

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    question_text = models.CharField(max_length=200)
    op1 = models.CharField(max_length=15)
    op2 = models.CharField(max_length=15)
    op3 = models.CharField(max_length=15)
    op4 = models.CharField(max_length=15)


class Choice(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.IntegerField()

class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_sender_id')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_recipient_id')
    accepted = models.BooleanField(default=False)