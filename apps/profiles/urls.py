# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('profiles.views.profile',
#    url(
#        regex = r'^$',
#        view  = 'index',
#        name  = 'profiles_all',
#    ),
    url(
        regex = r'^(?P<id>\d+)/$',
        view  = 'show',
        name  = 'show_profile',
    ),
    url(
        regex = r'^(?P<id>\d+)/edit/$',
        view  = 'edit',
        name  = 'edit_profile',
    ),
)

urlpatterns += patterns('profiles.views.auth',
    url(
        regex = r'^sign_up/$',
        view  = 'sign_up',
        name  = 'sign_up',
    ),
    url(
        regex = r'^sign_out/$',
        view  = 'sign_out',
        name  = 'sign_out',
    ),
)

urlpatterns += patterns('profiles.views.photoalbum',
    url (
        regex = r'^(?P<id>\d+)/photoalbums/$',
        view  = 'index',
        name  = 'photoalbums',
    ),
    url (
        regex = r'^(?P<id>\d+)/photoalbums/(?P<album_id>\d+)/$',
        view  = 'show',
        name  = 'show_photoalbum',
    ),
    url(
        regex = r'^(?P<id>\d+)/photoalbums/add/$',
        view  = 'add',
        name  = 'add_photoalbum',
    ),
)

urlpatterns += patterns('profiles.views.ajax',
    url (
        regex = r'^ajax/attr/(?P<attr_id>\d+)/$',
        view  = 'attribute',
        name  = 'aj_edit_attribute',
    ),
    url (
        regex = r'^ajax/declension/$',
        view  = 'declension',
        name  = 'aj_declension',
    ),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(
        regex  = r'^sign_in/$',
        view   = 'login',
        name   = 'sign_in',
        kwargs ={'template_name': 'profiles/sign_in.html' }
    ),
    url(
        regex  = r'^reset/$',
        view   = 'password_reset',
        name   = 'password_reset',
        kwargs ={'template_name': 'profiles/password_reset.html' }
    ),
    url(
        regex  = r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        view   = 'password_reset_confirm',
        name   = 'password_reset_confirm',
        kwargs ={'template_name': 'profiles/password_reset_confirm.html' }
    ),
    url(
        regex  = r'^reset/done/$',
        view   = 'password_reset_done',
        name   = 'password_reset_done',
        kwargs ={'template_name': 'profiles/password_reset_done.html' }
    ),
    url(
        regex  = r'^reset/complete/$',
        view   = 'password_reset_complete',
        name   = 'password_reset_complete',
        kwargs ={'template_name': 'profiles/password_reset_complete.html' }
    ),
)

