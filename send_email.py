"""Sending auto. emails."""
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER = "kevin.thalmann94@gmail.com"
PASSOWORD = os.environ.get('USER_PASSWORD')
SEND_TO = "kevin_thalmann@yahoo.de"
SUBJECT = "Relase Mail"
BOBY = "Es wurde ein neues Release gestartet."


def send_email(sender_email: str, sender_password: str,
               receiver_email: str, subject: str, message: str) -> None:
    """Sending auto. emails.

    Args:
        sender_email: _description_
        sender_password: _description_
        receiver_email: _description_
        subject: _description_
        message: _description_
    """
    # E-Mail-Inhalt erstellen
    email = MIMEMultipart()
    email['From'] = sender_email
    email['To'] = receiver_email
    email['Subject'] = subject
    email.attach(MIMEText(message))
    # Verbindung zum SMTP-Server herstellen
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = sender_email
    smtp_password = sender_password

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(smtp_username, smtp_password)
        # E-Mail senden
        server.sendmail(SENDER, SEND_TO, email.as_string())
        print("E-Mail erfolgreich gesendet!")  # noqa: T201
        # Verbindung zum SMTP-Server schließen
        server.quit()
    except Exception as e:  # noqa: BLE001
        print("Fehler beim Senden der E-Mail:", e)  # noqa: T201

if __name__ == "__main__":
    send_email(SENDER, PASSOWORD, SEND_TO, SUBJECT, BOBY)
