# Generated by Django 4.0.5 on 2022-06-30 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_is_ready_to_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.TextField(),
        ),
    ]
