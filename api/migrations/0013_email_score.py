# Generated by Django 4.1.6 on 2023-03-08 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_label_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='score',
            field=models.IntegerField(null=True),
        ),
    ]
