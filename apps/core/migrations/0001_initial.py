# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Question'
        db.create_table('core_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['Question'])

        # Adding model 'Answer'
        db.create_table('core_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Question'])),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['Answer'])


    def backwards(self, orm):
        
        # Deleting model 'Question'
        db.delete_table('core_question')

        # Deleting model 'Answer'
        db.delete_table('core_answer')


    models = {
        'core.answer': {
            'Meta': {'object_name': 'Answer'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Question']"})
        },
        'core.question': {
            'Meta': {'object_name': 'Question'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['core']
