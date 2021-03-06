# Generated by Django 4.0a1 on 2021-09-26 10:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conversation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='message',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 9, 26, 10, 6, 0, 56297, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
