from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from teams.models import Team, Player


urlpatterns = patterns('teams.views',
    url(r'^mine/$', 'mine'),
    url(r'^new/$', 'new', name='new_team'),
    url(r'^join/$', 'join', name='join_team'),
    url(r'^create/$', 'create_and_join', name='create_and_join_team'),
    url(r'^(?P<team_id>\d+)/players/new$', 'new_player'),
    url(r'^(?P<team_id>\d+)/players/(?P<player_id>\d+)/update/$', 'edit_player', name='edit_player'),
    url(r'^(?P<team_id>\d+)/players/(?P<player_id>\d+)$', 'player', name='player'),
    url(r'^(?P<team_id>\d+)/players/$', 'players'),
    url(r'^(?P<team_id>\d+)/update/$', 'update'),
    url(r'^(?P<team_id>\d+)/$', 'team_details', name='team_details'),
)

