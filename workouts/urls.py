from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from workouts.models import Workout
urlpatterns = patterns('workouts.views',
    #url(r'^$', 'index'),
    #url(r'^(?P<team_id>\d+)/$', 'details'),
    #url(r'^(?P<team_id>\d+)/captain/$', 'captain'),
    #url(r'^(?P<team_id>\d+)/roster/$', 'roster'),
    url(r'^mine/$', 'mine'),
    url(r'^$',
        ListView.as_view(queryset=Workout.objects.order_by('name'),),
       ),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(model=Workout,), name='workout_details'
       ),
)

