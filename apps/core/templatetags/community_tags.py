# -*- coding: utf-8 -*-
from django.template import Library, Node, Variable, TemplateSyntaxError

from core.models import Community

register = Library()

@register.inclusion_tag('community/_side_list.html', takes_context=True)
def communities_side_list(context):
    user = context.get('user', None)
    return { 'communities': Community.objects.allowed_read(user) }

