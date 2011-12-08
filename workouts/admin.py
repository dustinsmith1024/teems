from workouts.models import *
from django.contrib import admin


class StepAdmin(admin.TabularInline):
    model = Step
    extra = 1
    sortable_field_name = "position"
    fields = ['position', 'activity']
    #fields = ['activity','workout','order']
    #list_display = ['order', 'activity', 'workout']

class WorkoutAdmin(admin.ModelAdmin):
    fields = ['name','kind']
    list_filter = ['kind']
    inlines = (StepAdmin,)

class ActivitiesAdmin(admin.ModelAdmin):
    fields = ['name','kind','people_needed','location','instructions']
    list_filter = ['kind']

class PracticeAdmin(admin.ModelAdmin):
    fields = ['workout', 'team', 'date', 'notes']
    list_display = ['date', 'workout']

class IndividualAdmin(admin.ModelAdmin):
    fields = ['workout', 'player', 'date_suggested', 'date_complete', 'notes']
    list_display = ['workout', 'player', 'date_suggested', 'date_complete']

"""
class TeamAdmin(admin.ModelAdmin):
    fields = ['name','mascot', 'city', 'state']
    inlines = [PlayerInline]
    list_display = ('name', 'mascot')
    search_fields = ['name', 'mascot', 'city', 'state']
"""

#admin.site.register(Team, TeamAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Activity, ActivitiesAdmin)
#admin.site.register(Step, StepAdmin)
admin.site.register(Practice, PracticeAdmin)
admin.site.register(Individual, IndividualAdmin)

