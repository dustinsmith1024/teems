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
from teams.forms import TeamJoinForm, TeamPlayerForm
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
def edit_user(request, username):
    # If coach
    user = get_object_or_404(User, username=username)
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
            # IF COACHE
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
    #IF COACH
    return render_to_response("teams/coach_form.html", {'action': 'update', 'coach': coach, 'form': form, 'c':c},
                               context_instance=RequestContext(request))

    return render_to_response("teams/player_form.html", {'action': 'update', 'player': player, 'form': form, 'c':c},
                               context_instance=RequestContext(request))


def delete_user(request, user_id):
    user = get_object_or_404(User, username=username)
    return render_to_response('users/details.html', {'user': user}, context_instance=RequestContext(request))



def user_details(request, username):
    user = get_object_or_404(User, username=username)
    return render_to_response('users/details.html', {'user': user}, context_instance=RequestContext(request))


def users(request, team_id):
    users = User.objects.all()
    return render_to_response('users/list.html', {'users':users}, context_instance=RequestContext(request))
