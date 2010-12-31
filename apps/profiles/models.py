# -*- coding: utf-8 -*-
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

from hashlib import md5
from pytils import translit
import os.path

S_UNDEF  = 0
S_MALE   = 1
S_FEMALE = 2
SEX_CHOICES = (
    (S_UNDEF, u'не указано'),
    (S_MALE, u'мужской'),
    (S_FEMALE, u'женский'),
)

def user_upload_to(instance, filename):
    today = datetime.today()
    filename = translit.translify(filename)
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
    user        = models.OneToOneField(User)
    avatar      = models.ImageField(u'аватар', upload_to=user_upload_to, null=True, blank=True)
    sex         = models.IntegerField(u'пол', default=0, choices=SEX_CHOICES)
    birth_date  = models.DateField(u'дата рождения', null=True, blank=True)
    show_bd     = models.BooleanField(u'показывать на сайте?', default=True)
    summary     = models.TextField(u'Несколько слов о себе', blank=True, null=True)
    life_dids   = models.TextField(u'Несколько слов о себе', blank=True, null=True)
    good_at     = models.TextField(u'Несколько слов о себе', blank=True, null=True)
    people_say  = models.TextField(u'Несколько слов о себе', blank=True, null=True)
    favorites   = models.TextField(u'Несколько слов о себе', blank=True, null=True)
    never       = models.TextField(u'Несколько слов о себе', blank=True, null=True)
    thinking    = models.TextField(u'Несколько слов о себе', blank=True, null=True)
    friday      = models.TextField(u'Несколько слов о себе', blank=True, null=True)
    private     = models.TextField(u'Несколько слов о себе', blank=True, null=True)
    message_if  = models.TextField(u'Несколько слов о себе', blank=True, null=True)


    class Meta:
        app_label = 'profiles'

    @property
    def name(self):
        if self.user.first_name:
            return self.user.first_name
        else:
            return self.user.username

