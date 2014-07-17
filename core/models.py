from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Post(models.Model):
  author = models.ForeignKey(User)
  title = models.CharField(max_length=200)
  content = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

  def get_absolute_url(self):
    return u'/posts/{}'.format(self.id)

admin.site.register(Post)
