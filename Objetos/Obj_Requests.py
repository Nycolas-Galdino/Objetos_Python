import json
import requests as re


def verify_status_code(func) -> dict | list:
    def inner(*args, **kwargs):
        response: re.Response = func(*args, **kwargs)
        if response.status_code < 200 or response.status_code >= 300:
            raise ConnectionRefusedError(response.status_code,
                                         response.text)

        if not response.content:
            return response

        elif (isinstance(response.content, dict)
              or isinstance(response.content, list)):
            return response.json()

        else:
            return response.content

    return inner


class Request:
    @verify_status_code
    def get(url: str,
            headers: dict = None,
            params: dict = None,
            timeout: int = 30) -> re.Response:
        """
        Sends a GET request to the specified URL with optional headers and parameters and parses the response as a JSON object.

        Args:
            url (str): The URL to send the GET request to.
            headers (dict, optional): The headers to include in the request. Defaults to None.
            params (dict, optional): The parameters to include in the request. Defaults to None.

        Returns:
            json.loads: The response from the GET request, parsed as a JSON object.
        """

        return re.get(url, headers=headers, params=params, timeout=timeout)

    @verify_status_code
    def post(url: str,
             headers: dict = None,
             params: dict = None,
             data: dict | str = None,
             timeout: int = 30) -> re.Response:
        """
        Sends a POST request to the specified URL with optional headers, parameters, and data.

        Args:
            url (str): The URL to send the POST request to.
            headers (dict, optional): The headers to include in the request. Defaults to None.
            params (dict, optional): The parameters to include in the request. Defaults to None.
            data (dict, optional): The data to include in the request. Defaults to None.

        Returns:
            json.loads: The response from the POST request, parsed as a JSON object.
        """

        if isinstance(data, dict):
            data = json.dumps(data)

        return re.post(url, headers=headers, params=params, data=data, timeout=timeout)
