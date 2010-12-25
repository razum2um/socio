# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from openteam.decorators import render_to
from openteam.shortcuts import redirect_to_view

from blogs.forms import PostForm
from blogs.models import Blog, Community, Post

@render_to('post/index.html')
def index(request):
    posts = Post.objects.all()
    return { 'posts': posts }

@login_required
@render_to('post/new.html')
def new(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    post_form = PostForm(request.POST or None)

    if post_form.is_valid():
        post = post_form.save(commit=False)
        post.author = request.user
        post.save()
        blog.posts.add(post)

        return redirect_to_view('post',
            id = post.id
        )

    return {
        'blog': blog,
        'post_form': post_form,
    }

@render_to('post/show.html')
def show(request, id):
    post = get_object_or_404(Post, id=id)

    return {
        'post': post,
    }

@login_required
@render_to('post/edit.html')
def edit(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)
    post_form = PostForm(request.POST or None, instance=post)

    if post_form.is_valid():
        post.save()

        return redirect_to_view('post',
            id = post.id
        )

    return {
        'post': post,
        'post_form': post_form,
    }

@login_required
def delete(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)
    blog_id = post.blog.id
    post.delete()

    return redirect_to_view('blog', id=blog_id)

