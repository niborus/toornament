from abc import ABCMeta, abstractmethod
import requests
import aiohttp
from typing import Optional
from collections.abc import Iterable
from .information import Scopes
from .exceptions import UnknownScope, MissingScope
from time import time
from .functions_dictionary_helper import ParameterType
from .api_functions_doc import FUNCTIONS
from .schema_element import convert_to_dict_remove_none


def make_scopes_to_set(scopes) -> set:
    ret = set()

    if isinstance(scopes, str):
        scopes = scopes.split(' ')

    ret.update([scope.strip().lower() for scope in scopes])

    return ret


class BearerToken:
    def __init__(self, access_token, *, expires: Optional[int] = None, expires_in: Optional[int] = None,
                 scope: Optional, token_type=None):
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
            self.expires = int(
                time()) + 90000  # These are around 25 hours and the normal standard expiring time of Toornament Bearer Tokens.


class AbstractToornamentConnection(metaclass = ABCMeta):

    def __init__(self, x_api_key, *, client_id=None, client_secret=None, scopes=None,
                 bearer: Optional[BearerToken] = None, scope_check=True):
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
        self.bearer = bearer

        # Resolve Scopes
        if scopes is None:
            self.scopes = None
        elif isinstance(scopes, (str, Iterable)):
            self.scopes = make_scopes_to_set(scopes)
        else:
            raise TypeError('scopes has to be None, str or Iterable of str. Got {}'.format(type(scopes)))

        if scope_check and self.scopes:
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

    def _create_request_arguments(self, method, path, *, path_parameters, query_parameters, headers, json_dict=None,
                                  request_arguments=None, authorization=False) -> dict:

        headers['X-Api-Key'] = self.token
        headers['Accept'] = 'application/json'

        if authorization:
            headers['Authorization'] = 'Bearer {access_token}'.format(access_token = self.bearer.token)

        if request_arguments is None:
            request_arguments = {}

        url = self._base_url() + path.format(**path_parameters)

        if query_parameters:
            for name, param in query_parameters.items():
                if isinstance(param, list):
                    query_parameters[name] = ','.join(param)

        if json_dict is not None:
            request_arguments['json'] = json_dict
            headers['Content-Type'] = 'application/json'

        request_arguments.update(
            {
                'method': method,
                'url': url,
                'headers': headers,
                'params': query_parameters,
            }
        )

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

    def _prepare_request(self, function_name, *, request_arguments: Optional[dict]=None, parameter: dict):
        """Prepares the request.
        This function has no blocking elements and can be used in async and sync parts.
        :returns A Dict with parameters for request.request and aiohttp.ClientSession.request.
        :param function_name The Name of the Function to look up the Parameters in the dict.
        :param request_arguments Arguments given by the user to add to request.request or aiohttp.ClientSession.request.
        :param parameter A dict with Parameters of the Endpoint."""

        # Gets a dict with Attributes of the Parameters of the Endpoint
        required_parameters = FUNCTIONS[function_name]['parameters']

        # In sorted_parameters the parameters get sorted by there type.
        # All types and there order can be found in toornament/functions_dictionary_helper.py/ParameterType
        sorted_parameters = [{}, {}, {}]

        # The body argument is the JSON Payload and gets handled differently then the other parameters
        if parameter.get('body'):
            body = parameter.pop('body')
            json_dict = convert_to_dict_remove_none(body)
        else:
            # If there aren't any JSON-Parameters, don't send a JSON.
            json_dict = None

        # Iterates through all given parameters, sort them into sorted_parameters, and manipulate them, if necessary
        for parameter_name, parameter_value in parameter.items():

            # parameter_attributes are the attributes, that this parameter has.
            parameter_attributes = required_parameters[parameter_name]

            # Parameters that are None and Optional will be ignored and won't show up in the request.
            # If a Parameter is not optional or not None, it will get sorted.
            if not parameter_attributes['optional'] or parameter_value is not None:

                # If the Parameter expects a list, every individual value gets Converted
                if parameter_attributes['list']:
                    # Manipulate every element of the parameter with their Converter Function.
                    # Most of the time, this converts the value to a string or does nothing. Other Converters exist.
                    new_parameter_value = [parameter_attributes['converter'](element) for element in parameter_value]
                else:
                    # Manipulate the parameter with their Converter Function.
                    # Most of the time, this converts the value to a string or does nothing. Other Converters exist.
                    new_parameter_value = parameter_attributes['converter'](parameter_value)

                # If the parameter is a range, then the value has to be formatted again, turning it from
                # `x-y` to `type=x-y`.
                if parameter_name == 'range':
                    sorted_parameters[ParameterType.HEADER][parameter_name.capitalize()] = '{}={}'.format(
                        FUNCTIONS[function_name]['range'], new_parameter_value)
                # If the parameter is from type Header, the Name of the Parameters has to get capitalize.
                elif parameter_attributes['type'] == ParameterType.HEADER:
                    sorted_parameters[ParameterType.HEADER][parameter_name.capitalize()] = new_parameter_value
                # In any other case, the parameter can be added to the sorted_dict
                else:
                    sorted_parameters[parameter_attributes['type']][parameter_name] = new_parameter_value

        # Get Scopes of the Endpoint.
        scopes = FUNCTIONS[function_name]['scopes']
        # If the Endpoint don't have any scopes, it is a simple request. Otherwise, it's a authorized_request
        # Check if scopes are Missing
        if scopes and self.scope_check and not [scope for scope in scopes if scope in self.bearer.scopes]:
            raise MissingScope(scopes)

        # Giving sorted parameters and known attributes receive and return a dict for request.
        return self._create_request_arguments(
            method = FUNCTIONS[function_name]['method'],
            path = FUNCTIONS[function_name]['path'],
            headers = sorted_parameters[ParameterType.HEADER],
            path_parameters = sorted_parameters[ParameterType.PATH],
            query_parameters = sorted_parameters[ParameterType.QUERY],
            json_dict = json_dict,
            request_arguments = request_arguments,
            authorization = bool(scopes),
        )

    @staticmethod
    def _build_class_from_response(function_name, response: dict):
        """Builds a Class from the response."""

        if response is None:
            return None

        converter_function = FUNCTIONS[function_name]['response']['converter']
        is_list = FUNCTIONS[function_name]['response']['list']

        if is_list:
            return [converter_function(**element) for element in response]
        else:
            return converter_function(**response)


