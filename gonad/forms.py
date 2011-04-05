# -*- coding: utf-8 -*-

from django.forms import ModelForm
from gonad.models import Section

class StagingForm(ModelForm):
    '''Main form for staging sections.'''
    class Meta:
        model = Section
        fields = ('isgreat', 'pre_stage', 'stage', 'uncertain', 'notes',)
