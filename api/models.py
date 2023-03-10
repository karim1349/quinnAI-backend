from django.contrib.auth.models import User
from django.db import models


class Label(models.Model):
    label_id = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Email(models.Model):
    email_id = models.CharField(db_index=True, null=True,  max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="emails", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    labels = models.ManyToManyField(Label, blank=True)
    score = models.IntegerField(null=True)

    def __str__(self):
        return self.email_id
