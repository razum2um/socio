# -*- coding: utf-8 -*-
from datetime import date
from django.db import models
from django.contrib.auth.models import User

from helpers import O_CHOICES_M, MS_CHOICES_M, SEX_CHOICES, user_upload_to

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
        years = today.year - self.birth_date.year

        if all((x >= y) for x, y in zip(today.timetuple(), self.birth_date.timetuple())):
            age = years

        else:
            age = years - 1

        return age


def initialize_attributes_set(instance, **kwargs):
    if kwargs['created']:
        instance.attributes.create(name=u'Вкратце, обо мне',
                                   empty_text = u'нужно придумать текст если поле пустое',
                                   sort_order=5)
        instance.attributes.create(name=u'Чем я занимаюсь в жизни?',
                                   empty_text = u'нужно придумать текст если поле пустое',
                                   sort_order=10)
        instance.attributes.create(name=u'У меня неплохо получается...',
                                   empty_text = u'нужно придумать текст если поле пустое',
                                   sort_order=20)
        instance.attributes.create(name=u'Первое, что люди замечают обо мне',
                                   empty_text = u'нужно придумать текст если поле пустое',
                                   sort_order=30)
        instance.attributes.create(name=u'Мои любимые книги',
                                   empty_text = u'нужно придумать текст если поле пустое',
                                   sort_order=40)
        instance.attributes.create(name=u'Мои любимые фильмы',
                                   empty_text = u'нужно придумать текст если поле пустое',
                                   sort_order=50)
        instance.attributes.create(name=u'Моя любимая музыка',
                                   empty_text = u'нужно придумать текст если поле пустое',
                                   sort_order=60)
        instance.attributes.create(name=u'Шесть вещей которые всегда со мной',
                                   empty_text = u'нужно придумать текст если поле пустое',
                                   sort_order=70)
        instance.attributes.create(name=u'Я провожу много времени думая о..',
                                   empty_text = u'нужно придумать текст если поле пустое',
                                   sort_order=80)
        instance.attributes.create(name=u'В пятницу я обычно...',
                                   empty_text = u'нужно придумать текст если поле пустое',
                                   sort_order=90)
        instance.attributes.create(name=u'Пиши мне если...',
                                   empty_text = u'нужно придумать текст если поле пустое',
                                   sort_order=100)

models.signals.post_save.connect(initialize_attributes_set, UserProfile)

