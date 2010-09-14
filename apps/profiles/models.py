# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

class UserProfile (models.Model):
    user = models.OneToOneField(User)

