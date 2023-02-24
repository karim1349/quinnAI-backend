from django.conf import settings
from django.db import models


class Subscriber(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField()
    access_token = models.CharField(max_length=200)
    access_secret = models.CharField(max_length=200)
    expires_at = models.DateTimeField()

    tokens = models.IntegerField(default=0)
