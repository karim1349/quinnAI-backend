from django.contrib.auth.models import User
from django.db import models


class Label(models.Model):
    label_id = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Email(models.Model):
    email_id = models.CharField(db_index=True, null=True,  max_length=100)
    body = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="emails", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(db_index=True, max_length=256, null=True)
    sender = models.EmailField(db_index=True, null=True)
    source = models.TextField(null=True)
    labels = models.ManyToManyField(Label, blank=True)

    def __str__(self):
        return self.email_id
