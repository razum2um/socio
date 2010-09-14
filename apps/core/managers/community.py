# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.query import QuerySet

class CommunityQuerySet (QuerySet):

    def allowed_read(self, user):
        # TODO: сделать фильтрацию по сообществам доступным для чтения
        return self.all()


class CommunityManager (models.Manager):

    def get_query_set(self):
        return CommunityQuerySet(self.model, using=self._db)


    def allowed_read(self, user):
        # TODO: сделать фильтрацию по сообществам доступным для чтения
        return self.get_query_set().all()

