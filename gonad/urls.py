# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from gonad.views import *

urlpatterns = patterns('',
        # Home.
        (r'^$', main_page),

        # Where you stage gonads.
        (r'^staging/$', staging_page),
        # List of unstaged sections.
        (r'^unstaged/$', unstaged_page),
        # List of pre-staged sections.
        (r'^prestaged/$', prestaged_page),
        # List of staged sections.
        (r'^staged/$', staged_page),

        # Results
        # Tubules measurements.
        (r'^results/tubules/$', tubules_results),

        # Tubule page.
        url(r'^tubule/(\d+)/$', tubule_page, name='tubule_url'),
        # Section page.
        url(r'^section/(\d+)/$', section_page, name='section_url'),
        # Specimen page.
        url(r'^specimen/(\d+)/$', specimen_page, name='specimen_url'),
)
