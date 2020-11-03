# shabti/tests/test_patron.py
import pytest

from shabti import Patron


@pytest.mark.vcr()
def test_patron_from_url():
    patron = Patron('https://library.thegdl.org/iii/sierra-api/v5/patrons/1401561')

    assert patron.id == 1401561


@pytest.mark.vcr()
def test_patron_from_id():
    patron = Patron(1401561)

    assert patron.id == 1401561


@pytest.mark.vcr()
def test_patron_from_barcode():
    patron = Patron.from_barcode('D2491026132')

    assert patron.id == 1401561


@pytest.mark.vcr()
def test_patron_info(patron_keys):
    patron = Patron(1401561)
    res = patron.info()

    assert isinstance(res, dict)
    assert set(patron_keys).issubset(res.keys())


@pytest.mark.vcr()
def test_patron_info_with_fields(custom_patron_keys):
    patron = Patron(1401561)
    res = patron.info(fields=",".join(custom_patron_keys))

    assert isinstance(res, dict)
    assert set(custom_patron_keys).issubset(res.keys())
    assert res['id'] == 1401561
    assert res['names'][0] == "McCoy, Hank Philip"
