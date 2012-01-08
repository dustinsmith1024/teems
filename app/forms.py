from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationFormExtended(UserCreationForm): 
    def __init__(self, *args, **kwargs): 
        super(UserCreationFormExtended, self).__init__(*args, **kwargs) 
        self.fields['first_name'].required = True 
        self.fields['last_name'].required = True 
    class Meta: 
        model = User 
        fields = ('username', 'email', 'first_name', 'last_name') 
