# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from openteam.decorators import render_to
from openteam.shortcuts import redirect_to_view

from core.forms import PostForm
from core.models import Blog, Community, Post

@render_to('post/index.html')
def index(request):
    posts = Post.objects.all()
    return { 'posts': posts }

@login_required
@render_to('post/new.html')
def new(request, community_id, blog_id):
    community = get_object_or_404(Community, id=community_id)
    try:
        blog = community.blogs.get(id=blog_id)

        post_form = PostForm(request.POST or None)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            blog.posts.add(post)

            return redirect_to_view('post',
                community_id = community.id,
                blog_id      = blog.id,
                id           = post.id
            )

        return {
            'community': community,
            'blog': blog,
            'post_form': post_form,
        }

    except Blog.DoesNotExist:
        raise Http404



@render_to('post/show.html')
def show(request, community_id, blog_id, id):
    community = get_object_or_404(Community, id=community_id)
    try:
        blog = community.blogs.get(id=blog_id)
        post = blog.posts.get(id=id)

        return {
            'community': community,
            'blog': blog,
            'post': post,
        }

    except (Blog.DoesNotExist, Post.DoesNotExist):
        raise Http404

