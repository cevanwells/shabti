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
def test_session_request_get(shabti_config, patron_keys):
    api = Session(shabti_config['client_id'],
                  shabti_config['client_secret'],
                  shabti_config['endpoint'])

    response = api._request("GET", "patrons/1401561")

    assert isinstance(response, dict)
    assert set(patron_keys).issubset(response.keys())


@pytest.mark.vcr()
def test_session_request_post(shabti_config, patron_keys):
    api = Session(shabti_config['client_id'],
                  shabti_config['client_secret'],
                  shabti_config['endpoint'])
    qry = QueryString("patron", "b", "equals", "D2491026132")
    params = {'offset': '0', 'limit': '10'}
    headers = {'Content-type': 'application/json'}

    response = api._request("POST", "patrons/query", data=qry.to_json(), params=params, headers=headers)

    assert isinstance(response, dict)
    assert response['entries'][0]['link'] == "https://library.thegdl.org/iii/sierra-api/v5/patrons/1401561"
