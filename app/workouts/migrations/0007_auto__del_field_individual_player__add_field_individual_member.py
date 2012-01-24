# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Individual.player'
        db.delete_column('workouts_individual', 'player_id')

        # Adding field 'Individual.member'
        db.add_column('workouts_individual', 'member', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['teams.Member']), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Individual.player'
        db.add_column('workouts_individual', 'player', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['teams.Player']), keep_default=False)

        # Deleting field 'Individual.member'
        db.delete_column('workouts_individual', 'member_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'teams.member': {
            'Meta': {'object_name': 'Member'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Team']", 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True', 'null': 'True'})
        },
        'teams.team': {
            'Meta': {'object_name': 'Team'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mascot': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
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
            'people_needed': ('django.db.models.fields.IntegerField', [], {'default': "'1'"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Team']", 'null': 'True'})
        },
        'workouts.individual': {
            'Meta': {'object_name': 'Individual'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_complete': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_suggested': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Member']"}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'time_suggested': ('django.db.models.fields.TimeField', [], {'null': 'True'}),
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
            'time': ('django.db.models.fields.TimeField', [], {'null': 'True'}),
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
