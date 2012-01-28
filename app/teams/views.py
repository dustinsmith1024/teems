from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.template import Context, loader
from django.template import RequestContext
from teams.models import Team, Member, TeamForm
from teams.forms import TeamJoinForm, TeamPlayerForm, NewMemberForm
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
            messages.add_message(request, messages.SUCCESS, 'Team created!')
            return HttpResponseRedirect(reverse('team_details', args=(team.id,)))
    else:
        form = TeamForm() # An unbound form

    return render_to_response("teams/new.html", {'form': form, 'c':c},
                               context_instance=RequestContext(request))


@login_required
@csrf_protect
def create_and_join(request):
    """Create a new team and join it, should happen right after user reg"""
    c = {}
    c.update(csrf(request))
    if request.method == 'POST': # If the form has been submitted...
        form = TeamForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            team = form.save()
            member = request.user.member
            member.team = team
            member.save()
            messages.add_message(request, messages.SUCCESS, 'Team info created!')
            return HttpResponseRedirect(reverse('team_details', args=(team.id,)))
    else:
        form = TeamForm() # An unbound form

    return render_to_response("teams/create_and_join.html", {'form': form, 'c':c},
                               context_instance=RequestContext(request))


@login_required
@csrf_protect
def join(request):
    """Join a team using team secret"""
    c = {}
    c.update(csrf(request))
    if request.method == 'POST': # If the form has been submitted...
        form = TeamJoinForm(request.POST)
        if form.is_valid(): # All validation rules pass
            team = Team.objects.get(pk=form.cleaned_data['team'])
            if team.secret == form.cleaned_data['secret']:
                member = request.user.member
                member.team = team
                member.save()
                messages.add_message(request, messages.SUCCESS, 'Team joined!')
                return HttpResponseRedirect(reverse('team_details', args=(team.id,)))
            else:
                print 'secret does not match'
        else:
            print 'form not valid'
    else: 
        form = TeamJoinForm()

    return render_to_response("teams/join.html", {'form': form, 'c':c},
                               context_instance=RequestContext(request))



@login_required
@csrf_protect
def new_member(request, team_id):
    # If coach
    team = get_object_or_404(Team, pk=team_id)
    c = {}
    c.update(csrf(request))
    if request.method == 'POST': # If the form has been submitted...
        form = NewMemberForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            user = User(first_name = form.cleaned_data['first_name'],
                        last_name = form.cleaned_data['last_name'],
                        username = form.cleaned_data['username'],
                        email = form.cleaned_data['email'],
                       )
            user.set_password('password')
            user.save()
            member = Member(team=team, user=user, position=form.cleaned_data['position'],
                            number=form.cleaned_data['number'], kind='player',
                           )
            member.save()
            messages.add_message(request, messages.SUCCESS, 'New team member addeed!')
            return HttpResponseRedirect(reverse('user_details', args=(user.username,)))
    else:
        form = NewMemberForm()
    return render_to_response("teams/members/new.html", {'team':team, 'form': form, 'c':c},
                               context_instance=RequestContext(request))



@csrf_protect
def signup(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST': # If the form has been submitted...
        form = SignUpForm(request.POST) # A form bound to the POST data
        extension = SignUpExtension(request.POST)
        if form.is_valid() and extension.is_valid(): # All validation rules pass
            user = form.save()
            user_type = request.POST['user_type']
            member = Member(user=user, kind=user_type)
            member.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Thanks for joining ' + user.first_name + '!')
            return HttpResponseRedirect(reverse('users.user_details', args=(user.username,)))
        messages.add_message(request, messages.ERROR, 'Sorry, something bad happend creating a new user!')
    else:
        form = SignUpForm() # An unbound form
        extension = SignUpExtension(initial={'user_type':'player'})

    return render_to_response("signup.html", {'extension': extension, 'form': form, 'c':c},
                               context_instance=RequestContext(request))





@login_required
@csrf_protect
def edit_member(request, team_id, member_id):
    # If coach
    team = get_object_or_404(Team, pk=team_id)
    member = get_object_or_404(Member, pk=member_id)
    user = member.user
    c = {}
    c.update(csrf(request))
    if request.method == 'POST': # If the form has been submitted...
        form = TeamMemberForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.save()
            member.position = form.cleaned_data['position']
            member.number = form.cleaned_data['number']
            member.save()
            messages.add_message(request, messages.SUCCESS, 'Team member saved!')
            return HttpResponseRedirect(reverse('user_details', args=(user.username,)))
    else:
        form = TeamMemberForm({'first_name':user.first_name, 
                               'last_name': user.last_name, 
                               'number': member.number, 'position': member.position,
                               'email': user.email, 'username': user.username})
    return render_to_response("teams/members/edit.html", {'member': member, 'team':team, 'form': form, 'c':c},
                               context_instance=RequestContext(request))


@login_required
@csrf_protect
def edit(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    c = {}
    c.update(csrf(request))
    if request.method == 'POST': # If the form has been submitted...
        if request.POST.get('delete'):
            team.delete()
            messages.add_message(request, messages.SUCCESS, 'Team Deleted!')
            return HttpResponseRedirect(reverse('teams'))
        form = TeamForm(request.POST, instance=team) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Team info updated!')
            return HttpResponseRedirect(reverse('team_details', args=(team.id,)))
    else:
        form = TeamForm(instance=team) # An unbound form

    # pass action with the id, probably need a cleaner way of doing this
    return render_to_response("teams/edit.html", {'team': team, 'form': form, 'c':c},
                               context_instance=RequestContext(request))

@login_required
@csrf_protect
def mine(request):
    # If coach
    team = Member.objects.get(user=request.user).team
    return render_to_response('teams/detail.html', {'team':team}, context_instance=RequestContext(request))

def team_details(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    return render_to_response('teams/detail.html', {'team':team}, context_instance=RequestContext(request))


def teams(request):
    teams = Team.objects.all()
    return render_to_response('teams/list.html', {'teams':teams}, context_instance=RequestContext(request))



