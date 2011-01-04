# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

from models import UserProfile, PhotoAlbum

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
        exclude = ['user']
        model  = UserProfile

class PhotoAlbumForm (forms.ModelForm):

    class Meta:
        exclude = ['user', 'created_at', 'updated_at']
        model = PhotoAlbum
