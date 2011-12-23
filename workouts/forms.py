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

class StepForm2(forms.Form):
    """
    def __init__(self, *args, **kwargs):
        super(StepsForm, self).__init__(*args, **kwargs)
        self.fields["activities"].queryset = Activities.objects.filter(queryset=Activity)
    """
    activity = models.ForeignKey(Activity)
    position = forms.IntegerField()
    workout = models.ForeignKey(Workout)
    """
    activity = models.ForeignKey(Activity)
    workout = models.ForeignKey(Workout)
    position = models.PositiveSmallIntegerField(null=True)
    #field1 = forms.ModelChoiceField(queryset=..., empty_label="(Nothing)")
    """

def make_step_form(team):
    class StepsForm(forms.Form):
        activities = forms.ModelChoiceField(
                 queryset=Activity.objects.filter(team=team))
        position = forms.IntegerField()
    return StepsForm

"""
def make_update_step_form(team, activity):
    class StepsForm(forms.Form):
        activities = forms.ModelChoiceField(
                 queryset=Activity.objects.filter(team=team))
        position = forms.IntegerField()
    return StepsForm(initial = { 'activities': activities.pk }
"""



class TeamPlayerForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    number = forms.IntegerField()
    position = forms.CharField(max_length=3)
    #TODO: Autocreate this by first letter, last name, then number -> It should always be unique
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=100)
