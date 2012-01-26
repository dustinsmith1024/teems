from django.conf.urls.defaults import patterns, include, url
#from django.views.generic import DetailView, ListView


urlpatterns = patterns('teams.views',
    url(r'^mine/$', 'mine'),
    url(r'^new/$', 'new', name='new_team'),
    url(r'^join/$', 'join', name='join_team'),
    url(r'^create/$', 'create_and_join', name='create_and_join_team'),
    url(r'^(?P<team_id>\d+)/members/new$', 'new_member', name='new_member'),
    url(r'^(?P<team_id>\d+)/members/(?P<username>\d+)/edit/$', 'edit_member', name='edit_member'),
    url(r'^(?P<team_id>\d+)/edit/$', 'edit', name='edit_team'),
    url(r'^(?P<team_id>\d+)/$', 'team_details', name='team_details'),
    url(r'^$', 'teams', name='teams'),
)

