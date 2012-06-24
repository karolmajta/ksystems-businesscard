from django.conf.urls import patterns, include, url

from ..views import PageView

urlpatterns = patterns('',
    url(r'^(?P<username>\w+)/(?P<sitename>[-\w]+)/$', PageView.as_view(), name='site'),
)
