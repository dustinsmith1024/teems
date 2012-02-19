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
from teams.models import Team, Member
from models import *
from forms import *
import operator


def index(request):
    teams = Team.objects.all()
    c = Context({
        'teams': teams,
    })
    return render_to_response("teams/index.html", c,
                               context_instance=RequestContext(request))

@login_required
def mine(request):
    team = Member.objects.get(user=request.user).team
    practices = Practice.objects.filter(team=team).all()
    individuals = Member.objects.get(user=request.user).individual_set.all()
    for index, i in enumerate(individuals):
        individuals[index].date = i.date_suggested
        individuals[index].time = i.time_suggested
    combined = list(practices)
    combined.extend(list(individuals))
    combined.sort(key=operator.attrgetter('date', 'time'))
    show_date = False
    saved_date = False
    """ Put in some show_dates to help with formating on frontend """
    for index, i in enumerate(combined):
        combined[index].show_date = True
        if saved_date and saved_date == i.date:
            combined[index].show_date = False
        saved_date = i.date
    c = Context({
        #'individuals_list': individuals,
        #'practice_list': practices,
        'combined': combined,
    })
    return render_to_response("workouts/mine.html", c,
                               context_instance=RequestContext(request))

@login_required
def workouts(request):
    practices = Practice.objects.all()
    individuals = Individual.objects.all()
    i_set = []
    date = None
    time = None
    """
    for i in individual:
       #loop em all
    """
    workouts = Workout.objects.all()
    c = Context({
        'workout_list': workouts,
        'practice_list': practices,
        'individuals_list': individuals,
    })
    return render_to_response("workouts/list.html", c,
                               context_instance=RequestContext(request))


@login_required
@csrf_protect
def new_workout(request):
    c = {} 
    c.update(csrf(request))
    w = Workout()
    team = Member.objects.get(user=request.user).team
    if request.method == 'POST': # If the form has been submitted...
        workoutForm = WorkoutPlanForm(request.POST) #for update pass in instance=w
        if workoutForm.is_valid():
          workout = Workout(name=workoutForm.cleaned_data['name'], 
                      kind=workoutForm.cleaned_data['kind'],)
          formset_cls = formset_factory(make_step_form(team))
          form = formset_cls(request.POST)
          if form.is_valid():
              workout.save()
              for f in form:
                  if f.cleaned_data.get('activities'):
                      step = Step(workout=workout, activity=f.cleaned_data['activities'],
                                  position=f.cleaned_data['position'])
                      step.save()
              messages.add_message(request, messages.SUCCESS, 'Workout Created!')
              return HttpResponseRedirect(reverse('workout_details', args=(workout.id,)))
                  
    else:
        workoutForm = WorkoutPlanForm()
        form = formset_factory(make_step_form(team), extra=5)
    return render_to_response("workouts/new.html", {'action': 'new', 'workout': workoutForm, 'form': form, 'c':c},
                               context_instance=RequestContext(request))



@login_required
@csrf_protect
def edit_workout(request, workout_id):
    """
      Allows updating a workout and adding new activities on the fly
    """
    c = {}
    c.update(csrf(request))
    workout = get_object_or_404(Workout, pk=workout_id)
    team = Member.objects.get(user=request.user).team
    if request.method == 'POST': # If the form has been submitted...
        if request.POST.get('delete'):
          workout.delete()
          messages.add_message(request, messages.SUCCESS, 'Workout Deleted!')
          return HttpResponseRedirect(reverse('workouts'))
        workoutForm = WorkoutForm(request.POST) #for update pass in instance=w
        if workoutForm.is_valid():
          workout.name = workoutForm.cleaned_data['name']
          workout.kind = workoutForm.cleaned_data['kind']
          workout.save()
          for k in request.POST:
              if k.find("step_id") > 0:
                  if request.POST[k] != 'new': # just searching for step_id in the name - if not found then -1
                      num = k.split('-')[0]
                      step = Step.objects.get(pk=request.POST[k])
                      step.position = request.POST[num + '-position']
                      step.activity = Activity.objects.get(pk=request.POST[num + '-activities'])
                      step.duration = request.POST[num + '-duration']
                      step.save()
                  else:
                      num = k.split('-')[0]
                      if request.POST[num + '-activities']:
                          step = Step(workout=workout, activity=Activity.objects.get(pk=request.POST[num + '-activities']),
                                      position=request.POST[num + '-position'])
                          step.save()
          messages.add_message(request, messages.SUCCESS, 'Workout Updated!')
          if request.POST['save'] == 'add_another':
              return HttpResponseRedirect(reverse('edit_workout', args=(workout.id,)))
          else:
              return HttpResponseRedirect(reverse('workout_details', args=(workout.id,)))
    else:
        workoutForm = WorkoutForm(instance=workout)
        steps = Step.objects.filter(workout=workout)
        possible_activities = Activity.objects.filter(team=team)
    return render_to_response("workouts/edit.html", 
                              {'workout': workout,
                               'workout_form': workoutForm, 'activities': possible_activities, 
                               'steps':steps, 'c':c, 'current_step': len(steps), 'next_step': len(steps) + 1},
                               context_instance=RequestContext(request))


