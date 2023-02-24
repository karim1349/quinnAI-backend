import google.auth
from django.conf import settings
from django.contrib.auth.models import User
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from allauth.socialaccount.models import SocialToken

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']


def get_credentials(user):
    social_token = SocialToken.objects.get(account__user=user)
    info = {"token": social_token.token, "refresh_token": social_token.token_secret,  "client_id": settings.GOOGLE_CLIENT_ID, "client_secret": settings.GOOGLE_CLIENT_SECRET,}
    credentials = Credentials.from_authorized_user_info(info=info)
    return credentials


def get_user_labels(user_email, credentials):
    service = build('gmail', 'v1', credentials=credentials)

    try:
        user_labels = service.users().labels().list(userId=user_email).execute()
        return user_labels['labels']
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None


user = User.objects.all()[1]

credentials = get_credentials(user)
labels = get_user_labels("elhassanegargem@gmail.com", credentials)

print(labels)