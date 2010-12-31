# -*- coding: utf-8 -*-
from django.db import models

class Question(models.Model):
    body = models.TextField()

    class Meta:
        verbose_name = u'вопрос'
        verbose_name_plural = u'вопросы'

    def __unicode__(self):
        return self.body


class Answer(models.Model):
    question = models.ForeignKey(Question)
    body = models.TextField()

    class Meta:
        verbose_name = u'ответ'
        verbose_name_plural = u'ответы'

    def __unicode__(self):
        return self.question.name

