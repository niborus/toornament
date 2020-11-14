from abc import ABCMeta, abstractmethod
import requests
import aiohttp


class AbstractToornamentConnection(metaclass=ABCMeta):

    def __init__(self, token):
        self.token = token

    @staticmethod
    @abstractmethod
    def _base_url() -> str:
        """:returns The Base-URL of the API"""

    def create_request_arguments(self, method, path, *, path_parameters, query_parameters, headers, json=None, request_arguments=None) -> dict:

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


class SyncToornamentConnection(AbstractToornamentConnection, metaclass=ABCMeta):

    def _simple_access(self, *args, **kwargs) -> dict:

        request_arguments = self.create_request_arguments(*args, **kwargs)

        response = requests.request(**request_arguments)

        response.raise_for_status()

        return response.json()


class AsyncToornamentConnection(AbstractToornamentConnection, metaclass=ABCMeta):

    async def _simple_access(self, *args, **kwargs) -> dict:

        request_arguments = self.create_request_arguments(*args, **kwargs)

        async with aiohttp.ClientSession() as session:
            async with session.request(**request_arguments) as response:
                response.raise_for_status()
                return await response.json()
