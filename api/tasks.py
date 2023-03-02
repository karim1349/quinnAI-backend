from api.gmail_api import GmailClient
from api.models import Label


def creating_user_labels(user, selected_labels):
    cl = GmailClient(user)
    for label in selected_labels:
        cl.create_label(label)


def labeling_emails_of_user(user):
    pass
