from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class Team(models.Model):
    name = models.CharField(max_length=100)
    mascot = models.CharField(max_length=100,)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=2, null=True)

    def __unicode__(self):
        return self.name

    def location(self):
        return self.city + ", " + self.state

class Player(models.Model):
    user = models.ForeignKey(User, unique=True, null=True)
    team = models.ForeignKey(Team)
    #first_name = models.CharField(max_length=100)
    #last_name = models.CharField(max_length=100)
    number = models.IntegerField()
    position = models.CharField(null=True,max_length=10)

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def full_name(self):
        return self.first_name() + " " + self.last_name()

    def __unicode__(self):
        return self.full_name()


class TeamForm(ModelForm):
    class Meta:
        model = Team


class PlayerForm(ModelForm):
    #s = forms.ModelMultipleChoiceField(queryset=Team.objects.all())
    class Meta:
        model = Player