@login_required
@csrf_protect
def assign_workout(request, workout_id):
    """FIX THIS AND MAKE A FORM FOR IT
    """
    c = {}
    c.update(csrf(request))
    workout = get_object_or_404(Workout, pk=workout_id)
    team = Member.objects.get(user=request.user).team
    if request.method == 'POST': # If the form has been submitted...
          form = IndividualAssignForm(request.POST)
          if form.is_valid():
              member = Member.objects.get(pk=request.POST['member'])
              individual = Individual(workout=workout, member=member, 
                                      date_suggested=form.cleaned_data['date_suggested'],
                                      time_suggested=form.cleaned_data['time_suggested'],
                                     )
          try:
              individual.full_clean()
              individual.save()
              messages.add_message(request, messages.SUCCESS, 'Individual scheduled!')
              if not request.POST.get('add_another'):
                  return HttpResponseRedirect(reverse('workout_details', args=(workout.id,)))
              else:
                  return HttpResponseRedirect(reverse('assign_workout', args=(workout.id,)))
          except Exception:
              messages.add_message(request, messages.ERROR, 'Something happend with form!')
              return render_to_response("workouts/assign.html", {'form':form, 'workout': workout, 'team':team, 'c':c},
                                        context_instance=RequestContext(request))

    else:
        print 'here'
        form = IndividualAssignForm()

    return render_to_response("workouts/assign.html", {'form': form, 'workout': workout, 'team':team, 'c':c},
                               context_instance=RequestContext(request))


@login_required
@csrf_protect
def schedule_practice(request, workout_id):
    """
    """
    c = {}
    c.update(csrf(request))
    workout = get_object_or_404(Workout, pk=workout_id)
    team = Member.objects.get(user=request.user).team
    if request.method == 'POST': # If the form has been submitted...
          form = PracticeForm(request.POST)
          if form.is_valid():
              practice = Practice(workout=workout, team=team,
                                  date=form.cleaned_data['date'],
                                  time=form.cleaned_data['time'],
                                  notes=form.cleaned_data['notes'],
                                  )
              practice.save()
              messages.add_message(request, messages.SUCCESS, 'Practice scheduled!')
              return HttpResponseRedirect(reverse('practice', args=(practice.id,)))

    else:
        form = PracticeForm()

    return render_to_response("workouts/practices/schedule.html", {'form':form, 'workout': workout, 'team':team, 'c':c},
                               context_instance=RequestContext(request))


@login_required
@csrf_protect
def edit_practice(request, workout_id, practice_id):
    """
    """
    c = {} 
    c.update(csrf(request))
    workout = get_object_or_404(Workout, pk=workout_id)
    team = Member.objects.get(user=request.user).team
    practice = Practice.objects.get(pk=practice_id)
    if request.method == 'POST': # If the form has been submitted...
          if request.POST.get('cancel'):
              practice.delete()
              messages.add_message(request, messages.SUCCESS, 'Practice Cancelled!')
              return HttpResponseRedirect(reverse('workouts'))
          form = PracticeForm(request.POST)
          if form.is_valid():
              practice.date=form.cleaned_data['date']
              practice.time=form.cleaned_data['time']
              practice.notes=form.cleaned_data['notes']
              practice.save()
              messages.add_message(request, messages.SUCCESS, 'Practice Updated!')
              return HttpResponseRedirect(reverse('practice', args=(practice.id,)))
    else:
        form = PracticeForm(instance=practice)

    return render_to_response("workouts/practices/edit.html", {'form':form, 'practice': practice, 'workout': workout, 'team':team, 'c':c},
                               context_instance=RequestContext(request))




@login_required
def activities(request):
    team = Member.objects.get(user=request.user).team
    activities = Activity.objects.filter(team=team).all()
    return render_to_response("workouts/activities/activities_list.html", {'activities_list':activities},
                               context_instance=RequestContext(request))
    #return HttpResponse(template.render(c))

