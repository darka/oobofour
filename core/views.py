from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core import exceptions
from django.views import generic
from forms import PostForm
from models import Post

def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    # Automatically login after registration for a nice user experience!
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password2')
      form.save()
      user = authenticate(username=username, password=password)
      login(request, user)
      return HttpResponseRedirect("/")
  else:
    form = UserCreationForm()
  return render(request, "registration/register.html", {
    'form': form,
  })

class PostCreateView(generic.CreateView):
  model = Post
  form_class = PostForm

  def form_valid(self, form):
    self.object = form.save(commit = False)
    # Set post author to current user
    self.object.author = self.request.user 
    self.object.save
    return super(PostCreateView, self).form_valid(form)

class PostDetailView(generic.DetailView):
  model = Post

class IndexView(generic.ListView):
  model = Post
  
  def get_queryset(self):
    return Post.objects.all().order_by('-date')

class PostDeleteView(generic.DeleteView):
  model = Post
  success_url = '/'

  def dispatch(self, request, *args, **kwargs):
    check_permission(request.user, self.get_object())
    return super(PostDeleteView, self).dispatch(request, *args, **kwargs)

class PostUpdateView(generic.UpdateView):
  model = Post
  form_class = PostForm

  def dispatch(self, request, *args, **kwargs):
    check_permission(request.user, self.get_object())
    return super(PostUpdateView, self).dispatch(request, *args, **kwargs)

# Check to ensure editing/deleting user is the actual author
def check_permission(user, object):
  if user != object.author:
    raise exceptions.PermissionDenied()

