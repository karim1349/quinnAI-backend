from django.contrib.auth.models import User

from api.gmail_api import GmailClient


def set_email_label(user: User, email_id: str, label_id: str):
    client = GmailClient(user)
    return client.add_label_to_email(email_id, label_id)
