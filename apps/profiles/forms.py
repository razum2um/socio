# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

from models import UserProfile, PhotoAlbum, Photo, ProfileAttribute

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
    day = forms.IntegerField()
    month = forms.IntegerField()
    year = forms.IntegerField()

    class Meta:
        exclude = ['user']
        fields = ['birth_date', 'sex', 'marital_status', 'orientation']
        model  = UserProfile


class ProfileAttributeForm (forms.ModelForm):

    class Meta:
        fields = ['value']
        model = ProfileAttribute


class PhotoAlbumForm (forms.ModelForm):

    class Meta:
        exclude = ['user', 'created_at', 'updated_at']
        model = PhotoAlbum

class PhotoForm (forms.ModelForm):

    class Meta:
        exclude = ['album', 'created_at', 'updated_at']
        model = Photo

