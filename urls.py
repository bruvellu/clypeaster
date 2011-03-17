# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
import os
from gonad.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

site_media = os.path.join(
        os.path.dirname(__file__), 'media'
        )

urlpatterns = patterns('',
        (r'^$', main_page),
        # Admin
        (r'^admin/', include(admin.site.urls)),
        # Site media
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': site_media}),
)
