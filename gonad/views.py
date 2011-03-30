# -*- coding: utf-8 -*-
from gonad.models import *
from gonad.forms import *

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.db.models import Avg

# Main
def main_page(request):
    '''Temporary main page.'''
    specimens = Specimen.objects.all()
    # Aggregate by date for fun.
    means_by_date = specimens.values('collection_date').annotate(Avg('cross_sections_mean'), Avg('germ_layers_mean'), Avg('gla_indexes_mean'))
    variables = RequestContext(request, {
        'specimens': specimens,
        'means_by_date': means_by_date,
        })
    return render_to_response('main.html', variables)

# Staging page
def staging_page(request):
    '''Page where you can look at a random photo and stage it.
    
    The section on the left with the fields stage, preliminary stage and 
    observations on the right. So you can take notes and save.
    '''
    # TODO How do you hide the image location (showing the month)?
    # TODO Consider using Javascript to reload the images?
    variables = RequestContext(request, {
        'specimens': specimens,
        })
    return render_to_response('staging.html', variables)
