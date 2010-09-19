# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

from django.db import models
from openteam.models import TimestampModel
import mptt

class Comment(TimestampModel):
    """Comment model
    """
    parent  = models.ForeignKey('self', null = True, blank = True, related_name = 'children')
    author  = models.ForeignKey(User, related_name='comments', blank=True, null=True)
    content = models.TextField(u'текст')
    commentable = generic.GenericForeignKey(ct_field="_commentable_content_type", fk_field="_commentable_object_id")

    _commentable_content_type = models.ForeignKey(ContentType, related_name="comments")
    _commentable_object_id = models.PositiveIntegerField()

mptt.register(Comment)

