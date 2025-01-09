import requests
import json
import os
from datetime import datetime, timedelta
from utils.logger import setup_logger
from config.config import (
    LINKEDIN_CLIENT_ID,
    LINKEDIN_CLIENT_SECRET,
    LINKEDIN_REDIRECT_URI
)

logger = setup_logger()

class LinkedInAPI:
    def __init__(self):
        self.access_token = None
        self.token_expiry = None
        self.base_url = "https://api.linkedin.com/v2"
        self.token_file = "config/token.json"
        self._load_token()

    def _load_token(self):
        if os.path.exists(self.token_file):
            with open(self.token_file, 'r') as f:
                token_data = json.load(f)
                self.access_token = token_data.get('access_token')
                self.token_expiry = datetime.fromisoformat(token_data.get('expiry'))

    def _save_token(self):
        os.makedirs('config', exist_ok=True)
        with open(self.token_file, 'w') as f:
            json.dump({
                'access_token': self.access_token,
                'expiry': self.token_expiry.isoformat()
            }, f)

    def get_authorization_url(self):
        return (
            f"https://www.linkedin.com/oauth/v2/authorization?"
            f"response_type=code&"
            f"client_id={LINKEDIN_CLIENT_ID}&"
            f"redirect_uri={LINKEDIN_REDIRECT_URI}&"
            f"scope=w_member_social"
        )

    def get_access_token(self, authorization_code):
        url = "https://www.linkedin.com/oauth/v2/accessToken"
        data = {
            "grant_type": "authorization_code",
            "code": authorization_code,
            "client_id": LINKEDIN_CLIENT_ID,
            "client_secret": LINKEDIN_CLIENT_SECRET,
            "redirect_uri": LINKEDIN_REDIRECT_URI
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            token_data = response.json()
            self.access_token = token_data["access_token"]
            self.token_expiry = datetime.now() + timedelta(days=60)
            self._save_token()
            return self.access_token
        raise Exception(f"Failed to get access token: {response.text}")

    def create_post(self, content):
        if not self.access_token:
            raise Exception("Access token not set")

        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0"
        }

        post_data = {
            "author": "urn:li:person:b26a5b317",
            "commentary": content,
            "visibility": "PUBLIC",
            "distribution": {
                "feedDistribution": "MAIN_FEED",
                "targetEntities": [],
                "thirdPartyDistributionChannels": []
            },
            "content": {
                "article": {
                    "source": "https://www.linkedin.com/",
                    "title": "LinkedIn Post",
                    "description": content
                }
            }
        }

        response = requests.post(
            f"{self.base_url}/posts",
            headers=headers,
            json=post_data
        )

        if response.status_code == 201:
            logger.info("Successfully posted content")
            return response.json()
        
        error_msg = f"Failed to create post: {response.text}"
        logger.error(error_msg)
        raise Exception(error_msg)

    def refresh_token_if_needed(self):
        if not self.token_expiry or datetime.now() >= self.token_expiry:
            logger.info("Token expired, needs manual reauthorization")
            return False
        return True