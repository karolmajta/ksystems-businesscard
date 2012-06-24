from django.test import TestCase

from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.conf import settings
from django.template import loader, Context, Template
from django.contrib.auth.models import User

from ..models import BCardSite, BCardPage
from ..views import PageView

class BCardSiteTest(TestCase):
    
    def test_default_page_gets_created_on_creation(self):
        u = User.objects.create_user(username='company', password='somepass')
        s = BCardSite(user=u, name='site')
        s.save()
        self.assertIsNotNone(s.default_page)
    
    def test_default_page_has_title_from_settings(self):
        u = User.objects.create_user(username='company', password='pass')
        s = BCardSite(user=u, name='site')
        s.save()
        self.assertEquals(
                s.default_page.title, settings.BCARD_DEFAULT_PAGE_TITLE)
    
    def test_default_page_has_content_from_settings(self):
        u = User.objects.create_user(username='comp', password='pass')
        s = BCardSite(user=u, name='site')
        s.save()
        self.assertEquals(
                s.default_page.content, settings.BCARD_DEFAULT_PAGE_CONTENT)
    
    def test_template_gets_set_to_stencil_contents(self):
        u = User.objects.create_user(username='comp', password='pass')
        s = BCardSite(user=u, name='site')
        s.save()
        c = Context()
        expected = loader.get_template(settings.BCARD_DEFAULT_TEMPLATE)
        actual = s.template
        self.assertEquals(expected.render(c), actual.content)
    
    def test_cant_create_same_user_same_sitename(self):
        u1 = User.objects.create_user(username='comp', password='pass')
        BCardSite(user=u1, name='site').save()
        with self.assertRaises(IntegrityError):
            BCardSite(user=u1, name='site').save()
    
class BCardPageTest(TestCase):
    
    def test_cant_create_same_site_same_path(self):
        u = User.objects.create_user(username='comp', password='p')
        s = BCardSite(user=u, name='site')
        s.save()
        with self.assertRaises(IntegrityError):
            BCardPage(bcard=s, path=settings.BCARD_DEFAULT_PATH).save()
        
class PageViewTest(TestCase):
    
    def test_get_object_returns_basing_on_kwargs(self):
        u = User.objects.create_user(username='company', password='somepass')
        s = BCardSite(user=u, name='site')
        s.save()
        p = BCardPage(bcard=s, path='other-path/')
        p.save()
        
        v = PageView()
        v.kwargs = {'username': u.username,
                    'sitename': s.name,
                    'path': p.path}
        
        expected = p
        actual = v.get_object()
        self.assertEquals(actual, expected)
    
    def test_if_no_path_is_provided_returns_sites_default(self):
        u = User.objects.create_user(username='company', password='pass')
        s = BCardSite(user=u, name='site')
        s.save()
        
        v = PageView()
        v.kwargs = {'username': u.username, 'sitename': s.name}
        
        expected = s.default_page
        actual = v.get_object()
        self.assertEquals(expected, actual)
    
    def test_template_is_taken_from_site(self):
        u = User.objects.create_user(username='c', password='p')
        s = BCardSite(user=u, name='site')
        s.save()
        v = PageView()
        v.object = s.default_page
        
        expected = Template(s.template.content).render(Context())
        actual = v.get_template_names().render(Context())
        self.assertEquals(expected, actual)
    
    def test_expected_context(self):
        u = User.objects.create_user(username='c', password='p')
        s = BCardSite(user=u, name='site')
        s.save()
        p = BCardPage(bcard=s, path='contact-us/')
        p.save()
        v = PageView()
        v.kwargs = {'username': u.username}
        v.object = s.default_page
        ctx = v.get_context_data()
        self.assertEquals(ctx['company'], u.username)
        self.assertEquals(ctx['site_name'], s.name)
        self.assertEquals(ctx['page_title'], s.default_page.title)
        self.assertEquals(ctx['page_content'], s.default_page.content)
        self.assertEquals(2, len(ctx['pages']))