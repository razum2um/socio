# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

from models import UserProfile

class SignUpForm (forms.Form):

    email    = forms.EmailField(label=u'адрес электронной почты')


class SignInForm (forms.Form):

    email    = forms.EmailField(label=u'адрес электронной почты')
    password = forms.CharField(label=u'пароль', widget=forms.PasswordInput)


class UserForm (forms.ModelForm):

    class Meta:
        fields = ['first_name', 'last_name']
        model  = User


class UserProfileForm (forms.ModelForm):

    class Meta:
        fields = ['avatar']
        model  = UserProfile

