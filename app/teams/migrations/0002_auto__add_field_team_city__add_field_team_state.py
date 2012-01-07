# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Team.city'
        db.add_column('teams_team', 'city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True), keep_default=False)

        # Adding field 'Team.state'
        db.add_column('teams_team', 'state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Team.city'
        db.delete_column('teams_team', 'city')

        # Deleting field 'Team.state'
        db.delete_column('teams_team', 'state')


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
        }
    }

    complete_apps = ['teams']
