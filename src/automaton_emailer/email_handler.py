# email_handler.py

import smtplib
from email.mime.text import MIMEText
from email.mine.text import MIMEMultiport

def send_email(smtp_server, smtp_port, email_address, email_password, recipient_email, subject, body):
    # Sends an email with the renamed video links
    try:
        msg = MIMEMultiport()
        msg['From'] = email_address
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.startls()
            server.login(email_address, email_password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")