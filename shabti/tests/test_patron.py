# shabti/tests/test_patron.py
import pytest

from shabti import Session
from shabti import Patron


@pytest.mark.vcr()
def test_patron_from_url(shabti_config, patron_keys):
    api = Session(shabti_config['client_id'],
                  shabti_config['client_secret'],
                  shabti_config['endpoint'])

    res = Patron(api,
                 'https://library.thegdl.org/iii/sierra-api/v5/patrons/1401561')

    assert res.id == '1401561'


@pytest.mark.vcr()
def test_patron_from_id(shabti_config, patron_keys):
    api = Session(shabti_config['client_id'],
                  shabti_config['client_secret'],
                  shabti_config['endpoint'])

    res = Patron(api, '1401561')

    assert res.id == '1401561'


@pytest.mark.vcr()
def test_patron_from_barcode(shabti_config):
    api = Session(shabti_config['client_id'],
                  shabti_config['client_secret'],
                  shabti_config['endpoint'])

    res = Patron.from_barcode(api, 'D2491026132')

    assert res.id == '1401561'
