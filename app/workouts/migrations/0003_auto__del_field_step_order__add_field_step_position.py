# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Step.order'
        db.delete_column('workouts_step', 'order')

        # Adding field 'Step.position'
        db.add_column('workouts_step', 'position', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Step.order'
        db.add_column('workouts_step', 'order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1), keep_default=False)

        # Deleting field 'Step.position'
        db.delete_column('workouts_step', 'position')


    models = {
        'teams.player': {
            'Meta': {'object_name': 'Player'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Team']"})
        },
        'teams.team': {
            'Meta': {'object_name': 'Team'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mascot': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'})
        },
        'workouts.activity': {
            'Meta': {'object_name': 'Activity'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructions': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'default': "'Kind of Activity'", 'max_length': '50'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Activity Name'", 'max_length': '50'}),
            'people_needed': ('django.db.models.fields.IntegerField', [], {'default': "'1'"})
        },
        'workouts.individual': {
            'Meta': {'object_name': 'Individual'},
            'date_complete': ('django.db.models.fields.DateField', [], {}),
            'date_suggested': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Player']"}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workouts.Workout']"})
        },
        'workouts.practice': {
            'Meta': {'object_name': 'Practice'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Team']"}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workouts.Workout']"})
        },
        'workouts.step': {
            'Meta': {'ordering': "['workout', 'position']", 'object_name': 'Step'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workouts.Activity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workouts.Workout']"})
        },
        'workouts.workout': {
            'Meta': {'object_name': 'Workout'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'default': "'Kind of Workout'", 'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Workout Plane Name'", 'max_length': '50'}),
            'plan': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['workouts.Activity']", 'through': "orm['workouts.Step']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['workouts']
