# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404

from openteam.decorators import render_to
from openteam.shortcuts import redirect_to_view, get_object_or_none

from apps.profiles.forms import UserForm, UserProfileForm, PhotoAlbumForm, PhotoForm
from apps.profiles.models import UserProfile, PhotoAlbum, Photo


@login_required
@render_to("profiles/show.html")
def show(request, id):
    owner = get_object_or_404(User, id=id)

    if get_object_or_none(UserProfile, user=owner) is None:
        UserProfile.objects.create(user=owner)

    return dict(
        owner = owner,
        current_page = dict(
           title = u'Профиль',
            slug = 'dossier'
        ),
    )

@login_required
@render_to("profiles/edit.html")
def edit(request, id):
    owner = get_object_or_404(User, id=id)

    if request.user.id != owner.id and request.user.is_superuser == False:
        return redirect_to_view('index')

    profile = owner.get_profile()
    user_form = UserForm(request.POST or None, instance=owner, prefix='user')
    profile_form = UserProfileForm(request.POST or None, request.FILES or None, instance=profile, prefix='profile')

    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        return redirect_to_view('profile', id=owner.id)

    return {
        'profile_form': profile_form,
        'user_form': user_form,
        'owner': owner,
    }

#@render_to("profiles/block.html")
#def block(request, id):
#    return {}

#@render_to("profiles/delete.html")
#def delete(request, id):
#    return {}

@login_required
@render_to('profiles/dashboard.html')
def dashboard (request):
    return dict()

