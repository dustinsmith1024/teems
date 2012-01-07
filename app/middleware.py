import sys

"""
  Puts the .player and .team onto every request
  Make it easier to use them in the templates 
  And I dont have to assign in every view
"""
class UserPlayerMiddleware(object):
    def process_request(self, request):
        if request.user:
            player = request.user.player_set.get()
            request.user.player = player
            request.user.team = player.team

