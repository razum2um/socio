# -*- coding: utf-8 -*-
from comments.models import Comment
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic

from openteam.models import NameModel, TimestampModel

from blog import Blog

class Post (NameModel, TimestampModel):
    author   = models.ForeignKey(User, verbose_name=u'автор')
    blog    = models.ForeignKey(Blog, related_name='posts')
    announce = models.TextField(u'краткий анонс', null=True, blank=True)
    content  = models.TextField(u'текст', )
    is_draft = models.BooleanField(u'черновик?', default=True)

    comments = generic.GenericRelation(Comment,
        object_id_field     = "_commentable_object_id",
        content_type_field  = "_commentable_content_type"
    )


    class Meta:
        app_label = 'blogs'
        ordering = ['-created_at']

