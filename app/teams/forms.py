from teams.models import Team, Player
from django import forms
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

class TeamPlayerForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    number = forms.IntegerField()
    position = forms.CharField(max_length=3)
    #TODO: Autocreate this by first letter, last name, then number -> It should always be unique
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=100)

class SignUpExtension(forms.Form):
    position = forms.CharField(max_length=10)
    number = forms.IntegerField()
    user_type = forms.ChoiceField(widget=RadioSelect(),
                    choices=[['player','Player'],['coach','Coach, Manager, Other']])


