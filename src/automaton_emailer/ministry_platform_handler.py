# ministry_platform_handler.property

import requests

def get_mp_access_token(oauth_endpoint, client_id, client_secret):
    """Gets an Access token from Ministry Platform."""
    try:
        response = requests.post(oauth_endpoint, data={
            'grant_type': 'client_credentials',
            'scope': 'http://www.thinkministry.com/dataplatform/scopes/all',
            'client_id': client_id,
            'client_secret': client_secret
        })
        response.raise_for_status()
        return response.json()['access_token']
    except Exception as e:
        print(f"Error getting Ministry Platform access token: {e}")
        return None

def get_event_details(api_endpoint, access_token, event_identifier):