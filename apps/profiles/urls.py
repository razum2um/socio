# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('profiles.views',
#    url(
#        regex = r'^$',
#        view  = 'index',
#        name  = 'profiles_all',
#    ),
    url(
        regex = r'^(?P<id>\d+)/$',
        view  = 'show',
        name  = 'profile',
    ),
    url(
        regex = r'^signup/$',
        view  = 'sign_up',
        name  = 'sign_up',
    ),
    url(
        regex = r'^signout/$',
        view  = 'sign_out',
        name  = 'sign_out',
    ),
#    url(
#        regex = r'^(?P<id>\d+)/edit/$',
#        view  = 'edit',
#        name  = 'profiles_edit',
#    ),
#    url(
#        regex = r'^(?P<id>\d+)/delete/$',
#        view  = 'delete',
#        name  = 'profiles_delete',
#    ),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(
        regex  = r'^signin/$',
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

