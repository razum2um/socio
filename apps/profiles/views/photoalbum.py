# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms.models import modelformset_factory
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404

from openteam.decorators import render_to
from openteam.shortcuts import redirect_to_view

from apps.profiles.forms import PhotoForm, PhotoAlbumForm
from apps.profiles.models.photomodel import PhotoAlbum, Photo

@login_required
@render_to("profiles/photos.html")
def index(request, id):
    owner = get_object_or_404(User, id=id)
    albums = PhotoAlbum.objects.filter(user = owner)
    return dict(
        owner = owner,
        albums = albums,
        current_page = dict(
            title = u'Фотоальбомы',
            slug  = 'photoalbums',
        ),
    )

@login_required
@render_to("profiles/show_photoalbum.html")
def show(request, id, album_id):
    owner = get_object_or_404(User, id=id)
    album = get_object_or_404(PhotoAlbum, id=album_id)

    response = dict(
        owner = owner,
        album = album,
        current_page = dict(
            title = u'Альбом: %(name)s' % {'name': album.name},
            ),
        )

    if request.user == owner:
        PhotoFormset = modelformset_factory(Photo, form=PhotoForm, extra=2)
        config = {
            'form-TOTAL_FORMS': u'1',
            'form-INITIAL_FORMS': u'0',
            'form-MAX_NUM_FORMS': u'',
        }

        photo_formset = PhotoFormset(request.POST or config, request.FILES or config)

        if photo_formset.is_valid():
            for photo_form in photo_formset.forms:
                photo = photo_form.save(commit=False)
                photo.album = album
                photo.user = owner
                photo.save()

        response.update({'photo_formset': photo_formset})

    return response

@login_required
@render_to("profiles/add_photoalbum.html")
def add(request, id):
    owner = get_object_or_404(User, id=id)
    # take a look at http://djangosnippets.org/snippets/874/ plz
    # ... user._meta.get_all_related_objects() ...
    # too expensive for a deco to use with every user's staff?
    if request.user != owner:
        return HttpResponseForbidden('Take care of *your* account, please')

    album_form = PhotoAlbumForm(request.POST or None)

    if album_form.is_valid():
        album = album_form.save(commit=False)
        album.user = owner
        album.save()

        return redirect_to_view('show', id=owner.id, album_id=album.id)

    return dict(
        owner = owner,
        album_form = album_form,
        current_page = dict(
            title = u'Добавить альбом'
            ),
        )
