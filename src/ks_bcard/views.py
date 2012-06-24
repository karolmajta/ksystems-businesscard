from django.core.urlresolvers import reverse
from django.views.generic import DetailView
from django.template import Template, Context
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User

from models import BCardPage, BCardSite

class PageView(DetailView):
    '''
    View for displaying BCardSites and all of its contents.
    '''
    
    def get_object(self):
        '''
        If no path is provided use default page for username and sitename.
        If path is provided get site by username, sitename and path.
        '''
        user = get_object_or_404(User, username=self.kwargs['username'])
        bcard = get_object_or_404(BCardSite,
                user=user, name=self.kwargs['sitename'])
        if self.kwargs.has_key('path'):
            page = get_object_or_404(BCardPage,
                    bcard=bcard, path=self.kwargs['path'])
        else:
            page = bcard.default_page
        return page
    
    def get_template_names(self):
        '''
        Just get template from site.
        '''
        return Template(self.object.bcard.template.content)
    
    def get_context_data(self, **kwargs):
        page_objects = BCardPage.objects.filter(bcard=self.object.bcard)
        pages = []
        for p in page_objects:
            pages.append({
                'title': p.title,
                'url': reverse('page', kwargs={
                    'username': self.kwargs['username'],
                    'sitename': self.object.bcard.name,
                    'path': p.path,
                })
            })
        ctx = Context({
            'company': self.object.bcard.user.username,
            'site_name': self.object.bcard.name,
            'page_title': self.object.title,
            'page_content': self.object.content,
            'pages': pages,
        })
        return ctx