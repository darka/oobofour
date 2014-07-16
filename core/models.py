from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  author = models.ForeignKey(User)
  title = models.CharField(max_length=200)
  content = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
  author = models.ForeignKey(User)
  content = models.TextField()
