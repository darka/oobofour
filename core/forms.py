from django.forms import ModelForm
from models import Post

class PostForm(ModelForm):
  class Meta:
    model = Post
    exclude = ('author',)

  def save_with_user(self, user):
    post = super(PostForm, self).save(commit = False)
    post.author = user
    post.save()

    return post
