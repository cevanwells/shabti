# shabti/tests/test_connection.py
import pytest

from shabti import Session


@pytest.mark.vcr()
def test_connection_token(shabti_config):
    api = Session(shabti_config['client_id'],
                  shabti_config['client_secret'],
                  shabti_config['endpoint'])

    token_keys = ['access_token', 'token_type', 'expires_in']

    assert isinstance(api.token, dict)
    assert set(token_keys).issubset(api.token)
    assert api.token['token_type'] == 'bearer'
