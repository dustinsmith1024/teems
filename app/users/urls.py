from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('users.views',
    url(r'^(?P<username>\w+)/edit/$', 'edit_user', name='edit_user'),
    url(r'^(?P<username>\w+)/$', 'user_details', name='user_details'),
    url(r'^/$', 'users', name='users'),
)

