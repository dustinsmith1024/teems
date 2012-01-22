from django.conf.urls.defaults import patterns, include, url
#from django.views.generic import DetailView, ListView


urlpatterns = patterns('users.views',
    url(r'^(?P<username>\w+)/update/$', 'edit_user', name='edit_user'),
    url(r'^(?P<username>\w+)/delete/$', 'delete_user', name='delete_user'),
    url(r'^(?P<username>\w+)/$', 'user_details', name='user_details'),
    url(r'^/$', 'users', name='users'),
)

