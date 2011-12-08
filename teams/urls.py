from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from teams.models import Team, Player
urlpatterns = patterns('teams.views',
    #url(r'^$', 'index'),
    #url(r'^(?P<team_id>\d+)/$', 'details'),
    url(r'^mine/$', 'mine'),
    url(r'^(?P<team_id>\d+)/captain/$', 'captain'),
    url(r'^(?P<team_id>\d+)/roster/$', 'roster'),
    url(r'^$',
        ListView.as_view(queryset=Team.objects.order_by('name'),),
       ),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(model=Team,), name='team_details'
       ),
)

