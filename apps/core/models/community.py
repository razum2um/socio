# -*- coding: utf-8 -*-
from django.db import models
from openteam.models import NameModel, TimestampModel

from core.managers.community import CommunityManager

C_OPEN = 1
C_CLOSED = 2
C_INVITABLE = 3

C_TYPES = (
    (C_OPEN,      u'открытое'),
    (C_CLOSED,    u'закрытое'),
    (C_INVITABLE, u'по приглашению'),
)



class Community (NameModel, TimestampModel):
    description = models.TextField(u'описание', null=True, blank=True)

    objects = CommunityManager()

    class Meta:
        app_label = 'core'
        get_latest_by = 'created_at'

