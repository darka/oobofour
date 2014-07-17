from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from forms import PostForm
from models import Post

def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      new_user = form.save()
      return HttpResponseRedirect("/login")
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
      return HttpResponseRedirect("/")
  return render(request, 'new_post.html', { 'form': form })

class PostDetailView(generic.DetailView):
  model = Post
  template_name = 'post.html'

class PostUpdateView(generic.UpdateView):
  model = Post
  form_class = PostForm
  template_name = 'post_edit.html'

class IndexView(generic.ListView):
  template_name = 'list_posts.html'
  context_object_name = 'posts'

  def get_queryset(self):
    return Post.objects.all()
