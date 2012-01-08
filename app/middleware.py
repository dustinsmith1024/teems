import sys
from teams.models import *
"""
  Puts the .player and .team onto every request
  Make it easier to use them in the templates 
  And I dont have to assign in every view
"""
class UserPlayerMiddleware(object):
    def process_request(self, request):
        if request.user.is_authenticated():
            coach = Coach.objects.filter(user=request.user)
            player = Player.objects.filter(user=request.user)
            if player:
                request.user.player = player[0]
                if player[0].team:
                    request.user.team = player.team 

            if coach:
                request.user.coach = coach[0]
                if coach[0].team: 
                    request.user.team = coach.team 

