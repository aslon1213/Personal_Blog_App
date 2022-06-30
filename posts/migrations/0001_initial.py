# Generated by Django 4.0.5 on 2022-06-30 12:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('name', models.CharField(max_length=500)),
                ('post', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name=uuid.uuid4)),
            ],
        ),
    ]