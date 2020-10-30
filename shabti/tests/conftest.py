import pytest
import os
from shabti import Session

CLIENT_ID = os.environ.get('SHABTI_CLIENT_ID', None)
CLIENT_SECRET = os.environ.get('SHABTI_CLIENT_SECRET', None)
ENDPOINT = os.environ.get('SHABTI_SIERRA_URL', None)


@pytest.fixture(scope="session")
def vcr_config():
    return {
        "filter_headers": [('authorization', 'DUMMY')],
        "decode_compressed_response": True,
        "record_mode": 'new_episodes',
        "cassette_library_dir": 'shabti/tests/cassettes'
    }


@pytest.fixture(scope="session")
def shabti_config():
    return {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'endpoint': ENDPOINT
    }


@pytest.fixture(scope="session")
def api_session():
    return Session(CLIENT_ID, CLIENT_SECRET, ENDPOINT)


@pytest.fixture(scope="session")
def patron_keys():
    return ['id', 'expirationDate', 'birthDate', 'patronType',
            'patronCodes', 'homeLibraryCode', 'message',
            'blockInfo', 'moneyOwed']
