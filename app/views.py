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
from django.contrib.auth import authenticate, login

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
                player = Player(user=user)
                player.save()
            elif user_type == 'coach':
                coach = Coach(user=user)
                coach.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            login(request, user)
            messages.add_message(request, messages.INFO, 'Thanks for joining ' + user.first_name + '!')
            return HttpResponseRedirect(reverse('join_team'))
        messages.add_message(request, messages.INFO, 'Sorry, something bad happend creating a new user!')
    else:
        #return HttpResponseRedirect(reverse('mine'))
        form = SignUpForm() # An unbound form
        extension = SignUpExtension(initial={'user_type':'player'})
    return render_to_response("signup.html", {'extension': extension, 'form': form, 'c':c},
                               context_instance=RequestContext(request))

