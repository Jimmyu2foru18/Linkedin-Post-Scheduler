import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = str(Path(__file__).parent.parent)
sys.path.append(project_root)

from linkedin.linkedin_api import LinkedInAPI
from config.config import LINKEDIN_CLIENT_ID, LINKEDIN_CLIENT_SECRET

def test_post():
    linkedin_api = LinkedInAPI()
    
    # Get authorization URL
    auth_url = linkedin_api.get_authorization_url()
    print(f"\nPlease visit this URL in your browser:\n{auth_url}\n")
    
    # After authorization, you'll be redirected to a URL with a code
    # Even though it shows "localhost refused", you can still copy the code from the URL
    auth_code = input("Enter the code from the URL (everything after 'code='): ")
    
    # Get access token
    linkedin_api.get_access_token(auth_code)
    
    # Try to create a test post
    try:
        linkedin_api.create_post("Test post from LinkedIn Automation App!")
        print("Post created successfully!")
    except Exception as e:
        print(f"Error creating post: {str(e)}")

if __name__ == "__main__":
    test_post() 