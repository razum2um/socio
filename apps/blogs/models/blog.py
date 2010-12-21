# -*- coding: utf-8 -*-
from django.db import models
from openteam.models import TimestampModel, NameModel

from community import Community

class Blog (NameModel, TimestampModel):
    community = models.ForeignKey(Community,
            verbose_name = u'сообщества',
            related_name = 'blogs'
    )
    description = models.TextField(u'описание', null=True, blank=True)


    class Meta:
        app_label = 'blogs'
        get_latest_by = 'created_at'

