import requests
from app.core.config import settings

class ExternalAuthClient:
    def __init__(self):
        self.base_url = settings.external_api_base_url
        self.token = None
        self.refresh_token = None

    def login(self):
        url = f"{self.base_url}/oauth/token"

        data = {
            "grant_type": "password",
            "client_id": settings.external_client_id,
            "client_secret": settings.external_client_secret,
            "username": settings.external_username,
            "password": settings.external_password
        }

        response = requests.post(url, data=data)
        response.raise_for_status()

        payload = response.json()
        self.token = payload["access_token"]
        self.refresh_token = payload["refresh_token"]

        return self.token

    def refresh(self):
        url = f"{self.base_url}/oauth/token"

        data = {
            "grant_type": "refresh_token",
            "client_id": settings.external_client_id,
            "client_secret": settings.external_client_secret,
            "refresh_token": self.refresh_token
        }

        response = requests.post(url, data=data)
        response.raise_for_status()

        payload = response.json()
        self.token = payload["access_token"]
        self.refresh_token = payload["refresh_token"]

        return self.token
