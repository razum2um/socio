# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from helpers import user_upload_to
from openteam.models import NameModel, TimestampModel


class PhotoAlbum (NameModel, TimestampModel):
    user = models.ForeignKey(User)

    class Meta:
        app_label = 'profiles'
        ordering = ['created_at']        


class Photo (TimestampModel):
    album = models.ForeignKey(PhotoAlbum)
    photo = models.ImageField(upload_to=user_upload_to)
    is_cover = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        app_label = 'profiles'
        ordering = ['created_at']


