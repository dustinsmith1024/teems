import sys
from teams.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

"""
  Puts the .player and .team onto every request
  Make it easier to use them in the templates 
  And I dont have to assign in every view
"""
class UserPlayerMiddleware(object):
    def process_request(self, request):
        if request.user.is_authenticated():
            print request.user.id
            coach = Coach.objects.filter(user=request.user)
            player = Player.objects.filter(user=request.user.id)
            if player:
                print player
                request.user.player = player[0]
                if player[0].team:
                    request.user.team = player[0].team
                    print 'TEAM:' + request.user.team.name
		else:
                    if 'team' not in request.path:
                        return HttpResponseRedirect(reverse('join_team'))
                    else:
                        print player[0].team

            if coach:
                request.user.coach = coach[0]
                if coach[0].team: 
                    request.user.team = coach[0].team 
                else:
                    if 'team' not in request.path:
                        return HttpResponseRedirect(reverse('join_team'))

