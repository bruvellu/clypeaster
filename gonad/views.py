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
    '''Page where you can look at a random photo and stage it.'''
    if request.method == 'POST':
        section = Section.objects.get(id=request.POST['section'])
        # Differentiates between a manual edit and a random sample.
        # If it is a manual edit don't use POST to populate fields.
        if request.POST['edit']:
            form = StagingForm(instance=section)
        else:
            form = StagingForm(request.POST, instance=section)
            if form.is_valid():
                form.save()
    else:
        section = Section.objects.filter(stage=None).order_by('?')[0]
        form = StagingForm(instance=section)

    # Some stats just for fun.
    stats = {}
    stats['left'] = Section.objects.exclude(stage=None).count()
    stats['total'] = Section.objects.count()
    stats['ratio'] = stats['left'] / stats['total'] * 100

    variables = RequestContext(request, {
        'section': section,
        'form': form,
        'stats': stats,
        })
    return render_to_response('staging.html', variables)

# List of unstaged files
def unstaged_page(request):
    '''List of unstaged sections.

    Sections are in random order. Date and id are hidden to avoid bias during 
    classification of gonadal stage.
    '''
    sections = Section.objects.filter(pre_stage='', stage=None).order_by('?')
    variables = RequestContext(request, {
        'sections': sections,
        })
    return render_to_response('unstaged.html', variables)

# List of pre-staged files
def prestaged_page(request):
    '''List of prestaged sections.'''
    sections = Section.objects.filter(stage=None).exclude(pre_stage='')
    variables = RequestContext(request, {
        'sections': sections,
        'status': u'prestaged',
        })
    return render_to_response('sections.html', variables)

# List of staged files
def staged_page(request):
    '''List of staged sections.'''
    sections = Section.objects.exclude(stage=None)
    variables = RequestContext(request, {
        'sections': sections,
        'status': u'staged',
        })
    return render_to_response('sections.html', variables)

# Page of a gonadal tubule
def tubule_page(request, id):
    '''Standard page for a tubule.'''
    tubule = Tubule.objects.get(id=id)
    variables = RequestContext(request, {
        'tubule': tubule,
        })
    return render_to_response('tubule.html', variables)

# Page of a gonadal section
def section_page(request, id):
    '''Standard page for a tubule.'''
    section = Section.objects.get(id=id)
    variables = RequestContext(request, {
        'section': section,
        })
    return render_to_response('section.html', variables)
