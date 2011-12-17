from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import Context, loader
from django.template import RequestContext
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.forms.models import inlineformset_factory
from teams.models import Team, Player
from models import *
from forms import *

def index(request):
    teams = Team.objects.all()
    #display = ', '.join([team.name for team in teams])
    template = loader.get_template('teams/index.html')
    c = Context({
        'teams': teams,
    })
    return HttpResponse(template.render(c))
    #return HttpResponse("Hello, world. You're at the poll index.")

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

@login_required
@csrf_protect
def new_workout(request):
    c = {} 
    c.update(csrf(request))
    w = Workout()
    WorkoutStepForm = inlineformset_factory(Workout, Step)
    if request.method == 'POST': # If the form has been submitted...
        #form = WorkoutPlanForm(request.POST)
        if form.is_valid():
            print form
    else:
        workout = WorkoutPlanForm(instance=w)
        form = WorkoutStepForm(instance=workout)
    """
    team = Player.objects.get(user=request.user).team
    activities = Activity.objects.filter(team=team).all()
    template = loader.get_template('workouts/activities_list.html')
    c = Context({
        'activities_list': activities,
    })
    """
    return render_to_response("workouts/workout_form.html", {'action': 'new', 'form': form, 'c':c},
                               context_instance=RequestContext(request))

"""
def manage_books(request, author_id):
    author = Author.objects.get(pk=author_id)
    BookInlineFormSet = inlineformset_factory(Author, Book)
    if request.method == "POST":
        formset = BookInlineFormSet(request.POST, request.FILES, instance=author)
        if formset.is_valid():
            formset.save()
            # Do something.
    else:
        formset = BookInlineFormSet(instance=author)
    return render_to_response("manage_books.html", {
        "formset": formset,
    })
"""

def activities(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/?next=%s' % request.path)

    team = Player.objects.get(user=request.user).team
    activities = Activity.objects.filter(team=team).all()
    template = loader.get_template('workouts/activities_list.html')
    c = Context({
        'activities_list': activities,
    })
    return HttpResponse(template.render(c))

def activity(request, activity_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/?next=%s' % request.path)

    #team = Player.objects.get(user=request.user).team
    #team = get_object_or_404(Team, pk=team_id)
    activity = get_object_or_404(Activity, pk=activity_id)
    template = loader.get_template('workouts/activity.html')
    c = Context({
        'activity': activity,
    })
    return HttpResponse(template.render(c))

def new_activity(request):
    pass

def practices(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/?next=%s' % request.path)

    team = Player.objects.get(user=request.user).team
    practices = Practice.objects.filter(team=team).all()
    template = loader.get_template('workouts/practice_list.html')
    c = Context({
        'practice_list': practices,
    })
    return HttpResponse(template.render(c))

def practice(request, practice_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/?next=%s' % request.path)

    practice = get_object_or_404(Practice, pk=practice_id)
    template = loader.get_template('workouts/practice.html')
    c = Context({
        'practice': practice,
    })
    return HttpResponse(template.render(c))


