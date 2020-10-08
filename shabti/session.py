# shabti/connection.py
from requests.auth import HTTPBasicAuth
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

from .version import __version__


class Session(object):
    """shabti Connection class"""
    def __init__(self, client_id, client_secret, endpoint, version="v5"):
        self._endpoint = '{}/iii/sierra-api/{}'.format(endpoint, version)
        auth = HTTPBasicAuth(client_id, client_secret)
        client = BackendApplicationClient(client_id=client_id)
        self._session = OAuth2Session(client=client)
        self._session.headers['User-Agent'] = 'shabti/{}'.format(__version__)
        self._token = self._session.fetch_token(token_url='{}/token'.format(self._endpoint), auth=auth)

    @property
    def token(self):
        return self._token
