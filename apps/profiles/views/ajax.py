# -*- coding: utf-8 -*-
from openteam.decorators import ajax_only
from openteam.shortcuts import json_response

@ajax_only
def get_gender_marial(request):
    return json_response(dict())

@ajax_only
def get_gender_orientation(request):
    return json_response(dict())

