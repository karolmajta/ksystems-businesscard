import sys
from django.conf import settings
 

class StandaloneTestSuite(object):
    
    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'django.contrib.sites',
        # third party
        'django_coverage',
        'dbtemplates',
        'reversion',
    )

    def __init__(self, *args, **kwargs):
        self.apps = args

    def run_tests(self):
        """
        Fire up the Django test suite developed for version 1.4
        """
        settings.configure(
            DEBUG = True,
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': ':memory:',
                    'USER': '',
                    'PASSWORD': '',
                    'HOST': '',
                    'PORT': '',
                }
            },
            INSTALLED_APPS = self.INSTALLED_APPS + self.apps,
            ROOT_URLCONF = 'ks_bcard.tests.urls',
	    SITE_ID = 1,
        )
        from django.test.simple import DjangoTestSuiteRunner
        failures = DjangoTestSuiteRunner().run_tests(self.apps, verbosity=1)
        if failures:
            sys.exit(failures)

if __name__ == '__main__':
    StandaloneTestSuite('ks_bcard').run_tests()
