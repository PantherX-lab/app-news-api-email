import smtplib
import ssl
import os
from email.message import EmailMessage

def send_email(message: str):
    username = "appworld704@gmail.com"
    password = "tvesfuyonlniuuxr"
    receiver = "appworld704@gmail.com"

    if not username or not password or not receiver:
        raise ValueError("Email environment variables are missing")

    msg = EmailMessage()
    msg["From"] = username
    msg["To"] = receiver
    msg["Subject"] = "Tesla News Update"
    msg.set_content(message)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(username, password)
        server.send_message(msg)
