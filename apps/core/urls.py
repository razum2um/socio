# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('core.views',
    url(
        regex = '^$',
        view  = 'post.index',
        name  = 'posts'
    ),
# ------------------------------------------------------------------------------
    url(
        regex = '^communities/join/$',
        view  = 'community.join',
        name  = 'join_community'
    ),
    url(
        regex = '^communities/new/$',
        view  = 'community.new',
        name  = 'new_community'
    ),
    url(
        regex = '^communities/(?P<id>\d+)/$',
        view  = 'community.show',
        name  = 'community'
    ),
# ------------------------------------------------------------------------------
    url(
        regex = '^communities/(?P<community_id>\d+)/blogs/new/$',
        view  = 'blog.new',
        name  = 'new_blog'
    ),
    url(
        regex = '^communities/(?P<community_id>\d+)/blogs/(?P<id>\d+)/$',
        view  = 'blog.show',
        name  = 'blog'
    ),
# ------------------------------------------------------------------------------
    url(
        regex = '^communities/(?P<community_id>\d+)/blogs/(?P<blog_id>\d+)/posts/new/$',
        view  = 'post.new',
        name  = 'new_post'
    ),
    url(
        regex = '^communities/(?P<community_id>\d+)/blogs/(?P<blog_id>\d+)/posts/(?P<id>\d+)/$',
        view  = 'post.show',
        name  = 'post'
    ),

)

