# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

I_IRRELEVANT = 0
I_ALITTLE    = 1
I_SOMEWHAT   = 2
I_VERY       = 3
I_MANDATORY  = 4

IMPORTANCE = (
    (I_IRRELEVANT, u'неважно'),
    (I_ALITTLE, u'немного'),
    (I_SOMEWHAT, u'отчасти'),
    (I_VERY, u'очень важно'),
    (I_MANDATORY, u'обязательно'),
)

class Question(models.Model):
    body = models.TextField()

    class Meta:
        verbose_name = u'вопрос'
        verbose_name_plural = u'вопросы'

    def __unicode__(self):
        return self.body


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers')
    body = models.TextField()

    class Meta:
        verbose_name = u'ответ'
        verbose_name_plural = u'ответы'

    def __unicode__(self):
        return self.body

    
class UserAnswer (models.Model):
    user     = models.ForeignKey(User, related_name='answers')
    variant  = models.ForeignKey(Answer, related_name='variants')
    accepted = models.ManyToManyField(Answer)
    importance = models.IntegerField(u'степень важности', choices=IMPORTANCE)
    description = models.TextField(u'пояснение', null=True, blank=True)

    def __unicode__(self):
        return "%s %s" % (self.user.get_full_name(), self.variant.body)

