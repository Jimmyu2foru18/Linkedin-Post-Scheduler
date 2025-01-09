import requests
import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = str(Path(__file__).parent.parent)
sys.path.append(project_root)

from config.config import LINKEDIN_CLIENT_ID, LINKEDIN_CLIENT_SECRET

def get_profile_urn():
    # First, get an access token
    auth_url = "https://www.linkedin.com/oauth/v2/authorization"
    token_url = "https://www.linkedin.com/oauth/v2/accessToken"
    
    # Updated scopes - only using w_member_social
    auth_params = {
        'response_type': 'code',
        'client_id': LINKEDIN_CLIENT_ID,
        'redirect_uri': 'http://localhost:8000/callback',
        'scope': 'w_member_social',  # Only using required scope
        'state': '123456'
    }
    
    # Build the authorization URL
    auth_url = f"{auth_url}?{'&'.join(f'{k}={v}' for k, v in auth_params.items())}"
    
    print(f"""
    1. Visit this URL in your browser:
    {auth_url}
    """)
    
    auth_code = input("2. Enter the code from the redirect URL: ")
    
    # Get access token
    response = requests.post(token_url, data={
        'grant_type': 'authorization_code',
        'code': auth_code,
        'client_id': LINKEDIN_CLIENT_ID,
        'client_secret': LINKEDIN_CLIENT_SECRET,
        'redirect_uri': 'http://localhost:8000/callback'
    })
    
    if response.status_code != 200:
        print("Error getting access token:", response.text)
        return None
        
    access_token = response.json()['access_token']
    
    # Get profile data using v2/me endpoint
    headers = {'Authorization': f'Bearer {access_token}'}
    profile_response = requests.get('https://api.linkedin.com/v2/me', headers=headers)
    
    if profile_response.status_code == 200:
        data = profile_response.json()
        urn = data['id']
        print(f"\nYour LinkedIn URN is: {urn}")
        return urn
    else:
        print("Error getting profile data:", profile_response.text)
        return None

if __name__ == "__main__":
    get_profile_urn() 