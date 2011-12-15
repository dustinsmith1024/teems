from teams.models import Team, Player
from django import forms

class TeamPlayerForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=30)
    number = forms.IntegerField()
    position = forms.CharField(max_length=3)

