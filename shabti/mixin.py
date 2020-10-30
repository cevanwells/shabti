class ResourceMixin(object):
    _headers = {'Content-type': 'application/json'}
    _params = {'offset': '0', 'limit': '10'}

    def __init__(self, api, resource_id):
        url_array = resource_id.split('/')
        if len(url_array) > 1:
            self._id = resource_id.split('/')[-1]
        else:
            self._id = resource_id

        self._session = api

    @property
    def id(self):
        return self._id

    @classmethod
    def _create_path(cls, *args):
        built_path = '/'
        return built_path.join([cls._endpoint, *args])


class ResourceListMixin:
    pass
