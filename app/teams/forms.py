from teams.models import Team, Player
from django import forms

class TeamPlayerForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    number = forms.IntegerField()
    position = forms.CharField(max_length=3)
    #TODO: Autocreate this by first letter, last name, then number -> It should always be unique
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=100)
