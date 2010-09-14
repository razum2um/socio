# -*- coding: utf-8 -*-
from django.db import models
from openteam.models import TimestampModel, NameModel

from community import Community

class Blog (NameModel, TimestampModel):
    communities = models.ManyToManyField(Community,
            verbose_name = u'сообщества',
            related_name = 'blogs'
    )
    description = models.TextField(u'описание', null=True, blank=True)


    class Meta:
        app_label = 'core'
        get_latest_by = 'created_at'

