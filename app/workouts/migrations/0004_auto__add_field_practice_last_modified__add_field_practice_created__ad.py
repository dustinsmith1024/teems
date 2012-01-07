# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Practice.last_modified'
        db.add_column('workouts_practice', 'last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2011, 12, 4), blank=True), keep_default=False)

        # Adding field 'Practice.created'
        db.add_column('workouts_practice', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2011, 12, 4), blank=True), keep_default=False)

        # Adding field 'Individual.last_modified'
        db.add_column('workouts_individual', 'last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2011, 12, 4), blank=True), keep_default=False)

        # Adding field 'Individual.created'
        db.add_column('workouts_individual', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2011, 12, 4), blank=True), keep_default=False)

        # Changing field 'Individual.date_complete'
        db.alter_column('workouts_individual', 'date_complete', self.gf('django.db.models.fields.DateField')(null=True))

        # Adding field 'Activity.last_modified'
        db.add_column('workouts_activity', 'last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2011, 12, 4), blank=True), keep_default=False)

        # Adding field 'Activity.created'
        db.add_column('workouts_activity', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2011, 12, 4), blank=True), keep_default=False)

        # Adding field 'Workout.last_modified'
        db.add_column('workouts_workout', 'last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2011, 12, 4), blank=True), keep_default=False)

        # Adding field 'Workout.created'
        db.add_column('workouts_workout', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2011, 12, 4), blank=True), keep_default=False)

        # Adding field 'Step.last_modified'
        db.add_column('workouts_step', 'last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2011, 12, 4), blank=True), keep_default=False)

        # Adding field 'Step.created'
        db.add_column('workouts_step', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2011, 12, 4), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Practice.last_modified'
        db.delete_column('workouts_practice', 'last_modified')

        # Deleting field 'Practice.created'
        db.delete_column('workouts_practice', 'created')

        # Deleting field 'Individual.last_modified'
        db.delete_column('workouts_individual', 'last_modified')

        # Deleting field 'Individual.created'
        db.delete_column('workouts_individual', 'created')

        # Changing field 'Individual.date_complete'
        db.alter_column('workouts_individual', 'date_complete', self.gf('django.db.models.fields.DateField')(default=datetime.date(2011, 12, 4)))

        # Deleting field 'Activity.last_modified'
        db.delete_column('workouts_activity', 'last_modified')

        # Deleting field 'Activity.created'
        db.delete_column('workouts_activity', 'created')

        # Deleting field 'Workout.last_modified'
        db.delete_column('workouts_workout', 'last_modified')

        # Deleting field 'Workout.created'
        db.delete_column('workouts_workout', 'created')

        # Deleting field 'Step.last_modified'
        db.delete_column('workouts_step', 'last_modified')

        # Deleting field 'Step.created'
        db.delete_column('workouts_step', 'created')


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
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructions': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'default': "'Kind of Activity'", 'max_length': '50'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Activity Name'", 'max_length': '50'}),
            'people_needed': ('django.db.models.fields.IntegerField', [], {'default': "'1'"})
        },
        'workouts.individual': {
            'Meta': {'object_name': 'Individual'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_complete': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_suggested': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Player']"}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workouts.Workout']"})
        },
        'workouts.practice': {
            'Meta': {'object_name': 'Practice'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Team']"}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workouts.Workout']"})
        },
        'workouts.step': {
            'Meta': {'ordering': "['workout', 'position']", 'object_name': 'Step'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workouts.Activity']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workouts.Workout']"})
        },
        'workouts.workout': {
            'Meta': {'object_name': 'Workout'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'default': "'Kind of Workout'", 'max_length': '50'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Workout Plane Name'", 'max_length': '50'}),
            'plan': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['workouts.Activity']", 'through': "orm['workouts.Step']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['workouts']
