# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from numpy import array, mean, std

GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

OBJECTIVES = (
        ('10x', '10x'),
        ('20x', '20x'),
        ('40x', '40x'),
        ('100x', '100x'),
    )


class Specimen(models.Model):
    '''General characteristics of a sea biscuit speciment.'''
    oral = models.ImageField('oral side', upload_to='/static/morphometrics', 
            help_text='Photograph of specimen\'s oral side.')
    aboral = models.ImageField('aboral side', 
            upload_to='/static/morphometrics',
            help_text='Photograph of specimen\'s aboral side.')
    identifier = models.CharField(max_length=10, unique=True,
            help_text='Unique identification key of the specimen.')
    collection_date = models.DateField(null=True,
            help_text='Date when the specimen was collected and fixed.')
    location = models.CharField(max_length=10,
            help_text='Place where the specimen was collected.')
    gender = models.CharField(max_length=1, choices=GENDERS,
            help_text='Gender of the specimen.')
    weight = models.FloatField(null=True, blank=True,
            help_text='Wet-weight of the specimen in g.')
    gonad_weight = models.FloatField(null=True, blank=True, 
            help_text='Wet-weight of a single dissected gonad of the specimen '
            'in g.')
    length = models.FloatField(null=True, blank=True,
            help_text='Length of the specimen measured in a straight line from'
            ' the ambitus of ambulacrum III to the ambitus of interambulacrum '
            '5 in mm.')
    width = models.FloatField(null=True, blank=True,
            help_text='Larger width of the specimen measured in a straight '
            'line from the ambitus in mm (usually coincides with the distance '
            'between ambitus of ambulacrum IV and ambulacrum II.')
    height = models.PositiveIntegerField(null=True, blank=True, 
            help_text='Height of the specimen measured from the ground to the '
            'apex in mm.')
    border = models.PositiveIntegerField('border thickness', null=True, 
            blank=True, help_text='Thickness of the border of the specimen at '
            'the ambitus of ambulacrum III measured in mm.')
    # TODO Connect signal to auto update everytime a photo is staged.
    consensus_stage = models.CharField(max_length=300, blank=True,
            default='no data', help_text='Consensus gonadal stage of the ' 
            'specimen generate by the classification of individual slides.')
    # Mean and standard deviation values from tubules.
    cross_sections_mean = models.FloatField('mean of cross sections areas', 
            null=True, blank=True, help_text='Mean of the cross sections areas'
            ' in µm^2 of the different tubule\'s from the specimen.')
    cross_sections_sd = models.FloatField('sd of cross sections areas', 
            null=True, blank=True, help_text='Standard deviation of the cross '
            'sections areas in µm^2 of different tubule\'s from the '
            'specimen.')
    germ_layers_mean = models.FloatField('mean of germ layers areas', 
            null=True, blank=True, help_text='Mean of germ layers areas in '
            'µm^2.')
    germ_layers_sd = models.FloatField('sd of germ layers areas', null=True, 
            blank=True, help_text='Standard deviation of germ layers areas in '
            'µm^2.')
    gla_indexes_mean = models.FloatField('mean of germ layers areas indexes', 
            null=True, blank=True, help_text='Mean of indexes showing the '
            'proportion of the germ layer area in the total area of the '
            'tubule\'s cross section.')
    gla_indexes_sd = models.FloatField('sd of germ layers areas indexes', 
            null=True, blank=True, help_text='Standard deviation of indexes '
            'showing the proportion of the germ layer area in the total area '
            'of the tubule\'s cross section.')

    def __unicode__(self):
        if self.gender:
            return '%s (%s)' % (self.identifier, self.gender)
        else:
            return self.identifier


class Stage(models.Model):
    '''Gonadal stage.'''
    name = models.CharField('stage name', max_length=100,
            help_text='Name of the gonadal stage.')
    description = models.TextField('stage characteristics', blank=True,
            help_text='Full description with histological details of the '
            'stage.')

    def __unicode__(self):
        return self.name


