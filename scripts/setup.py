import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = str(Path(__file__).parent.parent)
sys.path.append(project_root)

from linkedin.linkedin_api import LinkedInAPI
from utils.logger import setup_logger

logger = setup_logger()

def setup():
    try:
        # Create config directory if it doesn't exist
        os.makedirs('config', exist_ok=True)
        
        linkedin_api = LinkedInAPI()
        
        # Get authorization URL
        auth_url = linkedin_api.get_authorization_url()
        print(f"\nPlease visit this URL in your browser:\n{auth_url}\n")
        
        auth_code = input("Enter the code from the URL (everything after 'code='): ")
        
        # Get access token
        access_token = linkedin_api.get_access_token(auth_code)
        if not access_token:
            raise Exception("Failed to get access token")
            
        print("\nSuccessfully set up!")
        return True
        
    except Exception as e:
        print(f"Error during setup: {str(e)}")
        return False

if __name__ == "__main__":
    setup() 