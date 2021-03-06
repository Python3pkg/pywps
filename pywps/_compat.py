##################################################################
# Copyright 2016 OSGeo Foundation,                               #
# represented by PyWPS Project Steering Committee,               #
# licensed under MIT, Please consult LICENSE.txt for details     #
##################################################################

import logging
import sys

__author__ = "Alex Morega"

LOGGER = logging.getLogger('PYWPS')
PY2 = sys.version_info[0] == 2

if PY2:
    LOGGER.debug('Python 2.x')
    text_type = str  # noqa
    from io import StringIO
    from flufl.enum import Enum
    from urllib.parse import urlparse
    from urllib.parse import urljoin
    from urllib.request import urlopen

else:
    LOGGER.debug('Python 3.x')
    text_type = str
    from io import StringIO
    from enum import Enum
    from urllib.parse import urlparse
    from urllib.parse import urljoin
    from urllib.request import urlopen
