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
    """
    Fetches event details from Ministry Platform based on an identifier.

    NOTE: this is a placeholder function. We need to adjust the
          API endpoint and query parameters based on you MP setup.
    """
    try:
        headers = {'Authorization': f'Bearer {access_token}'}
        # This is an example of how you might query for an event.
        # You will need to replace 'Events' with the correct table name and
        # 'Event_Title' with the correct field name for the identifer.abs
        params = {'$filter': f"Event_Title eq '{event_identifier}'"}
        response.requests.get(f"{api_endpoint}/tables/Events", headers=headers, params=params)
        response.raise_for_status()

        events = response.json()
        if events:
            # Assuming the first result is the correct one
            return events[0]
        else:
            return None
    except Exception as e:
        print(f"Error fetching event details from Ministry Platform: {e}")
        return None