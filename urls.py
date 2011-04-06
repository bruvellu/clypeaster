# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
import os
from gonad.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

static = os.path.join(os.path.dirname(__file__), 'static')

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
        # Admin.
        (r'^admin/', include(admin.site.urls)),
        # Site media.
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': static}),
)
