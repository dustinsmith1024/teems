from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf import settings
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^teams/', include('teams.urls')),
    url(r'^workouts/', include('workouts.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^$', 'views.index', name='index'),
    url(r'^learn/$', 'views.learn', name='learn'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^signup/$', 'views.signup', name='signup'),
    url(r'^$', 'views.index', name='index'),
    url(r'^robots\.txt$', direct_to_template,
             {'template': 'robots.txt', 'mimetype': 'text/plain'}),
)


if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )

