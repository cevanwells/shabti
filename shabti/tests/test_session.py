# shabti/tests/test_connection.py
import vcr
import os

from shabti import Session


CLIENT_ID = os.environ.get('SHABTI_CLIENT_ID', None)
CLIENT_SECRET = os.environ.get('SHABTI_CLIENT_SECRET', None)
ENDPOINT = os.environ.get('SHABTI_SIERRA_URL', None)

test_vcr = vcr.VCR(
    filter_headers=['authorization'],
    decode_compressed_response=True,
    cassette_library_dir='shabti/tests/fixtures',
    record_mode='new_episodes'
)

@test_vcr.use_cassette('test_connection_token.yaml')
def test_connection_token():
    api = Session(CLIENT_ID, CLIENT_SECRET, ENDPOINT)

    assert isinstance(api.token, dict)
    assert set(['access_token', 'token_type', 'expires_in']).issubset(api.token)
    assert api.token['token_type'] == 'bearer'
