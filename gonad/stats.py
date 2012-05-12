# -*- coding: utf-8 -*-

from datetime import date
from numpy import array, mean, std
from os import remove
from os.path import join
from pandas import *

import matplotlib.pyplot as plt

from settings import MEDIA_ROOT


class TubulePlots:
    def __init__(self, tubules):
        # Create instance for queryset.
        self.tubules = tubules

        # Build data frame and instantiate "self.data".
        self.build_data_frame(self.tubules)

        # Define grouped data by date.
        self.avg_by_date = self.data.groupby('dates').mean()
        self.std_by_date = self.data.groupby('dates').std()

        # Build plots.
        self.scatter_gla_by_cross()
        self.plot_areamean_by_date()
        self.plot_gla_by_date()

    def build_data_frame(self, tubules):
        '''Build data frames for tubules plots using pandas.'''
        # Get objects.
        ids = tubules.values_list('id', flat=True)
        cross_sections = tubules.values_list('cross_section', flat=True)
        germ_layer = tubules.values_list('germ_layer', flat=True)
        gla_indexes = tubules.values_list('gla_index', flat=True)
        dates = tubules.values_list('specimen__collection_date', flat=True)

        # Instantiate dictionary for DataFrame.
        data_dic = {
                'cross_section': cross_sections,
                'germ_layer': germ_layer,
                'gla_index': gla_indexes,
                'dates': dates,
                }

        #TODO Write csv with data frame for history.

        # Create DataFrame for tubule data.
        self.data = DataFrame(data_dic, index=ids)

    def scatter_gla_by_cross(self):
        '''Scatter plot with GLA by cross section area.'''
        # Define plot name.
        plot_name = 'gla_by_cross'

        # Clear plot.
        plt.clf()

        # Define data.
        cross_sections = self.data['cross_section'].tolist()
        gla_indexes = self.data['gla_index'].tolist()

        # Define paths.
        png_path = join(MEDIA_ROOT, 'plots/%s.png' % plot_name)
        pdf_path = join(MEDIA_ROOT, 'plots/%s.pdf' % plot_name)
        csv_path = join(MEDIA_ROOT, 'plots/%s.csv' % plot_name)

        # Define figure to handle the limits better.
        figure = plt.figure()

        # Plot options.
        plt.title(u'GLA index against the cross section area')

        # Plot data.
        plt.scatter(cross_sections, gla_indexes)

        # Plot save.
        figure.savefig(png_path)
        figure.savefig(pdf_path)

    def plot_areamean_by_date(self):
        '''Build plot for tubules measurements grouped by date.'''

        # Define plot name.
        plot_name = 'areamean_by_date'

        # Clear plot.
        plt.clf()

        # Define paths.
        png_path = join(MEDIA_ROOT, 'plots/%s.png' % plot_name)
        pdf_path = join(MEDIA_ROOT, 'plots/%s.pdf' % plot_name)
        csv_path = join(MEDIA_ROOT, 'plots/%s.csv' % plot_name)

        # Data points.
        x = self.avg_by_date.index.tolist()
        germ_layer = self.avg_by_date['germ_layer'].tolist()
        cross_section = self.avg_by_date['cross_section'].tolist()
        germ_layer_std = self.std_by_date['germ_layer'].tolist()
        cross_section_std = self.std_by_date['cross_section'].tolist()

        # Define figure to handle the limits better.
        figure = plt.figure()

        # Plot options.
        plt.xlabel(u'Collection date')
        plt.ylabel(u'Area in µm^2')
        plt.title(u'Cross section and germ layer area grouped by date')

        # Plot data.
        plt.errorbar(x, cross_section, yerr=cross_section_std, fmt='-', label=u'Cross section area', color='blue')
        plt.errorbar(x, germ_layer, yerr=germ_layer_std, fmt='-', label=u'Germ layer area', color='red')
        # Insert caption.
        plt.legend(loc='best')
        # Define x limits.
        plt.xlim(xmin=date(2006, 12, 01), xmax=date(2007, 12, 01))
        # Auto adjust figure paddings.
        figure.autofmt_xdate()

        # Plot save.
        figure.savefig(png_path)
        figure.savefig(pdf_path)

        #TODO Write CSV.

        #TODO Return data frame.

    def plot_gla_by_date(self):
        '''Build plot for gla indexes grouped by date.'''

        # Define plot name.
        plot_name = 'gla_by_date'

        # Clear plot.
        plt.clf()

        # Define paths.
        png_path = join(MEDIA_ROOT, 'plots/%s.png' % plot_name)
        pdf_path = join(MEDIA_ROOT, 'plots/%s.pdf' % plot_name)
        csv_path = join(MEDIA_ROOT, 'plots/%s.csv' % plot_name)

        # Data points.
        x = self.avg_by_date.index.tolist()
        gla_avg = self.avg_by_date['gla_index'].tolist()
        gla_std = self.std_by_date['gla_index'].tolist()

        # Define figure to handle the limits better.
        figure = plt.figure()

        # Plot options.
        plt.xlabel(u'Collection date')
        plt.ylabel(u'Ratio')
        plt.title(u'GLA index grouped by date')

        # Plot data.
        plt.errorbar(x, gla_avg, yerr=gla_std, fmt='-', label=u'GLA index', color='blue')
        plt.xlim(xmin=date(2006, 12, 01), xmax=date(2007, 12, 01))
        plt.ylim(ymin=0.0, ymax=1.0)
        figure.autofmt_xdate()

        # Plot save.
        figure.savefig(png_path)
        figure.savefig(pdf_path)

        #TODO Write CSV.

        #TODO Return data frame.

#TODO Correlation between GLA and tubule area. Does GLA vary with tubule size? 
# If yes, how to normalize the values?
# Hint: by using the residues from regression.