class SyncToornamentConnection(AbstractToornamentConnection, metaclass = ABCMeta):

    def _simple_access(self, *args, **kwargs):
        request_arguments = self._prepare_request(*args, **kwargs)

        response = requests.request(**request_arguments)

        response.raise_for_status()

        if response.status_code == 204:
            return None
        else:
            return response.json()

    def _authorized_access(self, *args, **kwargs):
        return self._simple_access(self, *args, **kwargs)

    def request_bearer_token(self) -> BearerToken:
        request_arguments = self._create_bearer_token_request_arguments()

        response = requests.post(**request_arguments)

        response.raise_for_status()

        return BearerToken(**response.json())

    def refresh_bearer_token(self):
        self.bearer = self.request_bearer_token()

    def _access(self, function_name, request_arguments, **parameter):
        """Sends a request to the API.
        This Part of function checks weather to use Authorized Access or Simple Access and Calls the Function."""

        if FUNCTIONS[function_name].get('scope'):
            response = self._authorized_access(function_name, request_arguments = request_arguments, parameter = parameter)
        else:
            response = self._simple_access(function_name, request_arguments = request_arguments, parameter = parameter)

        return self._build_class_from_response(function_name, response)


class AsyncToornamentConnection(AbstractToornamentConnection, metaclass = ABCMeta):

    async def _simple_access(self, *args, **kwargs):
        request_arguments = self._prepare_request(*args, **kwargs)

        async with aiohttp.ClientSession() as session:
            async with session.request(**request_arguments) as response:
                response.raise_for_status()
                if response.status == 204:
                    return None
                else:
                    return await response.json()

    async def _authorized_access(self, *args, **kwargs):
        return await self._simple_access(self, *args, **kwargs)

    async def request_bearer_token(self) -> BearerToken:
        request_arguments = self._create_bearer_token_request_arguments()

        async with aiohttp.ClientSession() as session:
            async with session.post(**request_arguments) as response:
                response.raise_for_status()
                json = await response.json()
                return BearerToken(**json)

    async def refresh_bearer_token(self):
        self.bearer = await self.request_bearer_token()

    async def _access(self, function_name, request_arguments, **parameter):
        """Sends a request to the API.
        This Part of function checks weather to use Authorized Access or Simple Access and Calls the Function."""

        if FUNCTIONS[function_name]['scopes']:
            response = await self._authorized_access(function_name, request_arguments = request_arguments, parameter = parameter)
        else:
            response = await self._simple_access(function_name, request_arguments = request_arguments, parameter = parameter)

        return self._build_class_from_response(function_name, response)
