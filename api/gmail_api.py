from allauth.socialaccount.models import SocialToken
from django.conf import settings
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]


def handle_errors(callable):
    def wrapper(*args, **kwargs):
        try:
            return callable(*args, **kwargs)
        except HttpError as error:
            raise HttpError(f"An error occurred: {error}")

    return wrapper


class GmailClient:
    def __init__(self, user_instance):
        social_token = SocialToken.objects.get(account__user=user_instance)
        info = {
            "token": social_token.token,
            "refresh_token": social_token.token_secret,
            "client_id": settings.GOOGLE_CLIENT_ID,
            "client_secret": settings.GOOGLE_CLIENT_SECRET,
        }
        self._credentials = Credentials.from_authorized_user_info(info=info)
        self._service = build("gmail", "v1", credentials=self._credentials)

    @handle_errors
    def get_user_labels(self):
        service = build("gmail", "v1", credentials=self._credentials)
        user_labels = service.users().labels().list(userId="me").execute()
        return user_labels["labels"]

    @handle_errors
    def get_message_details(self, message_id):
        last_email = (
            self._service.users().messages().get(userId="me", id=message_id).execute()
        )
        return last_email

    @handle_errors
    def get_last_email(self):

        results = (
            self._service.users().messages().list(userId="me", maxResults=1).execute()
        )
        # last_email_id = results['messages'][0]['id']
        return results

    @handle_errors
    def add_label_to_email(self, email_id, label_id):

        # Update the label of the email message
        label_ids = [label_id]
        # Call the Gmail API to update the label of the email message
        return (
            self._service.users()
            .messages()
            .modify(userId="me", id=email_id, body={"addLabelIds": label_ids})
            .execute()
        )

    @handle_errors
    def create_label(self, label_object):
        return (
            self._service.users()
            .labels()
            .create(userId="me", body=label_object)
            .execute()
        )


# user = User.objects.last()
# cl = GmailClient(user)
# label gouvernement id Label_6480842904800323051, label kamil personal Label_5
# cl.get_message_details("18682cd67ef83143")
# cl.last_email("elhassanegargem@gmail.com") dial kamil 186830a6953d9681
# cl.get_user_labels("elhassanegargem@gmail.com")
# msg["payload"]["parts"][0]["body"]

