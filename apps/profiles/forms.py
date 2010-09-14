# -*- coding: utf-8 -*-
from django import forms

class SignUpForm (forms.Form):

    email    = forms.EmailField(label=u'адрес электронной почты')

class SignInForm (forms.Form):

    email    = forms.EmailField(label=u'адрес электронной почты')
    password = forms.CharField(label=u'пароль', widget=forms.PasswordInput)

