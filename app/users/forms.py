from django import forms
from django.forms.widgets import Select, RadioSelect, CheckboxSelectMultiple
from django.contrib.localflavor.us.forms import USPhoneNumberField

class EditUserForm(forms.Form):
    user_type = forms.ChoiceField(
                    choices=[['player','Player'],['coach','Coach, Manager, Other']]
                    , label='User Type')
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    number = forms.IntegerField(required=False)
    position = forms.CharField(max_length=10, required=False)
    year = forms.CharField(max_length=20, required=False)
    #TODO: Autocreate this by first letter, last name, then number -> It should always be unique
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=100)
    phone = USPhoneNumberField(required=False)
    city = forms.CharField(required=False)
    state = forms.CharField(max_length=2, required=False)
    country = forms.CharField(max_length=50, required=False)
