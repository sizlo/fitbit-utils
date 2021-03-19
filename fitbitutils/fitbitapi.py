from fitbitutils.authenticate import Authenticator

import requests

class AuthenticationError(Exception):
    pass

class FitbitApi:
    
    def __init__(self):
        self._fitbit_url = "https://api.fitbit.com/1/"
        self.authenticator = Authenticator()

    def make_request(self, method: str, url: str, params: dict = None) -> dict:
        try:
            return self._do_request(method, url, params)
        except AuthenticationError:
            self.authenticator.authenticate()
            return self._do_request(method, url, params)

    def _do_request(self, method: str, url: str, params: dict) -> dict:
        headers = {
            "Authorization": f"Bearer {self.authenticator.access_token}",
            "Content-Length": "0"
        }

        full_url = clean_url(f"{self._fitbit_url}/{url}")
        response = requests.request(method, full_url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 401:
            raise AuthenticationError()

        response.raise_for_status()

        return response.json()

def clean_url(url):
    while "//" in url:
        url = url.replace("//", "/")
    return url.replace("https:/", "https://")
