from django.db import models


class Email(models.Model):
    body = models.TextField(blank=True, null=True)
    # user = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(db_index=True, max_length=256, null=True)
    sender = models.EmailField(db_index=True, null=True)
    source = models.TextField(null=True)
    headline = models.TextField(null=True)

    def __str__(self):
        return self.body
