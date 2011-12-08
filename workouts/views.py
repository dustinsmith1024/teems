from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.template import Context, loader
from django.template import RequestContext
from teams.models import Team, Player

def index(request):
    teams = Team.objects.all()
    #display = ', '.join([team.name for team in teams])
    template = loader.get_template('teams/index.html')
    c = Context({
        'teams': teams,
    })
    return HttpResponse(template.render(c))
    #return HttpResponse("Hello, world. You're at the poll index.")

def mine(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/?next=%s' % request.path)

    workouts = Player.objects.get(user=request.user).individual_set.all()
    template = loader.get_template('workouts/workout_list.html')
    c = Context({
        'workout_list': workouts,
    })
    return HttpResponse(template.render(c))

