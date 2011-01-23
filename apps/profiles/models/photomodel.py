# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from openteam.models import NameModel, TimestampModel
from openteam.shortcuts import get_object_or_none

from helpers import user_upload_to
from storage import MD5Storage

class PhotoAlbum (NameModel, TimestampModel):
    user = models.ForeignKey(User, related_name='photoalbums')

    @property
    def cover (self):
        return get_object_or_none(Photo, album=self)

    @property
    def random (self):
        return self.photos.order_by('?')

    class Meta:
        app_label = 'profiles'
        ordering = ['created_at']        


class Photo (TimestampModel):
    album = models.ForeignKey(PhotoAlbum, related_name='photos')
    photo = models.ImageField(upload_to=user_upload_to, storage=MD5Storage())
    is_cover = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        app_label = 'profiles'
        ordering = ['created_at']


