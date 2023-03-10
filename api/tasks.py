from pprint import pprint

import googleapiclient
from django.contrib.auth.models import User
from googleapiclient.errors import HttpError
from api.gmail_api import GmailClient
from api.models import Label, Email
from api.open_ai_client import score_email
from core.celery import app
from utils.gmail import get_email_elements


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


@app.task
def scoring_emails_of_user(user_pk, max_results=10):
    user = User.objects.get(pk=user_pk)
    client = GmailClient(user)
    emails = client.get_last_emails(max_results=10)
    for email in emails:
        detail = client.get_message_details(email["id"])
        subject, body = get_email_elements(detail)
        sender = user.email

        score = score_email(subject, sender, body[:500])
        obj, created = Email.objects.update_or_create(email_id=email["id"], user=user, defaults={"score": score})
