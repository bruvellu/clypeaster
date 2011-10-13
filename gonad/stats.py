# -*- coding: utf-8 -*-
from datetime import date
from numpy import array, mean, std
from os import remove
from os.path import join
from pandas import *

import matplotlib.pyplot as plt

from settings import MEDIA_ROOT

#TODO Mean of tubule measurements by date (all tubules, not by specimen).
# Cross section area, germ layer area, and GLA index.


class TubulePlots:
    def __init__(self, tubules):
        self.tubules = tubules

        # Build data frame.
        self.data = self.build_data_frame(tubules)

        # Build plots.
        self.scatter_gla_by_cross()
        self.plot_areamean_by_date()
        self.plot_gla_by_date()

    def build_data_frame(self, tubules):
        '''Build dataframes for tubules plots using pandas.'''
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

        # Create DataFrame for tubule data.
        data_frame = DataFrame(data_dic, index=ids)

        return data_frame

    def scatter_gla_by_cross(self):
        '''Scatter plot with GLA by cross section area.'''
        # Clear plot.
        plt.clf()

        # Define data.
        cross_sections = self.data['cross_section'].tolist()
        gla_indexes = self.data['gla_index'].tolist()

        # Define paths.
        png_path = join(MEDIA_ROOT, 'plots/gla_by_cross.png')
        pdf_path = join(MEDIA_ROOT, 'plots/gla_by_cross.pdf')

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
        # Clear plot.
        plt.clf()

        # Define grouped data.
        avg_data = self.data.groupby('dates').mean()

        # Define paths.
        png_path = join(MEDIA_ROOT, 'plots/areamean_by_date.png')
        pdf_path = join(MEDIA_ROOT, 'plots/areamean_by_date.pdf')

        #print data.mean()
        ## Data points.
        x = avg_data.index.tolist()
        germ_layer = avg_data['germ_layer'].tolist()
        cross_section = avg_data['cross_section'].tolist()
        #print germ_layer

        # Define figure to handle the limits better.
        figure = plt.figure()

        # Plot options.
        plt.xlabel(u'Collection date')
        plt.ylabel(u'Area in µm^2')
        plt.title(u'Cross section and germ layer area grouped by date')

        # Plot data.
        plt.plot_date(x, cross_section, fmt='-', label=u'Cross section area', color='blue')
        plt.plot_date(x, germ_layer, fmt='-', label=u'Germ layer area', color='red')
        # Insert caption.
        plt.legend(loc='upper right')
        # Define x limits.
        plt.xlim(xmin=date(2006, 12, 01), xmax=date(2007, 12, 01))
        # Auto adjust figure paddings.
        figure.autofmt_xdate()

        # Plot save.
        figure.savefig(png_path)
        figure.savefig(pdf_path)

    def plot_gla_by_date(self):
        '''Build plot for gla indexes grouped by date.'''
        # Clear plot.
        plt.clf()

        # Define grouped data.
        avg_data = self.data.groupby('dates').mean()

        # Define paths.
        png_path = join(MEDIA_ROOT, 'plots/gla_by_date.png')
        pdf_path = join(MEDIA_ROOT, 'plots/gla_by_date.pdf')

        # Data points.
        x = avg_data.index.tolist()
        gla_index = avg_data['gla_index'].tolist()

        # Define figure to handle the limits better.
        figure = plt.figure()

        # Plot options.
        plt.xlabel(u'Collection date')
        plt.ylabel(u'Ratio')
        plt.title(u'GLA index grouped by date')

        # Plot data.
        plt.plot_date(x, gla_index, fmt='-', label=u'GLA index', color='blue')
        plt.xlim(xmin=date(2006, 12, 01), xmax=date(2007, 12, 01))
        plt.ylim(ymin=0.0, ymax=1.0)
        figure.autofmt_xdate()

        # Plot save.
        figure.savefig(png_path)
        figure.savefig(pdf_path)


#TODO Correlation between GLA and tubule area. Does GLA vary with tubule size? 
# If yes, how to normalize the values?
# Hint: by using the residues from regression.
