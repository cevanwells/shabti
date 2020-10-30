# shabti/tests/test_patron.py
import pytest

from shabti import Patron


@pytest.mark.vcr()
def test_patron_from_url(api_session):
    patron = Patron(api_session,
                    'https://library.thegdl.org/iii/sierra-api/v5/patrons/1401561')

    assert patron.id == '1401561'


@pytest.mark.vcr()
def test_patron_from_id(api_session):
    patron = Patron(api_session, '1401561')

    assert patron.id == '1401561'


@pytest.mark.vcr()
def test_patron_from_barcode(api_session):
    res = Patron.from_barcode(api_session, 'D2491026132')

    assert res.id == '1401561'


@pytest.mark.vcr()
def test_patron_from_email(api_session):
    res = Patron.from_email(api_session, 'hmccoy@xavierinstitute.edu')
@pytest.mark.vcr()
@pytest.mark.skip(reason="this test requires a refactoring of QueryString")
def test_patron_from_phone(api_session):
    patron = Patron.from_phone(api_session, '810-555-4247')

    assert patron.id == '1401561'
@pytest.mark.vcr()
def test_patron_from_address(api_session):
    patron = Patron.from_address(api_session, '101 dundee lane')

    assert patron.id == '1401561'

    assert res.id == '1401561'
@pytest.mark.vcr()
def test_python_info(api_session, patron_keys):
    patron = Patron(api_session, '1401561')
    res = patron.info()

    assert isinstance(res, dict)
    assert set(patron_keys).issubset(res.keys())


@pytest.mark.vcr()
def test_python_info_with_fields(api_session):
    patron = Patron(api_session, '1401561')
    fields = ['names', 'barcodes', 'emails', 'addresses']
    res = patron.info(fields=fields)

    assert isinstance(res, dict)
    assert set(fields).issubset(res.keys())
    assert res['id'] == 1401561
    assert res['names'][0] == "McCoy, Hank Philip"
