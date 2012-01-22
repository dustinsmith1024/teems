from django import forms
from django.forms.widgets import Select, RadioSelect, CheckboxSelectMultiple

class EditUserForm(forms.Form):
    user_type = forms.ChoiceField(widget=RadioSelect(),
                    choices=[['player','I am a Player'],['coach','I am a Coach, Manager, Other']]
                    , label='User Type')
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    number = forms.IntegerField(required=False)
    position = forms.CharField(max_length=3, required=False)
    #TODO: Autocreate this by first letter, last name, then number -> It should always be unique
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=100)

