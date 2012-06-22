'''
Setup file for easy installation
'''
from os.path import join, dirname
from setuptools import setup

LONG_DESCRIPTION = '''
Ksystems-bcard is an app aiding easy creation of businesscard-like web pages
for many users.
'''


def long_description():
    '''
    Return long description from README.rst if it's present or return
    LONG_DESCRIPTION.
    '''
    try:
        return open(join(dirname(__file__), 'README.rst')).read()
    except IOError:
        return LONG_DESCRIPTION

setup(name='ksystems-businesscard',
      version='0.0.1',
      author='KSystems',
      author_email='office@ksystems.pl',
      description='Easy creation of businesscard-like web pages',
      license='Proprietary',
      keywords='django, businesscard',
      package_dir={'': 'src'},
      packages=['ks_bcard',
                'ks_bcard.tests'],
      long_description=long_description(),
      install_requires=['Django>=1.2.5',
                        'coverage>=3.5.2',
                        'django-coverage>=1.2.2',
                        'South>=0.7.5'],
      classifiers=['Framework :: Django',
                   'Development Status :: 4 - Beta',
                   'Topic :: Internet',
                   'License :: Proprietary',
                   'Intended Audience :: Developers',
                   'Environment :: Web Environment',
                   'Programming Language :: Python :: 2.7'])
