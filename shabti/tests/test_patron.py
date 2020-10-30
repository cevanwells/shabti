# shabti/tests/test_patron.py
import pytest

from shabti import Patron


@pytest.mark.vcr()
def test_patron_from_url(api_session, patron_keys):
    res = Patron(api_session,
                 'https://library.thegdl.org/iii/sierra-api/v5/patrons/1401561')

    assert res.id == '1401561'


@pytest.mark.vcr()
def test_patron_from_id(api_session, patron_keys):
    res = Patron(api_session, '1401561')

    assert res.id == '1401561'


@pytest.mark.vcr()
def test_patron_from_barcode(api_session):
    res = Patron.from_barcode(api_session, 'D2491026132')

    assert res.id == '1401561'


@pytest.mark.vcr()
def test_patron_from_email(api_session):
    pass
