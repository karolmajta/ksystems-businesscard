# This is dirty! If unit containes TestCase subclass with name A and functional
# contains TestCase subclass with name A it will only get imported once, but
# will do for now.

from unit import *
from functional import *