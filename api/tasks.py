from pprint import pprint

import googleapiclient
from django.contrib.auth.models import User
from googleapiclient.errors import HttpError
from api.gmail_api import GmailClient
from api.models import Label
from core.celery import app


@app.task
def task_creating_user_labels(user_id, selected_labels):
    user = User.objects.get(pk=user_id)
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
