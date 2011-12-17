from teams.models import Team, Player
from workouts.models import *
from django import forms
from django.forms.models import inlineformset_factory



class WorkoutPlanForm(forms.Form):
    name = forms.CharField(max_length=50)
    kind = forms.CharField(max_length=50)
    #plan = forms.ManyToManyField(Activity, through='Step')
    #step = forms.ModelMultipleChoiceField(queryset=Activity.objects.all())
    #steps = inlineformset_factory(Workout, Step)


class TeamPlayerForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    number = forms.IntegerField()
    position = forms.CharField(max_length=3)
    #TODO: Autocreate this by first letter, last name, then number -> It should always be unique
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=100)
