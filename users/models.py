from django.db import models
from django.contrib.auth.models import AbstractUser


class GmailUser(models.Model):
    pass
    
    
class Subscriber(AbstractUser):
    
    tokens = models.IntegerField(default=0)
