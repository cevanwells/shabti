# shabti/result_set.py

import json

from shabti import Patron


class ResultSet(object):
    def __init__(self, result_type, result_string):
        res = json.loads(result_string)

        self._type = result_type
        self._start = res['start']
        self._total = res['total']
        self._entries = []
        if self._type == 'patron':
            for entry in res['entries']:
                self._entries.append(Patron(entry['link']))

    def __len__(self):
        return self._total

    def __iter__(self):
        return iter(self.entries)

    def __getitem__(self, entry_num):
        return self._entries[entry_num]

    @property
    def total(self):
        return self._total

    @property
    def start(self):
        return self._start

    @property
    def entries(self):
        return self._entries
