# -*- coding: utf-8 -*-

from datetime import date
#from numpy import array, mean, std
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

        # Group data by date.
        self.data_by_date = self.data.groupby('date')

        # Define grouped data by date.
        self.avg_by_date = self.data_by_date.mean()
        self.std_by_date = self.data_by_date.std()

    def build_data_frame(self, tubules):
        '''Build data frames for tubules plots using pandas.'''
        # Get objects.
        ids = tubules.values_list('id', flat=True)
        cross_sections = tubules.values_list('cross_section', flat=True)
        germ_layers = tubules.values_list('germ_layer', flat=True)
        gla_indexes = tubules.values_list('gla_index', flat=True)
        dates = tubules.values_list('specimen__collection_date', flat=True)
        genders = tubules.values_list('specimen__gender', flat=True)
        gonad_weights = tubules.values_list('specimen__gonad_weight', flat=True)

        # Instantiate dictionary for DataFrame.
        data_dic = {
                'cross_section': cross_sections,
                'germ_layer': germ_layers,
                'gla_index': gla_indexes,
                'date': dates,
                'gender': genders,
                'gonad_weight': gonad_weights,
                }

        # Create DataFrame for tubule data.
        self.data = DataFrame(data_dic, index=ids)

        # Write CSV
        csv_path = join(MEDIA_ROOT, 'plots/tubules_data.csv')
        self.data.to_csv(csv_path)

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
        png_file = 'plots/%s.png' % plot_name
        png_path = join(MEDIA_ROOT, png_file)
        pdf_file = 'plots/%s.pdf' % plot_name
        pdf_path = join(MEDIA_ROOT, pdf_file)
        csv_file = 'plots/%s.csv' % plot_name
        csv_path = join(MEDIA_ROOT, csv_file)

        # Define figure to handle the limits better.
        figure = plt.figure()

        # Plot options.
        plt.title(u'GLA index against the cross section area')

        # Plot data.
        plt.scatter(cross_sections, gla_indexes)

        # Plot save.
        figure.savefig(png_path)
        figure.savefig(pdf_path)

        # Create data frame.
        plot_data_dic = {
                'cross_section': cross_sections,
                'gla_index': gla_indexes,
                }
        plot_data = DataFrame(plot_data_dic)

        # Write CSV.
        plot_data.to_csv(csv_path)

        # Create plot object.
        plot = {
                'data': plot_data,
                'png': png_file,
                'pdf': pdf_file,
                'csv': csv_file,
                }

        return plot

    def scatter_gla_by_weight(self):
        '''Scatter plot with GLA by gonad weight.'''
        # Define plot name.
        plot_name = 'gla_by_weight'

        # Clear plot.
        plt.clf()

        # Define data.
        gonad_weights = self.data['gonad_weight'].tolist()
        gla_indexes = self.data['gla_index'].tolist()

        # Define paths.
        png_file = 'plots/%s.png' % plot_name
        png_path = join(MEDIA_ROOT, png_file)
        pdf_file = 'plots/%s.pdf' % plot_name
        pdf_path = join(MEDIA_ROOT, pdf_file)
        csv_file = 'plots/%s.csv' % plot_name
        csv_path = join(MEDIA_ROOT, csv_file)

        # Define figure to handle the limits better.
        figure = plt.figure()

        # Plot options.
        plt.title(u'GLA index against gonad weight')

        # Plot data.
        plt.scatter(gonad_weights, gla_indexes)

        # Plot save.
        figure.savefig(png_path)
        figure.savefig(pdf_path)

        # Create data frame.
        plot_data_dic = {
                'gonad_weight': gonad_weights,
                'gla_index': gla_indexes,
                }
        plot_data = DataFrame(plot_data_dic)

        # Write CSV.
        plot_data.to_csv(csv_path)

        # Create plot object.
        plot = {
                'data': plot_data,
                'png': png_file,
                'pdf': pdf_file,
                'csv': csv_file,
                }

        return plot

    def scatter_cross_by_weight(self):
        '''Scatter plot with cross section by gonad weight.'''
        # Define plot name.
        plot_name = 'cross_by_weight'

        # Clear plot.
        plt.clf()

        # Define data.
        gonad_weights = self.data['gonad_weight'].tolist()
        cross_sections = self.data['cross_section'].tolist()

        # Define paths.
        png_file = 'plots/%s.png' % plot_name
        png_path = join(MEDIA_ROOT, png_file)
        pdf_file = 'plots/%s.pdf' % plot_name
        pdf_path = join(MEDIA_ROOT, pdf_file)
        csv_file = 'plots/%s.csv' % plot_name
        csv_path = join(MEDIA_ROOT, csv_file)

        # Define figure to handle the limits better.
        figure = plt.figure()

        # Plot options.
        plt.title(u'Cross section area against gonad weight')

        # Plot data.
        plt.scatter(gonad_weights, cross_sections)

        # Plot save.
        figure.savefig(png_path)
        figure.savefig(pdf_path)

        # Create data frame.
        plot_data_dic = {
                'gonad_weight': gonad_weights,
                'cross_section': cross_sections,
                }
        plot_data = DataFrame(plot_data_dic)

        # Write CSV.
        plot_data.to_csv(csv_path)

        # Create plot object.
        plot = {
                'data': plot_data,
                'png': png_file,
                'pdf': pdf_file,
                'csv': csv_file,
                }

        return plot

    def scatter_germ_by_weight(self):
        '''Scatter plot with germ layer by gonad weight.'''
        # Define plot name.
        plot_name = 'germ_by_weight'

        # Clear plot.
        plt.clf()

        # Define data.
        gonad_weights = self.data['gonad_weight'].tolist()
        germ_layers = self.data['germ_layer'].tolist()

        # Define paths.
        png_file = 'plots/%s.png' % plot_name
        png_path = join(MEDIA_ROOT, png_file)
        pdf_file = 'plots/%s.pdf' % plot_name
        pdf_path = join(MEDIA_ROOT, pdf_file)
        csv_file = 'plots/%s.csv' % plot_name
        csv_path = join(MEDIA_ROOT, csv_file)

        # Define figure to handle the limits better.
        figure = plt.figure()

        # Plot options.
        plt.title(u'Germ layer area against gonad weight')

        # Plot data.
        plt.scatter(gonad_weights, germ_layers)

        # Plot save.
        figure.savefig(png_path)
        figure.savefig(pdf_path)

        # Create data frame.
        plot_data_dic = {
                'gonad_weight': gonad_weights,
                'germ_layer': germ_layers,
                }
        plot_data = DataFrame(plot_data_dic)

        # Write CSV.
        plot_data.to_csv(csv_path)

        # Create plot object.
        plot = {
                'data': plot_data,
                'png': png_file,
                'pdf': pdf_file,
                'csv': csv_file,
                }

        return plot

    def plot_areamean_by_date(self):
        '''Build plot for tubules measurements grouped by date.'''

        # Define plot name.
        plot_name = 'areamean_by_date'

        # Clear plot.
        plt.clf()

        # Define paths.
        png_file = 'plots/%s.png' % plot_name
        png_path = join(MEDIA_ROOT, png_file)
        pdf_file = 'plots/%s.pdf' % plot_name
        pdf_path = join(MEDIA_ROOT, pdf_file)
        csv_file = 'plots/%s.csv' % plot_name
        csv_path = join(MEDIA_ROOT, csv_file)

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

        # Create data frame.
        plot_data_dic = {
                'germ_layer': germ_layer,
                'cross_section': cross_section,
                'germ_layer_std': germ_layer_std,
                'cross_section_std': cross_section_std,
                }
        plot_data = DataFrame(plot_data_dic, index=x)

        # Write CSV.
        plot_data.to_csv(csv_path)

        # Create plot object.
        plot = {
                'data': plot_data,
                'png': png_file,
                'pdf': pdf_file,
                'csv': csv_file,
                }

        return plot

    def plot_gla_by_date(self):
        '''Build plot for gla indexes grouped by date.'''

        # Define plot name.
        plot_name = 'gla_by_date'

        # Clear plot.
        plt.clf()

        # Define paths.
        png_file = 'plots/%s.png' % plot_name
        png_path = join(MEDIA_ROOT, png_file)
        pdf_file = 'plots/%s.pdf' % plot_name
        pdf_path = join(MEDIA_ROOT, pdf_file)
        csv_file = 'plots/%s.csv' % plot_name
        csv_path = join(MEDIA_ROOT, csv_file)

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

        # Create data frame.
        plot_data_dic = {
                'gla_avg': gla_avg,
                'gla_std': gla_std,
                }
        plot_data = DataFrame(plot_data_dic, index=x)

        # Write CSV.
        plot_data.to_csv(csv_path)

        # Create plot object.
        plot = {
                'data': plot_data,
                'png': png_file,
                'pdf': pdf_file,
                'csv': csv_file,
                }

        return plot


#TODO Correlation between GLA and tubule area. Does GLA vary with tubule size? 
# If yes, how to normalize the values?
# Hint: by using the residues from regression.
#TODO Do statistics.
