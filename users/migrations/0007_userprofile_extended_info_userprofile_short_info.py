# Generated by Django 4.0.5 on 2022-07-11 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_interest_rename_subscribers_subscriber_staffusers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='extended_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='short_info',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]