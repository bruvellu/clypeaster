# -*- coding: utf-8 -*-
from gonad.forms import *
from gonad.models import *
from gonad.stats import *

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.db.models import Avg

# Main
def main_page(request):
    '''Temporary main page.'''
    specimens = Specimen.objects.all()
    variables = RequestContext(request, {
        'specimens': specimens,
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
    stats['total'] = Section.objects.count()
    # Prestaged.
    stats['prestaged'] = Section.objects.exclude(pre_stage='').count()
    stats['prestaged_ratio'] = stats['prestaged'] / stats['total'] * float(100)
    # Staged.
    stats['staged'] = Section.objects.exclude(stage=None).count()
    stats['staged_ratio'] = stats['staged'] / stats['total'] * float(100)

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
    sections_male = Section.objects.filter(stage=None, specimen__gender='M').exclude(pre_stage='').order_by('pre_stage')
    sections_female = Section.objects.filter(stage=None, specimen__gender='F').exclude(pre_stage='').order_by('pre_stage')
    variables = RequestContext(request, {
        'sections_male': sections_male,
        'sections_female': sections_female,
        'status': u'prestaged',
        })
    return render_to_response('sections.html', variables)

# List of staged files
def staged_page(request):
    '''List of staged sections.'''
    sections_male = Section.objects.filter(specimen__gender='M').exclude(stage=None).order_by('stage')
    sections_female = Section.objects.filter(specimen__gender='F').exclude(stage=None).order_by('stage')
    variables = RequestContext(request, {
        'sections_male': sections_male,
        'sections_female': sections_female,
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

# Page with tables and graphics
def tubules_results(request):
    '''Results related to the measurements of the tubules.'''
    # Get tubules.
    tubules = Tubule.objects.exclude(cross_section=None)

    # Instantiate plots.
    tubules_stats = TubulePlots(tubules)

    # Plot gla_by_date.
    gla_by_date = tubules_stats.plot_gla_by_date()

    # Plot areamean_by_date.
    areamean_by_date = tubules_stats.plot_areamean_by_date()

    # Scatter gla_by_cross.
    gla_by_cross = tubules_stats.scatter_gla_by_cross()

    # Scatter gla_by_weight.
    gla_by_weight = tubules_stats.scatter_gla_by_weight()

    # Scatter cross_by_weight.
    cross_by_weight = tubules_stats.scatter_cross_by_weight()

    # Scatter germ_by_weight.
    germ_by_weight = tubules_stats.scatter_germ_by_weight()

    variables = RequestContext(request, {
        'tubules_data': tubules_stats.data,
        'gla_by_date': gla_by_date,
        'areamean_by_date': areamean_by_date,
        'gla_by_cross': gla_by_cross,
        'gla_by_weight': gla_by_weight,
        'cross_by_weight': cross_by_weight,
        'germ_by_weight': germ_by_weight,
        })

    return render_to_response('tubules_results.html', variables)
