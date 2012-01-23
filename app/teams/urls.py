from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from teams.models import Team, Player


urlpatterns = patterns('teams.views',
    url(r'^mine/$', 'mine'),
    url(r'^new/$', 'new', name='new_team'),
    url(r'^join/$', 'join', name='join_team'),
    url(r'^create/$', 'create_and_join', name='create_and_join_team'),
    url(r'^(?P<team_id>\d+)/members/new$', 'new_member', name='new_member'),
    url(r'^(?P<team_id>\d+)/members/(?P<member_id>\d+)/update/$', 'update_member', name='update_member'),
    url(r'^(?P<team_id>\d+)/update/$', 'update', name='update_team'),
    url(r'^(?P<team_id>\d+)/$', 'team_details', name='team_details'),
)

