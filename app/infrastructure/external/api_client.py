import requests
from app.infrastructure.external.auth_client import ExternalAuthClient
from app.core.config import settings

class ExternalApiClient:
    def __init__(self):
        self.auth = ExternalAuthClient()

    def _headers(self):
        if not self.auth.token:
            self.auth.login()

        return {
            "Authorization": f"Bearer {self.auth.token}",
            "Accept": "application/json"
        }

    def _url(self, path: str):
        return (
            f"{settings.external_api_base_url}/"
            f"{settings.external_api_version}"
            f"{path}"
        )

    def get(self, path: str, params: dict | None = None):
        url = self._url(path)
        response = requests.get(url, headers=self._headers(), params=params)

        if response.status_code == 401:
            self.auth.refresh()
            response = requests.get(url, headers=self._headers(), params=params)

        response.raise_for_status()
        return response.json()
