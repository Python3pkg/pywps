"""
Abstract Server class
"""

##################################################################
# Copyright 2016 OSGeo Foundation,                               #
# represented by PyWPS Project Steering Committee,               #
# licensed under MIT, Please consult LICENSE.txt for details     #
##################################################################


from abc import abstractmethod, ABCMeta
from contextlib import contextmanager
import shutil
import tempfile


@contextmanager
def temp_dir():
    """Creates temporary directory"""
    tmp = tempfile.mkdtemp()
    try:
        yield tmp
    finally:
        shutil.rmtree(tmp)


class PyWPSServerAbstract(object, metaclass=ABCMeta):
    """General stub for the PyWPS Server class.
    """

    route_base = '/'

    @abstractmethod
    def run(self):
        raise NotImplementedError()
