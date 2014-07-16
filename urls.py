from django.conf.urls.defaults import *
from django.views.generic import TemplateView
from django.contrib import admin
import dbindexer

handler500 = 'djangotoolbox.errorviews.server_error'

# django admin
admin.autodiscover()

# search for dbindexes.py in all INSTALLED_APPS and load them
dbindexer.autodiscover()

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', TemplateView.as_view(template_name="index.html")),
    ('^admin/', include(admin.site.urls)),
    ('^posts/new/$', 'core.views.new_post'),
    ('^posts/$', 'core.views.list_posts'),
    ('^login/$', 'django.contrib.auth.views.login'),
    ('^logout/$', 'django.contrib.auth.views.logout'),
)
