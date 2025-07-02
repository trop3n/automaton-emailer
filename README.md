Vimeo Automation Script
This script automates the process of renaming videos in a specific Vimeo folder based on event data from Ministry Platform and then emailing the links to a specified recipient.

How it Works
Vimeo Connection: The script connects to your Vimeo account using the provided API credentials.

Ministry Platform Connection: It connects to your Ministry Platform account to fetch event data.

Video-Event Matching: The script attempts to match videos in the specified Vimeo folder to events in Ministry Platform. This is a critical step, and you may need to adjust the matching logic based on your workflow. The current implementation assumes that the video's original title on Vimeo contains a unique identifier that can be used to look up the event in Ministry Platform (e.g., an event ID).

Renaming: Once a match is found, the video is renamed to the format YYYY-MM-DD First Name Last Name Memorial Service or YYYY-MM-DD First Name Last Name Wedding.

Emailing: Finally, the script sends an email containing the links to all the renamed videos to the specified recipient.

Setup and Configuration
Install Dependencies:

pip install PyVimeo requests

Vimeo API Credentials:

Go to the Vimeo Developer page and create a new app.

Generate an access token with "Private" and "Video" scopes.

You will need the Access Token, Client ID, and Client Secret.

Ministry Platform API Credentials:

You will need to get your API credentials from your Ministry Platform administrator.

You will need the API Endpoint, Client ID, and Client Secret.

Email Configuration:

You will need the following information for your email account:

SMTP Server (e.g., smtp.gmail.com)

SMTP Port (e.g., 587 for TLS)

Email Address

Password or App Password (for services like Gmail, you'll need to generate an App Password).

Configure the Script:

Open the config.py file and fill in all the required credentials from the steps above.

Running the Script
Once you have completed the setup and configuration, you can run the script from your terminal:

python main.py

Customization
The most likely part of the script you will need to customize is the video-event matching logic in the main.py file. The current implementation is a placeholder and assumes a simple matching rule. You will need to adapt this to your specific needs.