from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Questions(models.Model):
    number = models.IntegerField(null=True)
    paragraph = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    question = models.CharField(max_length=500, null=True)
    answer1 = models.CharField(max_length=200, null=True)
    answer2 = models.CharField(max_length=200, null=True)
    answer3 = models.CharField(max_length=200, null=True)
    answer4 = models.CharField(max_length=200, null=True)
    correct = models.CharField(max_length=2)
    explanation = models.TextField()

class QuestionsVerbal1(models.Model):
    number = models.IntegerField(null=True)
    paragraph = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    question = models.CharField(max_length=500, null=True)
    answer1 = models.CharField(max_length=200, null=True)
    answer2 = models.CharField(max_length=200, null=True)
    answer3 = models.CharField(max_length=200, null=True)
    answer4 = models.CharField(max_length=200, null=True)
    correct = models.CharField(max_length=2)
    explanation = models.TextField(null=True, blank=True)

class QuestionsVerbal2(models.Model):
    number = models.IntegerField(null=True)
    paragraph = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    question = models.CharField(max_length=500, null=True)
    answer1 = models.CharField(max_length=200, null=True)
    answer2 = models.CharField(max_length=200, null=True)
    answer3 = models.CharField(max_length=200, null=True)
    answer4 = models.CharField(max_length=200, null=True)
    correct = models.CharField(max_length=2)
    explanation = models.TextField(null=True, blank=True)

class QuestionsVerbal3(models.Model):
    number = models.IntegerField(null=True)
    paragraph = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    question = models.CharField(max_length=500, null=True)
    answer1 = models.CharField(max_length=200, null=True)
    answer2 = models.CharField(max_length=200, null=True)
    answer3 = models.CharField(max_length=200, null=True)
    answer4 = models.CharField(max_length=200, null=True)
    correct = models.CharField(max_length=2)
    explanation = models.TextField(null=True, blank=True)

class QuestionsMath1(models.Model):
    number = models.IntegerField(null=True)
    paragraph = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    question = models.CharField(max_length=500, null=True)
    answer1 = models.CharField(max_length=200, null=True)
    answer2 = models.CharField(max_length=200, null=True)
    answer3 = models.CharField(max_length=200, null=True)
    answer4 = models.CharField(max_length=200, null=True)
    correct = models.CharField(max_length=2)
    explanation = models.TextField(null=True, blank=True)

class Friendship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_of')
    accepted = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures', default='noavatar.jpg')
    name = models.CharField(max_length=20, null=True, blank=True)
    math_score = models.IntegerField(null=True, blank=True)
    verbal_score = models.IntegerField(null=True, blank=True)
    tokens = models.IntegerField(null=True, blank=True)
    numberoftest = models.IntegerField(null=True, default=0)
