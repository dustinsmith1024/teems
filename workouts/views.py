from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import Context, loader
from django.template import RequestContext
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.forms.models import formset_factory, inlineformset_factory
from teams.models import Team, Player
from models import *
from forms import *

def index(request):
    teams = Team.objects.all()
    template = loader.get_template('teams/index.html')
    c = Context({
        'teams': teams,
    })
    return HttpResponse(template.render(c))

def mine(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/?next=%s' % request.path)

    team = Player.objects.get(user=request.user).team
    practices = Practice.objects.filter(team=team).all()
    workouts = Player.objects.get(user=request.user).individual_set.all()
    template = loader.get_template('workouts/workout_list.html')
    c = Context({
        'workout_list': workouts,
        'practice_list': practices,
    })
    return HttpResponse(template.render(c))

def make_step_form(team):
    class StepsForm(forms.Form):
        activities = forms.ModelChoiceField(
                 queryset=Activity.objects.filter(team=team))
        position = forms.IntegerField()
    return StepsForm

@login_required
@csrf_protect
def new_workout(request):
    c = {} 
    c.update(csrf(request))
    w = Workout()
    #WorkoutStepForm = inlineformset_factory(Workout, Step)
    team = Player.objects.get(user=request.user).team
    if request.method == 'POST': # If the form has been submitted...
        workoutForm = WorkoutPlanForm(request.POST) #for update pass in instance=w
        if workoutForm.is_valid():
          print workoutForm
          w = Workout(name=workoutForm.cleaned_data['name'], 
                      kind=workoutForm.cleaned_data['kind'],)
          w.save()
          #personform      = PersonForm(request.POST, instance=person)
          form = WorkoutStepForm(request.POST, instance=w)
          #phoneformset    = PhoneFormSet(request.POST, request.FILES, instance=person)
          #form = WorkoutPlanForm(request.POST)
          if form.is_valid():
              print form
              form.save()
    else:
        # **** CAN PUT THE STEPS FORM INTO A METHOD AND THEN CREATE IT DYNAMICALLY 
        workoutForm = WorkoutPlanForm()
        #form = StepsForm()
        #form.fields['activities'].queryset = Activity.objects.filter(team=team)
        form = formset_factory(make_step_form(team), extra=5)
        """
        formset = formset_factory(StepsForm, extra=5)
        formset = formset(instance=form)
        form = formset
        """
    """
    team = Player.objects.get(user=request.user).team
    activities = Activity.objects.filter(team=team).all()
    template = loader.get_template('workouts/activities_list.html')
    c = Context({
        'activities_list': activities,
    })
    """
    return render_to_response("workouts/workout_form.html", {'action': 'new', 'workout': workoutForm, 'form': form, 'c':c},
                               context_instance=RequestContext(request))


@login_required
def activities(request):
    team = Player.objects.get(user=request.user).team
    activities = Activity.objects.filter(team=team).all()
    template = loader.get_template('workouts/activities_list.html')
    c = Context({
        'activities_list': activities,
    })
    return HttpResponse(template.render(c))

@login_required
def activity(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    template = loader.get_template('workouts/activity.html')
    c = Context({
        'activity': activity,
    })
    return HttpResponse(template.render(c))

@login_required
@csrf_protect
def new_activity(request):
    # If coach
    c = {}
    c.update(csrf(request))
    team = Player.objects.get(user=request.user).team
    if request.method == 'POST': # If the form has been submitted...
        form = ActivityForm(request.POST, instance=team) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            #activity = form.save()
            print form
            a = Activity(team=team, name=form.cleaned_data['name'],
                         kind=form.cleaned_data['kind'],
                         people_needed=form.cleaned_data['people_needed'],
                         location=form.cleaned_data['location'],
                         instructions=form.cleaned_data['instructions'])
            a.save()
            messages.add_message(request, messages.INFO, 'Activity created!')
            return HttpResponseRedirect(reverse('activity', args=(a.id,)))
    else:
        form = ActivityForm() # An unbound form

    return render_to_response("workouts/activity_form.html", {'action': 'new', 'form': form, 'c':c},
                               context_instance=RequestContext(request))

@login_required
def practices(request):
    team = Player.objects.get(user=request.user).team
    practices = Practice.objects.filter(team=team).all()
    template = loader.get_template('workouts/practice_list.html')
    c = Context({
        'practice_list': practices,
    })
    return HttpResponse(template.render(c))

@login_required
def practice(request, practice_id):
    practice = get_object_or_404(Practice, pk=practice_id)
    template = loader.get_template('workouts/practice.html')
    c = Context({
        'practice': practice,
    })
    return HttpResponse(template.render(c))


