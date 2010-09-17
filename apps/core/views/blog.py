# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404

from openteam.decorators import render_to
from openteam.shortcuts import redirect_to_view


from core.models import Community, Blog
from core.forms import BlogForm

@render_to('blog/index.html')
def index(request):
    blogs = Blog.objects.all()

    return {
        'blogs': blogs,
    }


@login_required
@render_to('blog/new.html')
def new(request, community_id):
    community = get_object_or_404(Community, id=community_id)
    blog_form = BlogForm()

    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            blog = blog_form.save()
            community.blogs.add(blog)
            return redirect_to_view('blog', community_id=community.id, id=blog.id)

    return {
        'community': community,
        'blog_form': blog_form,
    }


@render_to('blog/show.html')
def show(request, id):
    blog = get_object_or_404(Blog ,id=id)

    return {
        'blog': blog,
    }

