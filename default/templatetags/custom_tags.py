from django import template
from default.utils import *

register = template.Library()

@register.filter
def getToken(request):
    return request.session['token']

@register.filter
def isDr(request):
     return checkUserGroup(request, 'Doctor')