from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import Context, loader
from django.template import RequestContext
from teams.models import Team, Player, TeamForm, PlayerForm
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect

@login_required
@csrf_protect
def mine(request):
    # If coach
    c = {}
    c.update(csrf(request))
    if request.method == 'POST': # If the form has been submitted...
        form = TeamForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            #
            print 'team form save!'
            form.save()
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        #c = {}
        #c.update(csrf(request))
        form = TeamForm() # An unbound form

    #return render_to_response('teams/team_form.html', {
    #    'form': form,
    #     'c'
    #})
    return render_to_response("teams/team_form.html", {'form': form, 'c':c},
                               context_instance=RequestContext(request))
    # else
    """
    team = request.user.get_profile().team
    template = loader.get_template('teams/team_detail.html')
    c = Context({
        'team': team,
    })
    return HttpResponse(template.render(c))
    """
"""
def index(request):
    teams = Team.objects.all()
    #display = ', '.join([team.name for team in teams])
    template = loader.get_template('teams/index.html')
    c = Context({
        'teams': teams,
    })
    return HttpResponse(template.render(c))
    #return HttpResponse("Hello, world. You're at the poll index.")

def details(request, team_id):
    print 'details'
    team = get_object_or_404(Team, pk=team_id)
    return render_to_response('teams/details.html', {'team':team}, context_instance=RequestContext(request))
"""
def captain(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    try:
        chosen_captain = team.player_set.get(pk=request.POST['player'])
    except (KeyError, Player.DoesNotExist):
        return render_to_response('teams/details.html', {
            'team': team,
            'error_message': 'Chose!!!',
        }, context_instance=RequestContext(request))
    else:
        messages.add_message(request, messages.INFO, 'Hello world.')
        #chosen_captain.captain = True
        #chosen.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button
        return HttpResponseRedirect(reverse('team_details', args=(team.id,)))

def roster(request, team_id):
    return HttpResponse("This team: {0}".format(team_id))






