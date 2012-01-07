# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Activity'
        db.create_table('workouts_activity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Activity Name', max_length=50)),
            ('kind', self.gf('django.db.models.fields.CharField')(default='Kind of Activity', max_length=50)),
            ('people_needed', self.gf('django.db.models.fields.IntegerField')(default='1')),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('instructions', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal('workouts', ['Activity'])

        # Adding model 'Workout'
        db.create_table('workouts_workout', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Workout Plane Name', max_length=50)),
            ('kind', self.gf('django.db.models.fields.CharField')(default='Kind of Workout', max_length=50)),
        ))
        db.send_create_signal('workouts', ['Workout'])

        # Adding M2M table for field activities on 'Workout'
        db.create_table('workouts_workout_activities', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workout', models.ForeignKey(orm['workouts.workout'], null=False)),
            ('activity', models.ForeignKey(orm['workouts.activity'], null=False))
        ))
        db.create_unique('workouts_workout_activities', ['workout_id', 'activity_id'])

        # Adding model 'Practice'
        db.create_table('workouts_practice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workouts.Workout'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Team'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal('workouts', ['Practice'])

        # Adding model 'Individual'
        db.create_table('workouts_individual', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workouts.Workout'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Player'])),
            ('date_complete', self.gf('django.db.models.fields.DateField')()),
            ('date_suggested', self.gf('django.db.models.fields.DateField')()),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal('workouts', ['Individual'])


    def backwards(self, orm):
        
        # Deleting model 'Activity'
        db.delete_table('workouts_activity')

        # Deleting model 'Workout'
        db.delete_table('workouts_workout')

        # Removing M2M table for field activities on 'Workout'
        db.delete_table('workouts_workout_activities')

        # Deleting model 'Practice'
        db.delete_table('workouts_practice')

        # Deleting model 'Individual'
        db.delete_table('workouts_individual')


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
        'workouts.workout': {
            'Meta': {'object_name': 'Workout'},
            'activities': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['workouts.Activity']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'default': "'Kind of Workout'", 'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Workout Plane Name'", 'max_length': '50'})
        }
    }

    complete_apps = ['workouts']