@login_required
def activity(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    c = Context({
        'activity': activity,
    })
    return render_to_response("workouts/activities/detail.html", c,
                               context_instance=RequestContext(request))

@login_required
@csrf_protect
def new_activity(request):
    # If coach
    c = {}
    c.update(csrf(request))
    team = Member.objects.get(user=request.user).team
    if request.method == 'POST': # If the form has been submitted...
        form = ActivityForm(request.POST, instance=team) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            a = Activity(team=team, name=form.cleaned_data['name'],
                         kind=form.cleaned_data['kind'],
                         people_needed=form.cleaned_data['people_needed'],
                         location=form.cleaned_data['location'],
                         instructions=form.cleaned_data['instructions'])
            a.save()
            messages.add_message(request, messages.SUCCESS, 'Activity created!')
            return HttpResponseRedirect(reverse('activity', args=(a.id,)))
    else:
        form = ActivityForm() # An unbound form

    return render_to_response("workouts/activities/new.html", {'action': 'new', 'form': form, 'c':c},
                               context_instance=RequestContext(request))


@login_required
@csrf_protect
def edit_activity(request, activity_id):
    c = {}
    c.update(csrf(request))
    activity = get_object_or_404(Activity, pk=activity_id)
    if request.method == 'POST': # If the form has been submitted...
        if request.POST.get('cancel'):
            activity.delete()
            messages.add_message(request, messages.SUCCESS, 'Activity Deleted!')
            return HttpResponseRedirect(reverse('activities'))
        form = ActivityForm(request.POST, instance=activity) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            activity.name=form.cleaned_data['name']
            activity.kind=form.cleaned_data['kind']
            activity.people_needed=form.cleaned_data['people_needed']
            activity.location=form.cleaned_data['location']
            activity.instructions=form.cleaned_data['instructions']
            activity.save()
            messages.add_message(request, messages.SUCCESS, 'Activity updated!')
            return HttpResponseRedirect(reverse('activity', args=(activity.id,)))
    else:
        form = ActivityForm(instance=activity) # An unbound form

    return render_to_response("workouts/activities/edit.html", { 'activity': activity, 'form': form, 'c':c},
                               context_instance=RequestContext(request))



@login_required
def practices(request):
    team = Member.objects.get(user=request.user).team
    practices = Practice.objects.filter(team=team).all()
    c = Context({
        'practice_list': practices,
    })
    return render_to_response("workouts/practices/list.html", c,
                               context_instance=RequestContext(request))
    return HttpResponse(template.render(c))

@login_required
def practice(request, practice_id):
    practice = get_object_or_404(Practice, pk=practice_id)
    c = Context({
        'practice': practice,
    })
    return render_to_response("workouts/practices/detail.html", c,
                               context_instance=RequestContext(request))


@login_required
def individual(request, individual_id):
    individual = get_object_or_404(Individual, pk=individual_id)
    workout = individual.workout
    c = Context({
        'individual': individual,
        'workout': workout,
    })
    return render_to_response("workouts/individuals/detail.html", c,
                               context_instance=RequestContext(request))

@login_required
def workout(request, workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    c = Context({
        'workout': workout,
    })
    return render_to_response("workouts/detail.html", c,
                               context_instance=RequestContext(request))


@login_required
@csrf_protect
def edit_individual(request, individual_id):
    """
    """
    c = {}
    c.update(csrf(request))
    individual = get_object_or_404(Individual, pk=individual_id)
    workout = individual.workout
    form = IndividualEditForm(instance=individual)
    if request.method == 'POST':
        if request.POST.get('cancel'):
          individual.delete()
          messages.add_message(request, messages.SUCCESS, 'Individual Cancelled!')
          return HttpResponseRedirect(reverse('workouts'))
        form = IndividualEditForm(request.POST)
        if form.is_valid():
            individual.date_complete = form.cleaned_data['date_complete']
            individual.date_suggested = form.cleaned_data['date_suggested']
            individual.time_suggested = form.cleaned_data['time_suggested']
            individual.notes = form.cleaned_data['notes']
            individual.save()
            messages.add_message(request, messages.SUCCESS, 'Individual Updated!')
            return HttpResponseRedirect(reverse('individual', args=(individual.id,)))

    return render_to_response("workouts/individuals/edit.html", {'form': form, 'individual': individual, 'c':c},
                               context_instance=RequestContext(request))


