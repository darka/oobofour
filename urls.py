from django.conf.urls.defaults import *
from django.views.generic import TemplateView
from django.contrib import admin
from django.contrib.auth.views import login
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
    ('^admin/', include(admin.site.urls)),
    ('^posts/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view()),
    ('^posts/(?P<pk>[0-9]+)/edit/$', views.PostUpdateView.as_view()),
    ('^posts/new/$', views.new_post),
    ('^posts/$', RedirectView.as_view(url='/')),
    ('^login/$', login),
    ('^logout/$', logout),
    ('^register/$', views.register),
)
