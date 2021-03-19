from pathlib import Path
import urllib.parse as urlparse

import os

class SecretMissingError(Exception):
    pass

class Authenticator:

    def __init__(self):
        fitbit_api_client_id = "22C69C"
        token_expiry_seconds = 31536000  # 1 year
        
        self._auth_url = f"https://www.fitbit.com/oauth2/authorize?response_type=token&client_id={fitbit_api_client_id}&scope=activity%20nutrition%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight&expires_in={token_expiry_seconds}"
        self._secrets_path = f"{Path.home()}/.fitbitutils"

        try:
            self._read_secrets()
        except SecretMissingError:
            self.authenticate()

    def authenticate(self):
        print(f"Visit the following url to generate a token\n\n{self._auth_url}\n")
        print(f"Paste the url you were redirected to here")
        redirect_url = input("> ")
        print()
        self._save_from_url("user_id", redirect_url)
        self._save_from_url("access_token", redirect_url)
        self._read_secrets()
        print("Successfully authenticated")

    def _read_secrets(self):
        self.user_id = self._read_secret("user_id")
        self.access_token = self._read_secret("access_token")

    def _read_secret(self, secret_name: str) -> str:
        filename = f"{self._secrets_path}/{secret_name}"

        if not os.path.isfile(filename):
            raise SecretMissingError()

        with open(filename) as file:
            value = file.read()

        if value is None or len(value) == 0:
            raise SecretMissingError()

        return value

    def _save_from_url(self, field: str, url: str):
        parsed = urlparse.urlparse(url)
        fields = urlparse.parse_qs(parsed.fragment)
        value = fields[field][0]

        filename = f"{self._secrets_path}/{field}"
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, "w") as text_file:
            text_file.write(value)

if __name__ == "__main__":
    Authenticator()
