# -*- coding: utf-8 -*-
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

from hashlib import md5
import os.path

def user_upload_to(instance, filename):
    today = datetime.today()
    new_name = md5(filename)

    path =  "uploads/users/%(uid)d/%(year)d/%(month)d/%(day)d/a_%(filename)s%(ext)s" % {
            'uid': instance.user.id,
            'year': today.year,
            'month': today.month,
            'day': today.day,
            'filename': new_name.hexdigest(),
            'ext': os.path.splitext(filename)[-1]
        }
    print path
    return path


class UserProfile (models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(u'аватар', upload_to=user_upload_to, null=True, blank=True)
    description = models.TextField(u'Несколько слов о себе', blank=True, null=True)
    @property
    def name(self):
        if self.user.first_name:
            return self.user.first_name
        else:
            return self.user.username

