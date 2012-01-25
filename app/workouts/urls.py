from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from workouts.models import Workout

urlpatterns = patterns('workouts.views',
    url(r'^new/$', 'new_workout', name='new_workout'),
    url(r'^(?P<workout_id>\d+)/edit/$', 'edit_workout', name='edit_workout'),
    url(r'^(?P<workout_id>\d+)/assign/$', 'assign_workout', name='assign_workout'),
    url(r'^(?P<workout_id>\d+)/schedule/(?P<practice_id>\d+)$', 'edit_practice', name='edit_practice'),
    url(r'^(?P<workout_id>\d+)/schedule/$', 'schedule_practice', name='schedule_practice'),
    url(r'^mine/$', 'mine', name='mine'),
    url(r'^activities/new', 'new_activity', name='new_activity'),
    url(r'^activities/(?P<activity_id>\d+)/edit/$', 'edit_activity', name='edit_activity'),
    url(r'^activities/(?P<activity_id>\d+)/$', 'activity', name='activity'),
    url(r'^activities/', 'activities', name='activities'),
    url(r'^individuals/(?P<individual_id>\d+)/edit/$', 'edit_individual', name='edit_individual'),
    url(r'^individuals/(?P<individual_id>\d+)/$', 'individual', name='individual'),
    url(r'^practices/(?P<practice_id>\d+)/$', 'practice', name='practice'),
    url(r'^practices/', 'practices', name='pratices'),
    url(r'^$', 'workouts', name='workouts'),
    url(r'^(?P<workout_id>\d+)/$', 'workout', name='workout_details'),
)

