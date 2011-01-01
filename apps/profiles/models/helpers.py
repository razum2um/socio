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
