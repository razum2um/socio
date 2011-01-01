# -*- coding: utf-8 -*-
from django.db import models
from openteam.models import NameModel
from profilemodel import UserProfile

class ProfileAttribute (NameModel):
    value = models.TextField(null=True, blank=True)
    empty_text = models.TextField(null=True, blank=True)
    profile = models.ForeignKey(UserProfile, related_name='attributes')
    sort_order = models.IntegerField(default=100)

    class Meta:
        app_label = 'profiles'
        ordering = ['sort_order',]


