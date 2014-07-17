from django.conf.urls.defaults import *
from django.views.generic import TemplateView
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from core import views
from django.views.generic import RedirectView
import dbindexer
import djangoappengine

handler500 = 'djangotoolbox.errorviews.server_error'

# django admin
admin.autodiscover()

# search for dbindexes.py in all INSTALLED_APPS and load them
dbindexer.autodiscover()

urlpatterns = patterns('',
    ('^$', views.IndexView.as_view()),

    ('^posts/$', RedirectView.as_view(url='/')),
    ('^posts/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view()),
    ('^posts/(?P<pk>[0-9]+)/edit/$', login_required(views.PostUpdateView.as_view())),
    ('^posts/(?P<pk>[0-9]+)/delete/$', login_required(views.PostDeleteView.as_view())),
    ('^posts/new/$', login_required(views.PostCreateView.as_view())),

    ('^login/$', login),
    ('^logout/$', login_required(logout)),
    ('^register/$', views.register),

    ('^admin/', include(admin.site.urls)),
)
