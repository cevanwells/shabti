from shabti import ResourceMixin
from shabti import QueryString


class Patron(ResourceMixin):
    _endpoint = 'patrons'

    def __init__(self, api, resource_id):
        super().__init__(api, resource_id)

    @classmethod
    def from_barcode(cls, api, barcode):
        path = cls._create_path('query')
        qry = QueryString("patron", "b", "equals", barcode)
        res = api._request("POST", path, data=qry.to_json(),
                           params=cls._params, headers=cls._headers)

        return cls(api, res['entries'][0]['link'])

    @classmethod
    def from_email(cls, api, email):
        path = cls._create_path('query')
        qry = QueryString("patron", "z", "equals", email)
        res = api._request("POST", path, data=qry.to_json(),
                           params=cls._params, headers=cls._headers)

        return cls(api, res['entries'][0]['link'])
    @classmethod
    def from_address(cls, api, address):
        path = cls._create_path('query')
        qry = QueryString("patron", "a", "starts_with", address)
        res = api._request("POST", path, data=qry.to_json(),
                           params=cls._params, headers=cls._headers)

        return cls(api, res['entries'][0]['link'])
    def info(self, **kwargs):
        path = self._create_path(self._id)
        if 'fields' in kwargs:
            params = {'fields': kwargs['fields']}
        else:
            params = ''
        res = self._session._request("GET", path, params=params)

        return res
