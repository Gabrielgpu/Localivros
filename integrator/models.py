from django.db import models
from django.utils import timezone
from datetime import timedelta
import requests
import base64
from django.conf import settings

class Credentials(models.Model):
    access_token = models.TextField()
    refresh_token = models.TextField()
    expires_in = models.IntegerField()
    token_updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_token_valid(self, margin_minutes=5):
        expires_at = self.token_updated_at + timedelta(seconds=self.expires_in)
        return timezone.now() < (expires_at - timedelta(minutes=margin_minutes))

    def refresh(self):
        client_id = settings.EXTERNAL_CLIENT_ID
        client_secret = settings.EXTERNAL_CLIENT_SECRET
        token_url = settings.EXTERNAL_API_TOKEN_ENDPOINT

        credentials = f"{client_id}:{client_secret}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "1.0",
            "Authorization": f"Basic {encoded_credentials}"
        }

        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token
        }

        response = requests.post(token_url, headers=headers, data=data)

        if response.status_code == 200:
            token_data = response.json()
            self.access_token = token_data.get("access_token")
            self.refresh_token = token_data.get("refresh_token", self.refresh_token)
            self.expires_in = token_data.get("expires_in")
            self.save()
            return True
        return False
