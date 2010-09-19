# -*- coding: utf-8 -*-
from django.db import models
from core.managers.community import CommunityManager
from openteam.models import NameModel, TimestampModel
from pytils import translit


from hashlib import md5
import os.path

C_OPEN = 1
C_CLOSED = 2
C_INVITABLE = 3

C_TYPES = (
    (C_OPEN,      u'открытое'),
    (C_CLOSED,    u'закрытое'),
    (C_INVITABLE, u'по приглашению'),
)


def community_upload(instance, filename):
    filename = translit.translify(filename)
    new_name = md5(filename)
    path =  "uploads/communities/%(cid)d/p_%(filename)s%(ext)s" % {
            'cid': instance.id or 0,
            'filename': new_name.hexdigest(),
            'ext': os.path.splitext(filename)[-1]
        }
    print path
    return path


class Community (NameModel, TimestampModel):
    picture = models.ImageField(u'картинка', upload_to=community_upload, null=True, blank=True)
    description = models.TextField(u'описание', null=True, blank=True)

    objects = CommunityManager()

    class Meta:
        app_label = 'core'
        get_latest_by = 'created_at'

