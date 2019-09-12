import logging
logging.getLogger('unicum').addHandler(logging.NullHandler())

from .singletonobject import *
from .factoryobject import *
from .linkedobject import *
from .persistentobject import *
from .datarange import *
from .visibleobject import *

