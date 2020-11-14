from abc import ABCMeta, abstractmethod
import requests
import aiohttp
from typing import Optional
from collections.abc import Iterable
from .information import Scopes
from .exceptions import UnknownScope
from time import time


def make_scopes_to_set(scopes) -> set:
    ret = set()

    if isinstance(scopes, str):
        scopes = scopes.split(' ')

    ret.update([scope.strip().lower() for scope in scopes])

    return ret


class BearerToken:
    def __init__(self, access_token, *, expires: Optional[int] = None, expires_in: Optional[int] = None, scope: Optional, token_type=None):
        """A Bearer Token.
        :param access_token The Bearer Token.
        :param scope The scopes of that Token.
        :param expires The Unix-Timestamp of the expiring datetime.
        :param expires_in The number of seconds until the Token expires
        :param token_type Variable gets ignored.
        """
        self.token = access_token
        self.scopes = make_scopes_to_set(scope)

        if expires:
            self.expires = expires
        elif expires_in:
            self.expires = int(time()) + expires_in
        else:
            self.expires = int(time()) + 90000  # These are around 25 hours and the normal standard expiring time of Toornament Bearer Tokens.


class AbstractToornamentConnection(metaclass = ABCMeta):

    def __init__(self, x_api_key, *, client_id=None, client_secret=None, scopes=None, bearer: Optional[BearerToken]=None, scope_check=True):
        """Generates a new Connection to Toornament.
        :param x_api_key The API Key for simple Authentication.
        :param client_id Your application's client id.
        :param client_secret Your application's client secret.
        :param scopes The Scope(s) to use to request when requesting a Bearer Token.
        :param bearer The Bearer Token to start with.
        :param scope_check Checks the scopes when initializing the Class and before every request. This prevents 400-Errors."""
        self.token = x_api_key
        self.scope_check = scope_check
        self.client_id = client_id
        self.client_secret = client_secret
        self.bearer = BearerToken

        # Resolve Scopes
        if scopes is None:
            self.scopes = None
        elif isinstance(scopes, (str, Iterable)):
            self.scopes = make_scopes_to_set(scopes)
        else:
            raise TypeError('scopes has to be None, str or Iterable of str. Got {}'.format(type(scopes)))

        if scope_check:
            unknown_scopes = [scope for scope in self.scopes if scope not in Scopes.LIST_WITH_SCOPES]
            if unknown_scopes:
                raise UnknownScope(unknown_scopes)

            if bearer:
                unknown_scopes = [scope for scope in bearer.scopes if scope not in Scopes.LIST_WITH_SCOPES]
                if unknown_scopes:
                    raise UnknownScope(unknown_scopes)

    @staticmethod
    @abstractmethod
    def _base_url() -> str:
        """:returns The Base-URL of the API"""

    def _create_request_arguments(self, method, path, *, path_parameters, query_parameters, headers, json=None,
                                  request_arguments=None) -> dict:

        headers['X-Api-Key'] = self.token

        if request_arguments is None:
            request_arguments = {}

        url = self._base_url() + path.format(**path_parameters)

        if query_parameters:
            for name, param in query_parameters.items():
                if isinstance(param, list):
                    query_parameters[name] = ','.join(param)

        request_arguments.update(
            {
                'method': method,
                'url': url,
                'headers': headers,
                'params': query_parameters,
            }
        )

        if json is not None:
            request_arguments['json'] = json

        return request_arguments

    def _create_bearer_token_request_arguments(self):

        return {
            'url': 'https://api.toornament.com/oauth/v2/token',
            'data': {
                'grant_type': 'client_credentials',
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'scope': ' '.join(self.scopes)
            }
        }


class SyncToornamentConnection(AbstractToornamentConnection, metaclass = ABCMeta):

    def _simple_access(self, *args, **kwargs) -> dict:
        request_arguments = self._create_request_arguments(*args, **kwargs)

        response = requests.request(**request_arguments)

        response.raise_for_status()

        return response.json()

    def request_bearer_token(self) -> BearerToken:
        request_arguments = self._create_bearer_token_request_arguments()

        response = requests.post(**request_arguments)

        response.raise_for_status()

        return BearerToken(**response.json())

    def refresh_bearer_token(self):
        self.bearer = self.request_bearer_token()


class AsyncToornamentConnection(AbstractToornamentConnection, metaclass = ABCMeta):

    async def _simple_access(self, *args, **kwargs) -> dict:
        request_arguments = self._create_request_arguments(*args, **kwargs)

        async with aiohttp.ClientSession() as session:
            async with session.request(**request_arguments) as response:
                response.raise_for_status()
                return await response.json()

    async def request_bearer_token(self) -> BearerToken:
        request_arguments = self._create_bearer_token_request_arguments()

        async with aiohttp.ClientSession() as session:
            async with session.post(**request_arguments) as response:
                response.raise_for_status()
                json = await response.json()
                return BearerToken(**json)

    async def refresh_bearer_token(self):
        self.bearer = await self.request_bearer_token()
