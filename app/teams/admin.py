from teams.models import *
from django.contrib import admin


class PlayerAdmin(admin.ModelAdmin):
    fields = ['position', 'number', 'user']
    list_filter = ['position']

class PlayerInline(admin.TabularInline):
    model = Player
    extra = 1
    list_display = ('position', 'number','full_name', 'first_name', 'last_name')


class TeamAdmin(admin.ModelAdmin):
    fields = ['name', 'color', 'mascot', 'city', 'state']
    inlines = [PlayerInline]
    list_display = ('name', 'mascot')
    search_fields = ['name', 'mascot', 'city', 'state']

admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
