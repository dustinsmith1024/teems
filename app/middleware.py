import sys
from teams.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

"""
  Puts the .member and .team onto every request
  Make it easier to use them in the templates 
  And I dont have to assign in every view
"""
class UserPlayerMiddleware(object):
    def process_request(self, request):
        if request.user.is_authenticated():
            member = Member.objects.filter(user=request.user.id)
            if member:
                request.user.member = member[0]
                if member[0].team:
                    request.user.team = member[0].team
                else:
                    print 'No Team connection Found!'
            else:
                print 'No Member connection Found!'


