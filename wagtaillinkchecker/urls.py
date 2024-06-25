from __future__ import absolute_import, unicode_literals

from django.urls import re_path

from wagtaillinkchecker import views

urlpatterns = [
    re_path(r'^$', views.index,
        name='wagtaillinkchecker'),
    re_path(r'^settings/$', views.settings,
        name='wagtaillinkchecker_settings'),
    re_path(r'^scan/$', views.run_scan,
        name='wagtaillinkchecker_runscan'),
    re_path(r'^scan/(?P<scan_pk>\d+)/$', views.scan,
        name='wagtaillinkchecker_scan'),
    re_path(r'^scan/(?P<scan_pk>\d+)/delete$', views.delete,
        name='wagtaillinkchecker_delete'),
]
