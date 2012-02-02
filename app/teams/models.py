from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class Team(models.Model):
    name = models.CharField(max_length=100)
    mascot = models.CharField(max_length=100,)
    city = models.CharField(blank=True, max_length=50, null=True)
    state = models.CharField(blank=True,max_length=2, null=True)
    color = models.CharField(blank=True, null=True, max_length=6)
    secondary_color = models.CharField(blank=True, null=True, max_length=6)
    public = models.BooleanField()
    secret = models.CharField(blank=True, null=True, max_length=30)
    # Player vs Coach vs Whatever
    kind = models.CharField(blank=True, null=True, max_length=50)

    def __unicode__(self):
        return self.name

    def location(self):
        return self.city + ", " + self.state

class TeamForm(ModelForm):
    class Meta:
        model = Team

class Member(models.Model):
    user = models.ForeignKey(User, unique=True, null=True)
    team = models.ForeignKey(Team, null=True)
    # Is the position on the court or position in the office
    position = models.CharField(null=True, max_length=10)
    # Only needed for players, but could be used for coaches in baseball, etc
    number = models.IntegerField(null=True)
    # Player vs Coach vs Whatever
    kind = models.CharField(null=False, max_length=50)
    # year is based on type of team, pro, college, etc
    year = models.CharField(null=True, blank=True, max_length=20)
    city = models.CharField(null=True, blank=True, max_length=50)
    state = models.CharField(blank=True,max_length=2, null=True)
    country = models.CharField(blank=True,max_length=50, null=True)



    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def full_name(self):
        return self.first_name() + " " + self.last_name()

    def name(self):
        return self.full_name()

    def name_and_number(self, seperator="-"):
        return str(self.number) + " " + seperator + " " + self.name()

    def is_coach(self):
        return 'coach' == self.kind

    def is_player(self):
        return 'player' == self.kind

    def coaches(self, member):
        if self.is_coach():
            if member.team == self.team:
                return True
        return False

    def __unicode__(self):
        return self.full_name()



