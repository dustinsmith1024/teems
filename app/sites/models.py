from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=200)
    mascot = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

"""
class User(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
"""
