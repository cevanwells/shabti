# shabti/tests/test_connection.py
import pytest

from shabti import Session
from shabti import QueryString


@pytest.mark.vcr()
def test_session_token(shabti_config):
    api = Session(shabti_config['client_id'],
                  shabti_config['client_secret'],
                  shabti_config['endpoint'])

    token_keys = ['access_token', 'token_type', 'expires_in']

    assert isinstance(api.token, dict)
    assert set(token_keys).issubset(api.token)
    assert api.token['token_type'] == 'bearer'


@pytest.mark.vcr()
def test_session_request(shabti_config):
    api = Session(shabti_config['client_id'],
                  shabti_config['client_secret'],
                  shabti_config['endpoint'])

    response = api._request("GET", "patrons/1401561")

    patron_keys = ['id', 'expirationDate', 'birthDate', 'patronType',
                   'patronCodes', 'homeLibraryCode', 'message',
                   'blockInfo', 'moneyOwed']

    assert isinstance(response, dict)
    assert set(patron_keys).issubset(response)
