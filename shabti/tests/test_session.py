# shabti/tests/test_connection.py
import pytest

from shabti import QueryString


@pytest.mark.vcr()
def test_session_token(api_session):
    token_keys = ['access_token', 'token_type', 'expires_in']

    assert isinstance(api_session.token, dict)
    assert set(token_keys).issubset(api_session.token)
    assert api_session.token['token_type'] == 'bearer'


@pytest.mark.vcr()
def test_session_request_get(api_session, patron_keys):
    response = api_session._request("GET", "patrons/1401561")

    assert isinstance(response, dict)
    assert set(patron_keys).issubset(response.keys())


@pytest.mark.vcr()
def test_session_request_post(api_session, patron_keys):
    qry = QueryString("patron", "b", "equals", "D2491026132")
    params = {'offset': '0', 'limit': '10'}
    headers = {'Content-type': 'application/json'}

    response = api_session._request("POST", "patrons/query",
                                    data=qry.to_json(), params=params,
                                    headers=headers)

    assert isinstance(response, dict)
    assert response['entries'][0]['link'] == "https://library.thegdl.org/iii/sierra-api/v5/patrons/1401561"
