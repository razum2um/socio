# -*- coding: utf-8 -*-
from openteam.decorators import render_to


@render_to('core/index.html')
def index (request):
    return dict()

