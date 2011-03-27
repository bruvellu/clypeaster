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
