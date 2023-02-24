from allauth.account.signals import user_signed_up
from django.dispatch import receiver

from users.models import Subscriber


@receiver(user_signed_up)
def handle_user_signed_up(sender, request, user, **kwargs):
    social_login = kwargs.pop("sociallogin")
    token = social_login.token

    # Create a new Subscriber object and save it
    subscriber = Subscriber.objects.get_or_create(user=user, tokens=0)
    return subscriber
