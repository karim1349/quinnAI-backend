# Generated by Django 4.1.6 on 2023-02-24 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_email_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='headline',
            field=models.TextField(null=True),
        ),
    ]
