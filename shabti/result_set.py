# shabti/result_set.py

import json

from shabti import Session
from shabti import Patron


class ResultSet(object):
    _session = Session()

    def __init__(self, result_type, result_string):
        res = json.loads(result_string)

        self._type = result_type
        self._start = res['start']
        self._total = res['total']
        self._entries = []
        if self._type == 'patrons':
            for entry in res['entries']:
                self._entries.append(Patron(entry['link']))

    def __len__(self):
        return self._total

    def __iter__(self):
        return iter(self.entries)

    def __getitem__(self, entry_num):
        return self._entries[entry_num]

    def _list(self):
        return [str(resource.id) for resource in self._entries]

    @property
    def total(self):
        return self._total

    @property
    def start(self):
        return self._start

    @property
    def entries(self):
        return self._entries

    def info(self, **kwargs):
        params = {'id': ",".join(self._list())}
        if 'fields' in kwargs:
            params['fields'] = kwargs['fields']

        path = self._entries[0]._create_path('')

        ret = self._session._request("GET", path, params=params)
        return ret['entries']
