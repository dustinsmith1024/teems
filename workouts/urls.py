from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from workouts.models import Workout

urlpatterns = patterns('workouts.views',
    #url(r'^$', 'index'),
    #url(r'^(?P<team_id>\d+)/$', 'details'),
    #url(r'^(?P<team_id>\d+)/captain/$', 'captain'),
    #url(r'^(?P<team_id>\d+)/roster/$', 'roster'),
    url(r'^new/$', 'new_workout', name='new_workout'),
    url(r'^mine/$', 'mine'),
    url(r'^activities/new', 'new_activity', name='new_activity'),
    url(r'^activities/(?P<activity_id>\d+)/$', 'activity', name='activity'),
    url(r'^activities/', 'activities', name='activities'),
    url(r'^practices/(?P<practice_id>\d+)/$', 'practice', name='practice'),
    url(r'^practices/', 'practices', name='pratices'),
    #url(r'^(?P<workout_id>\d+)/$', 'workout', name='workout_details'),
    url(r'^$',
        ListView.as_view(queryset=Workout.objects.order_by('name'),),
       ),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(model=Workout,), name='workout_details'
       ),
)

