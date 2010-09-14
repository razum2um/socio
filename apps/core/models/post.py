# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from openteam.models import NameModel, TimestampModel

from blog import Blog

class Post (NameModel, TimestampModel):
    author   = models.ForeignKey(User, verbose_name=u'автор')
    blogs    = models.ManyToManyField(Blog, related_name='posts')
    content  = models.TextField(u'текст')
    is_draft = models.BooleanField(u'черновик?', default=True)

    class Meta:
        app_label = 'core'
        ordering = ['-created_at']

