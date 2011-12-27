from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from workouts.models import Workout

urlpatterns = patterns('workouts.views',
    url(r'^new/$', 'new_workout', name='new_workout'),
    url(r'^(?P<workout_id>\d+)/update/$', 'update_workout', name='update_workout'),
    url(r'^(?P<workout_id>\d+)/assign/$', 'assign_workout', name='assign_workout'),
    url(r'^mine/$', 'mine'),
    url(r'^activities/new', 'new_activity', name='new_activity'),
    url(r'^activities/(?P<activity_id>\d+)/$', 'activity', name='activity'),
    url(r'^activities/', 'activities', name='activities'),
    url(r'^practices/(?P<practice_id>\d+)/$', 'practice', name='practice'),
    url(r'^practices/', 'practices', name='pratices'),
    url(r'^$', 'workouts', name='workouts'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(model=Workout,), name='workout_details'
       ),
)

