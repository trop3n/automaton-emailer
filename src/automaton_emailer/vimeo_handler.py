# vimeo_handler.py

import vimeo

def get_vimeo_client(access_token, client_id, client_secret):
    """Initializes and returns the Vimeo client."""
    return vimeo.VimeoClient(
        token=access_token,
        key=client_id,
        secret=client_secret
    )

def get_videos_from_folder(client, folder_id):
    """Fetches all videos from a specific folder."""
    try:
        response = client.get(f'/me/projects/{folder_id}/videos')
        response.raise_for_status()
        return response.json()['data']
    except Exception as e:
        print(f"Error fetching videos from Vimeo folder: {e}")
        return []

def rename_video(client, video_uri, new_title):
    """Renames a video on Vimeo."""
    try:
        response = client.patch(video_uri, data={'name': new_title})
        response.raise_for_status()
        print(f"Successfully renamed video to: {new_title}")
        return True
    except Exception as e:
        print(f"Error renaming video {video_uri}: {e}")
        return False