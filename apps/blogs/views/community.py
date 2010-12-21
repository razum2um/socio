# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from openteam.decorators import post_only, render_to
from openteam.shortcuts import redirect_to_view

from core.forms import CommunityForm
from core.models import Community


@login_required
@render_to('community/join.html')
def join(request):
    communities = Community.objects.allowed_read(request.user)
    return {
        'communities': communities,
    }


@login_required
@render_to('community/new.html')
def new(request):
    community_form = CommunityForm(request.POST or None)

    if community_form.is_valid():
        community = community_form.save()

        return redirect_to_view('community', id=community.id)

    return {
        'community_form': community_form,
    }


@render_to('community/show.html')
def show(request, id):
    community = get_object_or_404(Community, id=id)
    return {
        'community': community,
    }

