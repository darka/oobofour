from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import PostForm
from models import Post

def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      new_user = form.save()
      return HttpResponseRedirect("/posts")
  else:
    form = UserCreationForm()
  return render(request, "registration/register.html", {
    'form': form,
  })

@login_required
def new_post(request):
  form = PostForm()
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      form.save(request.user)
      return HttpResponseRedirect(reverse('core.views.list_posts'))
  return render('new_post.html', { 'form': form })

def list_posts(request):
  posts = Post.objects.all()
  return render('list_posts.html', { 'posts' : posts })
