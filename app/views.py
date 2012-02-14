from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.template import Context, loader
from django.template import RequestContext
from teams.models import Member
from teams.forms import SignUpExtension
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from forms import SignUpForm, UserCreationFormExtended
from django.contrib.auth import authenticate, login
#from django.core.mail import send_mail


@csrf_protect
def signup(request):
    #send_mail('Practice Rescheduled', 'Tomorrows practice is now at 6:00pm.', 'dds1024@gmail.com', ['7128997278@vtext.com'], fail_silently=False)
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
            messages.add_message(request, messages.INFO, 'Thanks for joining ' + user.first_name + '!')
            return HttpResponseRedirect(reverse('user_details', args=(user.username,)))
        messages.add_message(request, messages.INFO, 'Sorry, something bad happend creating a new user!')
    else:
        form = SignUpForm() # An unbound form
        extension = SignUpExtension(initial={'user_type':'player'})

    return render_to_response("signup.html", {'extension': extension, 'form': form, 'c':c},
                               context_instance=RequestContext(request))




