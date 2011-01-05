# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.template.context import RequestContext
from django.template.loader import render_to_string

from openteam.decorators import ajax_only, render_to
from openteam.shortcuts import json_response

from apps.profiles.forms import ProfileAttributeForm
from apps.profiles.models.attributemodel import ProfileAttribute


@ajax_only
def get_gender_marial(request):
    return json_response(dict())

@ajax_only
def get_gender_orientation(request):
    return json_response(dict())

@ajax_only
@login_required
def attribute(request, attr_id):
    attribute = get_object_or_404(ProfileAttribute, id=attr_id)

    if request.user.is_superuser or request.user.id == attribute.profile.user.id:
        attribute_form = ProfileAttributeForm(request.POST or None, instance=attribute)

        if attribute_form.is_valid():
            attribute = attribute_form.save()
            return json_response(dict(html=attribute.value))

        html_form = render_to_string(
                template_name    = 'profiles/ajax/form_field.html',
                dictionary       = dict(form=attribute_form, attr_id=attr_id),
                context_instance = RequestContext(request))

        return json_response(dict(html=html_form))

    else:
        raise Http404

