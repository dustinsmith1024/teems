from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.template import Context, loader
from django.template import RequestContext
from teams.models import Team, Player, TeamForm, PlayerForm
from teams.forms import TeamPlayerForm
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect

@login_required
@csrf_protect
def new(request):
    # If coach
    c = {}
    c.update(csrf(request))
    if request.method == 'POST': # If the form has been submitted...
        form = TeamForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            team = form.save()
            messages.add_message(request, messages.INFO, 'Team info created!')
            return HttpResponseRedirect(reverse('view', args=(team.id,)))
    else:
        form = TeamForm() # An unbound form

    return render_to_response("teams/team_form.html", {'action': 'new', 'form': form, 'c':c},
                               context_instance=RequestContext(request))

@login_required
@csrf_protect
def new_player(request, team_id):
    # If coach
    team = get_object_or_404(Team, pk=team_id)
    c = {}
    c.update(csrf(request))
    if request.method == 'POST': # If the form has been submitted...
        form = TeamPlayerForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            print form.cleaned_data
            user = User(first_name = form.cleaned_data['first_name'],
                        last_name = form.cleaned_data['last_name'],
                        username = form.cleaned_data['username'],
                        email = form.cleaned_data['email'],
                       )
            user.set_password('password')
            user.save()
            player = Player(team=team, user=user, position=form.cleaned_data['position'],
                            number=form.cleaned_data['number']
                           )
            player.save()
            messages.add_message(request, messages.INFO, 'Player created!')
            return HttpResponseRedirect(reverse('player', args=(team.id, player.id)))
    else:
        form = TeamPlayerForm()
    return render_to_response("teams/player_form.html", {'action': 'new', 'team':team, 'form': form, 'c':c},
                               context_instance=RequestContext(request))


@login_required
@csrf_protect
def edit_player(request, team_id, player_id):
    # If coach
    team = get_object_or_404(Team, pk=team_id)
    player = get_object_or_404(Player, pk=player_id)
    user = player.user
    c = {}
    c.update(csrf(request))
    if request.method == 'POST': # If the form has been submitted...
        form = TeamPlayerForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.save()
            player.position = form.cleaned_data['position']
            player.number=form.cleaned_data['number']
            player.save()
            messages.add_message(request, messages.SUCCESS, 'Player updated!')
            return HttpResponseRedirect(reverse('player', args=(team.id, player.id)))
    else:
        form = TeamPlayerForm({'first_name':user.first_name, 
                               'last_name': user.last_name, 
                               'number': player.number, 'position': player.position,
                               'email': user.email, 'username': user.username})
    return render_to_response("teams/player_form.html", {'action': 'update', 'player': player, 'team':team, 'form': form, 'c':c},
                               context_instance=RequestContext(request))



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
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button
        return HttpResponseRedirect(reverse('team_details', args=(team.id,)))

@login_required
@csrf_protect
def update(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    c = {}
    c.update(csrf(request))
    if request.method == 'POST': # If the form has been submitted...
        form = TeamForm(request.POST, instance=team) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            messages.add_message(request, messages.INFO, 'Team info updated!')
            return HttpResponseRedirect(reverse('view', args=(team.id,)))
    else:
        form = TeamForm(instance=team) # An unbound form

    # pass action with the id, probably need a cleaner way of doing this
    return render_to_response("teams/team_form.html", {'action': str(team.id) + '/update', 'form': form, 'c':c},
                               context_instance=RequestContext(request))

@login_required
@csrf_protect
def mine(request):
    # If coach
    team = Player.objects.get(user=request.user).team
    return render_to_response('teams/team_detail.html', {'team':team}, context_instance=RequestContext(request))

def view(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    #RosterForm = inlineformset_factory(Team, Player)
    #formset = RosterForm(instance=team)
    #print formset
    return render_to_response('teams/team_detail.html', {'team':team}, context_instance=RequestContext(request))

def player(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    return render_to_response('teams/player.html', {'player': player}, context_instance=RequestContext(request))


def players(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    return render_to_response('teams/player.html', {'team':team}, context_instance=RequestContext(request))
 
def coach(request, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id)
    return render_to_response('teams/coach.html', {'coach': coach}, context_instance=RequestContext(request))


