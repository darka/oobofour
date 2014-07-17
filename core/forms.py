from django.forms import ModelForm
from models import Post

class PostForm(ModelForm):
  class Meta:
    model = Post
    exclude = ('author',)

  def save(self, user, commit = True):
    post = super(PostForm, self).save(commit = False)
    post.user = user

    if commit:
      post.save()

    return post
