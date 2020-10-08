import pytest
import os

CLIENT_ID = os.environ.get('SHABTI_CLIENT_ID', None)
CLIENT_SECRET = os.environ.get('SHABTI_CLIENT_SECRET', None)
ENDPOINT = os.environ.get('SHABTI_SIERRA_URL', None)


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [('authorization', 'DUMMY')],
        "decode_compressed_response": True,
        "record_mode": 'new_episodes',
        "cassette_library_dir": 'shabti/tests/cassettes'
    }


@pytest.fixture(scope="module")
def shabti_config():
    return {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'endpoint': ENDPOINT
    }
