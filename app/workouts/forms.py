from teams.models import Team, Member
from workouts.models import *
#from django import forms
import floppyforms as forms
from django.forms.models import inlineformset_factory
import datetime

class WorkoutPlanForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    kind = forms.CharField(max_length=50)


class StepForm2(forms.Form):
    activity = models.ForeignKey(Activity)
    position = forms.IntegerField()
    workout = models.ForeignKey(Workout)

def make_step_form(team):
    class StepsForm(forms.Form):
        activities = forms.ModelChoiceField(
                 queryset=Activity.objects.filter(team=team))
        position = forms.IntegerField()
    return StepsForm

class IndividualAssignForm(forms.Form):
    date_suggested = forms.DateField(initial=datetime.date.today, required=True, widget=forms.DateInput(attrs={'data-js-widget':'datepicker'}))
    time_suggested = forms.TimeField(initial='18:00')


class TeamPlayerForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100)
    number = forms.IntegerField()
    position = forms.CharField(max_length=3)
    #TODO: Autocreate this by first letter, last name, then number -> It should always be unique
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=100)
