# -*- coding: utf-8 -*-

import os
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

media = os.path.join(os.path.dirname(__file__), 'media')

urlpatterns = patterns('',
        # Gonads.
        url(r'^', include('analysis.gonad.urls')),

        # Admin.
        (r'^admin/', include(admin.site.urls)),

        # Site media.
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': media}),
)
