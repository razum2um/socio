# -*- coding: utf-8 -*-
from django import forms

from models import Community, Blog, Post

class BlogForm (forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['name', 'description']


class CommunityForm (forms.ModelForm):

    class Meta:
        model = Community
        fields = ['name', 'description']

class PostForm (forms.ModelForm):

    class Meta:
        model = Post
        fields = ['name','announce', 'content']

