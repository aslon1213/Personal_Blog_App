# Generated by Django 4.0.5 on 2022-06-30 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_id_alter_post_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_ready_to_post',
            field=models.BooleanField(default=False),
        ),
    ]