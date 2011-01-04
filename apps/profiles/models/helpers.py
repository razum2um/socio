# -*- coding: utf-8 -*-
from datetime import datetime
from pytils import translit
from hashlib import md5
import os.path

S_UNDEF  = 0
S_MALE   = 1
S_FEMALE = 2

SEX_CHOICES = (
    (S_UNDEF, u'не указано'),
    (S_MALE, u'мужской'),
    (S_FEMALE, u'женский'),
)

MS_UNDEF = 0
MS_SINGLE = 1
MS_DATING = 2
MS_INVOLVED = 3
MS_MARRIED = 4

MS_CHOICES_M = (
    (MS_UNDEF, u'не выбрано'),
    (MS_SINGLE, u'один'),
    (MS_DATING, u'встречаюсь'),
    (MS_INVOLVED, u'помолвлен'),
    (MS_MARRIED, u'женат'),
)

MS_CHOICES_F = (
    (MS_UNDEF, u'не выбрано'),
    (MS_SINGLE, u'одна'),
    (MS_DATING, u'встречаюсь'),
    (MS_INVOLVED, u'помолвлена'),
    (MS_MARRIED, u'замужем'),
)

O_STRAIGHT = 0
O_GAY = 1
O_BISEXUAL = 2

O_CHOICES_M = (
    (O_STRAIGHT, u'гетеро'),
    (O_GAY, u'гей'),
    (O_BISEXUAL, u'би'),
)

O_CHOICES_F = (
    (O_STRAIGHT, u'гетеро'),
    (O_GAY, u'лесби'),
    (O_BISEXUAL, u'би'),
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
    return path

