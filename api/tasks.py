from pprint import pprint

import googleapiclient
from googleapiclient.errors import HttpError
from api.gmail_api import GmailClient
from api.models import Label


def creating_user_labels(user, selected_labels):
    cl = GmailClient(user)
    for label in selected_labels:
        try:
            response = cl.create_label(label)
            Label.objects.create(user=user, label_id=response["id"])
        except HttpError:
            raise HttpError(f"error during creating template {label['name']}")


def scoring_emails_of_user(user):
    cl = GmailClient(user)


    pass
