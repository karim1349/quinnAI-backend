# Generated by Django 3.2.5 on 2023-02-18 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_email_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='user',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]