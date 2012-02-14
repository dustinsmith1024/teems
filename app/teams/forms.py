from teams.models import Team
from django import forms
from django.forms.widgets import Select, RadioSelect, CheckboxSelectMultiple
from django.contrib.localflavor.us.forms import USPhoneNumberField

class TeamPlayerForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    number = forms.IntegerField(required=False)
    position = forms.CharField(max_length=3, required=False)
    #TODO: Autocreate this by first letter, last name, then number -> It should always be unique
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=100)
    phone = USPhoneNumberField(required=False)

class SignUpExtension(forms.Form):
    user_type = forms.ChoiceField(widget=RadioSelect(),
                    choices=[['player','I am a Player'],['coach','I am a Coach, Manager, Other']]
                    , label='What type of user are you?')


class TeamJoinForm(forms.Form):
    secret = forms.CharField(max_length=30)
    choice = [(t.id, t.name) for t in Team.objects.all()]
    team = forms.ChoiceField(widget=Select(),
                             choices=choice)


class NewMemberForm(forms.Form):
    """For coaches to add a new member to a team"""
    user_type = forms.ChoiceField(widget=RadioSelect(),
                    choices=[['player','Player'],['coach','Coach, Manager, Other']]
                    , label='What type of team member?')
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    number = forms.IntegerField(required=False)
    position = forms.CharField(required=False)
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=100)


