# -*- coding: utf-8 -*-
from numpy import array, mean, std

# Signals
def calculate_gla(signal, instance, sender, **kwargs):
    '''Calculates the germ layer area index.'''
    if instance.cross_section and instance.germ_layer:
        gla = instance.germ_layer / instance.cross_section
        instance.gla_index = gla

def tubule_means(signal, instance, sender, **kwargs):
    '''Calculates the mean of tubules measurements for a specimen.'''
    # TODO Use Django aggregate function?
    # see http://docs.djangoproject.com/en/dev/topics/db/aggregation/
    # Avg, Count, Max, Min, StdDev, Sum, Variance can be used.
    # >>>
    # >>> from django.db.models import Avg
    # >>> instance.specimen.tubule_set.aggregate(Avg('cross_section'))
    # >>> instance.specimen.tubule_set.aggregate(StdDev('cross_section'))
    # >>> django.db.utils.DatabaseError: no such function: STDDEV_POP
    # XXX Sqlite does not support stddev, staying with numpy for now since I 
    # don't want to switch to PostgreSQL.

    # Specimen.
    sp = instance.specimen

    # Tubules.
    tubules = sp.tubule_set.all()

    # Cross section mean and standard deviation.
    cross_section_array = array([each.cross_section for each in tubules if 
        each.cross_section])
    sp.cross_sections_mean = cross_section_array.mean()
    sp.cross_sections_sd = cross_section_array.std()

    # Germ layer mean and standard deviation.
    germ_layer_array = array([each.germ_layer for each in tubules if 
        each.germ_layer])
    sp.germ_layers_mean = germ_layer_array.mean()
    sp.germ_layers_sd = germ_layer_array.std()

    # Germ layer area index mean and standard deviation.
    gla_index_array = array([each.gla_index for each in tubules if 
        each.gla_index])
    sp.gla_indexes_mean = gla_index_array.mean()
    sp.gla_indexes_sd = gla_index_array.std()

    # Save specimen.
    sp.save()

