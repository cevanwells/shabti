# shabti/resource_object.py
from abc import ABC, abstractmethod
from shabti import Session


class ResourceObject(ABC):
    _headers = {'Content-type': 'application/json'}
    _session = Session()

    def __init__(self, resource_id, **kwargs):
        self._path = ''
        if isinstance(resource_id, str):
            self._id = int(resource_id.split('/')[-1])
        else:
            self._id = resource_id

    @property
    def id(self):
        return self._id

    @abstractmethod
    def info(self, **kwargs):
        pass

    @classmethod
    def _create_path(cls, *args):
        path_sep = "/"
        return path_sep.join([str(cls._endpoint), *args])
