# -*- coding: utf-8 -*-
from datetime import date
from numpy import array, mean, std
from os import remove
from os.path import join

import matplotlib.pyplot as plot

from settings import MEDIA_ROOT

#TODO Mean of tubule measurements by date (all tubules, not by specimen).
# Cross section area, germ layer area, and GLA index.


class TubulePlots:
    def __init__(self, tubules):
        self.tubules = tubules
        self.cross_sections = tubules.values_list('cross_section', flat=True)
        self.germ_layers = tubules.values_list('germ_layer', flat=True)
        self.gla_indexes = tubules.values_list('gla_index', flat=True)
        #TODO Use pandas for numerical processing.

        # Build plots.
        self.gla_per_cross()

    def gla_per_cross(self):
        '''Scatter plot with GLA by cross section area.'''
        # Clear plot.
        plot.clf()

        # Define paths.
        png_path = join(MEDIA_ROOT, 'plots/gla_by_cross.png')
        pdf_path = join(MEDIA_ROOT, 'plots/gla_by_cross.pdf')

        # Define figure to handle the limits better.
        figure = plot.figure()

        # Plot options.
        plot.title(u'GLA index against the cross section area')

        # Plot data.
        plot.scatter(self.cross_sections, self.gla_indexes)

        # Plot save.
        figure.savefig(png_path)
        figure.savefig(pdf_path)

def plot_tubules_by_date(data):
    '''Build plot for tubules measurements grouped by date.'''
    # Clear plot.
    plot.clf()

    # Define paths.
    png_path = join(MEDIA_ROOT, 'plots/tubules_by_date.png')
    pdf_path = join(MEDIA_ROOT, 'plots/tubules_by_date.pdf')

    # Data points.
    x = [value['specimen__collection_date'] for value in data]
    germ_layer = [value['germ_layer__avg'] for value in data]
    cross_section = [value['cross_section__avg'] for value in data]

    # Define figure to handle the limits better.
    figure = plot.figure()

    # Plot options.
    plot.xlabel(u'Collection date')
    plot.ylabel(u'Area in µm^2')
    plot.title(u'Cross section and germ layer area grouped by date')

    # Plot data.
    plot.plot_date(x, cross_section, fmt='-', label=u'Cross section area', color='blue')
    plot.plot_date(x, germ_layer, fmt='-', label=u'Germ layer area', color='red')
    plot.legend(loc='upper right')
    plot.xlim(xmin=date(2006, 12, 01), xmax=date(2007, 12, 01))
    figure.autofmt_xdate()

    # Plot save.
    figure.savefig(png_path)
    figure.savefig(pdf_path)

    # Clear plot.
    plot.clf()

    # Define paths.
    png_path = join(MEDIA_ROOT, 'plots/gla_by_date.png')
    pdf_path = join(MEDIA_ROOT, 'plots/gla_by_date.pdf')

    # Data points.
    x = [value['specimen__collection_date'] for value in data]
    gla_index = [value['gla_index__avg'] for value in data]

    # Define figure to handle the limits better.
    figure = plot.figure()

    # Plot options.
    plot.xlabel(u'Collection date')
    plot.ylabel(u'Ratio')
    plot.title(u'GLA index grouped by date')

    # Plot data.
    plot.plot_date(x, gla_index, fmt='-', label=u'GLA index', color='blue')
    plot.xlim(xmin=date(2006, 12, 01), xmax=date(2007, 12, 01))
    plot.ylim(ymin=0.0, ymax=1.0)
    figure.autofmt_xdate()

    # Plot save.
    figure.savefig(png_path)
    figure.savefig(pdf_path)


#TODO Correlation between GLA and tubule area. Does GLA vary with tubule size? 
# If yes, how to normalize the values?
# Hint: by using the residues from regression.
