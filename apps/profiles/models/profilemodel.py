# -*- coding: utf-8 -*-
from datetime import date

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

from helpers import O_CHOICES_M, MS_CHOICES_M, SEX_CHOICES, user_upload_to

import json

class UserProfile (models.Model):
    user        = models.OneToOneField(User)
    sex         = models.IntegerField(u'пол', default=0, choices=SEX_CHOICES)
    birth_date  = models.DateField(u'дата рождения', null=True, blank=True)
    marital_status = models.IntegerField(u'семейное положение', default=0, choices=MS_CHOICES_M)
    orientation = models.IntegerField(u'ориентация', default=0, choices=O_CHOICES_M)

    class Meta:
        app_label = 'profiles'

    def __unicode__(self):
        return self.name

    @property
    def name(self):
        if self.user.first_name:
            return self.user.first_name
        else:
            return self.user.username

    @property
    def age(self):
        today = date.today()
        age = today - self.birth_date
        return int(age.days/365.25)


def initialize_attributes_set(instance, **kwargs):
    if kwargs['created']:
        with open(settings.PROFILE_INITIAL_ATTRIBUTES,'r') as fp:
            data = json.load(fp)
            for line in data:
                print line
                instance.attributes.create(
                        name       = line['name'],
                        empty_text = line['empty_text'],
                        sort_order = line['sort_order']
                        )

models.signals.post_save.connect(initialize_attributes_set, UserProfile)