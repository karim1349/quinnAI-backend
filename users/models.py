from django.conf import settings
from django.db import models


class Subscriber(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tokens = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.pk}"
