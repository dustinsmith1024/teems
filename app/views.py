from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.template import Context, loader
from django.template import RequestContext
from teams.models import Team, Player, TeamForm, PlayerForm, Coach
from teams.forms import SignUpExtension, TeamPlayerForm
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from forms import SignUpForm, UserCreationFormExtended

@csrf_protect
def signup(request):
    # If coach
    c = {}
    c.update(csrf(request))
    if request.method == 'POST': # If the form has been submitted...
        form = UserCreationFormExtended(request.POST) # A form bound to the POST data
        extension = SignUpExtension(request.POST)
        if form.is_valid() and extension.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            user = form.save()
            # print form.cleaned_data
            user_type = request.POST['user_type']
            if user_type == 'player':
                player = Player(user=user, position=extension.cleaned_data['position'],
                                number=extension.cleaned_data['number']
                               )
                player.save()
                messages.add_message(request, messages.INFO, 'Thanks for joining ' + user.first_name + '!')
                return HttpResponseRedirect(reverse('player', args=(player.id)))
            elif user_type == 'coach':
                coach = Coach(user=user, position=extension.cleaned_data['position'])
                coach.save()
                messages.add_message(request, messages.INFO, 'Thanks for joining ' + user.first_name + '!')
                return HttpResponseRedirect(reverse('coach', args=(coach.id)))
            messages.add_message(request, messages.INFO, 'Sorry, something bad happend creating a new user!')
    else:
        #return HttpResponseRedirect(reverse('mine'))
        form = SignUpForm() # An unbound form
        extension = SignUpExtension()
    return render_to_response("signup.html", {'extension': extension, 'form': form, 'c':c},
                               context_instance=RequestContext(request))

"""
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

def player(request, team_id, player_id):
    player = get_object_or_404(Player, pk=player_id)
    team = get_object_or_404(Team, pk=team_id)
    return render_to_response('teams/player.html', {'team':team, 'player': player}, context_instance=RequestContext(request))


def players(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    return render_to_response('teams/player.html', {'team':team}, context_instance=RequestContext(request))
 
"""
