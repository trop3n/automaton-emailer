# main.py

import config
import vimeo_handler
import ministry_platform_handler
import email_handler
from datetime import datetime

def main():
    # Get Vimeo client
    vimeo_client = vimeo_handler.get_vimeo_client(
        config.VIMEO_ACCESS_TOKEN,
        config.VIMEO_CLIENT_ID,
        config.VIMEO_CLIENT_SECRET
    )

    # Get Ministry Platform access token
    mp_access_token = ministry_platform_handler.get_mp_access_token(
        config.MP_OAUTH_ENDPOINT,
        config.MP_CLIENT_ID,
        config.MP_CLIENT_SECRET
    )

    if not vimeo_client or not mp_access_token:
        print("Could not connect to Vimeo or Ministry Platform. Exiting.")
        return

    # Get videos from the specified folder
    videos = vimeo_handler.get_videos_from_folder(vimeo_client, config.VIMEO_FOLDER_ID)
    
    renamed_videos = []

    for video in videos:
        # --- This is the matching logic that you may need to customize ---
        # For this example, we'll assume the original video title is the event identifier
        event_identifier = video['name']
        
        event_details = ministry_platform_handler.get_event_details(
            config.MP_API_ENDPOINT,
            mp_access_token,
            event_identifier
        )

        if event_details:
            # Assuming the event details contain 'Event_Start_Date', 'First_Name', 'Last_Name', and 'Event_Type'
            event_date_str = event_details.get('Event_Start_Date', '').split('T')[0]
            first_name = event_details.get('First_Name', 'FirstName')
            last_name = event_details.get('Last_Name', 'LastName')
            event_type = "Memorial Service" if "memorial" in event_details.get('Event_Type', '').lower() else "Wedding"

            new_title = f"{event_date_str} {first_name} {last_name} {event_type}"
            
            if vimeo_handler.rename_video(vimeo_client, video['uri'], new_title):
                renamed_videos.append({'title': new_title, 'link': video['link']})
        else:
            print(f"No matching event found for video: {video['name']}")

    if renamed_videos:
        # Send an email with the links
        subject = "Updated Vimeo Links for Weddings and Memorials"
        body = "<h3>Here are the updated links for the recent services:</h3><ul>"
        for video in renamed_videos:
            body += f"<li><a href='{video['link']}'>{video['title']}</a></li>"
        body += "</ul>"

        email_handler.send_email(
            config.SMTP_SERVER,
            config.SMTP_PORT,
            config.EMAIL_ADDRESS,
            config.EMAIL_PASSWORD,
            config.RECIPIENT_EMAIL,
            subject,
            body
        )

if __name__ == "__main__":
    main()