from django.db import models

class Email(models.Model):
    body = models.TextField(blank=True, null=True)
    user = models.EmailField(blank=True, null=True)
    source = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body