class SectionPhoto(models.Model):
    '''Abstract class for photos of histological sections.'''
    filename = models.CharField('filename', max_length=100,
            help_text='Filename of the photo archive.')
    objective = models.CharField('objective magnification', max_length=3, 
            choices=OBJECTIVES, help_text='Magnification of the objective used'
            ' to take the photomicrograph.')
    isgreat = models.BooleanField('good for publication', default=False,
            help_text='Mark best photos to be used in publication.')

    class Meta:
        abstract = True


class Tubule(SectionPhoto):
    '''Photo of a gonadal tubule.'''
    photo = models.ImageField('photo of the tubule', 
            upload_to='/static/tubules',
            help_text='Photomicrograph of the gonadal tubule.')
    specimen = models.ForeignKey(Specimen,
            verbose_name='specimen of this tubule', help_text='Specimen from '
            'which the gonadal sample was taken.')
    cross_section = models.FloatField('cross section area', null=True, 
            blank=True, help_text='Total area of the tubule\'s cross section '
            'in µm^2.')
    germ_layer = models.FloatField('germ layer area', null=True, blank=True,
            help_text='Area of the germ layer of the tubule\'s cross section ' 
            'in µm^2.')
    max_diameter = models.FloatField('maximum diameter', null=True, blank=True, 
            help_text='Maximum diameter of the tubule\'s cross section.')
    min_diameter = models.FloatField('minimum diameter', null=True, blank=True, 
            help_text='Minimum diameter of the tubule\'s cross section.')
    gla_index = models.FloatField('germ layer area index', null=True, 
            blank=True, help_text='Index showing the proportion of the germ '
            'layer area in the total area of the tubule\'s cross section.')

    def __unicode__(self):
        return '%s (%s)' % (self.filename, self.specimen.identifier)


class Section(SectionPhoto):
    '''Photo of a gonadal histological section.'''
    photo = models.ImageField('photo of gonadal tissue', 
            upload_to='/static/sections', help_text='A general section of '
            'gonadal tissue.')
    specimen = models.ForeignKey(Specimen,
            verbose_name='specimen of this section', help_text='Specimen from '
            'which the gonadal sample was taken.')
    pas = models.BooleanField('is PAS stained', help_text='Indicates if slide '
            'was stained with PAS reaction. Blue Toluidine, otherwise.')
    stage = models.ForeignKey(Stage, verbose_name='official gonadal stage', 
            null=True, blank=True, help_text='Indicates the definitive gonadal'
            ' stage of this histological section.')
    pre_stage = models.CharField('initial classification', max_length=100, 
            blank=True, help_text='Indicates the preliminary gonadal stage '
            'classification of this histological section.')
    notes = models.TextField('annotations', blank=True,
            help_text='Observations about this specific section.')
    uncertain = models.BooleanField('undefined stage', default=False, 
            help_text='Indicates if the classification of the gonadal stage is'
            ' dubious.')

    def __unicode__(self):
        return '%s (%s)' % (self.filename, self.specimen.identifier)


class StagingForm(ModelForm):
    '''Main form for staging sections.'''
    class Meta:
        model = Section
        fields = ('isgreat', 'pre_stage', 'stage', 'uncertain', 'notes',)


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
    # cross_section
    cross_section_array = array([each.cross_section for each in tubules if 
        each.cross_section])
    sp.cross_sections_mean = cross_section_array.mean()
    sp.cross_sections_sd = cross_section_array.std()
    # germ_layer
    germ_layer_array = array([each.germ_layer for each in tubules if 
        each.germ_layer])
    sp.germ_layers_mean = germ_layer_array.mean()
    sp.germ_layers_sd = germ_layer_array.std()
    # gla_index
    gla_index_array = array([each.gla_index for each in tubules if 
        each.gla_index])
    sp.gla_indexes_mean = gla_index_array.mean()
    sp.gla_indexes_sd = gla_index_array.std()
    # Save specimen.
    sp.save()

models.signals.pre_save.connect(calculate_gla, sender=Tubule)
models.signals.post_save.connect(tubule_means, sender=Tubule)
