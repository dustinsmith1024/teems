from django.db import models
from teams.models import Team, Player

class Activity(models.Model):
    """
      Individual piece of a workout like shoot, dribbling, etc...
    """
    name = models.CharField(max_length=50,default='Activity Name')
    kind = models.CharField(max_length=50,default='Kind of Activity')
    people_needed = models.IntegerField(default='1')
    location = models.CharField(max_length=200,null=True)
    instructions = models.TextField(null=True)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
      return self.name

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
      return self.activity + " - " + self.workout

class Practice(models.Model):
    """
     Team related workouts
     Join table to teams and workouts
     Allows us to reuse a workout more than once
    """
    workout = models.ForeignKey(Workout)
    team = models.ForeignKey(Team)
    date = models.DateField()
    notes = models.TextField(null=True)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def name(self):
      return self.workout.name

    def __unicode__(self):
      return "Practice for " + self.name()

class Individual(models.Model):
    """
      A workout that is assigned to a player. 
      Extra fields for tracking each one
    """
    workout = models.ForeignKey(Workout)
    player = models.ForeignKey(Player)
    date_complete = models.DateField(null=True, blank=True)
    date_suggested = models.DateField()
    notes = models.TextField(null=True)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def name(self):
        return self.workout.name

    def __unicode__(self):
      return self.name()

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
