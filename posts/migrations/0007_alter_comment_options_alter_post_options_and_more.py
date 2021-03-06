# Generated by Django 4.0.5 on 2022-07-07 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_interest_rename_subscribers_subscriber_staffusers_and_more'),
        ('posts', '0006_tag_alter_post_options_remove_post_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='post',
            name='colloborators',
            field=models.ManyToManyField(blank=True, related_name='colloborators', to='users.userprofile'),
        ),
    ]
