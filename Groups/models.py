from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from books_1.models import Book

# Create your models here.
class Group(models.Model):
    user = models.ManyToManyField(User)
    group_name = models.CharField(max_length = 120)
    group_password = models.CharField(max_length = 120)

class GroupList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, 
                                null=True)
    groups = models.ManyToManyField(Group, blank=True)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete = models.CASCADE)
    group_posted = models.ForeignKey(Group, on_delete=models.CASCADE)
    description = models.TextField()
