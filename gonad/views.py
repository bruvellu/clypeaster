# -*- coding: utf-8 -*-
from gonad.models import *
from gonad.forms import *

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

# Main
def main_page(request):
    '''Temporary main page.'''
    specimens = Specimen.objects.all()
    variables = RequestContext(request, {
        'specimens': specimens,
        })
    return render_to_response('main.html', variables)
