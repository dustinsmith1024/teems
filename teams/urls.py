from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from teams.models import Team, Player


urlpatterns = patterns('teams.views',
    url(r'^mine/$', 'mine'),
    url(r'^new/$', 'new'),
    url(r'^(?P<team_id>\d+)/players/new$', 'new_player'),
    url(r'^(?P<team_id>\d+)/players/(?P<player_id>\d+)$', 'player', name='player'),
    url(r'^(?P<team_id>\d+)/players$', 'players'),
    url(r'^(?P<team_id>\d+)/update/$', 'update'),
    url(r'^(?P<team_id>\d+)/captain/$', 'captain'),
    url(r'^$',
        ListView.as_view(queryset=Team.objects.order_by('name'),),
       ),
    url(r'^(?P<team_id>\d+)/$', 'view', name='view'),
    #    DetailView.as_view(model=Team,), name='team_details'
    #   ),
)

