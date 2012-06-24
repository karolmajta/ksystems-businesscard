from django.db import models
from django.conf import settings
from django.template import loader, Context
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from dbtemplates.models import Template as DBTemplate

class BCardPage(models.Model):
    '''
    Represents a single page of the site.
    '''
    class Meta:
        verbose_name = _('businesscard page')
        verbose_name_plural = _('businesscard pages')
        unique_together = ('bcard', 'path')
    
    bcard = models.ForeignKey('ks_bcard.BCardSite', null=False)
    path = models.CharField(max_length=100, null=False)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    
    def __str__(self):
        return '{0}/{1}/{2}'.format(self.bcard.user.username,
                self.bcard.name, self.path) 

class BCardSite(models.Model):
    '''
    Represetnts a single site a user owns.
    '''
    class Meta:
        verbose_name = _('businesscard')
        verbose_name_plural = _('businesscards')
        unique_together = ('user', 'name')

        
    user = models.ForeignKey(User)
    name = models.SlugField()
    default_page = models.OneToOneField(BCardPage,
            related_name='+',
            null=True,
            blank=True)
    template = models.OneToOneField(DBTemplate, null=True, blank=True)
    
    def save(self, **kwargs):
        '''
        If it's object creation first save with None as self.default_page,
        create default page basing on user settings, and save again.
        Same happens for self.template.
        If it's an update just save.
        '''
        if self.pk is None:
            super(BCardSite, self).save(**kwargs)
            path = settings.BCARD_DEFAULT_PATH
            def_page = BCardPage(bcard=self, path=path)
            def_page.title = settings.BCARD_DEFAULT_PAGE_TITLE
            def_page.content = settings.BCARD_DEFAULT_PAGE_CONTENT
            def_page.save()
            self.default_page = def_page
            def_template_content = loader.get_template(
                    settings.BCARD_DEFAULT_TEMPLATE).render(Context())
            def_template_name = '{0}/{1}'.format(
                    self, settings.BCARD_DEFAULT_TEMPLATE_NAME)
            def_template = DBTemplate(
                    name=def_template_name, content=def_template_content)
            def_template.save()
            self.template = def_template
        super(BCardSite, self).save(**kwargs)
        
    def __str__(self):
        return '{0}/{1}'.format(self.user.username, self.name)