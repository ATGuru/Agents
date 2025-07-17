import smtplib
from email.mime.text import MIMEText
import os

def send_email_notification(subject, body, to_email, smtp_server='localhost', smtp_port=25):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'meta-agent@localhost'
    msg['To'] = to_email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.sendmail(msg['From'], [to_email], msg.as_string())
        print(f"Notification sent to {to_email}")
    except Exception as e:
        print(f"Failed to send notification: {e}")

def notify_console(message):
    print(f"[NOTIFICATION] {message}")
