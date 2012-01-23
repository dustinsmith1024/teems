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
from users.forms import EditUserForm
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


@csrf_protect
def update_user(request, username):
    user = get_object_or_404(User, username=username)
    member = user.member_set.get()
    c = {}
    c.update(csrf(request))
    if request.method == 'POST': # If the form has been submitted...
        form = EditUserForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            member.number = form.cleaned_data['number']
            member.position = form.cleaned_data['position']
            member.kind = form.cleaned_data['user_type']
            user.save()
            member.save()
            messages.add_message(request, messages.INFO, 'User details updated!')
            return HttpResponseRedirect(reverse('user_details', args=(user.username,)))
        messages.add_message(request, messages.INFO, 'Sorry, something bad happend updatting a new user!')
    else:
        form = EditUserForm({'username': user.username,
                             'first_name': user.first_name,
                             'last_name': user.last_name,
                             'email': user.email,
                             'user_type': member.kind,
                             'position': member.position,
                             'number': member.number,
                            }) # An unbound form
    return render_to_response("users/update.html", {'form': form, 'c':c, 'edit_user':user},
                               context_instance=RequestContext(request))


def delete_user(request, user_id):
    user = get_object_or_404(User, username=username)
    return render_to_response('users/details.html', {'user': user}, context_instance=RequestContext(request))


def user_details(request, username):
    print username
    user = get_object_or_404(User, username=username)
    member = user.member_set.get()
    team = member.team
    return render_to_response('users/details.html', {'team':team, 'member':member, 'view_user': user}, context_instance=RequestContext(request))


def users(request, team_id):
    users = User.objects.all()
    return render_to_response('users/list.html', {'users':users}, context_instance=RequestContext(request))
