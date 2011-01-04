# -*- coding: utf-8 -*-
from openteam.decorators import render_to


@render_to('profiles/dashboard/form_field.html')
def render_form_field(request):
    return dict()

