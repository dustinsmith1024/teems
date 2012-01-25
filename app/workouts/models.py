from django.db import models
from teams.models import Team, Member
from django.forms import ModelForm

class Activity(models.Model):
    """
      Individual piece of a workout like shoot, dribbling, etc...
    """
    team = models.ForeignKey(Team,null=True)
    name = models.CharField(max_length=50,default='Activity Name')
    kind = models.CharField(max_length=50,default='Kind of Activity')
    people_needed = models.IntegerField(default='1')
    location = models.CharField(max_length=200,null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
      return self.name

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ('name', 'kind', 'people_needed', 'location', 'instructions',)


class Workout(models.Model):
    """
     A collection of activities in order base on steps 
     Steps are called the 'plan' via a join table
    """
    plan = models.ManyToManyField(Activity, through='Step')
    name = models.CharField(max_length=50,default='Workout Plane Name')
    kind = models.CharField(max_length=50,default='Kind of Workout')
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
      return self.name

class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = ('name', 'kind',)


class Step(models.Model):
    """
      Just a join model for Workouts and Activities
      Allows us to order the workout via the position attribute
    """
    activity = models.ForeignKey(Activity)
    workout = models.ForeignKey(Workout)
    position = models.PositiveSmallIntegerField(null=True)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['workout', 'position']

    def __unicode__(self):
      return str(self.activity.name) + " - " + str(self.workout)

class StepForm(ModelForm):
    class Meta:
        model = Step


class Practice(models.Model):
    """
     Team related workouts
     Join table to teams and workouts
     Allows us to reuse a workout more than once
    """
    workout = models.ForeignKey(Workout)
    team = models.ForeignKey(Team)
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def name(self):
      return self.workout.name

    def __unicode__(self):
      return "Practice for " + self.name()

class PracticeForm(ModelForm):
    class Meta:
        model = Practice
        fields = ['date', 'time', 'notes']


class Individual(models.Model):
    """
      A workout that is assigned to a member. 
      Extra fields for tracking each one
    """
    workout = models.ForeignKey(Workout)
    member = models.ForeignKey(Member)
    date_complete = models.DateField(null=True, blank=True)
    date_suggested = models.DateField()
    time_suggested = models.TimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def name(self):
        return self.workout.name

    def __unicode__(self):
      return self.name()

    class Meta:
        ordering = ['date_suggested', 'time_suggested']

class IndividualEditForm(ModelForm):
    class Meta:
        model = Individual
        fields = ['date_suggested', 'time_suggested', 'notes', 'date_complete']


"""
# Workouts by team members that they do individually
  - completed
  - due date
  - date complete
  - notes
"""
# WOrkouts by team members that they do with teammate but are not team practices

# Workouts by teams which are 'practices'

# Workouts by team which are extra - like lifting , and running
