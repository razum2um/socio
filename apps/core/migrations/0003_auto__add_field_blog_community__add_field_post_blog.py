# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Blog.community'
        db.add_column('core_blog', 'community', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='blogs', to=orm['core.Community']), keep_default=False)

        # Removing M2M table for field communities on 'Blog'
        db.delete_table('core_blog_communities')

        # Adding field 'Post.blog'
        db.add_column('core_post', 'blog', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='posts', to=orm['core.Blog']), keep_default=False)

        # Removing M2M table for field blogs on 'Post'
        db.delete_table('core_post_blogs')


    def backwards(self, orm):
        
        # Deleting field 'Blog.community'
        db.delete_column('core_blog', 'community_id')

        # Adding M2M table for field communities on 'Blog'
        db.create_table('core_blog_communities', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blog', models.ForeignKey(orm['core.blog'], null=False)),
            ('community', models.ForeignKey(orm['core.community'], null=False))
        ))
        db.create_unique('core_blog_communities', ['blog_id', 'community_id'])

        # Deleting field 'Post.blog'
        db.delete_column('core_post', 'blog_id')

        # Adding M2M table for field blogs on 'Post'
        db.create_table('core_post_blogs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm['core.post'], null=False)),
            ('blog', models.ForeignKey(orm['core.blog'], null=False))
        ))
        db.create_unique('core_post_blogs', ['post_id', 'blog_id'])


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
        'core.blog': {
            'Meta': {'object_name': 'Blog'},
            'community': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blogs'", 'to': "orm['core.Community']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'})
        },
        'core.community': {
            'Meta': {'object_name': 'Community'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'})
        },
        'core.post': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': "orm['core.Blog']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'})
        }
    }

    complete_apps = ['core']
