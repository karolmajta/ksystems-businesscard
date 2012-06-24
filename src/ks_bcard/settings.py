# DO NOT EDIT THIS FILE! THIS FILE IS INTENDED AS DEFAULT SETTINGS MODULE
# TO OVERRIDE ANY OF THEM EDIT YOUR PROJECT'S MAIN SETTINGS FILE

from django.conf import settings
from django.utils.translation import ugettext as _

# CREATE DEFAULT SETTINGS FOR YOUR APP HERE

# Default URL path to page that will be autocreated when new site
# is created.
BCARD_DEFAULT_PATH = 'welcome/'

# Default title of the autocreated page
BCARD_DEFAULT_PAGE_TITLE = _('Welcome to our page!')

# Default content of the autocreated page
BCARD_DEFAULT_PAGE_CONTENT = _('''
    <p>This page has not yet been created</p>
''')

# This template will be used as a stencil for bcard template
# on creation
BCARD_DEFAULT_TEMPLATE = 'ks_bcard/default.html'

# Name for default template
BCARD_DEFAULT_TEMPLATE_NAME = 'default.html'