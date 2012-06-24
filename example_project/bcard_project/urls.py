from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from ks_bcard.views import PageView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^pages/(?P<username>\w+)/(?P<sitename>[-\w]+)/$', PageView.as_view(), name='site'),

    url(r'^pages/(?P<username>\w+)/(?P<sitename>[-\w]+)/(?P<path>[-\/\w]+)$', PageView.as_view(), name='page'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()