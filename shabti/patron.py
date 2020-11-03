# shabti/patron.py
from shabti import ResourceObject


class Patron(ResourceObject):
    _endpoint = 'patrons'

    def __init__(self, resource_id, api_session=None):
        super().__init__(resource_id, api_session=api_session)

    @classmethod
    def from_barcode(cls, barcode):
        params = {'varFieldTag': 'b', 'varFieldContent': barcode}
        path = cls._create_path('find')
        res = cls._session._request("GET", path,
                                    params=params,
                                    headers=cls._headers)
        return cls(res['id'])

    def info(self, **kwargs):
        path = self._create_path(str(self._id))
        if 'fields' in kwargs:
            params = {'fields': kwargs['fields']}
        else:
            params = ''
        res = self._session._request("GET", path, params=params)

        return res
