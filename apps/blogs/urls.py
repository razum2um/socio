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
        regex = '^communities/$',
        view  = 'community.index',
        name  = 'communities'
    ),
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
        regex = '^community(?P<id>\d+)/$',
        view  = 'community.show',
        name  = 'community'
    ),
# ------------------------------------------------------------------------------
    url(
        regex = '^blogs/$',
        view  = 'blog.index',
        name  = 'blogs'
    ),
    url(
        regex = '^community(?P<community_id>\d+)/blogs/new/$',
        view  = 'blog.new',
        name  = 'new_blog'
    ),
    url(
        regex = '^blog(?P<id>\d+)/$',
        view  = 'blog.show',
        name  = 'blog'
    ),
    url(
        regex = '^blog-(?P<id>\d+)/delete/$',
        view  = 'blog.delete',
        name  = 'delete_blog'
    ),
# ------------------------------------------------------------------------------
    url(
        regex = '^blog(?P<blog_id>\d+)/posts/new/$',
        view  = 'post.new',
        name  = 'new_post'
    ),
    url(
        regex = '^post(?P<id>\d+)/$',
        view  = 'post.show',
        name  = 'post'
    ),
    url(
        regex = '^post(?P<id>\d+)/edit/$',
        view  = 'post.edit',
        name  = 'edit_post'
    ),
    url(
        regex = '^post(?P<id>\d+)/delete/$',
        view  = 'post.delete',
        name  = 'delete_post'
    ),
)

